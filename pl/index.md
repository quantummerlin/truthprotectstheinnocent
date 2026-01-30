---
layout: default
title: Home
lang: pl
---

<!-- Hero Section with Slideshow Background -->
<section class="hero">
    <div class="hero-slideshow">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-12.jpg" alt="" class="hero-slide active">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-19.jpg" alt="" class="hero-slide">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-26.jpg" alt="" class="hero-slide">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-33.jpg" alt="" class="hero-slide">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-40.jpg" alt="" class="hero-slide">
        <img src="/assets/images/testimonials/photo_2026-01-11_21-41-48.jpg" alt="" class="hero-slide">
    </div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
        <span class="hero-badge">⚠️ Pilne: rodzina rozdzielona</span>
        <h1>Prawda chroni niewinnych</h1>
        <p class="lead">Troje dzieci odebranych kochającym rodzicom we Włoszech. Trzy oficjalne uzasadnienia. Wszystkie trzy oficjalnie obalone.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Dzieci rozdzielone</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Fałszywe zarzuty</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Uzasadnione powody</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#share-now" class="btn btn-primary btn-lg">Udostępnij teraz</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">Zobacz dowody</a>
        </div>
    </div>
</section>

<script>
(function() {
    const slides = document.querySelectorAll('.hero-slide');
    let current = 0;
    setInterval(() => {
        slides[current].classList.remove('active');
        current = (current + 1) % slides.length;
        slides[current].classList.add('active');
    }, 5000);
})();
</script>

<!-- Meet The Family - Video Section -->
<section class="section">
    <div class="container">
        <div class="section-header">
            <h2>Poznaj rodzinę</h2>
            <p>To dzieci w centrum tej sprawy — zdrowe, szczęśliwe i dobrze rozwijające się przed odebraniem</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                    Twoja przeglądarka nie obsługuje wideo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Życie przed rozdzieleniem</div>
                    <p class="video-card-desc">Szczęśliwe dzieci żyjące blisko natury</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                    Twoja przeglądarka nie obsługuje wideo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Kochająca rodzina</div>
                    <p class="video-card-desc">Więź, którą władze rozrywają</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                    Twoja przeglądarka nie obsługuje wideo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Radość dzieciństwa</div>
                    <p class="video-card-desc">To, co dzieci utraciły</p>
                </div>
            </div>
        </div>
        
        <div class="quote-block" style="margin-top: 3rem;">
            "Te dzieci były zdrowe, szczęśliwe i dobrze się rozwijały. Teraz wykazują oznaki traumy spowodowanej samą interwencją, która miała je "chronić"."
            <cite>— Z wniosków oceny psychologicznej</cite>
        </div>
    </div>
</section>

<!-- What People Say About This Family -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>Co ludzie mówią o tej rodzinie</h2>
            <p>Świadectwa osób znających rodzinę Birmingham‑Trevallion</p>
        </div>
        
        <div class="testimonial-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-12.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-16.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-19.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-21.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-26.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-28.jpg" alt="Świadectwo" style="width: 100%; height: auto;">
            </div>
        </div>
        
        <div class="text-center mt-2">
            <p style="color: var(--color-gray-600); font-style: italic;">To prawdziwe wiadomości od osób, które znają rodzinę osobiście.</p>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark">
    <div class="container">
        <div class="section-header">
            <h2>Trzy fałszywe zarzuty</h2>
            <p style="color: var(--color-gray-400);">Każde oficjalne uzasadnienie zostało obalone przez włoskie władze</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Zarzut #1: „Dzieci niezaszczepione”</h4>
                        <span class="evidence-badge badge-disputed">OBALONE</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Zgromadzenie Chieti i Teramo potwierdziło, że dzieci były zaszczepione.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Źródło: oficjalne dokumenty regionalnego organu zdrowia</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Zarzut #2: „Dzieci nieuczone”</h4>
                        <span class="evidence-badge badge-disputed">OBALONE</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Ministerstwo Edukacji potwierdziło legalny homeschooling.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Ponad 15 000 dzieci we Włoszech uczy się w tym samym legalnym systemie.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Zarzut #3: „Dom niebezpieczny”</h4>
                        <span class="evidence-badge badge-disputed">OBALONE</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Certyfikowany geometra potwierdził, że konstrukcja nie jest zagrożona.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Źródło: profesjonalna ocena konstrukcji</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">Pytanie bez odpowiedzi:</strong> 
                <span style="color: var(--color-gray-300);">Skoro wszystkie trzy oficjalne uzasadnienia zostały obalone, na jakiej podstawie prawnej dzieci pozostają rozdzielone z rodzicami?</span>
            </div>
            
            <div class="text-center mt-2">
                <a href="/evidence/" class="btn btn-primary">Zobacz wszystkie dowody →</a>
            </div>
        </div>
    </div>
