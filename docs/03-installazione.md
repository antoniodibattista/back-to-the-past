# 03 — Installazione

Flusso completo: dal portatile di sviluppo ai due cabinati Asem.

```
[ Portatile Windows ]                 [ Asem #1 e #2 ]
  - questo repo            ── deploy ──▶  - Batocera installato su disco
  - scrive img su USB                     - /userdata popolato col nostro contenuto
```

---

## Fase 1 — Procurarsi Batocera (sul portatile)

1. Scarica l'immagine **x86_64** da https://batocera.org/download (file `.img.gz`).
2. Scarica uno scrittore di immagini:
   - **balenaEtcher** (consigliato, semplice) — oppure **Rufus**.
3. Inserisci una chiavetta USB (≥ 8 GB; verrà **cancellata**).

## Fase 2 — Creare la chiavetta avviabile

Con balenaEtcher:
1. *Flash from file* → seleziona `batocera-x86_64-*.img.gz` (non serve scompattarlo).
2. *Select target* → la chiavetta USB.
3. *Flash!* e attendi.

## Fase 3 — Primo avvio LIVE sull'Asem (senza installare)

1. Inserisci la chiavetta nell'Asem, accendi ed entra nel **boot menu** (di solito `F12`/`F11`/`ESC` — varia per BIOS).
2. Avvia da USB. Batocera parte in modalità live.
3. **Verifica l'hardware reale** con [`scripts/check-hardware.sh`](../scripts/check-hardware.sh) (vedi [01 — Hardware](01-hardware.md)). Annota CPU, RAM, dischi, touch, USB.
4. Verifica che **touchscreen** e **joypad USB** vengano riconosciuti.

> Se i 2 GB rendessero EmulationStation troppo pesante, qui valutiamo il piano B (Lakka). Vedi [02](02-sistema-operativo.md).

## Fase 4 — Installazione su disco interno

Avendo 128 GB+, installiamo Batocera sul disco interno per prestazioni e comodità.

1. Dal menu EmulationStation: **MENU → SYSTEM SETTINGS → INSTALL ON A NEW DISK** (oppure terminale: `batocera-install`).
2. Seleziona il disco interno dell'Asem come destinazione (**attenzione: cancella il disco**).
3. Conferma, attendi, rimuovi la chiavetta e riavvia.

Al riavvio Batocera parte dal disco. Lo storage è diviso in:
- **sistema** (read-only, aggiornabile)
- **`userdata`** ← qui vivono ROM, configurazioni, salvataggi, temi → **è ciò che deployamo noi**.

## Fase 5 — Deploy del nostro livello "Back To The Past"

Il contenuto di questo repo va in `/userdata` dell'Asem. Mappatura cartelle:

| Repo | Destinazione su Asem |
|---|---|
| `theme/back-to-the-past/` | `/userdata/themes/back-to-the-past/` |
| `config/batocera.conf` (chiavi) | `/userdata/system/batocera.conf` |
| `config/es_settings.cfg` | `/userdata/system/configs/emulationstation/es_settings.cfg` |
| `config/controllers/` | mappe joypad (in `batocera.conf` / ES) |
| `games/<sistema>/` | `/userdata/roms/<sistema>/` |

Metodi di deploy (uno qualsiasi):

- **Rete (consigliato):** Batocera espone una share di rete (SMB) `\\BATOCERA\share` e il **SSH** (utente `root`, password default `linux`). Dal portatile si copia con `scp`/`rsync` o trascinando nella share.
- **Chiavetta USB:** copia le cartelle e poi sposta in `/userdata`.

> Gli script in [`scripts/`](../scripts/) automatizzeranno questo deploy (es. `deploy.sh` via SSH/rsync). Vedi [ROADMAP](ROADMAP.md).

## Fase 6 — Kiosk & finalizzazione

1. Imposta la modalità **Kiosk** in EmulationStation (lockdown).
2. Abilita l'**avvio diretto** sul menu (già default) ed eventuale **attract mode**.
3. Configura touch (navigazione) + joypad (gioco).
4. Vedi [05 — Kiosk e controlli](05-kiosk-e-controlli.md).

## Fase 7 — Ripeti sul secondo Asem

Stessa procedura. Il bello del repo è che il deploy è **identico e riproducibile** sui due PC.

---

## Checklist rapida

- [ ] Immagine Batocera x86_64 scaricata
- [ ] Chiavetta USB creata (Etcher/Rufus)
- [ ] Boot live su Asem #1 OK
- [ ] `check-hardware.sh` eseguito e specifiche annotate
- [ ] Touch + joypad riconosciuti
- [ ] Installazione su disco interno
- [ ] Deploy tema/config/giochi
- [ ] Kiosk + controlli configurati
- [ ] Ripetuto su Asem #2
