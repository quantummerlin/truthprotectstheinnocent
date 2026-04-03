import re

langs = {
    'it': {
        'title': 'BREAKING 26 Marzo — Senato Italiano Riceve Catherine e Nathan | La Famiglia Nel Bosco',
        'description': 'ULTIME NOTIZIE 26 marzo 2026: Catherine e Nathan sono stati ricevuti dal Presidente del Senato Italiano con "grande umanità". Per la prima volta, Catherine ha parlato pubblicamente. Il livello più alto del governo italiano ha ascoltato la verità. #TruthProtectsTheInnocent #LaFamigliaNelBosco',
        'badge': 'BREAKING — 26 MARZO 2026',
        'headline': 'Il Senato Italiano Ha Ascoltato la Loro Verità',
        'lead': 'Oggi Catherine e Nathan sono stati ricevuti dal <strong>Presidente del Senato Italiano</strong> — con quella che Catherine ha definito <em>&ldquo;grande umanità.&rdquo;</em> Dopo, Catherine è uscita e ha parlato pubblicamente per la prima volta da quando è iniziata questa vicenda.',
        'quote_label': '🏛️ Il Primo Discorso Pubblico di Catherine — Fuori dal Senato Italiano',
        'quote_p1': '&ldquo;Dopo mesi di completo silenzio, Nathan ed io desideriamo esprimere la nostra sincera gratitudine a tutti coloro che ci hanno sostenuto in questi lunghi e profondamente difficili giorni, pieni di dolore e tristezza per i nostri bambini.',
        'quote_p2': 'Ciò che Nathan ed io siamo venuti ad offrire oggi era la nostra verità e il nostro continuo impegno come genitori responsabili, rispettosi e amorevoli. E con questa verità, nel dolore più insopportabile, siamo venuti cercando di essere ascoltati e di permetterci di essere di nuovo una famiglia.',
        'quote_p3': 'I nostri sinceri e sentiti ringraziamenti al Presidente del Senato Italiano per averci ricevuto e sostenuto con grande umanità.&rdquo;',
        'quote_attr': 'Catherine Birmingham, fuori dal Senato Italiano &bull; 26 Marzo 2026',
        'sig_line1': 'Il Presidente del Senato Italiano ha ascoltato la verità di questa famiglia.',
        'sig_line2': 'Questo è riconoscimento al massimo livello del governo italiano.',
        'cta_yellow': 'Il Senato li ha ascoltati. Ora il mondo deve agire.',
        'cta_desc': 'Ogni firma alla petizione aggiunge peso a ciò che è stato detto oggi al Senato Italiano.',
        'cta_btn1': '🏛️ Guarda il Video e Leggi la Lettera di Catherine',
        'cta_btn2': '→ Agisci Ora',
        'stat_senate': 'Senato Italiano<br>Li Ha Ricevuti',
        'stat_canale': 'Canale 5<br>Italia',
        'stat_global': 'Attenzione<br>Mondiale',
        'cta_primary': '🏛️ Visita il Senato',
        'cta_pet': '✍️ Firma la Petizione',
        'pet_url': '/it/petition/',
        'subtext': 'Tre bambini. Tre false accuse. Zero motivi validi.<br>Il Senato Italiano ha ora ascoltato ciò che il mondo già sa.',
    },
    'de': {
        'title': 'BREAKING 26. März — Italienischer Senat empfängt Catherine und Nathan | La Famiglia Nel Bosco',
        'description': 'EILMELDUNG 26. März 2026: Catherine und Nathan wurden vom Präsidenten des Italienischen Senats mit "großer Menschlichkeit" empfangen. Zum ersten Mal sprach Catherine öffentlich. Die höchste Ebene der italienischen Regierung hat die Wahrheit gehört. #TruthProtectsTheInnocent',
        'badge': 'BREAKING — 26. MÄRZ 2026',
        'headline': 'Der Italienische Senat Hat Ihre Wahrheit Gehört',
        'lead': 'Heute wurden Catherine und Nathan vom <strong>Präsidenten des Italienischen Senats</strong> empfangen — mit dem, was Catherine <em>&ldquo;große Menschlichkeit&rdquo;</em> nannte. Danach trat Catherine heraus und sprach zum ersten Mal seit Beginn dieser Tragödie öffentlich.',
        'quote_label': '🏛️ Catherines Erste Öffentliche Ansprache — Vor dem Italienischen Senat',
        'quote_p1': '&ldquo;Nach monatelangem völligem Schweigen möchten Nathan und ich unsere aufrichtige Dankbarkeit an alle ausdrücken, die uns in diesen langen und zutiefst schwierigen Tagen voller Schmerz und Trauer um unsere Kinder unterstützt haben.',
        'quote_p2': 'Was Nathan und ich heute anbieten kamen, war unsere Wahrheit und unser anhaltendes Bekenntnis als verantwortungsvolle, respektvolle und liebende Eltern zu sein. Und mit dieser Wahrheit, im unerträglichsten Schmerz, kamen wir und baten darum, gehört zu werden und uns erlauben, wieder eine Familie zu sein.',
        'quote_p3': 'Unser aufrichtiger und herzlicher Dank an den Präsidenten des Italienischen Senats für seinen Empfang und seine Unterstützung mit großer Menschlichkeit.&rdquo;',
        'quote_attr': 'Catherine Birmingham, vor dem Italienischen Senat &bull; 26. März 2026',
        'sig_line1': 'Der Präsident des Italienischen Senats hat die Wahrheit dieser Familie gehört.',
        'sig_line2': 'Dies ist Anerkennung auf höchster Ebene der italienischen Regierung.',
        'cta_yellow': 'Der Senat hat sie gehört. Jetzt muss die Welt handeln.',
        'cta_desc': 'Jede Unterschrift unter die Petition stärkt das, was heute im Italienischen Senat gesagt wurde.',
        'cta_btn1': '🏛️ Video ansehen und Catherines Brief lesen',
        'cta_btn2': '→ Jetzt handeln',
        'stat_senate': 'Italienischer Senat<br>Empfing Sie',
        'stat_canale': 'Canale 5<br>Italien',
        'stat_global': 'Weltweite<br>Aufmerksamkeit',
        'cta_primary': '🏛️ Zum Senatsbesuch',
        'cta_pet': '✍️ Petition unterzeichnen',
        'pet_url': '/de/petition/',
        'subtext': 'Drei Kinder. Drei falsche Behauptungen. Null gültige Gründe.<br>Der Italienische Senat hat nun gehört, was die Welt bereits weiß.',
    },
    'fr': {
        'title': 'BREAKING 26 Mars — Le Sénat Italien Reçoit Catherine et Nathan | La Famiglia Nel Bosco',
        'description': 'DERNIÈRE HEURE 26 mars 2026 : Catherine et Nathan ont été reçus par le Président du Sénat Italien avec "grande humanité". Pour la première fois, Catherine a pris la parole publiquement. Le plus haut niveau du gouvernement italien a entendu la vérité. #TruthProtectsTheInnocent',
        'badge': 'BREAKING — 26 MARS 2026',
        'headline': 'Le Sénat Italien a Entendu Leur Vérité',
        'lead': 'Aujourd\'hui, Catherine et Nathan ont été reçus par le <strong>Président du Sénat Italien</strong> — avec ce que Catherine a appelé <em>&ldquo;grande humanité.&rdquo;</em> Ensuite, Catherine est sortie et a parlé publiquement pour la première fois depuis le début de cette épreuve.',
        'quote_label': '🏛️ Première Prise de Parole Publique de Catherine — Devant le Sénat Italien',
        'quote_p1': '&ldquo;Après des mois de silence complet, Nathan et moi souhaitons exprimer notre gratitude sincère à tous ceux qui nous ont soutenus pendant ces longues et profondément difficiles journées emplie de douleur et de chagrin pour nos enfants.',
        'quote_p2': 'Ce que Nathan et moi sommes venus offrir aujourd\'hui, c\'était notre vérité et notre engagement continu en tant que parents responsables, respectueux et aimants. Et avec cette vérité, dans la douleur la plus insupportable, nous sommes venus pour demander à être entendus et pour nous permettre d\'être à nouveau une famille.',
        'quote_p3': 'Nos sincères et chaleureux remerciements au Président du Sénat Italien pour nous avoir reçus et soutenus avec grande humanité.&rdquo;',
        'quote_attr': 'Catherine Birmingham, devant le Sénat Italien &bull; 26 Mars 2026',
        'sig_line1': 'Le Président du Sénat Italien a entendu la vérité de cette famille.',
        'sig_line2': 'C\'est une reconnaissance au plus haut niveau du gouvernement italien.',
        'cta_yellow': 'Le Sénat les a entendus. Maintenant le monde doit agir.',
        'cta_desc': 'Chaque signature à la pétition ajoute du poids à ce qui a été dit aujourd\'hui au Sénat Italien.',
        'cta_btn1': '🏛️ Voir la Vidéo et Lire la Lettre de Catherine',
        'cta_btn2': '→ Agir Maintenant',
        'stat_senate': 'Sénat Italien<br>Les a Reçus',
        'stat_canale': 'Canale 5<br>Italie',
        'stat_global': 'Attention<br>Mondiale',
        'cta_primary': '🏛️ Voir la Visite au Sénat',
        'cta_pet': '✍️ Signer la Pétition',
        'pet_url': '/fr/petition/',
        'subtext': 'Trois enfants. Trois fausses affirmations. Zéro raison valable.<br>Le Sénat Italien a maintenant entendu ce que le monde sait déjà.',
    },
    'es': {
        'title': 'BREAKING 26 Marzo — El Senado Italiano Recibe a Catherine y Nathan | La Famiglia Nel Bosco',
        'description': 'ÚLTIMA HORA 26 marzo 2026: Catherine y Nathan fueron recibidos por el Presidente del Senado Italiano con "gran humanidad". Por primera vez, Catherine habló públicamente. El nivel más alto del gobierno italiano ha escuchado la verdad. #TruthProtectsTheInnocent',
        'badge': 'BREAKING — 26 DE MARZO 2026',
        'headline': 'El Senado Italiano Ha Escuchado Su Verdad',
        'lead': 'Hoy, Catherine y Nathan fueron recibidos por el <strong>Presidente del Senado Italiano</strong> — con lo que Catherine llamó <em>&ldquo;gran humanidad.&rdquo;</em> Después, Catherine salió y habló públicamente por primera vez desde que comenzó esta tragedia.',
        'quote_label': '🏛️ Primera Declaración Pública de Catherine — Fuera del Senado Italiano',
        'quote_p1': '&ldquo;Después de meses de completo silencio, Nathan y yo queremos expresar nuestra sincera gratitud a todos los que nos han apoyado durante estos largos y profundamente difíciles días llenos de dolor y tristeza por nuestros hijos.',
        'quote_p2': 'Lo que Nathan y yo vinimos a ofrecer hoy fue nuestra verdad y nuestro compromiso continuo como padres responsables, respetuosos y amorosos. Y con esta verdad, en el dolor más insoportable, vinimos pidiendo ser escuchados y que se nos permita ser una familia de nuevo.',
        'quote_p3': 'Nuestro sincero y sentido agradecimiento al Presidente del Senado Italiano por recibirnos y apoyarnos con gran humanidad.&rdquo;',
        'quote_attr': 'Catherine Birmingham, fuera del Senado Italiano &bull; 26 de Marzo 2026',
        'sig_line1': 'El Presidente del Senado Italiano ha escuchado la verdad de esta familia.',
        'sig_line2': 'Este es un reconocimiento al más alto nivel del gobierno italiano.',
        'cta_yellow': 'El Senado los ha escuchado. Ahora el mundo debe actuar.',
        'cta_desc': 'Cada firma en la petición añade peso a lo que se dijo hoy en el Senado Italiano.',
        'cta_btn1': '🏛️ Ver el Video y Leer la Carta de Catherine',
        'cta_btn2': '→ Actuar Ahora',
        'stat_senate': 'Senado Italiano<br>Los Recibió',
        'stat_canale': 'Canale 5<br>Italia',
        'stat_global': 'Atención<br>Mundial',
        'cta_primary': '🏛️ Ver la Visita al Senado',
        'cta_pet': '✍️ Firmar la Petición',
        'pet_url': '/es/petition/',
        'subtext': 'Tres niños. Tres afirmaciones falsas. Cero razones válidas.<br>El Senado Italiano ahora ha escuchado lo que el mundo ya sabe.',
    },
    'pt': {
        'title': 'BREAKING 26 Março — Senado Italiano Recebe Catherine e Nathan | La Famiglia Nel Bosco',
        'description': 'URGENTE 26 março 2026: Catherine e Nathan foram recebidos pelo Presidente do Senado Italiano com "grande humanidade". Pela primeira vez, Catherine falou publicamente. O mais alto nível do governo italiano ouviu a verdade. #TruthProtectsTheInnocent',
        'badge': 'BREAKING — 26 DE MARÇO 2026',
        'headline': 'O Senado Italiano Ouviu a Sua Verdade',
        'lead': 'Hoje, Catherine e Nathan foram recebidos pelo <strong>Presidente do Senado Italiano</strong> — com o que Catherine chamou de <em>&ldquo;grande humanidade.&rdquo;</em> Depois, Catherine saiu e falou publicamente pela primeira vez desde o início desta provação.',
        'quote_label': '🏛️ Primeiro Discurso Público de Catherine — Fora do Senado Italiano',
        'quote_p1': '&ldquo;Após meses de completo silêncio, Nathan e eu gostaríamos de expressar nossa sincera gratidão a todos que nos apoiaram durante esses longos e profundamente difíceis dias repletos de dor e tristeza pelos nossos filhos.',
        'quote_p2': 'O que Nathan e eu viemos oferecer hoje foi nossa verdade e nosso compromisso contínuo como pais responsáveis, respeitosos e amorosos. E com essa verdade, na dor mais insuportável, viemos pedindo para ser ouvidos e que nos permitam ser uma família novamente.',
        'quote_p3': 'Nossa sincera e cordial gratidão ao Presidente do Senado Italiano por nos receber e apoiar com grande humanidade.&rdquo;',
        'quote_attr': 'Catherine Birmingham, fora do Senado Italiano &bull; 26 de Março 2026',
        'sig_line1': 'O Presidente do Senado Italiano ouviu a verdade desta família.',
        'sig_line2': 'Este é um reconhecimento no mais alto nível do governo italiano.',
        'cta_yellow': 'O Senado os ouviu. Agora o mundo deve agir.',
        'cta_desc': 'Cada assinatura na petição acrescenta peso ao que foi dito hoje no Senado Italiano.',
        'cta_btn1': '🏛️ Ver o Vídeo e Ler a Carta de Catherine',
        'cta_btn2': '→ Agir Agora',
        'stat_senate': 'Senado Italiano<br>Os Recebeu',
        'stat_canale': 'Canale 5<br>Itália',
        'stat_global': 'Atenção<br>Mundial',
        'cta_primary': '🏛️ Ver a Visita ao Senado',
        'cta_pet': '✍️ Assinar a Petição',
        'pet_url': '/pt/petition/',
        'subtext': 'Três crianças. Três afirmações falsas. Zero razões válidas.<br>O Senado Italiano ouviu agora o que o mundo já sabe.',
    },
    'ru': {
        'title': 'СРОЧНО 26 Марта — Итальянский Сенат Принял Катрин и Натана | La Famiglia Nel Bosco',
        'description': 'СРОЧНО 26 марта 2026: Катрин и Натан были приняты Председателем Итальянского Сената с "большой человечностью". Впервые Катрин выступила публично. Высший уровень итальянского правительства услышал правду. #TruthProtectsTheInnocent',
        'badge': 'СРОЧНО — 26 МАРТА 2026',
        'headline': 'Итальянский Сенат Услышал Их Правду',
        'lead': 'Сегодня Катрин и Натан были приняты <strong>Председателем Итальянского Сената</strong> — с тем, что Катрин назвала <em>&ldquo;большой человечностью.&rdquo;</em> После этого Катрин вышла и впервые публично обратилась к людям с момента начала этого испытания.',
        'quote_label': '🏛️ Первое Публичное Обращение Катрин — Перед Итальянским Сенатом',
        'quote_p1': '&ldquo;После месяцев полного молчания мы с Натаном хотим выразить нашу искреннюю благодарность всем, кто поддерживал нас в эти долгие и невыносимо трудные дни, полные боли и скорби о наших детях.',
        'quote_p2': 'То, что мы с Натаном пришли сегодня предложить — это наша правда и наша неизменная преданность как ответственных, уважительных и любящих родителей. И с этой правдой, в невыносимой боли, мы пришли с просьбой быть услышанными и позволить нам снова быть семьёй.',
        'quote_p3': 'Наша искренняя и сердечная благодарность Председателю Итальянского Сената за то, что принял нас и поддержал с большой человечностью.&rdquo;',
        'quote_attr': 'Катрин Бирмингем, перед Итальянским Сенатом &bull; 26 Марта 2026',
        'sig_line1': 'Председатель Итальянского Сената услышал правду этой семьи.',
        'sig_line2': 'Это признание на высшем уровне итальянского правительства.',
        'cta_yellow': 'Сенат их услышал. Теперь мир должен действовать.',
        'cta_desc': 'Каждая подпись под петицией добавляет вес тому, что было сказано сегодня в Итальянском Сенате.',
        'cta_btn1': '🏛️ Смотреть Видео и Читать Письмо Катрин',
        'cta_btn2': '→ Действовать Сейчас',
        'stat_senate': 'Итальянский Сенат<br>Принял Их',
        'stat_canale': 'Canale 5<br>Италия',
        'stat_global': 'Мировое<br>Внимание',
        'cta_primary': '🏛️ Посетить Сенат',
        'cta_pet': '✍️ Подписать Петицию',
        'pet_url': '/ru/petition/',
        'subtext': 'Трое детей. Три ложных обвинения. Ноль законных оснований.<br>Итальянский Сенат теперь услышал то, что мир уже знает.',
    },
    'pl': {
        'title': 'BREAKING 26 Marca — Włoski Senat Przyjął Catherine i Nathana | La Famiglia Nel Bosco',
        'description': 'PILNE 26 marca 2026: Catherine i Nathan zostali przyjęci przez Przewodniczącego Włoskiego Senatu z "wielką ludzkością". Po raz pierwszy Catherine zabrała głos publicznie. Najwyższy szczebel włoskiego rządu usłyszał prawdę. #TruthProtectsTheInnocent',
        'badge': 'BREAKING — 26 MARCA 2026',
        'headline': 'Włoski Senat Wysłuchał Ich Prawdy',
        'lead': 'Dziś Catherine i Nathan zostali przyjęci przez <strong>Przewodniczącego Włoskiego Senatu</strong> — z tym, co Catherine nazwała <em>&ldquo;wielką ludzkością.&rdquo;</em> Następnie Catherine wyszła i po raz pierwszy publicznie zabrała głos od początku tej próby.',
        'quote_label': '🏛️ Pierwsze Publiczne Przemówienie Catherine — Przed Włoskim Senatem',
        'quote_p1': '&ldquo;Po miesiącach całkowitego milczenia, Nathan i ja chcielibyśmy wyrazić naszą serdeczną wdzięczność wszystkim, którzy wspierali nas przez te długie i głęboko trudne dni pełne bólu i smutku o nasze dzieci.',
        'quote_p2': 'To, co Nathan i ja przyszliśmy dziś zaoferować, to nasza prawda i nasze nieustanne zaangażowanie jako odpowiedzialnych, szanujących i kochających rodziców. I z tą prawdą, w najbardziej nieznośnym bólu, przyszliśmy prosząc o wysłuchanie i pozwolenie nam być znowu rodziną.',
        'quote_p3': 'Nasza szczera i serdeczna wdzięczność Przewodniczącemu Włoskiego Senatu za przyjęcie i wsparcie z wielką ludzkością.&rdquo;',
        'quote_attr': 'Catherine Birmingham, przed Włoskim Senatem &bull; 26 Marca 2026',
        'sig_line1': 'Przewodniczący Włoskiego Senatu wysłuchał prawdy tej rodziny.',
        'sig_line2': 'To uznanie na najwyższym szczeblu włoskiego rządu.',
        'cta_yellow': 'Senat ich wysłuchał. Teraz świat musi działać.',
        'cta_desc': 'Każdy podpis pod petycją dodaje siły temu, co zostało powiedziane dziś we Włoskim Senacie.',
        'cta_btn1': '🏛️ Obejrzyj Film i Przeczytaj List Catherine',
        'cta_btn2': '→ Działaj Teraz',
        'stat_senate': 'Włoski Senat<br>Przyjął Ich',
        'stat_canale': 'Canale 5<br>Włochy',
        'stat_global': 'Globalna<br>Uwaga',
        'cta_primary': '🏛️ Wizyta w Senacie',
        'cta_pet': '✍️ Podpisz Petycję',
        'pet_url': '/pl/petition/',
        'subtext': 'Troje dzieci. Trzy fałszywe twierdzenia. Zero ważnych powodów.<br>Włoski Senat teraz wysłuchał tego, co świat już wie.',
    },
}

