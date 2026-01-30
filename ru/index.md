---
layout: default
title: Home
lang: ru
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
        <span class="hero-badge">⚠️ Срочно: семья разлучена</span>
        <h1>Правда защищает невиновных</h1>
        <p class="lead">Трое детей изъяты у любящих родителей в Италии. Три официальных обоснования. Все три официально опровергнуты.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Дети разлучены</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Ложные обвинения</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Обоснованных причин</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#share-now" class="btn btn-primary btn-lg">Поделиться сейчас</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">Смотреть доказательства</a>
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
            <h2>Познакомьтесь с семьёй</h2>
            <p>Это дети в центре дела — здоровые, счастливые и развивавшиеся до их изъятия</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                    Ваш браузер не поддерживает видео.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Жизнь до разлучения</div>
                    <p class="video-card-desc">Счастливые дети, живущие рядом с природой</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                    Ваш браузер не поддерживает видео.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Любящая семья</div>
                    <p class="video-card-desc">Связь, которую власти разрывают</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                    Ваш браузер не поддерживает видео.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Детская радость</div>
                    <p class="video-card-desc">То, что дети потеряли</p>
                </div>
            </div>
        </div>
        
        <div class="quote-block" style="margin-top: 3rem;">
            "Эти дети были здоровыми, счастливыми и развивавшимися. Сейчас у них появились признаки травмы, вызванной самой "защитной" мерой."
            <cite>— Из выводов психологической оценки</cite>
        </div>
    </div>
</section>

