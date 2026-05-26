# 06 — Note legali: ROM, BIOS e copyright

> Disclaimer: questo documento è una guida pratica, **non** consulenza legale.

## Il principio

Gli **emulatori sono legali**. Le **ROM e i BIOS** dei giochi commerciali sono **opere protette da copyright**: scaricarli/distribuirli senza diritti è una violazione, anche per giochi vecchi e "fuori commercio" (l'abandonware **non** è una categoria legale riconosciuta).

## Cosa fa questo progetto

- ✅ **Non distribuiamo** ROM o BIOS commerciali. Non finiscono nel repo (vedi [`.gitignore`](../.gitignore), che blocca le estensioni ROM e i BIOS).
- ✅ Versioniamo solo la **struttura delle cartelle** in [`games/`](../games/) e, al massimo, giochi **esplicitamente liberi** (homebrew, freeware, public domain, demo/shareware ridistribuibili).
- ✅ L'utente aggiunge **le proprie** ROM dei giochi che **possiede legalmente** (es. dump delle proprie cartucce), sotto la propria responsabilità.

## Fonti di giochi legali (da poter includere/usare)

- **Homebrew moderni**: scene NES/SNES/Mega Drive/GB attive (spesso su itch.io o siti degli autori) con licenze che ne permettono la ridistribuzione — **verificare sempre la licenza del singolo titolo**.
- **Public domain / freeware ROM**: raccolte storiche di homebrew e demo.
- **Shareware DOS** classico (es. la versione shareware di Doom, Commander Keen, Wolfenstein 3D) — redistribuibile secondo le rispettive licenze shareware.
- **BIOS liberi**: alcuni sistemi hanno BIOS open (es. per Amiga esiste l'AROS; per altri no). I BIOS proprietari (PS1, Neo Geo…) vanno procurati da hardware proprio.

> Prima di includere **qualsiasi** gioco in `games/`, controlla e annota la sua licenza nel README della relativa cartella.

## Uso previsto

Progetto **personale**, due cabinati domestici, uso privato. Niente noleggio, vendita o esposizione commerciale dei cabinati con giochi protetti.

## In sintesi

| | |
|---|---|
| Emulatori (Batocera/RetroArch) | ✅ Liberi/open |
| Nostri tema/script/config | ✅ MIT (questo repo) |
| Homebrew/PD/shareware ridistribuibili | ✅ con verifica licenza |
| ROM/BIOS commerciali | ❌ non nel repo; l'utente usa i propri |