</section>

<!-- The Documented Harm -->
<section class="section impact-section">
    <div class="container">
        <div class="impact-content">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center;">
                <div>
                    <h2 style="color: white;">Udokumentowana szkoda</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">Wykwalifikowany psycholog przeprowadził ocenę dzieci po odebraniu. Wnioski były na tyle istotne, że psycholog zwołał formalną konferencję prasową.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Kluczowy wniosek:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">Dzieci wykazują teraz <strong>zachowania autouszkadzające</strong>, których <strong>nie było przed rozdzieleniem</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">Przed odebraniem dzieci opisywano jako zdrowe, szczęśliwe i dobrze rozwijające się. Żyły na zewnątrz, uczyły się z natury i miały ograniczony czas przed ekranem.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">„Ochrona” powoduje szkodę.</strong></p>
                </div>
                <div class="impact-video">
                    <video controls style="border-radius: 1rem;">
                        <source src="/assets/videos/family2.MOV" type="video/mp4">
                    </video>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- What You Can Do -->
<section class="section" id="share-now">
    <div class="container">
        <div class="section-header">
            <h2>Chcesz zrobić coś teraz?</h2>
            <p>Nie musisz wpłacać pieniędzy. Nie musisz się nigdzie zapisywać.</p>
        </div>
        
        <!-- The One Thing CTA - Chase Hughes style -->
        <div style="background: linear-gradient(135deg, #1e3a5f, #2d5a8a); border-radius: 1.5rem; padding: 3rem; text-align: center; max-width: 800px; margin: 0 auto;">
            <h3 style="color: #f59e0b; font-size: 1.5rem; margin-bottom: 1rem;">Nie potrzebujemy twoich pieniędzy. Nie potrzebujemy twoich danych.</h3>
            <h2 style="color: white; font-size: 2rem; margin-bottom: 1.5rem;">Potrzebujemy tylko, żebyś udostępnił ten link.</h2>
            
            <p style="color: var(--color-gray-300); font-size: 1.2rem; margin-bottom: 1.5rem;">Jedno udostępnienie właściwej osobie może zmienić wszystko. Dziennikarzowi. Urzędnikowi. Komuś, kto zna kogoś.</p>
            
            <p style="color: white; font-size: 1.1rem; margin-bottom: 2rem;"><strong>Udostępnienie tego pięciu osobom, którym ufasz, jest warte więcej niż jakakolwiek darowizna.</strong></p>
            
            <div style="background: rgba(255,255,255,0.1); border-radius: 0.5rem; padding: 1rem; margin-bottom: 1.5rem;">
                <code style="color: #f59e0b; font-size: 1.1rem; word-break: break-all;">truthprotectstheinnocent.quantummerlin.com</code>
            </div>
            
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <button onclick="navigator.clipboard.writeText('truthprotectstheinnocent.quantummerlin.com').then(()=>this.textContent='✓ Skopiowano!')" class="btn btn-primary btn-lg" style="background: white; color: var(--color-primary); min-width: 200px;">📋 Skopiuj link</button>
                <a href="https://wa.me/?text=Three%20children%20separated%20from%20loving%20parents.%20Three%20official%20reasons.%20All%20three%20proven%20false.%20truthprotectstheinnocent.quantummerlin.com" class="btn btn-lg" style="background: #25D366; color: white;">💬 WhatsApp</a>
            </div>
            
            <p style="color: var(--color-gray-400); font-size: 0.9rem; margin-top: 2rem; margin-bottom: 0;">Pomyśl o 5 osobach, którym to nie jest obojętne. Wyślij teraz, zanim zapomnisz.</p>
        </div>
        
        <!-- Secondary Actions -->
        <div class="action-grid" style="margin-top: 3rem;">
            <div class="action-card">
                <div class="action-icon">📧</div>
                <h3>Wyślij e‑mail do urzędników</h3>
                <p>Chcesz zrobić więcej? Wyślij list bezpośrednio do włoskich parlamentarzystów.</p>
                <a href="/action/#email" class="btn btn-outline">Pobierz list</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Media społecznościowe</h3>
                <p>Udostępniaj na swoich platformach gotowe posty i #TruthProtectsTheInnocent</p>
                <a href="/action/#share" class="btn btn-outline">Szablony udostępniania</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Kontakt z mediami</h3>
                <p>Znasz dziennikarza? Ta historia zasługuje na nagłośnienie. Przekaż dalej.</p>
                <a href="/action/#media" class="btn btn-outline">Materiały dla mediów</a>
            </div>
        </div>
    </div>
