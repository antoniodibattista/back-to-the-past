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
- [ ] Tema EmulationStation "Back To The Past" (`theme/`)
- [ ] File di config con tuning per Atom (`config/batocera.conf`, `es_settings.cfg`)
- [ ] Mappe controller riproducibili (`config/controllers/`)
- [ ] Script `deploy.sh` (push del repo su `/userdata` via SSH/rsync)
- [ ] Selezione/struttura giochi + giochi liberi inclusi (`games/`)

## Fase 4 — Kiosk & finalizzazione
- [ ] Modalità Kiosk + sequenza di sblocco manutenzione
- [ ] Attract mode / screensaver
- [ ] Splash di boot brandizzato
- [ ] Tuning prestazioni per sistema (shader off, rewind off, core leggeri)

## Fase 5 — Clonazione su Asem #2
- [ ] Ripetere installazione + deploy
- [ ] Verifica parità tra i due cabinati

## Idee future (nice-to-have)
- [ ] Un gioco originale "fatto in casa" per il cabinato (sotto-progetto a sé, ≠ emulatore)
- [ ] Pulsante fisico/illuminazione (se si aggiungono controlli arcade reali via encoder USB)
- [ ] Backup automatico di `userdata`
- [ ] Immagine "golden" pronta da riscrivere su un nuovo disco
