---
layout: default
title: Home
lang: pt
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
        <span class="hero-badge">⚠️ Urgente: Família Separada</span>
        <h1>A Verdade Protege Os Inocentes</h1>
        <p class="lead">Três crianças removidas dos seus pais amorosos na Itália. Três justificativas oficiais. Todas as três comprovadamente falsas por fontes oficiais.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Crianças Separadas</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Acusações Falsas</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Razões Válidas</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#share-now" class="btn btn-primary btn-lg">Compartilhar Agora</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">Ver As Provas</a>
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
            <h2>Conheça A Família</h2>
            <p>Estas são as crianças no centro deste caso — saudáveis, felizes e prosperando antes de serem levadas</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                    Seu navegador não suporta o elemento de vídeo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Vida Antes da Separação</div>
                    <p class="video-card-desc">Crianças felizes vivendo junto à natureza</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                    Seu navegador não suporta o elemento de vídeo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Uma Família Amorosa</div>
                    <p class="video-card-desc">O vínculo que as autoridades estão quebrando</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                    Seu navegador não suporta o elemento de vídeo.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Alegria da Infância</div>
                    <p class="video-card-desc">O que essas crianças perderam</p>
                </div>
            </div>
        </div>
        
        <div class="quote-block" style="margin-top: 3rem;">
            "Estas crianças eram saudáveis, felizes e prosperavam. Agora mostram sinais de trauma causados pela própria intervenção que deveria 'protegê-las'."
            <cite>— De conclusões da avaliação psicológica</cite>
        </div>
    </div>
</section>

<!-- What People Say About This Family -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>O Que As Pessoas Dizem Sobre Esta Família</h2>
            <p>Depoimentos de pessoas que conhecem a família Birmingham-Trevallion</p>
        </div>
        
        <div class="testimonial-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-12.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-16.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-19.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-21.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-26.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-28.jpg" alt="Depoimento" style="width: 100%; height: auto;">
            </div>
        </div>
        
        <div class="text-center mt-2">
            <p style="color: var(--color-gray-600); font-style: italic;">Estas são mensagens reais de pessoas que conhecem a família pessoalmente.</p>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark">
    <div class="container">
        <div class="section-header">
            <h2>As Três Alegações Falsas</h2>
            <p style="color: var(--color-gray-400);">Cada justificativa oficial foi refutada pelas próprias autoridades italianas</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Alegação #1: "Crianças não vacinadas"</h4>
                        <span class="evidence-badge badge-disputed">DESMENTIDO</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">A Assembleia de Chieti e Teramo confirmou que as crianças estavam vacinadas.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Fonte: registros oficiais da autoridade regional de saúde</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Alegação #2: "Crianças não educadas"</h4>
                        <span class="evidence-badge badge-disputed">DESMENTIDO</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">O Ministério da Educação confirmou que as crianças foram educadas em casa legalmente.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Mais de 15.000 crianças na Itália seguem o mesmo programa legal.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Alegação #3: "Casa insegura"</h4>
                        <span class="evidence-badge badge-disputed">DESMENTIDO</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Um geômetra certificado confirmou que a estrutura não está em risco.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Fonte: avaliação profissional da estrutura</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">A Pergunta Que Ninguém Consegue Responder:</strong> 
                <span style="color: var(--color-gray-300);">Se todas as três justificativas oficiais foram comprovadamente falsas, com que base legal essas crianças continuam separadas de seus pais?</span>
            </div>
            
            <div class="text-center mt-2">
                <a href="/evidence/" class="btn btn-primary">Ver Todas As Provas →</a>
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
                    <h2 style="color: white;">O Dano Documentado</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">Um psicólogo qualificado realizou uma avaliação das crianças após a remoção. As conclusões foram significativas a ponto de o psicólogo realizar uma coletiva de imprensa formal.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Conclusão Principal:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">As crianças agora apresentam <strong>comportamentos de autolesão</strong> que <strong>não existiam antes da separação</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">Antes da remoção, estas crianças eram descritas como saudáveis, felizes e prosperando. Viviam ao ar livre, aprendiam com a natureza e tinham pouco tempo de tela.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">A "proteção" está causando o dano.</strong></p>
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
            <h2>Quer Fazer Algo Agora?</h2>
            <p>Você não precisa doar. Não precisa se cadastrar em nada.</p>
        </div>
        
        <!-- The One Thing CTA - Chase Hughes style -->
        <div style="background: linear-gradient(135deg, #1e3a5f, #2d5a8a); border-radius: 1.5rem; padding: 3rem; text-align: center; max-width: 800px; margin: 0 auto;">
            <h3 style="color: #f59e0b; font-size: 1.5rem; margin-bottom: 1rem;">Não precisamos do seu dinheiro. Não precisamos dos seus dados.</h3>
            <h2 style="color: white; font-size: 2rem; margin-bottom: 1.5rem;">Só precisamos que você compartilhe este link.</h2>
            
            <p style="color: var(--color-gray-300); font-size: 1.2rem; margin-bottom: 1.5rem;">Um compartilhamento para a pessoa certa pode mudar tudo. Um jornalista. Uma autoridade. Alguém que conhece alguém.</p>
            
            <p style="color: white; font-size: 1.1rem; margin-bottom: 2rem;"><strong>Compartilhar isso com cinco pessoas de confiança vale mais do que qualquer doação que poderíamos pedir.</strong></p>
            
            <div style="background: rgba(255,255,255,0.1); border-radius: 0.5rem; padding: 1rem; margin-bottom: 1.5rem;">
                <code style="color: #f59e0b; font-size: 1.1rem; word-break: break-all;">truthprotectstheinnocent.quantummerlin.com</code>
            </div>
            
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <button onclick="navigator.clipboard.writeText('truthprotectstheinnocent.quantummerlin.com').then(()=>this.textContent='✓ Copiado!')" class="btn btn-primary btn-lg" style="background: white; color: var(--color-primary); min-width: 200px;">📋 Copiar Link</button>
                <a href="https://wa.me/?text=Three%20children%20separated%20from%20loving%20parents.%20Three%20official%20reasons.%20All%20three%20proven%20false.%20truthprotectstheinnocent.quantummerlin.com" class="btn btn-lg" style="background: #25D366; color: white;">💬 WhatsApp</a>
            </div>
            
            <p style="color: var(--color-gray-400); font-size: 0.9rem; margin-top: 2rem; margin-bottom: 0;">Pense em 5 pessoas que se importariam com isso. Envie agora, antes de esquecer.</p>
        </div>
        
        <!-- Secondary Actions -->
        <div class="action-grid" style="margin-top: 3rem;">
            <div class="action-card">
                <div class="action-icon">📧</div>
                <h3>Enviar Email às Autoridades</h3>
                <p>Pronto para fazer mais? Envie uma carta diretamente às autoridades parlamentares italianas.</p>
                <a href="/action/#email" class="btn btn-outline">Obter a Carta</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Redes Sociais</h3>
                <p>Compartilhe nas suas plataformas com posts prontos e #TruthProtectsTheInnocent</p>
                <a href="/action/#share" class="btn btn-outline">Modelos de Compartilhamento</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Contatar a Imprensa</h3>
                <p>Conhece um jornalista? Esta história merece cobertura. Repasse.</p>
                <a href="/action/#media" class="btn btn-outline">Recursos de Mídia</a>
            </div>
        </div>
    </div>
