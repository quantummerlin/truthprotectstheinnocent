/*
===========================================
QUOTES DATA FILE
===========================================
All quotes from public comments - easy to add more
===========================================
*/

const QUOTES_DATA = [
    // ACTION - Demanding immediate action
    {
        text: "Order the release of these children. We can't take it anymore. Do it as if they were your children — you who are a mother. NOW!",
        author: "Moraldo Canale",
        country: "Italy",
        category: "action"
    },
    {
        text: "Please Giorgia, don't talk — DO something.",
        author: "Giuseppina Rago",
        country: "Italy",
        category: "action"
    },
    {
        text: "Every day is traumatic for the children. Make the children of Catherine and Nathan come home — there is NO valid reason to divide this family.",
        author: "Daniela Lozar",
        country: "Italy",
        category: "action"
    },
    {
        text: "Finally release these children from foster homes. We can't wait for bureaucratic timescales — children grow up fast — with severe trauma.",
        author: "Jane Torrisi",
        country: "Italy",
        category: "action"
    },
    {
        text: "President Meloni, you have the power and the moral duty — since you are a woman and a mother — to help these children. Put an end to this sadistic and perverse torment.",
        author: "Nadia Zandonà",
        country: "Italy",
        category: "action"
    },
    {
        text: "Release those children and put those who caused all this disgrace into the foster home instead!",
        author: "Alfonso Cifolelli",
        country: "Italy",
        category: "action"
    },
    {
        text: "Do something, stop just talking!",
        author: "Lidia Carli",
        country: "Italy",
        category: "action"
    },
    {
        text: "MOVE IT! We can't take it anymore!",
        author: "Elena Spironello",
        country: "Italy",
        category: "action"
    },
    {
        text: "Send inspectors to the foster homes instead of talking for election spots!",
        author: "Velia Altigondo",
        country: "Italy",
        category: "action"
    },
    {
        text: "Help these children!",
        author: "Piscopo Gerardo",
        country: "Italy",
        category: "action"
    },

    // FAMILY - Specifically naming the family
    {
        text: "This family was living in peace, joy and serenity. They asked nothing of anyone. They certainly had no need of socio-welfare re-education from ignorant people with great prejudices.",
        author: "Lina Haddad",
        country: "Italy",
        category: "family"
    },
    {
        text: "Make Catherine and Nathan the parents they were before this disaster. Leave Italy a reason to be grateful to you for something done well.",
        author: "Lucia Ruocco",
        country: "Italy",
        category: "family"
    },
    {
        text: "They were perfectly fine — not drugged, not beaten.",
        author: "Arabella Vallone",
        country: "Italy",
        category: "family"
    },
    {
        text: "The 'protection' is creating the trauma — these poor children will carry this with them for life.",
        author: "Giusi Finielli",
        country: "Italy",
        category: "family"
    },
    {
        text: "The 'Famiglia del Bosco' — hated by the powers that be.",
        author: "Caterina Ciccone",
        country: "Italy",
        category: "family"
    },
    {
        text: "What did these poor parents do? They wanted to educate their children in a sober manner. They neither mistreated nor denied love.",
        author: "Valentina Di Gaetano",
        country: "Italy",
        category: "family"
    },

    // CORRUPTION - Systemic issues, money, Bibbiano
    {
        text: "Social workers make €300 per day per child.",
        author: "Cristinaeumberto Fiorello",
        country: "Italy",
        category: "corruption"
    },
    {
        text: "I know a family in Umbria with a 'park' of 80 foster children held hostage until age 18.",
        author: "Giovanna Rossi",
        country: "Italy",
        category: "corruption"
    },
    {
        text: "Let's not forget Bibbiano. How many lies do social workers tell just to take children from families?",
        author: "Nicoletta Mognato",
        country: "Italy",
        category: "corruption"
    },
    {
        text: "The quasi-mafia apparatus that manages this issue — the Bibbiano model, forever and across all of Italy.",
        author: "Lorella Proserpio",
        country: "Italy",
        category: "corruption"
    },
    {
        text: "35,000 children removed.",
        author: "Antoinette Carlino",
        country: "Italy",
        category: "corruption"
    },
    {
        text: "The system is rotten and based only on economic interest — to self-finance and sustain foster homes and social workers, guaranteeing their salaries.",
        author: "Antonio Scerbo",
        country: "Italy",
        category: "corruption"
    },

    // INTERNATIONAL - Non-Italian commenters
    {
        text: "Did I hear right? There is no registration or system that covers all these cases? Children are 'missing' in the system? In Italy? The land of FAMILY?! Ripping children away from their families is sinister, wicked and sick.",
        author: "Donna Lee Corboy",
        country: "United Kingdom",
        category: "international"
    },
    {
        text: "The entire social services system must be reformed. Instead of giving money to the war machine, invest in the Italian people — children are the future.",
        author: "Donna Lee Corboy",
        country: "United Kingdom",
        category: "international"
    },
    {
        text: "This should not have happened! Reunite the family immediately!",
        author: "Rita Horvath",
        country: "Hungary",
        category: "international"
    },
    {
        text: "Please intervene for the love of God — these children deserve to live with love with their parents.",
        author: "Vera Movsesyan",
        country: "Armenia",
        category: "international"
    },
    {
        text: "These children are not Italian.",
        author: "Mariana Lant",
        country: "International",
        category: "international"
    },

    // SKEPTICAL - Cross-party support
    {
        text: "I have never agreed with Giorgia but with this speech I feel like applauding her!",
        author: "Luisa Carbone",
        country: "Italy",
        category: "skeptical"
    },
    {
        text: "I don't approve of her as Prime Minister but on this — absolutely yes.",
        author: "Natascia Piscitelli",
        country: "Italy",
        category: "skeptical"
    },
    {
        text: "Look at that — I had to agree with her!!!",
        author: "Lucia Grimaldi",
        country: "Italy",
        category: "skeptical"
    },
    {
        text: "Words, words, words... if they were real she would have already acted.",
        author: "Cinzia Lucin",
        country: "Italy",
        category: "skeptical"
    },
    {
        text: "Good words — but meanwhile what is being done for this family?",
        author: "Noemi Milano",
        country: "Italy",
        category: "skeptical"
    },

    // LEGAL - Calls for legal reform
    {
        text: "We must separate judges — not families.",
        author: "Filippo Pagliai",
        country: "Italy",
        category: "legal"
    },
    {
        text: "A decree law can be done immediately — just as you did with the false pandemic.",
        author: "Teresa Falcone",
        country: "Italy",
        category: "legal"
    },
    {
        text: "I emailed President Mattarella directly. I urge everyone to do the same.",
        author: "Antonella Merlo",
        country: "Italy",
        category: "legal"
    },
    {
        text: "The parents should appeal to the European Court of Human Rights — this is the only solution I see for their salvation.",
        author: "Stefano Zacconi",
        country: "Italy",
        category: "legal"
    },
    {
        text: "Change the law that permits these child kidnappings from families.",
        author: "Cinzia Colle",
        country: "Italy",
        category: "legal"
    }
];

const QUOTES_STATS = {
    totalComments: 243,
    uniqueVoices: 198,
    supportFamily: 100,
    supportSeparation: 0,
    countries: 8,
    lastUpdated: "March 2026"
};

const COUNTRY_FLAGS = {
    "Italy": "🇮🇹",
    "United Kingdom": "🇬🇧",
    "Germany": "🇩🇪",
    "France": "🇫🇷",
    "Spain": "🇪🇸",
    "Hungary": "🇭🇺",
    "Armenia": "🇦🇲",
    "International": "🌍",
    "Australia": "🇦🇺",
    "USA": "🇺🇸"
};