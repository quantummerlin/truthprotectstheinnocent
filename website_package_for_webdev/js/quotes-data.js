// =============================================================================
// QUOTES DATA FOR WEBSITE TICKER
// Public Comments Analysis — Trevallion-Birmingham Family Case
// Updated: March 8, 2026 — Batches 1 + 2
// =============================================================================

const QUOTES_DATA = [
    // =========================================================================
    // BATCH 1 — Meloni Facebook Video — March 2026 — 243 comments
    // =========================================================================
    {
        text: "This family was living in peace, joy and serenity. They asked nothing of anyone.",
        author: "Lina Haddad",
        country: "Italy",
        category: "family",
        batch: 1,
        rating: "diamond"
    },
    {
        text: "I have never agreed with Giorgia but with this speech I feel like applauding her!",
        author: "Luisa Carbone",
        country: "Italy",
        category: "supportive",
        batch: 1,
        rating: "gold"
    },
    {
        text: "The 'protection' is creating the trauma — these poor children will carry this with them for life.",
        author: "Giusi Finielli",
        country: "Italy",
        category: "family",
        batch: 1,
        rating: "gold"
    },
    {
        text: "They were perfectly fine — not drugged, not beaten.",
        author: "Arabella Vallone",
        country: "Italy",
        category: "family",
        batch: 1,
        rating: "gold"
    },
    {
        text: "Did I hear right? In Italy? The land of FAMILY?! Ripping children away from their families is sinister, wicked and sick.",
        author: "Donna Lee Corboy",
        country: "United Kingdom",
        category: "international",
        batch: 1,
        rating: "gold"
    },
    {
        text: "The quasi-mafia apparatus — the Bibbiano model, forever and across all of Italy.",
        author: "Lorella Proserpio",
        country: "Italy",
        category: "corruption",
        batch: 1,
        rating: "gold"
    },
    {
        text: "Every day is traumatic for the children. Make the children of Catherine and Nathan come home — there is NO valid reason to divide this family.",
        author: "Daniela Lozar",
        country: "Italy",
        category: "action",
        batch: 1,
        rating: "gold"
    },
    {
        text: "The system is rotten and based only on economic interest — to self-finance and sustain foster homes and social workers.",
        author: "Antonio Scerbo",
        country: "Italy",
        category: "corruption",
        batch: 1,
        rating: "gold"
    },
    {
        text: "35,000 children removed from families in Italy — where is the outrage?",
        author: "Antoinette Carlino",
        country: "Italy",
        category: "corruption",
        batch: 1,
        rating: "silver"
    },
    {
        text: "€300 per day per child in foster care. Follow the money.",
        author: "Cristinaeumberto Fiorello",
        country: "Italy",
        category: "corruption",
        batch: 1,
        rating: "silver"
    },
    
    // =========================================================================
    // BATCH 2 — Pozzolo Facebook Post — March 8, 2026 — 520 comments
    // Women's Day Irony — Siblings Separated Revealed
    // =========================================================================
    {
        text: "The children are learning from the Italian State that bullying always wins.",
        author: "Cianti Ivano",
        country: "Italy",
        category: "family",
        batch: 2,
        rating: "diamond"
    },
    {
        text: "Orphans of living parents.",
        author: "Marzia Teixeira",
        country: "Italy",
        category: "family",
        batch: 2,
        rating: "gold"
    },
    {
        text: "My mother was driven mad because they told her I was dead. I beg you to intervene immediately.",
        author: "Mariella Papavero",
        country: "Italy",
        category: "personal",
        batch: 2,
        rating: "gold"
    },
    {
        text: "They are separated from each other too — they are annihilating them.",
        author: "Marisa Mansutti",
        country: "Italy",
        category: "family",
        batch: 2,
        rating: "gold"
    },
    {
        text: "The State is strong with the weak and weak with the strong.",
        author: "Cristina Belardinelli",
        country: "Italy",
        category: "corruption",
        batch: 2,
        rating: "gold"
    },
    {
        text: "Today is Women's Day — a day to abolish because not even one woman treated like this mother is acceptable. This is the festival of the JUDGES.",
        author: "Faby Tony",
        country: "Italy",
        category: "action",
        batch: 2,
        rating: "gold"
    },
    {
        text: "I hope the mother and father don't collapse and don't make an extreme gesture.",
        author: "Primavera Livia",
        country: "Italy",
        category: "action",
        batch: 2,
        rating: "gold"
    },
    {
        text: "The lawyers should denounce the judge and social worker for psychological abuse of minors.",
        author: "Claudio Alberti",
        country: "Italy",
        category: "legal",
        batch: 2,
        rating: "gold"
    },
    {
        text: "They have already destroyed this family — not 'are destroying' — ALREADY DESTROYED.",
        author: "Multiple Commenters",
        country: "Italy",
        category: "family",
        batch: 2,
        rating: "gold"
    },
    {
        text: "Judges and social workers should be investigated. They bear responsibility if the desperate woman takes extreme action.",
        author: "Domenico Ventura",
        country: "Italy",
        category: "legal",
        batch: 2,
        rating: "gold"
    },
    {
        text: "Not just that family — they have destroyed many, creating an insurmountable wall.",
        author: "Vita Maria Nardiello",
        country: "Italy",
        category: "corruption",
        batch: 2,
        rating: "silver"
    },
    {
        text: "Mattarella, where are you? If you truly honour your republic, do something for these children.",
        author: "Domenica Tronconi",
        country: "Italy",
        category: "action",
        batch: 2,
        rating: "silver"
    },
    {
        text: "The law should protect the weakest — not divide them from their mothers.",
        author: "Angelina Ambrosio",
        country: "Italy",
        category: "legal",
        batch: 2,
        rating: "silver"
    },
    {
        text: "In Italy a magistrate and a social worker have more power than Louis XIV ever had.",
        author: "Oliviero Lanzoni",
        country: "Italy",
        category: "corruption",
        batch: 2,
        rating: "silver"
    },
    {
        text: "Another family — Valentina's family — 135 days, 3 children taken. Zero media coverage.",
        author: "Olha Filimonova",
        country: "Ukraine",
        category: "international",
        batch: 2,
        rating: "silver"
    },
    {
        text: "30,000 minors taken from their families... and they speak only of one family.",
        author: "Cristian Pesaresi",
        country: "Italy",
        category: "corruption",
        batch: 2,
        rating: "silver"
    }
];

