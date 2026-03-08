# Installation Guide for Web Developer
## How to Add These Components to Your Site

---

## Quick Start (5 Minutes)

### 1. INCLUDE THE FILES

Copy these folders to your website:
```
/css/ticker.css
/js/quotes-data.js
/js/ticker.js
```

### 2. ADD THE TICKER (Bottom of Every Page)

Add this before `</body>`:
```html
<link rel="stylesheet" href="css/ticker.css">
<script src="js/quotes-data.js"></script>
<script src="js/ticker.js"></script>

<div id="quotes-ticker" class="ticker-wrapper">
    <div class="ticker-stats">
        <span class="ticker-stats-number">243</span>
        <span class="ticker-stats-label">VOICES</span>
    </div>
    <div class="ticker-scroll-container">
        <div class="ticker-scroll" id="ticker-scroll"></div>
    </div>
    <div class="ticker-pause-indicator" id="pause-indicator">⏸ PAUSED</div>
</div>
```

---

## TICKER OPTIONS

### Position: Bottom (Default)
The ticker sits at the bottom of the screen.

### Position: Top
Add class `ticker-top` to the wrapper:
```html
<div id="quotes-ticker" class="ticker-wrapper ticker-top">
```

### Speed
Edit `css/ticker.css` and change:
```css
--ticker-speed: 80s; /* Default: 80 seconds for one full scroll */
```

### Colors
Edit `css/ticker.css` and change:
```css
--ticker-bg: #1a1a2e;        /* Background color */
--ticker-accent: #f39c12;    /* Accent color */
--ticker-quote-color: #e0e0e0; /* Quote text color */
```

---

## ADDING NEW QUOTES

When you have new comments to add, edit `js/quotes-data.js`:

```javascript
// Add to the QUOTES_DATA array:
{
    text: "The English translation of the quote",
    author: "Name of person",
    country: "Italy", // or UK, Germany, etc.
    category: "action", // action, family, corruption, international, skeptical, legal
    original: "Original Italian text (optional)"
}
```

Then update the stats:
```javascript
const QUOTES_STATS = {
    totalComments: 243, // Update this number
    uniqueVoices: 198,  // Update this number
    // ...
}
```

---

## FULL PAGES

### Public Voice Page
Copy `/public-voice/public-voice.html` content to your page.
Requires: `quotes-data.js`

### Gold Quotes Page
Copy `/gold-quotes/gold-quotes.html` content to your page.
No dependencies.

### Stats Counter
Copy the component from `/components/stats-counter-component.html`
Place anywhere on your site.

---

## WORDPRESS

1. Upload CSS to your theme's `/css/` folder
2. Upload JS to your theme's `/js/` folder
3. Add ticker HTML to `footer.php` before `</body>`
4. Use shortcodes or page templates for full pages

---

## SQUARESPACE

1. Go to Settings → Advanced → Code Injection
2. Add CSS to Header section (wrapped in `<style>` tags)
3. Add JS to Footer section (wrapped in `<script>` tags)
4. Add ticker HTML to Footer section

---

## SHOPIFY

1. Go to Online Store → Themes → Edit Code
2. Add CSS to `theme.css.liquid`
3. Add JS to a new file in Assets folder
4. Add ticker HTML to `theme.liquid` before `</body>`

---

## TESTING

1. Open your site
2. The ticker should appear at the bottom
3. It should scroll automatically
4. Click to pause/unpause
5. Hover to pause temporarily

---

## TROUBLESHOOTING

**Ticker not showing:**
- Check CSS file is linked correctly
- Check z-index is high enough
- Check for JavaScript errors in console

**Ticker not scrolling:**
- Check `quotes-data.js` is loaded
- Check for JavaScript errors in console
- Check ticker-scroll element exists

**Ticker too fast/slow:**
- Edit `--ticker-speed` in CSS

---

## NEED HELP?

All components are self-contained HTML/CSS/JS.
They work on any platform that allows custom code.