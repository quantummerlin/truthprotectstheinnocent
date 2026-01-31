---
layout: default
title: Home
lang: en
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
        <span class="hero-badge">⚠️ Urgent: Family Separated</span>
        <h1>Truth Protects The Innocent</h1>
        <p class="lead">Three children removed from their loving parents in Italy. Three official justifications given. All three proven false by official sources.</p>
        
        <div class="hero-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">Children Separated</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">3</span>
                <span class="hero-stat-label">False Claims</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">0</span>
                <span class="hero-stat-label">Valid Reasons</span>
            </div>
        </div>
        
        <div class="hero-cta">
            <a href="#share-now" class="btn btn-primary btn-lg">Share This Now</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">See The Evidence</a>
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
            <h2>Meet The Family</h2>
            <p>These are the children at the center of this case — healthy, happy, and thriving before they were taken</p>
        </div>
        
        <div class="video-gallery">
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family1.MP4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Life Before Separation</div>
                    <p class="video-card-desc">Happy children living close to nature</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family2.MOV" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">A Loving Family</div>
                    <p class="video-card-desc">The bond that authorities are breaking</p>
                </div>
            </div>
            
            <div class="video-card">
                <video controls playsinline preload="metadata">
                    <source src="/assets/videos/family3.MP4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <div class="video-card-overlay">
                    <div class="video-card-title">Childhood Joy</div>
                    <p class="video-card-desc">What these children have lost</p>
                </div>
            </div>
        </div>
        
        <div class="quote-block" style="margin-top: 3rem;">
            "These children were healthy, happy, and thriving. Now they're showing signs of trauma caused by the very intervention that was supposed to 'protect' them."
            <cite>— From psychological assessment findings</cite>
        </div>
    </div>
</section>

<!-- What People Say About This Family -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="section-header">
            <h2>What People Say About This Family</h2>
            <p>Testimonials from people who know the Birmingham-Trevallion family</p>
        </div>
        
        <div class="testimonial-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-12.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-16.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-19.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-21.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-26.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
            <div class="testimonial-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-md);">
                <img src="/assets/images/testimonials/photo_2026-01-11_21-41-28.jpg" alt="Testimonial" style="width: 100%; height: auto;">
            </div>
        </div>
        
        <div class="text-center mt-2">
            <p style="color: var(--color-gray-600); font-style: italic;">These are real messages from people who know the family personally.</p>
        </div>
    </div>
</section>

<!-- Media Coverage Section -->
<section class="section">
    <div class="container">
        <div class="section-header">
            <h2>📰 In The Press</h2>
            <p>Major Italian newspapers are covering this story</p>
        </div>
        
        <div class="press-gallery" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
            <div class="press-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-lg);">
                <img src="/assets/images/photo_2026-01-30_21-50-16.jpg" alt="Corriere della Sera" style="width: 100%; height: auto;">
                <div style="padding: 1rem;">
                    <span style="background: var(--color-accent); color: white; padding: 0.2rem 0.6rem; border-radius: 1rem; font-size: 0.7rem; font-weight: 600;">CORRIERE DELLA SERA</span>
                    <p style="color: var(--color-gray-700); font-weight: 600; font-size: 0.9rem; margin: 0.5rem 0 0.5rem 0;">"Those who don't conform get put under guardianship"</p>
                    <p style="color: var(--color-gray-600); font-size: 0.8rem; margin: 0; line-height: 1.4;">Author Susanna Tamaro compares the Birmingham-Trevallion case to Vittorio Sgarbi, arguing that people with talent and intelligence outside the norm face persecution. She questions why the state decides to put children under guardianship when families don't conform to bureaucratic standards.</p>
                </div>
            </div>
            
            <div class="press-card" style="background: white; border-radius: 1rem; overflow: hidden; box-shadow: var(--shadow-lg);">
                <img src="/assets/images/photo_2026-01-30_21-49-52.jpg" alt="Il Centro" style="width: 100%; height: auto;">
                <div style="padding: 1rem;">
                    <span style="background: var(--color-primary); color: white; padding: 0.2rem 0.6rem; border-radius: 1rem; font-size: 0.7rem; font-weight: 600;">IL CENTRO</span>
                    <p style="color: var(--color-gray-700); font-weight: 600; font-size: 0.9rem; margin: 0.5rem 0 0.5rem 0;">"She's hostile, must be revoked immediately"</p>
                    <p style="color: var(--color-gray-600); font-size: 0.8rem; margin: 0; line-height: 1.4;">Full-page report on the formal eight-page complaint submitted to the Professional Order of Social Workers, challenging the social worker's conduct. The family's lawyers argue the social worker is hostile and should be immediately removed from the case.</p>
                </div>
            </div>
        </div>
        
        <div class="text-center mt-2">
            <a href="/media/" class="btn btn-outline">View All Media Coverage →</a>
        </div>
    </div>
