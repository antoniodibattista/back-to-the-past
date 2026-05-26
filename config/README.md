# config/

File di configurazione versionati, da deployare su `/userdata` dell'Asem. Servono a rendere i due cabinati **identici e riproducibili**.

## Contenuto previsto

| File / cartella | Destinazione su Asem | Scopo |
|---|---|---|
| `batocera.conf` | `/userdata/system/batocera.conf` | Opzioni globali e per-sistema: core scelti, **shader off**, **rewind off**, frameskip, ecc. (tuning Atom — vedi [docs/04](../docs/04-giochi-consigliati.md)) |
| `es_settings.cfg` | `/userdata/system/configs/emulationstation/es_settings.cfg` | UI Mode = **Kiosk**, screensaver/attract, tema attivo |
| `controllers/` | mappe joypad | Mapping joypad USB salvato, per riapplicarlo identico sul 2° PC |

## Come si generano

1. Si configura tutto **a mano** una volta su Asem #1 (joypad, opzioni, tuning).
2. Si copiano i file risultanti da `/userdata` **dentro questo repo** (`config/`).
3. Si versiona e si **deploya** sul 2° Asem → setup identico.

## Stato

- ✅ **`batocera.conf`** — file reale catturato dall'Asem #1 (deploy diretto in `/userdata/system/`). Impostazioni chiave attive:
  - `system.language=it_IT`, `system.kblayout=it`, `system.timezone=Europe/Rome`
  - `updates.enabled=0` → **niente aggiornamenti automatici** (la V5.25 NON va aggiornata: romperebbe la GMA 3150)
  - Tuning GMA 3150: `global.shaderset=none`, `global.bezel=none`, `global.rewind=0`, `global.smooth=0`, `global.integerscale=0`, `global.ratio=auto`
- ✅ **`es_settings.cfg`** — `UIMode=Kiosk` (lockdown). **Screensaver DISABILITATO** (`ScreenSaverTime=0`): il "dim" a 5 min causava **blocco al risveglio** sulla GMA 3150 (audio che continua, schermo scuro che non si riattiva). Deploy in `/userdata/system/configs/emulationstation/`. ⚠️ ES riscrive il file in chiusura: per editarlo via SSH, **fermare ES → editare → riavviare ES** (vedi [docs/05](../docs/05-kiosk-e-controlli.md))
- ⏳ `controllers/` — da fare quando arrivano i joypad

> Per l'Asem #2: copiare `batocera.conf` in `/userdata/system/` e riavviare.

## Patch di sistema — `patches/`

- **`patches/viceControllers.py`** — corregge un bug di Batocera V5.25: i giochi **C64 (vice) crashano all'avvio se non c'è un joypad** collegato (`listVice` usato prima di essere inizializzato). Deploy: copiare in `/usr/lib/python2.7/site-packages/configgen/generators/vice/viceControllers.py`, rimuovere il `.pyc` accanto, poi **`batocera-save-overlay`** per renderla permanente.
  > ⚠️ Le modifiche al sistema `/` stanno in RAM e si perdono al riavvio: serve `batocera-save-overlay`. `/userdata` (config, rom, temi) è invece persistente.