</section>

<!-- International Attention -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <h2>Międzynarodowa uwaga</h2>
                <p>Ta sprawa przyciągnęła uwagę na najwyższych szczeblach</p>
            </div>
            
            <div class="stats-grid" style="margin-bottom: 2rem;">
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇦🇺</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Ambasada Australii poinformowana</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇮🇹</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Włoscy urzędnicy powiadomieni</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🌍</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Wsparcie na świecie rośnie</div>
                </div>
            </div>
            
            <p class="text-center" style="font-size: 1.1rem;">Rodzina nie może publicznie zabierać głosu, gdy trwają postępowania prawne. <strong>Ale my możemy.</strong></p>
            <p class="text-center">Presja społeczna i uwaga międzynarodowa są kluczowe, aby zapewnić sprawiedliwe traktowanie tej sprawy.</p>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>Prawda musi zostać powiedziana</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Troje dzieci jest rozdzielonych z rodzicami na podstawie twierdzeń, które zostały obalone. Obecnie występują udokumentowane szkody psychologiczne. To nie jest ochrona dzieci — to niesprawiedliwość.</p>
            
            <div class="hero-cta">
                <a href="/evidence/" class="btn btn-primary btn-lg">Zobacz dowody</a>
                <a href="/action/" class="btn btn-secondary btn-lg">Działaj teraz</a>
            </div>
            
            <p style="margin-top: 2rem; color: var(--color-gray-500);">Zapisz tę stronę, aby otrzymywać aktualizacje. Udostępnij ją osobom, które wierzą w sprawiedliwość.</p>
        </div>
    </div>
</section>

<!-- Language Selector -->
<div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
    <div style="background: white; padding: 0.5rem; border-radius: 0.5rem; box-shadow: var(--shadow-lg);">
        <a href="/" style="padding: 0.25rem 0.5rem;">🇬🇧</a>
        <a href="/it/" style="padding: 0.25rem 0.5rem;">🇮🇹</a>
        <a href="/de/" style="padding: 0.25rem 0.5rem;">🇩🇪</a>
        <a href="/fr/" style="padding: 0.25rem 0.5rem;">🇫🇷</a>
        <a href="/es/" style="padding: 0.25rem 0.5rem;">🇪🇸</a>
        <a href="/pt/" style="padding: 0.25rem 0.5rem;">🇵🇹</a>
        <a href="/ru/" style="padding: 0.25rem 0.5rem;">🇷🇺</a>
        <a href="/pl/" style="padding: 0.25rem 0.5rem; font-weight: bold;">🇵🇱</a>
    </div>
</div>

<style>
@media (max-width: 900px) {
    .impact-section [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>
