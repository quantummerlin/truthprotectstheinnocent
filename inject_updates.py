import os

root = r'c:\Users\WIPED\A Worldwide Meditation\truthprotectstheinnocent'

def make_section(badge, new_comment, ls_label, ls_h3, ls_p, ls_link, st_label, st_h3, st_p, st_alt, st_link):
    return f"""
{new_comment}
<section style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 2rem 0;">
    <div class="container">
        <div style="max-width: 900px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <span style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.8); padding: 0.4rem 1.25rem; border-radius: 2rem; font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase;">\U0001f5de\ufe0f {badge}</span>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
                <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 1rem; padding: 1.5rem;">
                    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 0.5rem;">{ls_label}</div>
                    <h3 style="color: white; font-size: 1.05rem; margin: 0 0 0.75rem 0; line-height: 1.4;">{ls_h3}</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 0.875rem; line-height: 1.6; margin: 0 0 1rem 0;">{ls_p}</p>
                    <a href="/2026/03/14/la-stampa-social-workers-statement.html" style="display: block; text-align: center; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.25); color: white; padding: 0.6rem 1rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; font-size: 0.85rem;">{ls_link}</a>
                </div>
                <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 1rem; padding: 1.5rem;">
                    <div style="font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: rgba(255,255,255,0.5); margin-bottom: 0.5rem;">{st_label}</div>
                    <h3 style="color: white; font-size: 1.05rem; margin: 0 0 0.75rem 0; line-height: 1.4;">{st_h3}</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 0.875rem; line-height: 1.6; margin: 0 0 0.75rem 0;">{st_p}</p>
                    <img src="/assets/images/stadium-banner-march-2026.jpg" alt="{st_alt}" style="width: 100%; border-radius: 0.5rem; margin-bottom: 0.75rem;">
                    <a href="/2026/03/15/football-fan-stadium-support.html" style="display: block; text-align: center; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.25); color: white; padding: 0.6rem 1rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; font-size: 0.85rem;">{st_link}</a>
                </div>
            </div>
        </div>
    </div>
</section>

"""

