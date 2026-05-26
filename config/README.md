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

> ⚠️ Questi file sono specifici di Batocera: vanno popolati **dopo** la prima installazione (Fase 2-3 della [ROADMAP](../docs/ROADMAP.md)). Per ora la cartella è un segnaposto.
