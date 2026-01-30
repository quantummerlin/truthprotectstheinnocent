---
layout: default
title: Home
lang: de
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
        <span class="hero-badge">⚠️ Dringend: Familie Getrennt</span>
        <h1>Die Wahrheit Schützt Die Unschuldigen</h1>
        <p class="lead">Drei Kinder wurden in Italien von ihren liebevollen Eltern getrennt. Drei offizielle Begründungen. Alle drei als falsch erwiesen.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Kinder Getrennt</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Falsche Behauptungen</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Gültige Gründe</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#teilen" class="btn btn-primary btn-lg">Jetzt Teilen</a>
            <a href="#beweise" class="btn btn-secondary btn-lg">Beweise Ansehen</a>
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

<!-- Die Wahrheit -->
<section class="section" id="wahrheit">
    <div class="container">
        <div class="container-narrow">
            <div class="quote-block" style="background: linear-gradient(135deg, #f0fdf4, #dcfce7); border-left-color: #22c55e;">
                <h3 style="color: #166534; margin-bottom: 1rem;">🇮🇹 Die Wahrheit (La Verità)</h3>
                <p style="font-style: italic; color: #166534; font-size: 1.1rem;">"Die Kinder waren niemals unsicher, isoliert oder vernachlässigt. Sie lebten in einer stabilen und sicheren Umgebung, alle ihre Bedürfnisse wurden erfüllt, sie waren sozialisiert, gesellschaftsbewusst und erhielten eine legale, anerkannte und bewährte Steiner-Bildung."</p>
                <p style="color: #374151; margin-top: 1rem;">"Die Kooperation der Familie resultierte nicht aus Fehlverhalten, sondern aus Zusammenarbeit. Sie entschieden sich, jede Anfrage in gutem Glauben zu erfüllen, obwohl sie bereits bewiesen hatten, dass das Wohlergehen, die Bildung und die Entwicklung ihrer Kinder vollständig gewährleistet waren."</p>
            </div>
        </div>
    </div>
</section>

<!-- Meet The Family - Video Section -->
<section class="section" id="familie" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>Lernen Sie Die Familie Kennen</h2>
            <p>Dies sind die Kinder im Mittelpunkt dieses Falls — gesund, glücklich und gedeihend, bevor sie weggenommen wurden</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Das Leben Vor Der Trennung</div>
                    <p class="video-card-desc">Glückliche Kinder, die naturverbunden leben</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Eine Liebevolle Familie</div>
                    <p class="video-card-desc">Die Bindung, die die Behörden zerstören</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Kindliche Freude</div>
                    <p class="video-card-desc">Was diese Kinder verloren haben</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark" id="beweise">
    <div class="container">
        <div class="section-header">
            <h2>Die Drei Falschen Behauptungen</h2>
            <p style="color: var(--color-gray-400);">Jede offizielle Begründung wurde von den italienischen Behörden selbst widerlegt</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Behauptung #1: "Kinder nicht geimpft"</h4>
                        <span class="evidence-badge badge-disputed">WIDERLEGT</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Die Versammlung von Chieti und Teramo bestätigte, dass die Kinder geimpft waren.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Quelle: Offizielle Aufzeichnungen der regionalen Gesundheitsbehörde</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Behauptung #2: "Kinder nicht unterrichtet"</h4>
                        <span class="evidence-badge badge-disputed">WIDERLEGT</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Das Bildungsministerium bestätigte, dass die Kinder legal zu Hause unterrichtet wurden.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Über 15.000 Kinder in Italien folgen demselben legalen Programm.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Behauptung #3: "Haus unsicher"</h4>
                        <span class="evidence-badge badge-disputed">WIDERLEGT</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Ein zertifizierter Geometer bestätigte, dass die Struktur nicht gefährdet ist.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Quelle: Professionelle Strukturbewertung</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">Die Unbeantwortete Frage:</strong> 
                <span style="color: var(--color-gray-300);">Wenn alle drei offiziellen Begründungen als falsch erwiesen wurden, auf welcher rechtlichen Grundlage bleiben diese Kinder von ihren Eltern getrennt?</span>
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
                    <h2 style="color: white;">Der Dokumentierte Schaden</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">Ein qualifizierter Psychologe führte nach der Entfernung eine Bewertung der Kinder durch. Die Ergebnisse waren so bedeutsam, dass der Psychologe eine formelle Pressekonferenz abhielt.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Hauptergebnis:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">Die Kinder zeigen jetzt <strong>selbstverletzendes Verhalten</strong>, das <strong>vor der Trennung nicht existierte</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">Vor der Entfernung wurden diese Kinder als gesund, glücklich und gedeihend beschrieben. Sie lebten im Freien, lernten von der Natur und hatten begrenzte Bildschirmzeit.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">Der "Schutz" verursacht den Schaden.</strong></p>
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
<section class="section" id="handeln">
    <div class="container">
        <div class="section-header">
            <h2>Was Sie Tun Können</h2>
            <p>Öffentliches Bewusstsein und Druck sind unerlässlich. Ihre Stimme zählt.</p>
        </div>
        
        <div class="action-grid">
            <div class="action-card urgent">
                <div class="action-icon">📧</div>
                <h3>E-Mail an Beamte</h3>
                <p>Schreiben Sie an italienische Parlamentsbeamte. Jede E-Mail erzeugt diplomatischen Druck und zeigt, dass die Welt zuschaut.</p>
                <a href="#email" class="btn btn-danger">E-Mail-Vorlagen Erhalten</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Fakten Teilen</h3>
                <p>Teilen Sie diese Geschichte in sozialen Medien. Verwenden Sie #TruthProtectsTheInnocent. Lassen Sie die Menschen wissen, was passiert.</p>
                <a href="#teilen" class="btn btn-outline">Jetzt Teilen</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Medien Kontaktieren</h3>
                <p>Wenden Sie sich an Journalisten und Nachrichtenagenturen. Diese Geschichte verdient Berichterstattung. Medienaufmerksamkeit schafft Verantwortlichkeit.</p>
                <a href="#medien" class="btn btn-outline">Medienressourcen</a>
            </div>
        </div>
    </div>
