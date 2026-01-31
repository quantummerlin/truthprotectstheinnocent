---
layout: default
title: Home
lang: it
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
        <span class="hero-badge">⚠️ Urgente: Famiglia Separata</span>
        <h1>La Verità Protegge Gli Innocenti</h1>
        <p class="lead">Tre bambini allontanati dai loro genitori amorevoli in Italia. Tre giustificazioni ufficiali. Tutte e tre dimostrate false.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Bambini Separati</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">False Accuse</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Motivi Validi</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#share-now" class="btn btn-primary btn-lg">Condividi Ora</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">Vedi Le Prove</a>
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

<!-- La Verità -->
<section class="section" id="verita">
    <div class="container">
        <div class="container-narrow">
            <div class="quote-block" style="background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-left-color: #22c55e;">
                <h3 style="color: #166534; margin-bottom: 1rem;">🇮🇹 La Verità</h3>
                <p style="font-style: italic; color: #166534; font-size: 1.1rem;">"I bambini non sono mai stati insicuri, isolati o trascurati. Vivevano in un ambiente stabile e sicuro, tutti i loro bisogni erano soddisfatti, erano socializzati, consapevoli della società e ricevevano un'educazione Steiner legale, riconosciuta e comprovata."</p>
                <p style="color: #374151; margin-top: 1rem;">"L'obbedienza delle famiglie non deriva da un comportamento scorretto, ma dalla cooperazione. Hanno scelto di soddisfare ogni richiesta in buona fede, pur avendo dimostrato che il benessere, l'istruzione e lo sviluppo dei loro figli erano già pienamente garantiti."</p>
            </div>
        </div>
    </div>
</section>

<!-- Meet The Family - Video Section -->
<section class="section" id="famiglia" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>Conosci La Famiglia</h2>
            <p>Questi sono i bambini al centro di questo caso — sani, felici e fiorenti prima di essere portati via</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">La Vita Prima della Separazione</div>
                    <p class="video-card-desc">Bambini felici che vivono a contatto con la natura</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Una Famiglia Amorevole</div>
                    <p class="video-card-desc">Il legame che le autorità stanno spezzando</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">La Gioia dell'Infanzia</div>
                    <p class="video-card-desc">Ciò che questi bambini hanno perso</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark" id="prove">
    <div class="container">
        <div class="section-header">
            <h2>Le Tre False Accuse</h2>
            <p style="color: var(--color-gray-400);">Ogni giustificazione ufficiale è stata smentita dalle stesse autorità italiane</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Accusa #1: "Bambini non vaccinati"</h4>
                        <span class="evidence-badge badge-disputed">SMENTITA</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">L'Assemblea di Chieti e Teramo ha confermato che i bambini erano vaccinati.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Fonte: Registri ufficiali dell'autorità sanitaria regionale</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Accusa #2: "Bambini non istruiti"</h4>
                        <span class="evidence-badge badge-disputed">SMENTITA</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Il Ministero dell'Istruzione ha confermato che i bambini seguivano legalmente l'istruzione parentale.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Oltre 15.000 bambini in Italia seguono lo stesso programma legale.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Accusa #3: "Casa non sicura"</h4>
                        <span class="evidence-badge badge-disputed">SMENTITA</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Un geometra certificato ha confermato che la struttura non è a rischio.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Fonte: Valutazione strutturale professionale</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">La Domanda Senza Risposta:</strong> 
                <span style="color: var(--color-gray-300);">Se tutte e tre le giustificazioni ufficiali sono state dimostrate false, su quale base legale questi bambini rimangono separati dai loro genitori?</span>
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
                    <h2 style="color: white;">Il Danno Documentato</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">Uno psicologo qualificato ha condotto una valutazione dei bambini dopo la loro rimozione. I risultati erano così significativi che lo psicologo ha tenuto una conferenza stampa formale.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Risultato Chiave:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">I bambini mostrano ora <strong>comportamenti autolesionistici</strong> che <strong>non esistevano prima della separazione</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">Prima della rimozione, questi bambini erano descritti come sani, felici e fiorenti. Vivevano all'aperto, imparavano dalla natura e avevano un tempo limitato davanti agli schermi.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">La "protezione" sta causando il danno.</strong></p>
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
            <h2>Cosa Puoi Fare</h2>
            <p>La consapevolezza pubblica e la pressione sono essenziali. La tua voce conta.</p>
        </div>
        
        <div class="action-grid">
            <div class="action-card urgent">
                <div class="action-icon">📧</div>
                <h3>Scrivi ai Funzionari</h3>
                <p>Scrivi ai funzionari parlamentari italiani. Ogni email crea pressione diplomatica e dimostra che il mondo sta guardando.</p>
                <a href="#email" class="btn btn-danger">Ottieni i Modelli Email</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Condividi i Fatti</h3>
                <p>Condividi questa storia sui social media. Usa #TruthProtectsTheInnocent. Fai sapere alle persone cosa sta succedendo.</p>
                <a href="#share-now" class="btn btn-outline">Condividi Ora</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Contatta i Media</h3>
                <p>Contatta giornalisti e testate giornalistiche. Questa storia merita copertura. L'attenzione dei media crea responsabilità.</p>
                <a href="#media" class="btn btn-outline">Risorse Media</a>
            </div>
        </div>
    </div>
