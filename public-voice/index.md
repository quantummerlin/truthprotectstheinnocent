---
layout: default
title: "Public Voice — 1,235 Voices Speak Out"
description: "1,235 public comments from Italy and around the world demanding the release of Utopia, Galorian and Blue Bell. 96% support the family. Voices from 12+ countries."
permalink: /public-voice/
lang: en
---

<style>
.pv-hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    padding: 4rem 0 3rem;
    color: white;
    text-align: center;
}
.pv-hero h1 { font-size: 2.5rem; font-weight: 900; margin-bottom: 1rem; }
.pv-hero p { font-size: 1.15rem; color: rgba(255,255,255,0.8); max-width: 700px; margin: 0 auto 2rem; }
.pv-hero-stats { display: flex; justify-content: center; flex-wrap: wrap; gap: 2rem; margin: 2rem 0; }
.pv-hero-stat { text-align: center; }
.pv-hero-stat .num { font-size: 3rem; font-weight: 900; color: #f39c12; line-height: 1; }
.pv-hero-stat .lbl { font-size: 0.85rem; color: rgba(255,255,255,0.65); text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

.pv-filters {
    background: white;
    padding: 0.85rem 0;
    border-bottom: 2px solid #e5e7eb;
    position: sticky;
    top: 70px;
    z-index: 100;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}
.pv-filter-inner {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    justify-content: flex-start;
    overflow-x: auto;
    padding: 0 1rem;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    -ms-overflow-style: none;
    flex-wrap: nowrap;
}
.pv-filter-inner::-webkit-scrollbar { display: none; }
.pv-filter-inner::before {
    content: 'Filter:';
    font-size: 0.75rem;
    font-weight: 700;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 1px;
    white-space: nowrap;
    flex-shrink: 0;
    margin-right: 0.25rem;
}
.pv-filter-btn {
    padding: 0.4rem 1rem;
    border-radius: 2rem;
    border: 2px solid #e5e7eb;
    background: white;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    color: #374151;
    white-space: nowrap;
    flex-shrink: 0;
}
.pv-filter-btn:hover, .pv-filter-btn.active { background: #1a1a2e; color: white; border-color: #1a1a2e; }
.pv-filter-btn[data-cat="action"].active { background: #e74c3c; border-color: #e74c3c; }
.pv-filter-btn[data-cat="family"].active { background: #9b59b6; border-color: #9b59b6; }
.pv-filter-btn[data-cat="corruption"].active { background: #e67e22; border-color: #e67e22; }
.pv-filter-btn[data-cat="international"].active { background: #1abc9c; border-color: #1abc9c; }
.pv-filter-btn[data-cat="skeptical"].active { background: #f39c12; border-color: #f39c12; }
.pv-filter-btn[data-cat="legal"].active { background: #3498db; border-color: #3498db; }
.pv-filter-btn[data-cat="personal"].active { background: #e91e8c; border-color: #e91e8c; }
.pv-filter-btn[data-cat="supportive"].active { background: #27ae60; border-color: #27ae60; }

.pv-search {
    padding: 0.4rem 1rem;
    border-radius: 2rem;
    border: 2px solid #e5e7eb;
    font-size: 0.85rem;
    width: 180px;
    min-width: 140px;
    flex-shrink: 0;
    outline: none;
}
.pv-search:focus { border-color: #1a1a2e; }

.pv-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
    padding: 3rem 0;
}
.pv-card {
    background: white;
    border-radius: 1rem;
    padding: 1.5rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    border-left: 4px solid #e5e7eb;
    transition: transform 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}
.pv-card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.12); }
.pv-card[data-category="action"] { border-left-color: #e74c3c; }
.pv-card[data-category="family"] { border-left-color: #9b59b6; }
.pv-card[data-category="corruption"] { border-left-color: #e67e22; }
.pv-card[data-category="international"] { border-left-color: #1abc9c; }
.pv-card[data-category="skeptical"] { border-left-color: #f39c12; }
.pv-card[data-category="legal"] { border-left-color: #3498db; }
.pv-card.hidden { display: none; }

.pv-quote {
    font-size: 0.95rem;
    line-height: 1.7;
    color: #374151;
    font-style: italic;
}
.pv-quote::before { content: '\201C'; }
.pv-quote::after { content: '\201D'; }
.pv-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: #6b7280;
}
.pv-flag { font-size: 1rem; }
.pv-author { color: #1a1a2e; }
.pv-cat-badge {
    margin-left: auto;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 0.2rem 0.6rem;
    border-radius: 1rem;
    font-weight: 700;
    background: #f3f4f6;
    color: #6b7280;
}
[data-category="action"] .pv-cat-badge { background: #fee2e2; color: #b91c1c; }
[data-category="family"] .pv-cat-badge { background: #f3e8ff; color: #7e22ce; }
[data-category="corruption"] .pv-cat-badge { background: #ffedd5; color: #c2410c; }
[data-category="international"] .pv-cat-badge { background: #d1fae5; color: #065f46; }
[data-category="skeptical"] .pv-cat-badge { background: #fef9c3; color: #854d0e; }
[data-category="legal"] .pv-cat-badge { background: #dbeafe; color: #1d4ed8; }

.pv-count-bar {
    background: #f9fafb;
    padding: 1.25rem 0;
    border-bottom: 1px solid #e5e7eb;
    text-align: center;
    font-size: 0.95rem;
    color: #6b7280;
}
.pv-count-bar strong { color: #111827; }
.pv-no-results { text-align: center; padding: 4rem 0; color: #6b7280; font-size: 1.1rem; display: none; }
</style>

<!-- Hero -->
<div class="pv-hero">
    <div class="container">
        <h1>The World Speaks Out</h1>
        <p>Hundreds of people — from Italy and around the world — have publicly commented across two sources, demanding the immediate return of Utopia, Galorian and Blue Bell to their parents.</p>
        <div class="pv-hero-stats">
            <div class="pv-hero-stat"><div class="num">1,235</div><div class="lbl">Public Comments</div></div>
            <div class="pv-hero-stat"><div class="num">1,058</div><div class="lbl">Unique Voices</div></div>
            <div class="pv-hero-stat"><div class="num">96%</div><div class="lbl">Support the Family</div></div>
            <div class="pv-hero-stat"><div class="num">12+</div><div class="lbl">Countries</div></div>
        </div>
        <p style="font-size: 0.85rem; color: rgba(255,255,255,0.5); margin-top: 1rem;">Audience intelligence data sourced from <a href="https://ai.quantummerlin.com" target="_blank" rel="noopener" style="color: #f39c12;">ai.quantummerlin.com</a> · Names anonymised per GDPR</p>
        <div style="display:flex;gap:2rem;justify-content:center;flex-wrap:wrap;margin-top:1rem;">
            <div style="background:rgba(255,255,255,0.08);border-radius:0.75rem;padding:0.75rem 1.25rem;font-size:0.85rem;color:rgba(255,255,255,0.7);">📣 Batch 1: Meloni Facebook · 243 comments</div>
            <div style="background:rgba(255,255,255,0.08);border-radius:0.75rem;padding:0.75rem 1.25rem;font-size:0.85rem;color:rgba(255,255,255,0.7);">📣 Batch 2: Pozzolo Facebook · 520 comments · March 8, 2026 (Women's Day)</div>
            <div style="background:rgba(243,156,18,0.15);border:1px solid rgba(243,156,18,0.3);border-radius:0.75rem;padding:0.75rem 1.25rem;font-size:0.85rem;color:rgba(255,255,255,0.85);">🆕 Batch 3: Pozzolo Facebook Reel · 472 comments · March 10, 2026</div>
        </div>
    </div>
</div>

<!-- Filter Bar -->
<div class="pv-filters">
    <div class="container">
        <div class="pv-filter-inner">
            <button class="pv-filter-btn active" data-cat="all">All Voices</button>
            <button class="pv-filter-btn" data-cat="action">⚡ Demanding Action</button>
            <button class="pv-filter-btn" data-cat="family">💜 For the Family</button>
            <button class="pv-filter-btn" data-cat="corruption">🔥 Corruption</button>
            <button class="pv-filter-btn" data-cat="international">🌍 International</button>
            <button class="pv-filter-btn" data-cat="skeptical">🤔 Cross-Party</button>
            <button class="pv-filter-btn" data-cat="legal">⚖️ Legal Reform</button>
            <button class="pv-filter-btn" data-cat="personal">💔 Personal Story</button>
            <button class="pv-filter-btn" data-cat="supportive">🟢 Supportive</button>
            <input type="search" class="pv-search" id="pv-search" placeholder="Search quotes…">
        </div>
    </div>
</div>

<!-- Count bar -->
<div class="pv-count-bar" id="pv-count-bar">
    Showing <strong id="pv-visible-count">—</strong> of <strong>1,235</strong> voices
</div>

<!-- Quote Grid -->
<div class="container">
    <div class="pv-grid" id="pv-grid"></div>
    <div class="pv-no-results" id="pv-no-results">No voices found for that filter. Try another category.</div>
</div>

<!-- CTA -->
<section class="section" style="background: #f9fafb; text-align: center;">
    <div class="container">
        <h2>Add Your Voice</h2>
        <p style="color: #6b7280; max-width: 600px; margin: 0 auto 2rem;">Join the hundreds already speaking out. Share this page, sign the petition, or write directly to Italian officials.</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
            <a href="/petition/" class="btn btn-primary">🇺🇳 Sign the UN Petition</a>
            <a href="/action/" class="btn btn-secondary">Write to Officials</a>
            <a href="/" class="btn btn-outline">Back to Home</a>
        </div>
        <!-- Data Compliance Notice -->
        <div style="margin-top: 2.5rem; padding: 1.5rem 2rem; background: white; border: 1px solid #e5e7eb; border-radius: 1rem; max-width: 800px; margin-left: auto; margin-right: auto; text-align: left;">
            <p style="color: #6b7280; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem;">🛡️ Data Source & Privacy Compliance</p>
            <p style="color: #6b7280; font-size: 0.85rem; line-height: 1.7; margin-bottom: 0.75rem;">The voices on this page are derived from <strong style="color: #374151;">audience intelligence reports</strong> generated by <a href="https://ai.quantummerlin.com" target="_blank" rel="noopener" style="color: #f39c12; font-weight: 600;">ai.quantummerlin.com</a>, analysing publicly visible comments on public Facebook posts.</p>
            <p style="color: #6b7280; font-size: 0.85rem; line-height: 1.7; margin-bottom: 0.75rem;">In accordance with <strong style="color: #374151;">GDPR</strong>, <strong style="color: #374151;">Italian privacy law (D.Lgs. 196/2003)</strong>, and the principle of <strong style="color: #374151;">contextual integrity</strong>: all commenter names are anonymised to first name and last initial; aggregate statistics are published freely; and quotes are presented in translated/paraphrased form. No verbatim quotes are published alongside identifying information.</p>
            <p style="color: #6b7280; font-size: 0.85rem; line-height: 1.7; margin: 0;"><strong style="color: #374151;">Removal requests:</strong> If you recognise your words and wish them removed, contact <a href="mailto:privacy@quantummerlin.com" style="color: #f39c12; font-weight: 600;">privacy@quantummerlin.com</a>. See our <a href="/privacy/" style="color: #f39c12; font-weight: 600;">Privacy Policy</a>.</p>
        </div>
    </div>
</section>

<script src="/js/quotes-data.js"></script>
<script>
(function() {
    const grid = document.getElementById('pv-grid');
    const noResults = document.getElementById('pv-no-results');
    const countEl = document.getElementById('pv-visible-count');
    const FLAGS = typeof COUNTRY_FLAGS !== 'undefined' ? COUNTRY_FLAGS : {};
    const CAT_LABELS = {
        action: 'Demanding Action',
        family: 'For the Family',
        corruption: 'Systemic Corruption',
        international: 'International',
        skeptical: 'Cross-Party',
        legal: 'Legal Reform',
        personal: 'Personal Story',
        supportive: 'Supportive'
    };

    // Render cards
    function renderCards(data) {
        grid.innerHTML = '';
        data.forEach(function(q) {
            const flag = FLAGS[q.country] || '🌍';
            const card = document.createElement('div');
            card.className = 'pv-card';
            card.dataset.category = q.category;
            card.innerHTML =
                '<p class="pv-quote">' + q.text + '</p>' +
                '<div class="pv-meta">' +
                    '<span class="pv-flag">' + flag + '</span>' +
                    '<span class="pv-author">' + q.author + '</span> &mdash; ' + q.country +
                    '<span class="pv-cat-badge">' + (CAT_LABELS[q.category] || q.category) + '</span>' +
                '</div>';
            grid.appendChild(card);
        });
    }

    // Filter + search
    let activeCat = 'all';
    let searchTerm = '';

    function applyFilter() {
        if (!grid) return;
        let filtered = typeof QUOTES_DATA !== 'undefined' ? QUOTES_DATA : [];
        if (activeCat !== 'all') filtered = filtered.filter(function(q){ return q.category === activeCat; });
        if (searchTerm) filtered = filtered.filter(function(q){
            return (q.text + q.author + q.country).toLowerCase().includes(searchTerm);
        });
        renderCards(filtered);
        countEl.textContent = filtered.length;
        noResults.style.display = filtered.length === 0 ? 'block' : 'none';
    }

    // Init
    if (typeof QUOTES_DATA !== 'undefined') {
        applyFilter();
    }

    // Filter buttons
    document.querySelectorAll('.pv-filter-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            document.querySelectorAll('.pv-filter-btn').forEach(function(b){ b.classList.remove('active'); });
            this.classList.add('active');
            activeCat = this.dataset.cat;
            applyFilter();
        });
    });

    // Search
    var searchBox = document.getElementById('pv-search');
    if (searchBox) {
        searchBox.addEventListener('input', function() {
            searchTerm = this.value.toLowerCase().trim();
            applyFilter();
        });
    }
})();
</script>
