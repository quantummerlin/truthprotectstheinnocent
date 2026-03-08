/*
===========================================
TICKER JAVASCRIPT
===========================================
*/

document.addEventListener('DOMContentLoaded', function() {
    initTicker();
});

function initTicker() {
    var tickerScroll = document.getElementById('ticker-scroll');

    if (!tickerScroll) {
        console.warn('Ticker element not found');
        return;
    }

    var tickerHTML = '';

    // Duplicate content for seamless looping
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
