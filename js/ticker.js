/*
===========================================
TICKER JAVASCRIPT
===========================================
*/

document.addEventListener('DOMContentLoaded', function() {
    initTicker();
});

function initTicker() {
    const tickerScroll = document.getElementById('ticker-scroll');
    const pauseIndicator = document.getElementById('pause-indicator');
    
    if (!tickerScroll) {
        console.warn('Ticker element not found');
        return;
    }
    
    let tickerHTML = '';
    
    // Duplicate content for seamless looping
    QUOTES_DATA.forEach(quote => {
        tickerHTML += createTickerItem(quote);
    });
    QUOTES_DATA.forEach(quote => {
        tickerHTML += createTickerItem(quote);
    });
    
    tickerScroll.innerHTML = tickerHTML;
    
    // Pause on click
    tickerScroll.addEventListener('click', function() {
        this.classList.toggle('paused');
        if (pauseIndicator) {
            pauseIndicator.classList.toggle('visible');
        }
    });
    
    updateStats();
}

function createTickerItem(quote) {
    const flag = COUNTRY_FLAGS[quote.country] || '🌍';
    return '<div class="ticker-item" data-category="' + quote.category + '">' +
        '<span class="ticker-flag">' + flag + '</span>' +
        '<span class="ticker-quote">' + quote.text + '</span>' +
        '<span class="ticker-author">' + quote.author + '</span>' +
    '</div>';
}

function updateStats() {
    const statsNumber = document.querySelector('.ticker-stats-number');
    if (statsNumber) {
        statsNumber.textContent = QUOTES_STATS.totalComments;
    }
}

function addNewQuote(quoteObj) {
    QUOTES_DATA.push(quoteObj);
    QUOTES_STATS.totalComments++;
    
    const tickerScroll = document.getElementById('ticker-scroll');
    if (tickerScroll) {
        const item = createTickerItem(quoteObj);
        tickerScroll.innerHTML += item + item;
    }
    
    updateStats();
}