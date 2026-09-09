# 1+1=3 — Gazeta Satirike (Website-Struktur & Workflow-Doku)

Albanische Satirezeitung über Kosovo & Albanien. Statische Website, gehostet auf **Cloudflare Pages** (kostenlos), täglich befüllt durch einen **Genspark Workflow**.

## Dateistruktur (auf GitHub hochladen in Repo-Root)

```
/                (Repo-Root)
├── index.html           → Startseite (Aufmacher + Rubrik-Sektionen)
├── politike.html        → Rubrik Politik
├── ekonomia.html        → Rubrik Wirtschaft
├── edukimi.html         → Rubrik Bildung/PISA
├── turizmi.html         → Rubrik Tourismus
├── showbiz.html         → Rubrik Showbiz
├── sporti.html          → Rubrik Sport
├── rreth-nesh.html      → Über uns
├── kontakti.html        → Kontakt
├── privat.html          → Datenschutz (GDPR)
├── kushtet.html         → Impressum/Nutzungsbedingungen  ← PLATZHALTER AUSFÜLLEN
├── assets/
│   └── stili.css        → Design-System (alle Seiten nutzen diese Datei)
└── artikuj/             → Artikel (ein HTML pro Artikel)
    ├── imazhe/          → Artikelbilder (PNG/WebP)
    ├── 2026-09-09-qeveria-pa-buxhet.html   (Beispiel)
    ├── 2026-09-09-inflacioni-32.html       (Beispiel)
    └── 2026-09-09-pisa-rekord.html         (Beispiel)
```

## WICHTIGE REGELN FÜR DEN WORKFLOW (neue Artikel)

1. **Dateiname:** `artikuj/YYYY-MM-DD-kurz-slug.html` (nur ASCII, keine Umlaute/ë!)
2. **Bild:** vorher generieren (16:9), speichern nach `artikuj/imazhe/<slug>.png`, im Artikel einbinden als `<img src="imazhe/<slug>.jpg">`
3. **Vorlage:** Beispiel-Artikel `artikuj/2026-09-09-qeveria-pa-buxhet.html` exakt kopieren; das Design hängt an `../assets/stili.css` — nie ändern, nur Inhalt ersetzen
4. **Pfade im Artikel:** CSS = `../assets/stili.css`, Navigation = `../index.html` etc., Bilder = `imazhe/...`
5. **Nach dem neuen Artikel:** Startseite `index.html` + zugehörige Rubrik-Seite (z.B. `politike.html`) updaten — neuen Artikel als Karte/Zeile mit Link einfügen (Kartenlayout aus bestehenden Karten kopieren)
6. **Sprache:** immer Albanisch (Kosovo-Dialekt), Satire-Stil, Disclaimer im Footer bleibt
7. **Nie tote Links:** Jede Karte/Zeile, die einen Artikel verlinkt, muss auf eine wirklich existierende Datei zeigen

## Platzhalter, die der Betreiber ausfüllen muss

- `kushtet.html` → Name, Adresse, Email des Betreibers (Impressum — gesetzlich nötig!)
- `kontakti.html` + `privat.html` → Email-Adresse
- In allen Artikel-Seiten: die Share-URLs enthalten `https://1plus1eq3.com/...` → nach Domain-Kauf durch die echte Domain ersetzen (Workflow kann das beim Generieren machen)

## Genspark-Workflow (Tagesablauf — Beschreibung für den Builder)

> Täglich um 08:00 (Europe/Zurich):
> 1. Web-Suche nach aktuellen Nachrichten aus Kosovo und Albanien (Politik, Wirtschaft, Sport, Showbiz, Tourismus)
> 2. Wähle 1–2 Themen, schreibe je einen satirischen Artikel auf Albanisch (Stil: absurde Rechnungen, erfundene Zitate, Running Gag "1+1=3")
> 3. Generiere zu jedem Artikel ein satirisches Bild (16:9, ohne Text)
> 4. Erstelle die Artikeldatei nach dem Schema oben (Vorlage 2026-09-09-qeveria-pa-buxhet.html kopieren, Inhalt ersetzen)
> 5. Aktualisiere index.html und die passende Rubrik-Seite (neue Artikelkarte einfügen, älteste entfernen wenn nötig)
> 6. Committe alle Änderungen an GitHub → Cloudflare Pages deployed automatisch
> Danach optional: Artikel auf Facebook/WhatsApp teilen (Link kopieren).
