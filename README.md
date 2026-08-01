# IIT Bombay To IAS

A responsive, static marketing website for **IIT Bombay To IAS** — an exam-prep brand
for UPSC, BPSC and other competitive exams. It promotes paid courses, a planned
AI-powered learning platform, and free YouTube resources.

Built with plain **HTML, CSS and vanilla JavaScript** — no build step required.

## Project structure

```
index.html          Home page
ai-platform.html    AI platform (coming soon) page
courses.html        Course catalog
resources.html      Free resources
about.html          About / founder
contact.html        Contact details
roadmap.html        Product roadmap
courses/            Individual course pages
css/style.css       All site styles (responsive)
js/config.js        Central site settings (links, contact, socials)
js/script.js        Applies config + responsive navigation (hamburger menu)
images/             Logo and course images
```

## Managing site content

Common values (enrollment form link, email, phone, and social links) live in one
place: [`js/config.js`](js/config.js). Edit a value there once and it updates on
every page automatically — no HTML editing needed.

```js
window.SITE_CONFIG = {
  enrollFormUrl: "https://forms.gle/...",   // "Enroll Now" buttons
  email: "...",                              // contact email
  phone: "...",                              // mobile / WhatsApp
  telegramUrl: "...",
  instagramUrl: "...",
  youtubeChannelUrl: "...",
  youtubePlaylistUrl: "..."
};
```

In the HTML, elements pick up these values through `data-cfg-href` (links) and
`data-cfg-text` (text) hooks, which `js/script.js` fills in on page load.

## Run locally

Just open `index.html` in a browser, or serve the folder:

```powershell
# Python 3
python -m http.server 8000
# then visit http://localhost:8000
```

## Responsive design

The layout adapts across screen sizes using fluid typography (`clamp()`) and CSS
media queries:

- **Phones (≤600px)** – stacked buttons, condensed spacing, hamburger menu.
- **Tablets (≤900px)** – hamburger navigation, single-column course layout.
- **Laptops / desktops** – full horizontal navbar and multi-column grids.
- **Large monitors (≥1600px)** – content is capped and centered for readability.

The navigation collapses into a hamburger menu (added by `js/script.js`) on
smaller screens.

## Deploy to GitHub Pages

This is a **project site** hosted on the `Abhi1191` account in a repository named
`iitbombaytoias`, so it publishes at a sub-path of that account's Pages domain.

1. Make sure `index.html` and the `css/`, `js/`, `images/` folders sit at the
   **root** of the repository (not inside a sub-folder).
2. Create an empty repository named `iitbombaytoias` at
   https://github.com/Abhi1191, then commit and push:

   ```powershell
   git init
   git add .
   git commit -m "Responsive site update"
   git branch -M main
   git remote add origin https://github.com/aakash563/iitbombaytoias.git
   git push -u origin main
   ```

3. In the repo, go to **Settings → Pages** and confirm the source is
   **Deploy from a branch**, branch **main**, folder **/ (root)**.
4. The site goes live at **https://aakash563.github.io/iitbombaytoias/** (allow a
   minute for the first build).
