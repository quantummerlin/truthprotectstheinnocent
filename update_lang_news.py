"""
Updates the "latest update" section in all 7 language files
with the two newest developments: Senate visit (Mar 26) and children sick/Easter (Mar 29).
"""

langs = {
    'it': {
        'comment_old': '<!-- AGGIORNAMENTO — 15 MARZO 2026 -->',
        'comment_new': '<!-- AGGIORNAMENTO — 29 MARZO 2026 -->',
        'badge': '🗞️ AGGIORNAMENTO — 29 MARZO 2026',
        'c1_label': 'SENATO ITALIANO · 26 MAR 2026',
        'c1_title': 'Catherine e Nathan ricevuti dal Presidente del Senato Italiano',
        'c1_desc': 'Per la prima volta, Catherine e Nathan sono stati ricevuti con &ldquo;grande umanità&rdquo;. Catherine ha parlato pubblicamente per la prima volta da quando è iniziata questa vicenda.',
        'c1_btn': '🏛️ Guarda il video e leggi la lettera →',
        'c2_label': 'BAMBINI MALATI · 29 MAR 2026',
        'c2_title': 'Tutti e tre i bambini sono malati. La madre non può raggiungerli. La Pasqua si avvicina.',
        'c2_desc': 'Il Prof. Cantelmi pubblica il resoconto della notte di dolore di Catherine. GreenStyle chiede pubblicamente: potranno trascorrere la Pasqua (5 aprile) con mamma e papà?',
        'c2_btn': '🆕 Aggiornamento completo →',
    },
    'de': {
        'comment_old': '<!-- NEUESTE ENTWICKLUNG — 15. MÄRZ 2026 -->',
        'comment_new': '<!-- NEUESTE ENTWICKLUNG — 29. MÄRZ 2026 -->',
        'badge': '🗞️ AKTUALISIERUNG — 29. MÄRZ 2026',
        'c1_label': 'ITALIENISCHER SENAT · 26. MÄR 2026',
        'c1_title': 'Catherine und Nathan vom Präsidenten des Italienischen Senats empfangen',
        'c1_desc': 'Zum ersten Mal wurden Catherine und Nathan mit &ldquo;großer Menschlichkeit&rdquo; empfangen. Catherine sprach erstmals öffentlich seit Beginn dieser Tragödie.',
        'c1_btn': '🏛️ Video ansehen und Brief lesen →',
        'c2_label': 'KRANKE KINDER · 29. MÄR 2026',
        'c2_title': 'Alle drei Kinder sind krank. Die Mutter kann nicht zu ihnen. Ostern nähert sich.',
        'c2_desc': 'Prof. Cantelmi veröffentlicht einen Bericht über Catherines Nacht der Qual. GreenStyle fragt öffentlich: Können sie Ostern (5. April) mit Mama und Papa verbringen?',
        'c2_btn': '🆕 Vollständiges Update →',
    },
    'fr': {
        'comment_old': '<!-- DERNIÈRE MISE À JOUR — 15 MARS 2026 -->',
        'comment_new': '<!-- DERNIÈRE MISE À JOUR — 29 MARS 2026 -->',
        'badge': '🗞️ MISE À JOUR — 29 MARS 2026',
        'c1_label': 'SÉNAT ITALIEN · 26 MARS 2026',
        'c1_title': 'Catherine et Nathan reçus par le Président du Sénat Italien',
        'c1_desc': 'Pour la première fois, Catherine et Nathan ont été reçus avec &ldquo;grande humanité&rdquo;. Catherine a pris la parole publiquement pour la première fois depuis le début de cette épreuve.',
        'c1_btn': '🏛️ Voir la vidéo et lire la lettre →',
        'c2_label': 'ENFANTS MALADES · 29 MARS 2026',
        'c2_title': 'Les trois enfants sont malades. La mère ne peut pas les rejoindre. Pâques approche.',
        'c2_desc': 'Prof. Cantelmi publie le récit de la nuit d\'angoisse de Catherine. GreenStyle pose publiquement la question&nbsp;: peuvent-ils passer Pâques (5 avril) avec leurs parents&nbsp;?',
        'c2_btn': '🆕 Mise à jour complète →',
    },
    'es': {
        'comment_old': '<!-- ACTUALIZACIÓN — 15 DE MARZO DE 2026 -->',
        'comment_new': '<!-- ACTUALIZACIÓN — 29 DE MARZO DE 2026 -->',
        'badge': '🗞️ ACTUALIZACIÓN — 29 DE MARZO 2026',
        'c1_label': 'SENADO ITALIANO · 26 MAR 2026',
        'c1_title': 'Catherine y Nathan recibidos por el Presidente del Senado Italiano',
        'c1_desc': 'Por primera vez, Catherine y Nathan fueron recibidos con &ldquo;gran humanidad&rdquo;. Catherine habló públicamente por primera vez desde el inicio de esta tragedia.',
        'c1_btn': '🏛️ Ver el video y leer la carta →',
        'c2_label': 'NIÑOS ENFERMOS · 29 MAR 2026',
        'c2_title': 'Los tres niños están enfermos. La madre no puede llegar a ellos. Se acerca la Pascua.',
        'c2_desc': 'Prof. Cantelmi publica el relato de la noche de angustia de Catherine. GreenStyle pregunta públicamente: ¿podrán pasar la Pascua (5 de abril) con mamá y papá?',
        'c2_btn': '🆕 Actualización completa →',
    },
    'pt': {
        'comment_old': '<!-- ATUALIZAÇÃO — 15 DE MARÇO DE 2026 -->',
        'comment_new': '<!-- ATUALIZAÇÃO — 29 DE MARÇO DE 2026 -->',
        'badge': '🗞️ ATUALIZAÇÃO — 29 DE MARÇO 2026',
        'c1_label': 'SENADO ITALIANO · 26 MAR 2026',
        'c1_title': 'Catherine e Nathan recebidos pelo Presidente do Senado Italiano',
        'c1_desc': 'Pela primeira vez, Catherine e Nathan foram recebidos com &ldquo;grande humanidade&rdquo;. Catherine falou publicamente pela primeira vez desde o início desta provação.',
        'c1_btn': '🏛️ Ver o vídeo e ler a carta →',
        'c2_label': 'CRIANÇAS DOENTES · 29 MAR 2026',
        'c2_title': 'As três crianças estão doentes. A mãe não pode alcançá-las. A Páscoa se aproxima.',
        'c2_desc': 'Prof. Cantelmi publica relato da noite de angústia de Catherine. GreenStyle pergunta publicamente: eles poderão passar a Páscoa (5 de abril) com mamãe e papai?',
        'c2_btn': '🆕 Atualização completa →',
    },
    'ru': {
        'comment_old': '<!-- ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ — 15 МАРТА 2026 -->',
        'comment_new': '<!-- ПОСЛЕДНЕЕ ОБНОВЛЕНИЕ — 29 МАРТА 2026 -->',
        'badge': '🗞️ ОБНОВЛЕНИЕ — 29 МАРТА 2026',
        'c1_label': 'ИТАЛЬЯНСКИЙ СЕНАТ · 26 МАР 2026',
        'c1_title': 'Катрин и Натан приняты Председателем Итальянского Сената',
        'c1_desc': 'Впервые Катрин и Натан были приняты с &ldquo;большой человечностью&rdquo;. Катрин впервые публично выступила с момента начала этого испытания.',
        'c1_btn': '🏛️ Смотреть видео и читать письмо →',
        'c2_label': 'ДЕТИ БОЛЬНЫ · 29 МАР 2026',
        'c2_title': 'Все три ребёнка больны. Мать не может добраться до них. Приближается Пасха.',
        'c2_desc': 'Проф. Кантельми публикует рассказ о мучительной ночи Катрин. GreenStyle публично спрашивает: смогут ли они провести Пасху (5 апреля) с мамой и папой?',
        'c2_btn': '🆕 Полное обновление →',
    },
    'pl': {
        'comment_old': '<!-- NAJNOWSZA AKTUALIZACJA — 15 MARCA 2026 -->',
        'comment_new': '<!-- NAJNOWSZA AKTUALIZACJA — 29 MARCA 2026 -->',
        'badge': '🗞️ AKTUALIZACJA — 29 MARCA 2026',
        'c1_label': 'WŁOSKI SENAT · 26 MAR 2026',
        'c1_title': 'Catherine i Nathan przyjęci przez Przewodniczącego Włoskiego Senatu',
        'c1_desc': 'Po raz pierwszy Catherine i Nathan zostali przyjęci z &ldquo;wielką ludzkością&rdquo;. Catherine po raz pierwszy publicznie zabrała głos od początku tej próby.',
        'c1_btn': '🏛️ Obejrzyj film i przeczytaj list →',
        'c2_label': 'CHORE DZIECI · 29 MAR 2026',
        'c2_title': 'Wszystkie troje dzieci jest chorych. Matka nie może do nich dotrzeć. Wielkanoc się zbliża.',
        'c2_desc': 'Prof. Cantelmi publikuje relację z nocy udręki Catherine. GreenStyle publicznie pyta: czy będą mogli spędzić Wielkanoc (5 kwietnia) z mamą i tatą?',
        'c2_btn': '🆕 Pełna aktualizacja →',
    },
}

