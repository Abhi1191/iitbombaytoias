/* ============================================================
   FREE AI STUDY CHATBOT  (100% client-side, no server, no API key)
   ------------------------------------------------------------
   Reads the study PDF (window.SITE_CONFIG.chatbotPdfUrl) directly
   in the browser using Mozilla's pdf.js, then answers questions by
   finding the most relevant passages. Nothing is sent anywhere.

   Mount point: an element with id="study-chatbot".
   ============================================================ */
(function () {
  "use strict";

  var PDFJS_SRC = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js";
  var PDFJS_WORKER = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";

  var STOPWORDS = {
    the: 1, a: 1, an: 1, of: 1, to: 1, in: 1, is: 1, are: 1, and: 1, or: 1,
    for: 1, on: 1, at: 1, by: 1, with: 1, as: 1, it: 1, its: 1, this: 1, that: 1,
    what: 1, which: 1, who: 1, whom: 1, how: 1, why: 1, when: 1, where: 1, was: 1,
    were: 1, be: 1, been: 1, do: 1, does: 1, did: 1, can: 1, could: 1, will: 1,
    would: 1, should: 1, about: 1, into: 1, from: 1, me: 1, my: 1, tell: 1,
    explain: 1, define: 1, give: 1, list: 1, some: 1, any: 1, please: 1, i: 1
  };

  // Lines that carry the seller/buyer watermark — never surface these.
  var WATERMARK = /levelupias|karol bagh|pusa road|metro pillar|rajnandani|@gmail\.com|ph:\s*\d|email:|new delhi-?110005|\b\d{10}\b/i;

  var passages = [];
  var docTermFreq = {};
  var loaded = false;
  var loadingPromise = null;

  function tokenize(text) {
    var out = [];
    var words = String(text).toLowerCase().match(/[a-z0-9]+/g) || [];
    for (var i = 0; i < words.length; i++) {
      var w = words[i];
      if (w.length > 1 && !STOPWORDS[w]) out.push(w);
    }
    return out;
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("Failed to load " + src)); };
      document.head.appendChild(s);
    });
  }

  function addPassages(pageText) {
    // Split page text into sentence-ish chunks of a few sentences each.
    var sentences = pageText.replace(/\s+/g, " ").split(/(?<=[.:;])\s+/);
    var buf = "";
    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i].trim();
      if (!s || WATERMARK.test(s)) continue;
      buf += (buf ? " " : "") + s;
      if (buf.length >= 240 || i === sentences.length - 1) {
        var clean = buf.trim();
        if (clean.length > 25) {
          var tokens = tokenize(clean);
          passages.push({ text: clean, tokens: tokens });
          for (var t = 0; t < tokens.length; t++) {
            docTermFreq[tokens[t]] = (docTermFreq[tokens[t]] || 0) + 1;
          }
        }
        buf = "";
      }
    }
  }

  function ensurePdfText(pdfUrl) {
    if (loaded) return Promise.resolve();
    if (loadingPromise) return loadingPromise;
    loadingPromise = (function () {
      var chain = window.pdfjsLib ? Promise.resolve() : loadScript(PDFJS_SRC);
      return chain.then(function () {
        window.pdfjsLib.GlobalWorkerOptions.workerSrc = PDFJS_WORKER;
        return window.pdfjsLib.getDocument(pdfUrl).promise;
      }).then(function (pdf) {
        var seq = Promise.resolve();
        for (var p = 1; p <= pdf.numPages; p++) {
          (function (pageNum) {
            seq = seq.then(function () {
              return pdf.getPage(pageNum).then(function (page) {
                return page.getTextContent();
              }).then(function (content) {
                var text = content.items.map(function (it) { return it.str; }).join(" ");
                addPassages(text);
              });
            });
          })(p);
        }
        return seq;
      }).then(function () {
        loaded = true;
      });
    })();
    return loadingPromise;
  }

  function answer(question) {
    var qTokens = tokenize(question);
    if (!qTokens.length || !passages.length) return null;
    var N = passages.length;
    var best = null;
    var bestScore = 0;
    for (var i = 0; i < passages.length; i++) {
      var p = passages[i];
      var score = 0;
      for (var q = 0; q < qTokens.length; q++) {
        var term = qTokens[q];
        if (p.tokens.indexOf(term) === -1) continue;
        // Rarer terms across the document carry more weight (idf-like).
        var idf = Math.log((N + 1) / ((docTermFreq[term] || 0) + 1)) + 1;
        score += idf;
      }
      if (score > bestScore) { bestScore = score; best = p; }
    }
    if (!best || bestScore <= 0) return null;
    return best.text;
  }

  function init() {
    var mount = document.getElementById("study-chatbot");
    if (!mount) return;
    var cfg = window.SITE_CONFIG || {};
    var pdfUrl = cfg.chatbotPdfUrl;
    var topic = cfg.chatbotTopic || "this topic";
    if (!pdfUrl) return;

    mount.innerHTML =
      '<div class="chatbot">' +
      '  <div class="chatbot-header">' +
      '    <span class="chatbot-dot"></span> AI Study Assistant &middot; ' + topic +
      '  </div>' +
      '  <div class="chatbot-log" id="chatbot-log" aria-live="polite"></div>' +
      '  <div class="chatbot-chips" id="chatbot-chips"></div>' +
      '  <form class="chatbot-form" id="chatbot-form">' +
      '    <input type="text" id="chatbot-input" autocomplete="off" ' +
      '           placeholder="Ask about ' + topic + '..." aria-label="Ask a question" />' +
      '    <button type="submit" class="btn">Ask</button>' +
      '  </form>' +
      '  <p class="chatbot-note">Free &amp; private — the PDF is read in your browser. Answers are drawn directly from the notes.</p>' +
      '</div>';

    var log = mount.querySelector("#chatbot-log");
    var form = mount.querySelector("#chatbot-form");
    var input = mount.querySelector("#chatbot-input");
    var chips = mount.querySelector("#chatbot-chips");

    function bubble(text, who) {
      var el = document.createElement("div");
      el.className = "chatbot-msg chatbot-" + who;
      el.textContent = text;
      log.appendChild(el);
      log.scrollTop = log.scrollHeight;
      return el;
    }

    bubble("Hi! Ask me anything about " + topic + " and I'll answer from the study notes.", "bot");

    var samples = ["What is a PVTG?", "Explain the POCSO Act", "Causes of child labour", "Theories of juvenile delinquency"];
    samples.forEach(function (q) {
      var chip = document.createElement("button");
      chip.type = "button";
      chip.className = "chatbot-chip";
      chip.textContent = q;
      chip.addEventListener("click", function () { ask(q); });
      chips.appendChild(chip);
    });

    var busy = false;
    function ask(question) {
      if (busy) return;
      question = (question || "").trim();
      if (!question) return;
      bubble(question, "user");
      input.value = "";
      busy = true;
      var thinking = bubble("Reading the notes…", "bot");
      ensurePdfText(pdfUrl).then(function () {
        var reply = answer(question);
        thinking.textContent = reply
          ? reply
          : "I couldn't find that in these notes. Try rephrasing, or use a keyword like \"POCSO\", \"child labour\", \"tribal\" or \"juvenile\".";
        busy = false;
      }).catch(function () {
        thinking.textContent = "Sorry — I couldn't load the study PDF right now. Please check your connection and try again.";
        busy = false;
      });
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      ask(input.value);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
