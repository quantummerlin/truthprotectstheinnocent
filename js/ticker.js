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
    var pauseIndicator = document.getElementById('pause-indicator');
    var tickerWrapper = document.getElementById('quotes-ticker');

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

    // Whole wrapper is clickable to pause/resume
    if (tickerWrapper) {
        tickerWrapper.addEventListener('click', function() {
            var isPaused = tickerScroll.classList.toggle('paused');
            tickerWrapper.classList.toggle('is-paused', isPaused);
            if (pauseIndicator) {
                if (isPaused) {
                    pauseIndicator.textContent = '\u23F8 PAUSED \u2014 CLICK TO RESUME';
                    pauseIndicator.classList.add('visible');
                } else {
                    pauseIndicator.classList.remove('visible');
                }
            }
        });
    }

    updateStats();
}

function createTickerItem(quote) {
    var flag = (typeof COUNTRY_FLAGS !== 'undefined' && COUNTRY_FLAGS[quote.country]) ? COUNTRY_FLAGS[quote.country] : '\uD83C\uDF0D';
    return '<div class="ticker-item" data-category="' + quote.category + '">' +
        '<span class="ticker-flag">' + flag + '</span>' +
        '<span class="ticker-quote">' + quote.text + '</span>' +
        '<span class="ticker-author">' + quote.author + '</span>' +
    '</div>';
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
