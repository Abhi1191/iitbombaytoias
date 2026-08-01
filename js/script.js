console.log("Welcome to IIT Bombay To IAS");

/* Apply centralized values from js/config.js to the page.
   Hooks: data-cfg-href (link), data-cfg-text (text), data-cfg-src (image). */
function applySiteConfig() {
    const cfg = window.SITE_CONFIG;
    if (!cfg) return;

    document.querySelectorAll("[data-cfg-href]").forEach(function (el) {
        const value = cfg[el.getAttribute("data-cfg-href")];
        if (value) el.setAttribute("href", value);
    });

    document.querySelectorAll("[data-cfg-text]").forEach(function (el) {
        const value = cfg[el.getAttribute("data-cfg-text")];
        if (value) el.textContent = value;
    });

    document.querySelectorAll("[data-cfg-src]").forEach(function (el) {
        const value = cfg[el.getAttribute("data-cfg-src")];
        if (value) el.setAttribute("src", value);
    });
}

/* Responsive navigation: inject a hamburger toggle and wire it up.
   Works on every page since the navbar markup is shared. */
document.addEventListener("DOMContentLoaded", function () {
    applySiteConfig();

    const nav = document.querySelector("nav");
    if (!nav) return;

    const logo = nav.querySelector(".logo");
    if (!logo) return;

    const toggle = document.createElement("button");
    toggle.className = "menu-toggle";
    toggle.setAttribute("aria-label", "Toggle navigation menu");
    toggle.setAttribute("aria-expanded", "false");
    toggle.innerHTML = "<span></span><span></span><span></span>";

    logo.insertAdjacentElement("afterend", toggle);

    toggle.addEventListener("click", function () {
        const isOpen = nav.classList.toggle("nav-open");
        toggle.setAttribute("aria-expanded", String(isOpen));
    });

    // Close the menu after tapping any link (mobile).
    nav.querySelectorAll("ul a").forEach(function (link) {
        link.addEventListener("click", function () {
            nav.classList.remove("nav-open");
            toggle.setAttribute("aria-expanded", "false");
        });
    });
});