</section>

<!-- Email Template -->
<section class="section" id="email" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <h2>📧 Modello Email per Funzionari Italiani</h2>
            
            <div class="alert alert-info">
                <strong>Contatti Prioritari:</strong><br>
                • michela.brambilla@camera.it (Commissione Infanzia)<br>
                • ciro.maschio@camera.it (Commissione Giustizia)<br>
                • Sempre in CC: gabinetto.ministro@cert.esteri.it
            </div>
            
            <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; font-family: monospace; font-size: 0.85rem; white-space: pre-wrap; margin: 1rem 0; border: 1px solid var(--color-gray-200);">Oggetto: Richiesta di attenzione istituzionale – tutela dei minori e unità familiare

Egregio/a [Nome del Funzionario],

Mi chiamo [Il Tuo Nome] e sono cittadino/a residente a [La Tua Città/Paese].

Le scrivo in merito a una situazione di preoccupazione umanitaria che riguarda la famiglia Birmingham-Trevallion, attualmente separata in Italia.

Le tre principali giustificazioni fornite per la rimozione dei bambini sono state smentite da fonti ufficiali:

1. VACCINAZIONI: L'Assemblea di Chieti e Teramo ha confermato che i bambini erano vaccinati.
2. ISTRUZIONE: Il Ministero dell'Istruzione ha confermato che i bambini seguivano correttamente l'istruzione parentale.
3. ABITAZIONE: Un geometra certificato ha confermato che la struttura non è a rischio di stabilità.

Inoltre, una valutazione psicologica ha documentato comportamenti di autolesionismo emergenti nei bambini — comportamenti che non esistevano prima della separazione.

Chiedo rispettosamente: se tutte le giustificazioni ufficiali sono state dimostrate false, su quale base legale continua questa separazione?

La Sua attenzione a questa situazione contribuirebbe a sostenere i principi di equità, tutela dei minori e unità familiare.

Distinti saluti,
[Il Tuo Nome]
[La Tua Città/Paese]</div>
            
            <button onclick="navigator.clipboard.writeText(document.querySelector('#email div[style*=monospace]').innerText).then(()=>alert('Modello copiato!'))" class="btn btn-primary" style="width: 100%;">📋 Copia Modello Email</button>
        </div>
    </div>
</section>

<!-- Support -->
<section class="section">
    <div class="container">
        <div class="container-narrow text-center">
            <h2>📬 Invia un Messaggio di Supporto</h2>
            <p>Mostra il tuo sostegno alla famiglia.</p>
            <div style="background: var(--color-gray-50); padding: 2rem; border-radius: 1rem; margin: 2rem 0;">
                <p>Invia un'email a:</p>
                <p style="font-size: 1.5rem; font-weight: 700; color: var(--color-primary);">support@quantummerlin.com</p>
                <a href="mailto:support@quantummerlin.com?subject=Messaggio di Supporto - Famiglia Birmingham-Trevallion" class="btn btn-primary" style="margin-top: 1rem;">Invia Messaggio di Supporto</a>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Teaser -->
<section class="section">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <span class="hero-badge" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b; margin-bottom: 1rem;">Contesto Completo</span>
                <h2>Domande Sulla Copertura Mediatica?</h2>
                <p>Alcune notizie sono state incomplete o decontestualizzate. Ottieni la storia completa.</p>
            </div>
            
            <div style="background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-radius: 1.5rem; padding: 2.5rem; margin: 2rem 0; box-shadow: var(--shadow-lg);">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">X</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Nessun bagno = trascuratezza"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Realtà: I WC compostanti sono legali ovunque. Bagno completo ora installato.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">X</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Bambini non istruiti"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Realtà: Istruzione Steiner legale, confermata dal Ministero dell'Istruzione.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">X</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Stile di vita estremo"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Realtà: Scelte sostenibili basate sui valori, sempre più comuni nel mondo.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">X</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Genitori non qualificati"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Realtà: Entrambi professionalmente formati. Valutazioni confermano alta capacità.</p>
                        </div>
                    </div>
                </div>
                
                <div style="text-align: center; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.1);">
                    <p style="color: var(--color-gray-600); margin-bottom: 1rem;">La copertura mediatica è spesso incompleta. Ottieni informazioni complete e accurate.</p>
                    <a href="/faq/" class="btn btn-primary btn-lg">Leggi le FAQ Complete →</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>La Verità Deve Essere Raccontata</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Tre bambini sono separati dai loro genitori sulla base di accuse dimostrate false. Ora mostrano danni psicologici documentati. Questa non è protezione dell'infanzia — questa è ingiustizia.</p>
            
            <div class="hero-cta">
                <a href="/evidence/" class="btn btn-primary btn-lg">Vedi Le Prove</a>
                <a href="/action/" class="btn btn-secondary btn-lg">Agisci Ora</a>
            </div>
            
            <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                <p style="color: var(--color-gray-300); margin: 0;"><strong style="color: white;">#TruthProtectsTheInnocent</strong> · <strong style="color: white;">#LaFamigliaNelBosco</strong></p>
            </div>
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