</section>

<!-- Email Template -->
<section class="section" id="email" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <h2>📧 E-Mail-Vorlage für Italienische Beamte</h2>
            
            <div class="alert alert-info">
                <strong>Prioritätskontakte:</strong><br>
                • michela.brambilla@camera.it (Kinderkommission)<br>
                • ciro.maschio@camera.it (Justizkommission)<br>
                • Immer in CC: gabinetto.ministro@cert.esteri.it
            </div>
            
            <div style="background: white; padding: 1.5rem; border-radius: 0.5rem; font-family: monospace; font-size: 0.85rem; white-space: pre-wrap; margin: 1rem 0; border: 1px solid var(--color-gray-200);">Betreff: Richiesta di attenzione istituzionale – tutela dei minori e unità familiare

Egregio/a [Name des Beamten],

Mein Name ist [Ihr Name] und ich bin Bürger/in mit Wohnsitz in [Ihr Land].

Ich schreibe Ihnen bezüglich einer humanitären Situation, die die Familie Birmingham-Trevallion betrifft, die derzeit in Italien getrennt ist.

Die drei Hauptbegründungen für die Entfernung der Kinder wurden durch offizielle Quellen widerlegt:

1. IMPFUNGEN: Die Versammlung von Chieti und Teramo bestätigte, dass die Kinder geimpft waren.
2. BILDUNG: Das Bildungsministerium bestätigte den legalen Heimunterricht.
3. WOHNUNG: Ein zertifizierter Geometer bestätigte, dass die Struktur nicht gefährdet ist.

Darüber hinaus hat eine psychologische Bewertung selbstverletzendes Verhalten bei den Kindern dokumentiert — Verhaltensweisen, die vor der Trennung nicht existierten.

Ich frage respektvoll: Wenn alle offiziellen Begründungen als falsch erwiesen wurden, auf welcher rechtlichen Grundlage wird diese Trennung fortgesetzt?

Mit freundlichen Grüßen,
[Ihr Name]
[Ihr Land]</div>
            
            <button onclick="navigator.clipboard.writeText(document.querySelector('#email div[style*=monospace]').innerText).then(()=>alert('Vorlage kopiert!'))" class="btn btn-primary" style="width: 100%;">📋 E-Mail-Vorlage Kopieren</button>
        </div>
    </div>
</section>

<!-- Support -->
<section class="section">
    <div class="container">
        <div class="container-narrow text-center">
            <h2>📬 Unterstützungsnachricht Senden</h2>
            <p>Zeigen Sie Ihre Unterstützung für die Familie.</p>
            <div style="background: var(--color-gray-50); padding: 2rem; border-radius: 1rem; margin: 2rem 0;">
                <p>E-Mail senden an:</p>
                <p style="font-size: 1.5rem; font-weight: 700; color: var(--color-primary);">support@quantummerlin.com</p>
                <a href="mailto:support@quantummerlin.com?subject=Unterstützungsnachricht - Familie Birmingham-Trevallion" class="btn btn-primary" style="margin-top: 1rem;">Unterstützungsnachricht Senden</a>
            </div>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>Die Wahrheit Muss Erzählt Werden</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Drei Kinder sind von ihren Eltern getrennt, basierend auf Behauptungen, die als falsch erwiesen wurden. Sie zeigen jetzt dokumentierten psychologischen Schaden. Das ist kein Kinderschutz — das ist Ungerechtigkeit.</p>
            
            <div class="hero-cta">
                <a href="#beweise" class="btn btn-primary btn-lg">Beweise Ansehen</a>
                <a href="#handeln" class="btn btn-secondary btn-lg">Jetzt Handeln</a>
            </div>
            
            <div style="margin-top: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                <p style="color: var(--color-gray-300); margin: 0;"><strong style="color: white;">#TruthProtectsTheInnocent</strong> · <strong style="color: white;">#LaFamigliaNelBosco</strong></p>
            </div>
        </div>
    </div>
</section>

<!-- Language Selector -->
<div style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;">
    <div style="background: white; padding: 0.5rem; border-radius: 0.5rem; box-shadow: var(--shadow-lg);">
        <a href="/" style="padding: 0.25rem 0.5rem;">🇬🇧</a>
        <a href="/it/" style="padding: 0.25rem 0.5rem;">🇮🇹</a>
        <a href="/de/" style="padding: 0.25rem 0.5rem; font-weight: bold;">🇩🇪</a>
        <a href="/fr/" style="padding: 0.25rem 0.5rem;">🇫🇷</a>
        <a href="/es/" style="padding: 0.25rem 0.5rem;">🇪🇸</a>
    </div>
</div>

<style>
@media (max-width: 900px) {
    .impact-section [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>