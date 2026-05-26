# ROADMAP — Back To The Past

Stato a oggi: **Asem #1: Batocera V5.25 installata e funzionante su SSD interna. Prossimo: livello "kiosk" (tema, config, giochi).**

## Fase 0 — Progettazione ✅
- [x] Definire obiettivi e vincoli (Atom 64-bit, 2 GB RAM, touch + joypad)
- [x] Scegliere il sistema: **Batocera.linux x86_64**
- [x] Decidere di **non** scrivere un emulatore proprio (usiamo RetroArch)
- [x] Definire l'architettura a livelli e il livello "kiosk" come nostro deliverable
- [x] Documentazione di base + struttura repo

## Fase 1 — Ricognizione hardware ✅
- [x] Identificato modello CPU/GPU Asem #1: **Atom D525 (Pineview) + GMA 3150**, 64-bit
- [x] Decisa build OS: **Batocera "Intel Atom / old low-powered (V5.25)"** (la GMA 3150 esclude le build moderne)
- [x] Boot live di Batocera (V5.25) su Asem #1 — ES gira fluida, NES testato OK (8+ min, GMA 3150 regge il 2D)
- [x] Hardware confermato: disco unico = **SSD SanDisk U100 32 GB**, rete **eth0** (DHCP, WiFi off)

## Fase 2 — Installazione base ✅ (Asem #1)
- [x] Batocera V5.25 installata sul disco interno (metodo `dd`, vedi [03 — Fase 4](03-installazione.md)); area dati auto-espansa a ~26 GB
- [x] Rete OK (eth0 DHCP)
- [ ] Lingua/tastiera da rifinire
- [ ] Prima configurazione joypad (quando arrivano)

## Fase 3 — Livello "Back To The Past" (sviluppo nel repo)
- [x] Tema EmulationStation "Back To The Past" v1 (`theme/`) — synthwave/arcade; tenuto come alternativa. Attivo: **es-theme-carbon** (ha le grafiche dei sistemi) + locandine via scraper
- [x] File di config con tuning per Atom (`config/batocera.conf`, `config/es_settings.cfg` con ThemeSet=carbon + Kiosk)
- [x] Selezione/struttura giochi + giochi liberi (`games/` + ScummVM)
- [x] **Locandine/box art** scaricate con lo scraper (tutti i giochi) — vedi [games/README](../games/README.md)
- [ ] Mappe controller riproducibili (`config/controllers/`) — quando arrivano i joypad
- [ ] Script `deploy.sh` (push del repo su `/userdata` via SSH/rsync)

## Fase 4 — Kiosk & finalizzazione (Asem #1)
- [x] Modalità **Kiosk** attiva + sblocco manutenzione via SSH (vedi [05](05-kiosk-e-controlli.md))
- [x] Screensaver (dim a 5 min, protegge il pannello)
- [x] Tuning prestazioni GMA 3150 (shader/bezel off, rewind/smooth off) — in `config/batocera.conf`
- [ ] Splash di boot brandizzato "Back To The Past"
- [ ] Attract mode con video/immagini (richiede scraping dei giochi)

## Fase 5 — Clonazione su Asem #2
- [ ] Ripetere installazione + deploy
- [ ] Verifica parità tra i due cabinati

## Idee future (nice-to-have)
- [ ] Un gioco originale "fatto in casa" per il cabinato (sotto-progetto a sé, ≠ emulatore)
- [ ] Pulsante fisico/illuminazione (se si aggiungono controlli arcade reali via encoder USB)
- [ ] Backup automatico di `userdata`
- [ ] Immagine "golden" pronta da riscrivere su un nuovo disco