</section>

<!-- International Attention -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <h2>Atenção Internacional</h2>
                <p>Este caso atraiu atenção nos níveis mais altos</p>
            </div>
            
            <div class="stats-grid" style="margin-bottom: 2rem;">
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇦🇺</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Embaixada da Austrália Ciente</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇮🇹</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Autoridades Italianas Contatadas</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🌍</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Apoio Mundial Crescendo</div>
                </div>
            </div>
            
            <p class="text-center" style="font-size: 1.1rem;">A família não pode falar publicamente enquanto os processos legais estão em andamento. <strong>Mas nós podemos.</strong></p>
            <p class="text-center">A pressão pública e a atenção internacional são essenciais para garantir que este caso receba tratamento justo.</p>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>A Verdade Precisa Ser Contada</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Três crianças estão separadas de seus pais com base em alegações que foram comprovadamente falsas. Agora apresentam danos psicológicos documentados. Isto não é proteção infantil — é injustiça.</p>
            
            <div class="hero-cta">
                <a href="/evidence/" class="btn btn-primary btn-lg">Ver As Provas</a>
                <a href="/action/" class="btn btn-secondary btn-lg">Agir Agora</a>
            </div>
            
            <p style="margin-top: 2rem; color: var(--color-gray-500);">Salve este site para atualizações. Compartilhe com outras pessoas que acreditam na justiça.</p>
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
        <a href="/pt/" style="padding: 0.25rem 0.5rem; font-weight: bold;">🇵🇹</a>
        <a href="/ru/" style="padding: 0.25rem 0.5rem;">🇷🇺</a>
        <a href="/pl/" style="padding: 0.25rem 0.5rem;">🇵🇱</a>
    </div>
</div>

<style>
@media (max-width: 900px) {
    .impact-section [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>