</section>

<!-- The Three False Claims -->
<section class="section section-dark">
    <div class="container">
        <div class="section-header">
            <h2>The Three False Claims</h2>
            <p style="color: var(--color-gray-400);">Each official justification has been disproven by Italian authorities themselves</p>
        </div>
        
        <div class="container-narrow">
            <div class="evidence-grid">
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Claim #1: "Children not vaccinated"</h4>
                        <span class="evidence-badge badge-disputed">DISPROVEN</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">The Assembly of Chieti and Teramo confirmed the children were vaccinated.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Source: Official regional health authority records</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Claim #2: "Children not educated"</h4>
                        <span class="evidence-badge badge-disputed">DISPROVEN</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">The Ministry of Education confirmed the children were legally educated using Steiner pedagogy.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Following the legal parental instruction framework used by over 15,000 families in Italy.</p>
                </div>
                
                <div class="evidence-card verified" style="background: rgba(255,255,255,0.05); border-left-color: #ef4444;">
                    <div class="evidence-header">
                        <h4 style="color: white;">❌ Claim #3: "House unsafe"</h4>
                        <span class="evidence-badge badge-disputed">DISPROVEN</span>
                    </div>
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">A certified geometer confirmed the structure is not at risk.</strong></p>
                    <p class="evidence-source" style="color: var(--color-gray-500);">Source: Professional structural assessment</p>
                </div>
            </div>
            
            <div class="alert alert-warning" style="margin-top: 2rem; background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                <strong style="color: #fbbf24;">The Question Nobody Can Answer:</strong> 
                <span style="color: var(--color-gray-300);">If all three official justifications have been proven false, on what legal basis do these children remain separated from their parents?</span>
            </div>
            
            <div class="text-center mt-2">
                <a href="/evidence/" class="btn btn-primary">View Complete Evidence →</a>
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
                    <h2 style="color: white;">The Documented Harm</h2>
                    <p style="color: var(--color-gray-300); font-size: 1.1rem;">A qualified psychologist conducted an assessment of the children after their removal. The findings were significant enough that the psychologist held a formal press conference.</p>
                    
                    <div style="background: rgba(220, 38, 38, 0.2); border-left: 4px solid #dc2626; padding: 1.5rem; border-radius: 0.5rem; margin: 1.5rem 0;">
                        <h4 style="color: #fca5a5; margin-bottom: 0.5rem;">Key Finding:</h4>
                        <p style="color: white; font-size: 1.1rem; margin: 0;">The children are now exhibiting <strong>self-harm behaviors</strong> that <strong>did not exist before the separation</strong>.</p>
                    </div>
                    
                    <p style="color: var(--color-gray-300);">Before the removal, these children were described as healthy, happy, and thriving. They lived outdoors, learned from nature, and had limited screen time.</p>
                    
                    <p style="color: var(--color-gray-300);"><strong style="color: white;">The "protection" is causing the harm.</strong></p>
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
            <h2>Want To Do Something Right Now?</h2>
            <p>You don't need to donate. You don't need to sign up for anything.</p>
        </div>
        
        <!-- The One Thing CTA - Chase Hughes style -->
        <div style="background: linear-gradient(135deg, #1e3a5f, #2d5a8a); border-radius: 1.5rem; padding: 3rem; text-align: center; max-width: 800px; margin: 0 auto;">
            <h3 style="color: #f59e0b; font-size: 1.5rem; margin-bottom: 1rem;">We don't need your money. We don't need your data.</h3>
            <h2 style="color: white; font-size: 2rem; margin-bottom: 1.5rem;">We just need you to share this link.</h2>
            
            <p style="color: var(--color-gray-300); font-size: 1.2rem; margin-bottom: 1.5rem;">One share to the right person could change everything. A journalist. An official. Someone who knows someone.</p>
            
            <p style="color: white; font-size: 1.1rem; margin-bottom: 2rem;"><strong>Sharing this with five people you trust is worth more than any donation we could ask for.</strong></p>
            
            <div style="background: rgba(255,255,255,0.1); border-radius: 0.5rem; padding: 1rem; margin-bottom: 1.5rem;">
                <code style="color: #f59e0b; font-size: 1.1rem; word-break: break-all;">truthprotectstheinnocent.quantummerlin.com</code>
            </div>
            
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
                <button onclick="navigator.clipboard.writeText('truthprotectstheinnocent.quantummerlin.com').then(()=>this.textContent='✓ Copied!')" class="btn btn-primary btn-lg" style="background: white; color: var(--color-primary); min-width: 200px;">📋 Copy Link</button>
                <a href="https://wa.me/?text=Three%20children%20separated%20from%20loving%20parents.%20Three%20official%20reasons.%20All%20three%20proven%20false.%20truthprotectstheinnocent.quantummerlin.com" class="btn btn-lg" style="background: #25D366; color: white;">💬 WhatsApp</a>
            </div>
            
            <p style="color: var(--color-gray-400); font-size: 0.9rem; margin-top: 2rem; margin-bottom: 0;">Think of 5 people who would care about this. Send it now, before you forget.</p>
        </div>
        
        <!-- Secondary Actions -->
        <div class="action-grid" style="margin-top: 3rem;">
            <div class="action-card">
                <div class="action-icon">📧</div>
                <h3>Email Officials</h3>
                <p>Ready to do more? Send a letter directly to Italian parliamentary officials.</p>
                <a href="/action/#email" class="btn btn-outline">Get The Letter</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📢</div>
                <h3>Social Media</h3>
                <p>Share on your platforms with ready-made posts and #TruthProtectsTheInnocent</p>
                <a href="/action/#share" class="btn btn-outline">Share Templates</a>
            </div>
            
            <div class="action-card">
                <div class="action-icon">📰</div>
                <h3>Contact Media</h3>
                <p>Know a journalist? This story deserves coverage. Pass it on.</p>
                <a href="/action/#media" class="btn btn-outline">Media Resources</a>
            </div>
        </div>
    </div>