def build_new_hero_body(t, psych_block):
    return f"""
        <!-- Breaking Badge -->
        <div class="sixty-mins-badge-wrap">
            <span class="sixty-mins-badge sixty-mins-badge-aired" id="sixtyMinsBadge">
                {t['badge']}
            </span>
        </div>

        <h1 class="sixty-mins-headline">{t['headline']}</h1>
        <p class="lead">{t['lead']}</p>

        <!-- Senate Quote Box -->
        <div style="background: rgba(0,0,0,0.75); border: 1px solid rgba(124,58,237,0.7); border-left: 5px solid #7c3aed; border-radius: 1rem; padding: 1.5rem 2rem; margin-bottom: 1.75rem; text-align: left; max-width: 720px; margin-left: auto; margin-right: auto;">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem; flex-wrap: wrap;">
                <span style="background: rgba(124,58,237,0.3); border: 1px solid rgba(124,58,237,0.6); color: #c4b5fd; font-weight: 700; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; padding: 0.3rem 0.9rem; border-radius: 2rem;">{t['quote_label']}</span>
            </div>
            <p style="color: white; font-size: 1rem; line-height: 1.8; font-style: italic; margin: 0 0 0.75rem 0;">{t['quote_p1']}</p>
            <p style="color: rgba(255,255,255,0.9); font-size: 1rem; line-height: 1.8; font-style: italic; margin: 0 0 0.75rem 0;">{t['quote_p2']}</p>
            <p style="color: #c4b5fd; font-size: 1.05rem; line-height: 1.8; font-style: italic; font-weight: 700; margin: 0 0 1rem 0;">{t['quote_p3']}</p>
            <p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin: 0;">\u2014 <strong style="color: rgba(255,255,255,0.9);">{t['quote_attr']}</strong></p>
        </div>

        <!-- Significance Statement -->
        <div style="background: rgba(124,58,237,0.2); border: 2px solid rgba(124,58,237,0.6); border-radius: 0.75rem; padding: 0.9rem 1.5rem; margin-bottom: 1.75rem; text-align: center; max-width: 720px; margin-left: auto; margin-right: auto;">
            <p style="color: white; font-size: 1.05rem; font-weight: 700; margin: 0;">{t['sig_line1']}<br><span style="color: #c4b5fd;">{t['sig_line2']}</span></p>
        </div>

        <!-- CTA Box -->
        <div class="hero-alert-box">
            <p style="color: #fef08a; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem;">{t['cta_yellow']}</p>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1rem;">{t['cta_desc']}</p>
            <div class="hero-alert-btns">
                <a href="/senate/breaking/2026/03/26/senate-visit-catherine-addresses-public.html"
                   style="background: #7c3aed; color: white; padding: 0.75rem 1.5rem; border-radius: 0.5rem; text-decoration: none; font-weight: 700; font-size: 0.95rem; display: block; text-align: center;">{t['cta_btn1']}</a>
                <a href="/action/"
                   style="background: rgba(255,255,255,0.15); color: white; border: 1.5px solid rgba(255,255,255,0.5); padding: 0.75rem 1.5rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; font-size: 0.95rem; display: block; text-align: center;">{t['cta_btn2']}</a>
            </div>
        </div>

{psych_block}
        <!-- Coverage Stats -->
        <div class="hero-stats sixty-mins-stats">
            <div class="hero-stat">
                <span class="hero-stat-number">\U0001f3db\ufe0f</span>
                <span class="hero-stat-label">{t['stat_senate']}</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">\U0001f1e6\U0001f1fa</span>
                <span class="hero-stat-label">60 Minutes<br>Australia</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">\U0001f1ee\U0001f1f9</span>
                <span class="hero-stat-label">{t['stat_canale']}</span>
            </div>
            <div class="hero-stat">
                <span class="hero-stat-number">\U0001f30d</span>
                <span class="hero-stat-label">{t['stat_global']}</span>
            </div>
        </div>

        <div class="hero-cta">
            <a href="/senate/breaking/2026/03/26/senate-visit-catherine-addresses-public.html" class="btn btn-primary btn-lg btn-glow">{t['cta_primary']}</a>
            <a href="{t['pet_url']}" class="btn btn-secondary btn-lg">{t['cta_pet']}</a>
            <a href="/evidence/" class="btn btn-secondary btn-lg">Evidence</a>
        </div>

        <p class="sixty-mins-subtext">{t['subtext']}</p>
    </div>
</section>"""

