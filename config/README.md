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
- ⏳ `es_settings.cfg` (UI Kiosk, screensaver) — da fare in fase kiosk
- ⏳ `controllers/` — da fare quando arrivano i joypad

> Per l'Asem #2: copiare `batocera.conf` in `/userdata/system/` e riavviare.