def build_section(t):
    return (
        f'{t["comment_new"]}\n'
        '<section style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 2rem 0;">\n'
        '    <div class="container">\n'
        '        <div style="max-width: 900px; margin: 0 auto;">\n'
        '            <div style="text-align: center; margin-bottom: 1.5rem;">\n'
        f'                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.8); padding: 0.4rem 1.25rem; border-radius: 2rem; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">{t["badge"]}</span>\n'
        '            </div>\n'
        '            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">\n'
        # Card 1 — Senate
        '                <div style="background: rgba(124,58,237,0.12); border: 1px solid rgba(124,58,237,0.35); border-radius: 1rem; padding: 1.5rem;">\n'
        f'                    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #c4b5fd; margin-bottom: 0.5rem;">{t["c1_label"]}</div>\n'
        f'                    <h3 style="color: white; font-size: 1.05rem; margin: 0 0 0.75rem 0; line-height: 1.4;">{t["c1_title"]}</h3>\n'
        f'                    <p style="color: rgba(255,255,255,0.7); font-size: 0.875rem; line-height: 1.6; margin: 0 0 1rem 0;">{t["c1_desc"]}</p>\n'
        f'                    <a href="/senate/breaking/2026/03/26/senate-visit-catherine-addresses-public.html" style="display: block; text-align: center; background: rgba(124,58,237,0.4); border: 1px solid rgba(124,58,237,0.6); color: white; padding: 0.6rem 1rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; font-size: 0.85rem;">{t["c1_btn"]}</a>\n'
        '                </div>\n'
        # Card 2 — Sick children / Easter
        '                <div style="background: rgba(220,38,38,0.1); border: 1px solid rgba(220,38,38,0.35); border-radius: 1rem; padding: 1.5rem;">\n'
        f'                    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #fca5a5; margin-bottom: 0.5rem;">{t["c2_label"]}</div>\n'
        f'                    <h3 style="color: white; font-size: 1.05rem; margin: 0 0 0.75rem 0; line-height: 1.4;">{t["c2_title"]}</h3>\n'
        f'                    <p style="color: rgba(255,255,255,0.7); font-size: 0.875rem; line-height: 1.6; margin: 0 0 1rem 0;">{t["c2_desc"]}</p>\n'
        f'                    <a href="/update/breaking/2026/03/29/children-sick-easter-separated.html" style="display: block; text-align: center; background: rgba(220,38,38,0.35); border: 1px solid rgba(220,38,38,0.5); color: white; padding: 0.6rem 1rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; font-size: 0.85rem;">{t["c2_btn"]}</a>\n'
        '                </div>\n'
        '            </div>\n'
        '        </div>\n'
        '    </div>\n'
        '</section>\n'
    )

for lang, t in langs.items():
    path = f'{lang}/index.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    old_comment = t['comment_old']
    start = text.find(old_comment)
    if start == -1:
        print(f'WARN: {lang} — comment not found: {repr(old_comment)}')
        continue

    # Find the closing </section> for this block
    section_end = text.find('</section>', start)
    if section_end == -1:
        print(f'WARN: {lang} — </section> not found after comment')
        continue
    section_end += len('</section>\n')

    old_block = text[start:section_end]
    new_block = build_section(t)

    text = text[:start] + new_block + text[section_end:]

    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'{lang}: OK')

print('Done.')