// =============================================================================
// STATS — Updated March 8, 2026
// =============================================================================

const QUOTES_STATS = {
    totalComments: 1344,
    uniqueVoices: 1130,
    supportFamily: 96,
    supportSeparation: 4,
    countries: 12,
    lastUpdated: "March 12, 2026",
    batches: [
        { 
            number: 1, 
            source: "Meloni Facebook Video", 
            date: "March 2026", 
            count: 243,
            uniqueVoices: 198,
            countries: 8
        },
        { 
            number: 2, 
            source: "Pozzolo Facebook Post", 
            date: "March 8, 2026", 
            count: 520,
            uniqueVoices: 480,
            countries: 5,
            notes: "Women's Day, siblings separated revealed"
        },
        {
            number: 3,
            source: "Pozzolo Facebook Reel",
            date: "March 10, 2026",
            count: 472,
            uniqueVoices: 380,
            countries: 4,
            notes: "Viral reel — 115-like top comment asking what lies behind the persecution"
        },
        {
            number: 4,
            source: "RAI Ore 14 YouTube",
            date: "March 9, 2026",
            count: 109,
            uniqueVoices: 72,
            countries: 3,
            notes: "Italian national public broadcaster, 6.5M subscribers, 5700+ views, 82% support — most credible mainstream figure"
        }
    ]
};

// =============================================================================
// COUNTRY FLAGS
// =============================================================================

const COUNTRY_FLAGS = {
    "Italy": "🇮🇹",
    "United Kingdom": "🇬🇧",
    "Hungary": "🇭🇺",
    "Armenia": "🇦🇲",
    "Ukraine": "🇺🇦",
    "Romania": "🇷🇴",
    "Australia": "🇦🇺",
    "International": "🌍"
};

// =============================================================================
// CATEGORIES
// =============================================================================

const CATEGORIES = {
    "action": { name: "Demand Action", icon: "🔴" },
    "family": { name: "Family Focus", icon: "🟣" },
    "corruption": { name: "Corruption/Money", icon: "🟠" },
    "skeptical": { name: "Words Not Deeds", icon: "🟡" },
    "supportive": { name: "Supportive", icon: "🟢" },
    "legal": { name: "Legal Reform", icon: "🔵" },
    "international": { name: "International", icon: "🌍" },
    "personal": { name: "Personal Story", icon: "💜" }
};

// =============================================================================
// HELPER FUNCTIONS
// =============================================================================

function getQuotesByCategory(category) {
    return QUOTES_DATA.filter(q => q.category === category);
}

function getQuotesByBatch(batchNumber) {
    return QUOTES_DATA.filter(q => q.batch === batchNumber);
}

function getDiamondQuotes() {
    return QUOTES_DATA.filter(q => q.rating === "diamond");
}

function getGoldQuotes() {
    return QUOTES_DATA.filter(q => q.rating === "gold");
}

function getRandomQuote() {
    return QUOTES_DATA[Math.floor(Math.random() * QUOTES_DATA.length)];
}

// Export
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { 
        QUOTES_DATA, 
        QUOTES_STATS, 
        COUNTRY_FLAGS, 
        CATEGORIES,
        getQuotesByCategory,
        getQuotesByBatch,
        getDiamondQuotes,
        getGoldQuotes,
        getRandomQuote
    };
}