<!-- What People Say About This Family -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>Что говорят об этой семье</h2>
            <p>Отзывы людей, которые знают семью Бирмингем‑Треваллион</p>
        </div>
        
        <div class="testimonial-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-12.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-16.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-19.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-21.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-26.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-28.jpg" alt="Отзыв" style="width: 100%; height: auto;">
            </div>
        </div>
        
        <div class="text-center mt-2">
            <p style="color: var(--color-gray-600); font-style: italic;">Это реальные сообщения от людей, которые лично знают семью.</p>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark">
    <div class="container">
        <div class="section-header">
            <h2>Три ложных основания</h2>
            <p style="color: var(--color-gray-400);">Каждое официальное обоснование было опровергнуто самими итальянскими властями</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Основание №1: «Дети не привиты»</h4>
                        <span class="evidence-badge badge-disputed">ОПРОВЕРГНУТО</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Ассамблея Кьети и Терамо подтвердила, что дети были вакцинированы.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Источник: официальные записи регионального органа здравоохранения</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Основание №2: «Дети не обучаются»</h4>
                        <span class="evidence-badge badge-disputed">ОПРОВЕРГНУТО</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Министерство образования подтвердило законное домашнее обучение.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Более 15 000 детей в Италии следуют той же законной программе.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Основание №3: «Дом небезопасен»</h4>
                        <span class="evidence-badge badge-disputed">ОПРОВЕРГНУТО</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Сертифицированный геометр подтвердил, что конструкция не представляет риска.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Источник: профессиональное заключение по прочности</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">Вопрос, на который нет ответа:</strong> 
                <span style="color: var(--color-gray-300);">Если все три официальных основания опровергнуты, на каком правовом основании дети остаются разлучёнными с родителями?</span>
            </div>
            
            <div class="text-center mt-2">
                <a href="/evidence/" class="btn btn-primary">Смотреть все доказательства →</a>
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
                    <h2 style="color: white;">Зафиксированный вред</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">Квалифицированный психолог провёл оценку детей после изъятия. Выводы оказались настолько серьёзными, что психолог провёл официальную пресс‑конференцию.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Ключевой вывод:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">У детей появились <strong>самоповреждающие поведения</strong>, которых <strong>не было до разлучения</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">До изъятия дети описывались как здоровые, счастливые и развивавшиеся. Они жили на природе, учились через природу и мало времени проводили за экранами.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">«Защита» причиняет вред.</strong></p>
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
            <h2>Хотите сделать что‑то прямо сейчас?</h2>
            <p>Не нужно донатить. Не нужно нигде регистрироваться.</p>
        </div>
        
        <!-- The One Thing CTA - Chase Hughes style -->
        <div style="background: linear-gradient(135deg, #1e3a5f, #2d5a8a); border-radius: 1.5rem; padding: 3rem; text-align: center; max-width: 800px; margin: 0 auto;">
            <h3 style="color: #f59e0b; font-size: 1.5rem; margin-bottom: 1rem;">Нам не нужны ваши деньги. Нам не нужны ваши данные.</h3>
            <h2 style="color: white; font-size: 2rem; margin-bottom: 1.5rem;">Нам нужно лишь, чтобы вы поделились этой ссылкой.</h2>
            
            <p style="color: var(--color-gray-300); font-size: 1.2rem; margin-bottom: 1.5rem;">Одно сообщение нужному человеку может изменить всё. Журналисту. Чиновнику. Тому, кто знает нужных людей.</p>
            
            <p style="color: white; font-size: 1.1rem; margin-bottom: 2rem;"><strong>Поделиться этим с пятью людьми, которым вы доверяете, ценнее любой суммы пожертвований.</strong></p>
            
            <div style="background: rgba(255,255,255,0.1); border-radius: 0.5rem; padding: 1rem; margin-bottom: 1.5rem;">
                <code style="color: #f59e0b; font-size: 1.1rem; word-break: break-all;">truthprotectstheinnocent.quantummerlin.com</code>
            </div>
            
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <button onclick="navigator.clipboard.writeText('truthprotectstheinnocent.quantummerlin.com').then(()=>this.textContent='✓ Скопировано!')" class="btn btn-primary btn-lg" style="background: white; color: var(--color-primary); min-width: 200px;">📋 Скопировать ссылку</button>
                <a href="https://wa.me/?text=Three%20children%20separated%20from%20loving%20parents.%20Three%20official%20reasons.%20All%20three%20proven%20false.%20truthprotectstheinnocent.quantummerlin.com" class="btn btn-lg" style="background: #25D366; color: white;">💬 WhatsApp</a>
            </div>
            
            <p style="color: var(--color-gray-400); font-size: 0.9rem; margin-top: 2rem; margin-bottom: 0;">Подумайте о пяти людях, которым это небезразлично. Отправьте сейчас, пока не забыли.</p>
        </div>
        
        <!-- Secondary Actions -->
        <div class="action-grid" style="margin-top: 3rem;">
            <div class="action-card">
                <div class="action-icon">📧</div>
                <h3>Письмо чиновникам</h3>
                <p>Готовы сделать больше? Отправьте письмо итальянским парламентским чиновникам.</p>
                <a href="/action/#email" class="btn btn-outline">Получить письмо</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Социальные сети</h3>
                <p>Поделитесь в своих соцсетях готовыми постами и #TruthProtectsTheInnocent</p>
                <a href="/action/#share" class="btn btn-outline">Шаблоны для публикаций</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Связаться со СМИ</h3>
                <p>Есть знакомый журналист? Эта история заслуживает освещения. Передайте информацию.</p>
                <a href="/action/#media" class="btn btn-outline">Ресурсы для СМИ</a>
            </div>
        </div>
    </div>
</section>

<!-- International Attention -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <h2>Международное внимание</h2>
                <p>Это дело привлекло внимание на самых высоких уровнях</p>
            </div>
            
            <div class="stats-grid" style="margin-bottom: 2rem;">
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇦🇺</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Посольство Австралии осведомлено</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇮🇹</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Итальянские чиновники уведомлены</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🌍</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Поддержка по всему миру растёт</div>
                </div>
            </div>
            
            <p class="text-center" style="font-size: 1.1rem;">Семья не может говорить публично, пока идут юридические процедуры. <strong>Но мы можем.</strong></p>
            <p class="text-center">Общественное давление и международное внимание необходимы, чтобы это дело рассматривалось справедливо.</p>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>Правду нужно сказать</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Трое детей разлучены с родителями на основании утверждений, которые были опровергнуты. Сейчас у них зафиксирован психологический вред. Это не защита детей — это несправедливость.</p>
            
            <div class="hero-cta">
                <a href="/evidence/" class="btn btn-primary btn-lg">Смотреть доказательства</a>
                <a href="/action/" class="btn btn-secondary btn-lg">Действовать сейчас</a>
            </div>
            
            <p style="margin-top: 2rem; color: var(--color-gray-500);">Сохраните сайт для обновлений. Поделитесь с теми, кто верит в справедливость.</p>
        </div>
    </div>
</section>

<style>
@media (max-width: 900px) {
    .impact-section [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>
