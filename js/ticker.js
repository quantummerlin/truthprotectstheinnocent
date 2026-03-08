/*
===========================================
TICKER JAVASCRIPT
===========================================
*/

document.addEventListener('DOMContentLoaded', function() {
    initTicker();
});

function getDailyQuote() {
    var daysSinceEpoch = Math.floor(Date.now() / 86400000);
    var idx = daysSinceEpoch % QUOTES_DATA.length;
    return QUOTES_DATA[idx];
}

function initTicker() {
    var tickerScroll = document.getElementById('ticker-scroll');

    if (!tickerScroll) {
        console.warn('Ticker element not found');
        return;
    }

    var qotd = getDailyQuote();
    var tickerHTML = createQOTDItem(qotd);

    // All quotes x2 for seamless loop
    QUOTES_DATA.forEach(function(quote) {
        tickerHTML += createTickerItem(quote);
    });
    QUOTES_DATA.forEach(function(quote) {
        tickerHTML += createTickerItem(quote);
    });

    tickerScroll.innerHTML = tickerHTML;

    // Pause scroll on hover so user can read; resume on mouse-leave
    tickerScroll.addEventListener('mouseenter', function() {
        this.style.animationPlayState = 'paused';
    });
    tickerScroll.addEventListener('mouseleave', function() {
        this.style.animationPlayState = 'running';
    });

    updateStats();
    injectHomepageVoices();
}

function createQOTDItem(quote) {
    var flag = (typeof COUNTRY_FLAGS !== 'undefined' && COUNTRY_FLAGS[quote.country]) ? COUNTRY_FLAGS[quote.country] : '\uD83C\uDF0D';
    return '<a href="/public-voice/" class="ticker-item ticker-qotd" data-category="' + quote.category + '">' +
        '<span class="ticker-qotd-label">\u2B50 Today</span>' +
        '<span class="ticker-flag">' + flag + '</span>' +
        '<span class="ticker-quote">' + quote.text + '</span>' +
        '<span class="ticker-author">' + quote.author + '</span>' +
    '</a>';
}

function createTickerItem(quote) {
    var flag = (typeof COUNTRY_FLAGS !== 'undefined' && COUNTRY_FLAGS[quote.country]) ? COUNTRY_FLAGS[quote.country] : '\uD83C\uDF0D';
    return '<a href="/public-voice/" class="ticker-item" data-category="' + quote.category + '">' +
        '<span class="ticker-flag">' + flag + '</span>' +
        '<span class="ticker-quote">' + quote.text + '</span>' +
        '<span class="ticker-author">' + quote.author + '</span>' +
    '</a>';
}

function updateStats() {
    var statsNumber = document.querySelector('.ticker-stats-number');
    if (statsNumber && typeof QUOTES_STATS !== 'undefined') {
        statsNumber.textContent = QUOTES_STATS.totalComments;
    }
}

// Inject 3 random voices into homepage #public-voices-strip if present
function injectHomepageVoices() {
    var strip = document.getElementById('public-voices-strip');
    if (!strip || typeof QUOTES_DATA === 'undefined') return;

    // Pick 3 diverse voices (one diamond, one gold, one random)
    var diamonds = QUOTES_DATA.filter(function(q){ return q.rating === 'diamond'; });
    var golds    = QUOTES_DATA.filter(function(q){ return q.rating === 'gold'; });
    var day      = Math.floor(Date.now() / 86400000);

    var picks = [
        diamonds[day % diamonds.length],
        golds[(day + 1) % golds.length],
        QUOTES_DATA[(day * 7 + 3) % QUOTES_DATA.length]
    ];

    strip.innerHTML = picks.map(function(q) {
        var flag = (typeof COUNTRY_FLAGS !== 'undefined' && COUNTRY_FLAGS[q.country]) ? COUNTRY_FLAGS[q.country] : '\uD83C\uDF0D';
        return '<div class="pv-strip-card">' +
            '<p class="pv-strip-quote">' + q.text + '</p>' +
            '<div class="pv-strip-meta">' + flag + ' <strong>' + q.author + '</strong> \u2014 ' + q.country + '</div>' +
        '</div>';
    }).join('');
}

function addNewQuote(quoteObj) {
    QUOTES_DATA.push(quoteObj);
    if (typeof QUOTES_STATS !== 'undefined') QUOTES_STATS.totalComments++;

    var tickerScroll = document.getElementById('ticker-scroll');
    if (tickerScroll) {
        var item = createTickerItem(quoteObj);
        tickerScroll.innerHTML += item + item;
    }

    updateStats();
}
