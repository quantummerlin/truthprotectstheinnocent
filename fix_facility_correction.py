"""
Correction: the children were court-ordered to be moved to a new facility,
but the family was able to appeal and the transfer was blocked.
All references to "moved to a new facility" (as a completed fact) must be corrected.
"""

import os

def fix(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    original = text
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f'  WARN: pattern not found in {path}:\n    {repr(old[:80])}')
    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'  OK: {path}')
    else:
        print(f'  UNCHANGED: {path}')

# ─────────────────────────────────────────────────────────────────────────────
# 1. Main post about the court order / appeal
# ─────────────────────────────────────────────────────────────────────────────
fix('_posts/2026-03-08-children-moved-new-facility-catherine-banned.md', [
    (
        'title: "After 60 Minutes Airs: Authorities Move Children to New Facility — Catherine Banned From Staying"',
        'title: "After 60 Minutes Airs: Court Orders Children Moved to New Facility — Family Successfully Appeals"'
    ),
    (
        'summary: "Following the broadcast of the 60 Minutes segment, Italian authorities have ruled to move the children to a new facility where Catherine is not permitted to stay. A video captures the heartbreaking goodbye."',
        'summary: "Following the 60 Minutes broadcast, the court ordered the children to be transferred to a new facility where Catherine would not be permitted to stay. Catherine and the children said goodbye — but the family successfully appealed the order. The transfer did not proceed."'
    ),
    (
        '## Children Moved After 60 Minutes Broadcast\n\nIn the wake of the international attention brought by the 60 Minutes television segment, Italian authorities have ruled to transfer the three Birmingham-Trevallion children to a **new facility** — with one devastating condition: **Catherine is not allowed to stay there.**\n\nThis move follows directly after the case received global media coverage, raising serious questions about whether the transfer is a punitive response to the family speaking out publicly.',
        '## Court Orders Children Transferred — Family Successfully Appeals\n\nIn the wake of the international attention brought by the 60 Minutes television segment, the court issued an order to transfer the three Birmingham-Trevallion children to a **new facility** — with one devastating condition attached: **Catherine would not be permitted to stay there.**\n\nThis order followed directly after the case received global media coverage, raising serious questions about whether the transfer was a punitive response to the family speaking out publicly.\n\n**The family appealed the order — and succeeded.** The transfer was blocked. The children were not moved.'
    ),
    (
        '## The Goodbye\n\nThe moment Catherine had to say goodbye to her children before they were taken to the new facility was captured on video.',
        '## The Goodbye\n\nFacing the prospect of her children being taken away to a facility where she could not follow, Catherine said goodbye to them. The moment was captured on video.\n\n*Update: The family successfully appealed the court order. The transfer did not take place.*'
    ),
    (
        '<li><strong>Catherine is banned from the new facility</strong> — she will no longer be able to stay near her children</li>',
        '<li><strong>The court ordered Catherine banned from the new facility</strong> — but the family appealed and the transfer order was successfully challenged</li>'
    ),
    (
        'No explanation has been given. The children are now being moved to a new facility where Catherine cannot stay — and still no one in authority has provided a legitimate justification.',
        'No explanation was given for why the court would separate the children further from their mother. The family challenged the order and successfully appealed — the transfer did not proceed. Still, no one in authority has provided a legitimate justification for why this order was made in the first place.'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 2. Updates timeline page
# ─────────────────────────────────────────────────────────────────────────────
fix('pages/updates.md', [
    (
        'Children moved to new facility — Catherine banned from staying',
        'Court orders children moved to new facility — family successfully appeals'
    ),
    (
        'Following 60 Minutes, Italian authorities transferred the children to a new facility where Catherine is not permitted to stay. The goodbye was filmed.',
        'After 60 Minutes aired, the court ordered the children transferred to a new facility where Catherine could not stay. Catherine recorded a goodbye — but the family successfully appealed the court order, and the transfer did not proceed.'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 3. English homepage (index.md — may have CRLF, handled by universal replace)
# ─────────────────────────────────────────────────────────────────────────────
fix('index.md', [
    (
        'now they have been moved to a new facility where Catherine cannot stay',
        'the court ordered the children transferred to a new facility where Catherine could not stay — the family successfully appealed, and the transfer was blocked'
    ),
    (
        '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Moved to New Facility</p>',
        '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Transfer Order Appealed</p>'
    ),
    (
        '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">After 60 Minutes aired, Catherine was banned from the new facility where her children are now held</p>',
        '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">After 60 Minutes aired, the court ordered the children moved to a new facility banning Catherine — the family appealed and blocked the transfer</p>'
    ),
    (
        '"headline": "Children Moved to New Facility — Catherine Banned After 60 Minutes Broadcast"',
        '"headline": "Court Orders Children Moved to New Facility — Family Successfully Appeals and Blocks Transfer"'
    ),
    (
        '"description": "After the 60 Minutes Australia broadcast, Italian authorities moved the children to a new facility and banned Catherine Birmingham from staying there."',
        '"description": "After the 60 Minutes Australia broadcast, the court ordered the children moved to a new facility and banned Catherine Birmingham from staying there. The family successfully appealed and blocked the transfer."'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 4. La Stampa post — references to children being moved
# ─────────────────────────────────────────────────────────────────────────────
fix('_posts/2026-03-14-la-stampa-social-workers-statement.md', [
    (
        'the reason the children were moved to a new facility was **because of Catherine\'s presence**',
        'the reason the court ordered the children to a new facility was **because of Catherine\'s presence** (though the family successfully appealed and the transfer was blocked)'
    ),
    (
        'The children were moved to a new facility — now officially admitted to be <strong>because Catherine was present and advocating for them</strong>',
        'The court ordered the children to a new facility — now officially admitted to be <strong>because Catherine was present and advocating for them</strong> (the family successfully appealed this order)'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 5. Football stadium post
# ─────────────────────────────────────────────────────────────────────────────
fix('_posts/2026-03-15-football-fan-stadium-support.md', [
    (
        'They have seen the children moved to a new facility.',
        'They have seen the court order to move the children to a new facility — and the family\'s successful appeal that blocked it.'
    ),
    (
        'Catherine has been **banned from staying at the new facility**',
        'The court ordered Catherine **banned from staying at a new facility** — an order the family successfully appealed'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 6. Senate post — reference to banned from new facility
# ─────────────────────────────────────────────────────────────────────────────
fix('_posts/2026-03-26-senate-visit-catherine-addresses-public.md', [
    (
        'Catherine was **banned from staying** at the new facility after the transfer',
        'The court ordered Catherine **banned from a new facility** — an order the family successfully appealed, blocking the transfer'
    ),
])

# ─────────────────────────────────────────────────────────────────────────────
# 7. Language files — psych/red-section references
# ─────────────────────────────────────────────────────────────────────────────
lang_fixes = {
    'it': [
        (
            'ora li hanno trasferiti in una nuova struttura dove <strong style="color: #fef08a;">Catherine non può rimanere</strong>',
            'il tribunale ha ordinato il loro trasferimento in una nuova struttura dove <strong style="color: #fef08a;">Catherine non avrebbe potuto rimanere</strong> — la famiglia ha presentato ricorso con successo e il trasferimento è stato bloccato'
        ),
        (
            '<h2 style="color: white; font-size: 2rem; margin-bottom: 1rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">Bambini Spostati — Catherine Esclusa dalla Nuova Struttura</h2>',
            '<h2 style="color: white; font-size: 2rem; margin-bottom: 1rem; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">Ordine di Trasferimento Impugnato — La Famiglia Fa Ricorso con Successo</h2>'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Spostati in Nuova Struttura</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Ordine di Trasferimento Impugnato</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Dopo 60 Minutes, Catherine è stata esclusa dalla nuova struttura dove sono stati trasferiti i bambini</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Dopo 60 Minutes, il tribunale ha ordinato lo spostamento dei bambini escludendo Catherine — la famiglia ha fatto ricorso e bloccato il trasferimento</p>'
        ),
    ],
    'de': [
        (
            'jetzt wurden sie in eine neue Einrichtung gebracht, in der <strong style="color: #fef08a;">Catherine nicht bleiben darf</strong>',
            'ordnete das Gericht ihre Verlegung in eine neue Einrichtung an, in der <strong style="color: #fef08a;">Catherine nicht bleiben dürfte</strong> — die Familie legte erfolgreich Widerspruch ein und die Verlegung wurde blockiert'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">In neue Einrichtung verlegt</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Verlegungsanordnung erfolgreich angefochten</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Nach 60 Minutes wurde Catherine von der neuen Einrichtung ausgeschlossen, in die ihre Kinder gebracht wurden</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Nach 60 Minutes ordnete das Gericht die Verlegung an und schloss Catherine aus — die Familie legte Widerspruch ein und blockierte die Verlegung</p>'
        ),
    ],
    'fr': [
        (
            'maintenant ils ont été transférés dans un nouvel établissement où <strong style="color: #fef08a;">Catherine ne peut pas rester</strong>',
            'le tribunal a ordonné leur transfert vers un nouvel établissement où <strong style="color: #fef08a;">Catherine ne pourrait pas rester</strong> — la famille a fait appel avec succès et le transfert a été bloqué'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Transférés dans un Nouvel Établissement</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Ordonnance de Transfert Contestée avec Succès</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Après 60 Minutes, Catherine a été exclue du nouvel établissement où ses enfants ont été transférés</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Après 60 Minutes, le tribunal a ordonné le transfert en excluant Catherine — la famille a fait appel et bloqué le transfert</p>'
        ),
    ],
    'es': [
        (
            'ahora los han trasladado a una nueva instalación donde <strong style="color: #fef08a;">Catherine no puede quedarse</strong>',
            'el tribunal ordenó su traslado a una nueva instalación donde <strong style="color: #fef08a;">Catherine no podría quedarse</strong> — la familia apeló con éxito y el traslado fue bloqueado'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Trasladados a Nueva Instalación</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Orden de Traslado Recurrida con Éxito</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Tras 60 Minutes, Catherine fue excluida de la nueva instalación donde fueron trasladados los niños</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Tras 60 Minutes, el tribunal ordenó el traslado excluyendo a Catherine — la familia apeló y bloqueó el traslado</p>'
        ),
    ],
    'pt': [
        (
            'agora foram transferidas para uma nova instalação onde <strong style="color: #fef08a;">Catherine não pode ficar</strong>',
            'o tribunal ordenou a transferência para uma nova instalação onde <strong style="color: #fef08a;">Catherine não poderia ficar</strong> — a família recorreu com sucesso e a transferência foi bloqueada'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Transferidas para Nova Instalação</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Ordem de Transferência Recorrida com Sucesso</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Após 60 Minutes, Catherine foi banida da nova instalação para onde as crianças foram transferidas</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Após 60 Minutes, o tribunal ordenou a transferência excluindo Catherine — a família recorreu e bloqueou a transferência</p>'
        ),
    ],
    'ru': [
        (
            'теперь их перевели в новое учреждение, где <strong style="color: #fef08a;">Катрин не может оставаться</strong>',
            'суд постановил перевести их в новое учреждение, где <strong style="color: #fef08a;">Катрин не могла бы оставаться</strong> — семья успешно обжаловала это решение, и перевод был заблокирован'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Переведены в Новое Учреждение</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Решение о Переводе Успешно Обжаловано</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">После эфира 60 Minutes Катрин была отстранена от нового учреждения, куда перевели детей</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">После эфира 60 Minutes суд постановил перевести детей, запретив Катрин оставаться — семья обжаловала решение и заблокировала перевод</p>'
        ),
    ],
    'pl': [
        (
            'teraz zostały przeniesione do nowej placówki, gdzie <strong style="color: #fef08a;">Catherine nie może przebywać</strong>',
            'sąd nakazał przeniesienie do nowej placówki, gdzie <strong style="color: #fef08a;">Catherine nie mogłaby przebywać</strong> — rodzina skutecznie odwołała się od tego nakazu i przeniesienie zostało zablokowane'
        ),
        (
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Przeniesione do Nowej Placówki</p>',
            '<p style="color: #fef08a; font-weight: 600; margin-bottom: 0.25rem;">Nakaz Przeniesienia Skutecznie Zaskarżony</p>'
        ),
        (
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Po emisji 60 Minutes Catherine została wykluczona z nowej placówki, do której przeniesiono dzieci</p>',
            '<p style="color: rgba(255,255,255,0.85); font-size: 0.95rem; margin: 0;">Po emisji 60 Minutes sąd nakazał przeniesienie dzieci wykluczając Catherine — rodzina odwołała się i zablokowała przeniesienie</p>'
        ),
    ],
}

for lang, patches in lang_fixes.items():
    fix(f'{lang}/index.md', patches)

print('\nDone. Checking for any remaining "moved to a new facility" as completed fact...')
import re
files_to_check = [
    'index.md', 'pages/updates.md',
    '_posts/2026-03-08-children-moved-new-facility-catherine-banned.md',
    '_posts/2026-03-14-la-stampa-social-workers-statement.md',
    '_posts/2026-03-15-football-fan-stadium-support.md',
    '_posts/2026-03-26-senate-visit-catherine-addresses-public.md',
] + [f'{l}/index.md' for l in lang_fixes]

for f in files_to_check:
    with open(f, encoding='utf-8') as fh:
        t = fh.read()
    # look for "moved to a new facility" as completed action (not in quotes/headings about old titles)
    hits = re.findall(r'(?i)(?:moved|transferred|trasferiti|verlegt|transférés|trasladados|transferidas|перевели|przeniesione).*(?:new facility|nuova struttura|neue Einrichtung|nouvel établissement|nueva instalación|nova instalação|новое учреждение|nowej placówki)', t)
    for h in hits:
        if 'appeal' not in h.lower() and 'ordine' not in h.lower() and 'ordnete' not in h.lower() and 'ordonn' not in h.lower() and 'orden' not in h.lower() and 'ordered' not in h.lower() and 'nakaz' not in h.lower() and 'постановил' not in h.lower() and 'odwołała' not in h.lower() and 'ricorso' not in h.lower():
            print(f'  POSSIBLE REMAINING: {f}: {repr(h[:120])}')
