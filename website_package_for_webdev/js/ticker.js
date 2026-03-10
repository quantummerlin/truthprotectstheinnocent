// =============================================================================
// TICKER FUNCTIONALITY — TRUTH PROTECTS THE INNOCENT
// Updated: March 8, 2026
// =============================================================================

// Initialize ticker when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initTicker();
    initStatsCounter();
});

// =============================================================================
// TICKER INITIALIZATION
// =============================================================================

function initTicker() {
    const tickerContent = document.querySelector('.ticker-content');
    if (!tickerContent) return;
    
    // Clear existing content
    tickerContent.innerHTML = '';
    
    // Build ticker HTML
    let tickerHTML = buildTickerHTML();
    
    // Duplicate content for seamless infinite scroll
    tickerContent.innerHTML = tickerHTML + tickerHTML;
    
    // Add click-to-pause functionality
    tickerContent.addEventListener('click', function() {
        const isPaused = this.style.animationPlayState === 'paused';
        this.style.animationPlayState = isPaused ? 'running' : 'paused';
    });
}

function buildTickerHTML() {
    let html = '';
    
    QUOTES_DATA.forEach((quote, index) => {
        const flag = COUNTRY_FLAGS[quote.country] || '🌍';
        const category = CATEGORIES[quote.category] || { icon: '⚪' };
        
        html += `
            <span class="ticker-item">
                <span class="quote-text">"${quote.text}"</span>
                <span class="quote-author">— ${quote.author}</span>
                <span class="quote-flag">${flag}</span>
            </span>
            <span class="ticker-separator">${category.icon}</span>
        `;
    });
    
    return html;
}

// =============================================================================
// ADD NEW QUOTE (for dynamic updates)
// =============================================================================

function addNewQuote(text, author, country, category) {
    const newQuote = {
        text: text,
        author: author,
        country: country,
        category: category,
        batch: QUOTES_STATS.batches.length + 1,
        rating: "bronze"
    };
    
    QUOTES_DATA.push(newQuote);
    QUOTES_STATS.totalComments++;
    QUOTES_STATS.uniqueVoices++;
    
    // Rebuild ticker
    initTicker();
    
    console.log('New quote added:', newQuote);
}

// =============================================================================
// STATS COUNTER
// =============================================================================

function initStatsCounter() {
    const statsContainer = document.querySelector('.stats-counter');
    if (!statsContainer) return;
    
    statsContainer.innerHTML = `
        <div class="stat-item">
            <span class="stat-number" id="stat-comments">${QUOTES_STATS.totalComments.toLocaleString()}</span>
            <span class="stat-label">Comments Analysed</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" id="stat-voices">${QUOTES_STATS.uniqueVoices.toLocaleString()}</span>
            <span class="stat-label">Unique Voices</span>
        </div>
        <div class="stat-item">
            <span class="stat-number stat-highlight" id="stat-support">${QUOTES_STATS.supportFamily}%</span>
            <span class="stat-label">Support Family</span>
        </div>
        <div class="stat-item">
            <span class="stat-number stat-warning" id="stat-separation">${QUOTES_STATS.supportSeparation}%</span>
            <span class="stat-label">Support Separation</span>
        </div>
        <div class="stat-item">
            <span class="stat-number" id="stat-countries">${QUOTES_STATS.countries}+</span>
            <span class="stat-label">Countries</span>
        </div>
    `;
}

// =============================================================================
// ANIMATE COUNTERS (optional animation on scroll)
// =============================================================================

function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.innerText.replace(/[^0-9]/g, ''));
        const suffix = counter.innerText.replace(/[0-9]/g, '');
        let current = 0;
        const increment = target / 50;
        const duration = 1500;
        const stepTime = duration / 50;
        
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.innerText = target + suffix;
                clearInterval(timer);
            } else {
                counter.innerText = Math.floor(current) + suffix;
            }
        }, stepTime);
    });
}

// =============================================================================
// FILTER QUOTES BY CATEGORY
// =============================================================================

function filterByCategory(category) {
    const tickerContent = document.querySelector('.ticker-content');
    if (!tickerContent) return;
    
    let filteredQuotes = QUOTES_DATA;
    
    if (category && category !== 'all') {
        filteredQuotes = QUOTES_DATA.filter(q => q.category === category);
    }
    
    let html = '';
    filteredQuotes.forEach(quote => {
        const flag = COUNTRY_FLAGS[quote.country] || '🌍';
        const cat = CATEGORIES[quote.category] || { icon: '⚪' };
        
        html += `
            <span class="ticker-item">
                <span class="quote-text">"${quote.text}"</span>
                <span class="quote-author">— ${quote.author}</span>
                <span class="quote-flag">${flag}</span>
            </span>
            <span class="ticker-separator">${cat.icon}</span>
        `;
    });
    
    tickerContent.innerHTML = html + html;
}

// =============================================================================
// EXPORT FUNCTIONS
// =============================================================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initTicker,
        initStatsCounter,
        addNewQuote,
        animateCounters,
        filterByCategory
    };
}