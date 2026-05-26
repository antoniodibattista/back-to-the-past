# ROADMAP — Back To The Past

Stato a oggi: **progettazione completata, inizio setup.**

## Fase 0 — Progettazione ✅
- [x] Definire obiettivi e vincoli (Atom 64-bit, 2 GB RAM, touch + joypad)
- [x] Scegliere il sistema: **Batocera.linux x86_64**
- [x] Decidere di **non** scrivere un emulatore proprio (usiamo RetroArch)
- [x] Definire l'architettura a livelli e il livello "kiosk" come nostro deliverable
- [x] Documentazione di base + struttura repo

## Fase 1 — Ricognizione hardware
- [ ] Boot live di Batocera su Asem #1
- [ ] Eseguire `scripts/check-hardware.sh` e annotare specifiche reali (modello Atom, RAM, dischi, GPU, touch, USB)
- [ ] Verificare riconoscimento touchscreen + joypad USB
- [ ] Confermare che 2 GB reggano EmulationStation (altrimenti piano B: Lakka)

## Fase 2 — Installazione base
- [ ] Installare Batocera sul disco interno dell'Asem #1
- [ ] Configurare lingua/tastiera/rete
- [ ] Prima configurazione joypad

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