langs = {
    'de': {
        'badge': 'NEUESTE ENTWICKLUNG \u2014 15. M\u00c4RZ 2026',
        'new_comment': '<!-- NEUESTE ENTWICKLUNG \u2014 15. M\u00c4RZ 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14. M\u00c4R 2026',
        'ls_h3': 'Sozialarbeiter geben zu: \u201eNach der Entfernung der Mutter wurden gute Beziehungen mit den Kindern wiederhergestellt\u201c',
        'ls_p': 'La Stampa berichtet \u00fcber die \u00f6ffentliche Erkl\u00e4rung der Sozialarbeiter nach dem Besuch der Nationalen Kinderrechts-Garantin \u2014 und vergleicht die Familie mit einer anderen italienischen Alternativfamilie, deren Kinder nie entfernt wurden.',
        'ls_link': '\U0001f4f0 Vollst\u00e4ndigen Artikel lesen \u2192',
        'st_label': 'SOLIDARIT\u00c4T \u00b7 M\u00c4RZ 2026',
        'st_h3': 'Im Stadion: \u201eDear Catherine and Nathan \u2014 You\'ll Never Walk Alone\u201c',
        'st_p': 'Ein Fu\u00dfballfan hielt ein handbemaltes Banner f\u00fcr Zehntausende sichtbar hoch.',
        'st_alt': 'Stadion-Banner \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd Mehr erfahren \u2192',
        'leaked': '<!-- DURCHGESICKERTE INFORMATIONEN - DRINGEND -->',
    },
    'it': {
        'badge': 'AGGIORNAMENTO \u2014 15 MARZO 2026',
        'new_comment': '<!-- AGGIORNAMENTO \u2014 15 MARZO 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 MAR 2026',
        'ls_h3': "Assistenti sociali ammettono: \"Dopo l'allontanamento della madre, le relazioni con i bambini sono migliorate\"",
        'ls_p': "La Stampa riporta la dichiarazione pubblica degli assistenti sociali dopo la visita della Garante Nazionale \u2014 e confronta la famiglia con un'altra famiglia alternativa italiana i cui figli non sono mai stati allontanati.",
        'ls_link': "\U0001f4f0 Leggi l'articolo completo \u2192",
        'st_label': 'SOLIDARIET\u00c0 \u00b7 MARZO 2026',
        'st_h3': 'Dallo stadio: "Dear Catherine and Nathan \u2014 You\'ll Never Walk Alone"',
        'st_p': 'Un tifoso ha mostrato uno striscione dipinto a mano a decine di migliaia di persone durante una partita di calcio italiana.',
        'st_alt': 'Striscione allo stadio \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd Leggi di pi\u00f9 \u2192',
        'leaked': '<!-- ULTIME NOTIZIE - URGENTE -->',
    },
    'es': {
        'badge': 'ACTUALIZACI\u00d3N \u2014 15 DE MARZO DE 2026',
        'new_comment': '<!-- ACTUALIZACI\u00d3N \u2014 15 DE MARZO DE 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 MAR 2026',
        'ls_h3': 'Trabajadores sociales reconocen: "Tras la expulsi\u00f3n de la madre, se restablecieron las buenas relaciones con los ni\u00f1os"',
        'ls_p': 'La Stampa informa sobre la declaraci\u00f3n p\u00fablica de los trabajadores sociales tras la visita de la Garante Nacional \u2014 y compara a la familia con otra familia alternativa italiana cuyos hijos nunca fueron separados.',
        'ls_link': '\U0001f4f0 Leer el art\u00edculo completo \u2192',
        'st_label': 'SOLIDARIDAD \u00b7 MARZO 2026',
        'st_h3': 'Desde el estadio: "Dear Catherine and Nathan \u2014 You\'ll Never Walk Alone"',
        'st_p': 'Un aficionado sostuvo una pancarta pintada a mano ante decenas de miles de personas en un partido de f\u00fatbol italiano.',
        'st_alt': 'Pancarta en el estadio \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd Leer m\u00e1s \u2192',
        'leaked': '<!-- INFORMACI\u00d3N FILTRADA - URGENTE -->',
    },
    'fr': {
        'badge': 'DERNI\u00c8RE MISE \u00c0 JOUR \u2014 15 MARS 2026',
        'new_comment': '<!-- DERNI\u00c8RE MISE \u00c0 JOUR \u2014 15 MARS 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 MARS 2026',
        'ls_h3': 'Les travailleurs sociaux avouent\u00a0: \u00ab\u00a0Apr\u00e8s le d\u00e9part de la m\u00e8re, de bonnes relations avec les enfants ont \u00e9t\u00e9 r\u00e9tablies\u00a0\u00bb',
        'ls_p': "La Stampa rapporte la d\u00e9claration publique des travailleurs sociaux apr\u00e8s la visite de la Garante nationale \u2014 et compare la famille \u00e0 une autre famille alternative italienne dont les enfants n'ont jamais \u00e9t\u00e9 s\u00e9par\u00e9s.",
        'ls_link': "\U0001f4f0 Lire l'article complet \u2192",
        'st_label': 'SOLIDARIT\u00c9 \u00b7 MARS 2026',
        'st_h3': 'Depuis le stade\u00a0: \u00ab\u00a0Dear Catherine and Nathan \u2014 You\'ll Never Walk Alone\u00a0\u00bb',
        'st_p': "Un supporter a brandi une banderole peinte \u00e0 la main devant des dizaines de milliers de personnes lors d'un match de football en Italie.",
        'st_alt': 'Banderole au stade \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd En savoir plus \u2192',
        'leaked': '<!-- INFORMATIONS DIVU',
    },
    'pl': {
        'badge': 'NAJNOWSZA AKTUALIZACJA \u2014 15 MARCA 2026',
        'new_comment': '<!-- NAJNOWSZA AKTUALIZACJA \u2014 15 MARCA 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 MAR 2026',
        'ls_h3': 'Pracownicy socjalni przyznaj\u0105: \u201ePo usuni\u0119ciu matki przywr\u00f3cono dobre relacje z dzie\u0107mi\u201c',
        'ls_p': 'La Stampa relacjonuje publiczne o\u015bwiadczenie pracownik\u00f3w socjalnych po wizycie Krajowego Rzecznika Praw Dziecka \u2014 i por\u00f3wnuje rodzin\u0119 z inn\u0105 w\u0142osk\u0105 rodzin\u0105 alternatywn\u0105, kt\u00f3rej dzieci nigdy nie zosta\u0142y odebrane.',
        'ls_link': '\U0001f4f0 Przeczytaj pe\u0142ny artyku\u0142 \u2192',
        'st_label': 'SOLIDARNO\u015a\u0106 \u00b7 MARZEC 2026',
        'st_h3': 'Ze stadionu: \u201eDear Catherine and Nathan \u2014 You\'ll Never Walk Alone\u201c',
        'st_p': 'Kibic trzyma\u0142 r\u0119cznie namalowany transparent przed dziesi\u0105tkami tysi\u0119cy os\u00f3b podczas w\u0142oskiego meczu pi\u0142ki no\u017cnej.',
        'st_alt': 'Transparent na stadionie \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd Dowiedz si\u0119 wi\u0119cej \u2192',
        'leaked': '<!-- WYCIEK INFORMACJI - PILNE -->',
    },
    'pt': {
        'badge': 'ATUALIZA\u00c7\u00c3O \u2014 15 DE MAR\u00c7O DE 2026',
        'new_comment': '<!-- ATUALIZA\u00c7\u00c3O \u2014 15 DE MAR\u00c7O DE 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 MAR 2026',
        'ls_h3': 'Assistentes sociais admitem: "Ap\u00f3s a remo\u00e7\u00e3o da m\u00e3e, boas rela\u00e7\u00f5es com as crian\u00e7as foram restabelecidas"',
        'ls_p': 'La Stampa relata a declara\u00e7\u00e3o p\u00fablica dos assistentes sociais ap\u00f3s a visita da Garante Nacional \u2014 e compara a fam\u00edlia com outra fam\u00edlia alternativa italiana cujos filhos nunca foram afastados.',
        'ls_link': '\U0001f4f0 Leia o artigo completo \u2192',
        'st_label': 'SOLIDARIEDADE \u00b7 MAR\u00c7O 2026',
        'st_h3': 'Do est\u00e1dio: "Dear Catherine and Nathan \u2014 You\'ll Never Walk Alone"',
        'st_p': 'Um adepto exibiu uma faixa pintada \u00e0 m\u00e3o para dezenas de milh\u00f5es de pessoas durante um jogo de futebol italiano.',
        'st_alt': 'Faixa no est\u00e1dio \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd Leia mais \u2192',
        'leaked': '<!-- INFORMA\u00c7\u00d5ES VAZADAS - URGENTE -->',
    },
    'ru': {
        'badge': '\u041f\u041e\u0421\u041b\u0415\u0414\u041d\u0415\u0415 \u041e\u0411\u041d\u041e\u0412\u041b\u0415\u041d\u0418\u0415 \u2014 15 \u041c\u0410\u0420\u0422\u0410 2026',
        'new_comment': '<!-- \u041f\u041e\u0421\u041b\u0415\u0414\u041d\u0415\u0415 \u041e\u0411\u041d\u041e\u0412\u041b\u0415\u041d\u0418\u0415 \u2014 15 \u041c\u0410\u0420\u0422\u0410 2026 -->',
        'ls_label': 'LA STAMPA \u00b7 14 \u041c\u0410\u0420 2026',
        'ls_h3': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u044e\u0442: \u00ab\u041f\u043e\u0441\u043b\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f \u0441 \u0434\u0435\u0442\u044c\u043c\u0438 \u043d\u0430\u043b\u0430\u0434\u0438\u043b\u0438\u0441\u044c\u00bb',
        'ls_p': 'La Stampa \u0441\u043e\u043e\u0431\u0449\u0430\u0435\u0442 \u043e \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e\u043c \u0437\u0430\u044f\u0432\u043b\u0435\u043d\u0438\u0438 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432 \u043f\u043e\u0441\u043b\u0435 \u0432\u0438\u0437\u0438\u0442\u0430 \u041d\u0430\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0443\u043f\u043e\u043b\u043d\u043e\u043c\u043e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u043f\u043e \u043f\u0440\u0430\u0432\u0430\u043c \u0434\u0435\u0442\u0435\u0439.',
        'ls_link': '\U0001f4f0 \u0427\u0438\u0442\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u044c\u044e \u2192',
        'st_label': '\u0421\u041e\u041b\u0418\u0414\u0410\u0420\u041d\u041e\u0421\u0422\u042c \u00b7 \u041c\u0410\u0420\u0422 2026',
        'st_h3': '\u0421 \u0442\u0440\u0438\u0431\u0443\u043d \u0441\u0442\u0430\u0434\u0438\u043e\u043d\u0430: \u00abDear Catherine and Nathan \u2014 You\'ll Never Walk Alone\u00bb',
        'st_p': '\u0411\u043e\u043b\u0435\u043b\u044c\u0449\u0438\u043a \u043f\u043e\u0434\u043d\u044f\u043b \u0441\u0430\u043c\u043e\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u0431\u0430\u043d\u043d\u0435\u0440 \u043d\u0430 \u0438\u0442\u0430\u043b\u044c\u044f\u043d\u0441\u043a\u043e\u043c \u043c\u0430\u0442\u0447\u0435.',
        'st_alt': '\u0411\u0430\u043d\u043d\u0435\u0440 \u043d\u0430 \u0441\u0442\u0430\u0434\u0438\u043e\u043d\u0435 \u2014 You\'ll Never Walk Alone',
        'st_link': '\u26bd \u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435 \u2192',
        'leaked': '<!-- \u0423\u0422\u0415\u0427\u041a\u0410 \u0418\u041d\u0424\u041e\u0420\u041c\u0410\u0426\u0418\u0418 - \u0421\u0420\u041e\u0427\u041d\u041e -->',
    },
}

for lang, d in langs.items():
    fpath = os.path.join(root, lang, 'index.md')
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if d['new_comment'] in content:
        print(f'SKIP({lang}): already updated')
        continue
    idx = content.find(d['leaked'])
    if idx == -1:
        print(f'MISS({lang}): leaked comment not found')
        continue
    section = make_section(d['badge'], d['new_comment'], d['ls_label'], d['ls_h3'], d['ls_p'], d['ls_link'], d['st_label'], d['st_h3'], d['st_p'], d['st_alt'], d['st_link'])
    content = content[:idx] + section + content[idx:]
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'OK: {lang}')