</section>

<!-- FAQ Teaser - Addressing Media Misrepresentations -->
<section class="section">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <span class="hero-badge" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b; margin-bottom: 1rem;">📋 Complete Context</span>
                <h2>Questions About Media Coverage?</h2>
                <p>Some reporting has been incomplete or taken out of context. Get the full story.</p>
            </div>
            
            <div style="background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-radius: 1.5rem; padding: 2.5rem; margin: 2rem 0; box-shadow: var(--shadow-lg);">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">❌</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"No bathroom = neglect"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Reality: Composting toilets are legal worldwide. Full bathroom now installed.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">❌</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Children not educated"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Reality: Legal Steiner education, confirmed by Ministry of Education.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">❌</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Extreme lifestyle"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Reality: Values-based sustainable living, increasingly common worldwide.</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 1rem; align-items: flex-start;">
                        <div style="background: rgba(239, 68, 68, 0.1); color: #dc2626; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; flex-shrink: 0;">❌</div>
                        <div>
                            <strong style="color: var(--color-gray-700);">"Unqualified parents"</strong>
                            <p style="color: var(--color-gray-600); font-size: 0.9rem; margin: 0.25rem 0 0 0;">Reality: Both professionally trained. Assessments confirmed high capability.</p>
                        </div>
                    </div>
                </div>
                
                <div style="text-align: center; padding-top: 1rem; border-top: 1px solid rgba(0,0,0,0.1);">
                    <p style="color: var(--color-gray-600); margin-bottom: 1rem;">Media coverage is often incomplete. Get complete, factual information.</p>
                    <a href="/faq/" class="btn btn-primary btn-lg">📋 Read Full FAQ →</a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- International Attention -->
<section class="section" style="background: var(--color-gray-50);">
    <div class="container">
        <div class="container-narrow">
            <div class="section-header">
                <h2>International Attention</h2>
                <p>This case has attracted attention at the highest levels</p>
            </div>
            
            <div class="stats-grid" style="margin-bottom: 2rem;">
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇦🇺</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Australian Embassy Aware</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🇮🇹</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Italian Officials Contacted</div>
                </div>
                <div class="stat-card" style="background: white; box-shadow: var(--shadow-md);">
                    <div class="stat-number" style="color: var(--color-primary);">🌍</div>
                    <div class="stat-label" style="color: var(--color-gray-600);">Worldwide Support Growing</div>
                </div>
            </div>
            
            <p class="text-center" style="font-size: 1.1rem;">The family cannot speak publicly while legal proceedings are ongoing. <strong>But we can.</strong></p>
            <p class="text-center">Public pressure and international attention are essential to ensuring this case receives fair treatment.</p>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section class="section section-dark" style="text-align: center;">
    <div class="container">
        <div class="container-narrow">
            <h2>The Truth Must Be Told</h2>
            <p style="font-size: 1.2rem; color: var(--color-gray-300); margin-bottom: 2rem;">Three children are separated from their parents based on claims that have been proven false. They are now showing documented psychological harm. This is not child protection — this is injustice.</p>
            
            <div class="hero-cta">
                <a href="/evidence/" class="btn btn-primary btn-lg">See The Evidence</a>
                <a href="/action/" class="btn btn-secondary btn-lg">Take Action Now</a>
            </div>
            
            <p style="margin-top: 2rem; color: var(--color-gray-500);">Bookmark this site for updates. Share it with others who believe in justice.</p>
        </div>
    </div>
</section>

<style>
/* Responsive grid fix for impact section */
@media (max-width: 900px) {
    .impact-section [style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>