for lang, t in langs.items():
    path = f'{lang}/index.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update front matter
    text = re.sub(r'title: ".*?"', f'title: "{t["title"]}"', text, count=1)
    text = re.sub(r'description: ".*?"', f'description: "{t["description"]}"', text, count=1, flags=re.DOTALL)
    text = re.sub(r'updated: .*', 'updated: 2026-03-26-senate', text, count=1)

    # 2. Update background video
    text = text.replace(
        '<source src="/assets/videos/60-minutes-trailer.mp4" type="video/mp4">',
        '<source src="/assets/videos/senate invite.mp4" type="video/mp4">'
    )

    # 3. Extract the psychiatrist block (from its comment to the badge)
    hero_content_start = text.find('<div class="hero-content">')
    section_end = text.find('</section>', hero_content_start)

    # Find psych comment (varies slightly per language)
    psych_markers = [
        '<!-- Valutazione Psichiatrica',
        '<!-- Psychiater Zitat',
        '<!-- Évaluation Psychiatrique',
        '<!-- Evaluación Psiquiátrica',
        '<!-- Avaliação Psiquiátrica',
        '<!-- Психиатрическая оценка',
        '<!-- Ocena Psychiatryczna',
    ]
    psych_start = -1
    for marker in psych_markers:
        idx = text.find(marker, hero_content_start)
        if idx != -1:
            psych_start = idx
            break

    # Find end of the psych block (the closing div after the red summary bar)
    # The psych block ends after the red "no alternative" summary div's closing </div>
    # which is followed by a blank line and then the badge
    badge_pos = text.find('<div class="sixty-mins-badge-wrap">', hero_content_start)

    if psych_start == -1 or badge_pos == -1:
        print(f'ERROR: {lang} - could not find psych block or badge. psych={psych_start}, badge={badge_pos}')
        continue

    psych_block = text[psych_start:badge_pos]

    # 4. Build new content: everything from badge to </section>
    # Replace from psych_start to section_end+len('</section>')
    before_hero_body = text[:psych_start]
    after_section = text[section_end + len('</section>'):]

    new_hero = build_new_hero_body(t, psych_block)
    new_text = before_hero_body + new_hero + after_section

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print(f'{lang}: done (len={len(new_text)})')

print('All languages updated.')
