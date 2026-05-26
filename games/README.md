# games/

Struttura delle collezioni di giochi e (solo) i titoli **legalmente ridistribuibili**.

> ⚠️ **Leggi [docs/06 — Legale](../docs/06-legale.md).** Qui NON vanno ROM/BIOS commerciali. Il [`.gitignore`](../.gitignore) blocca le estensioni ROM per sicurezza. Si versiona la **struttura** e, al massimo, homebrew/PD/shareware con licenza verificata.

## Mappatura su Asem
Ogni sottocartella corrisponde a un sistema di Batocera e va in `/userdata/roms/<sistema>/`.

| Cartella | Sistema | Estensioni tipiche |
|---|---|---|
| `mame/` | Arcade (MAME) | `.zip` |
| `fbneo/` | Arcade (FinalBurn Neo) | `.zip` |
| `nes/` | Nintendo NES | `.nes` |
| `snes/` | Super Nintendo | `.sfc` `.smc` |
| `megadrive/` | Sega Mega Drive | `.md` `.bin` `.gen` |
| `gb/` `gbc/` | Game Boy / Color | `.gb` `.gbc` |
| `gba/` | Game Boy Advance | `.gba` |
| `dos/` | MS-DOS | cartelle/`.zip` |

(Nomi cartella esatti = quelli attesi da Batocera; vedi wiki.)

## Giochi attualmente installati su Asem #1 (tutti legali)

**Inclusi di serie in Batocera V5.25** (homebrew/freeware):

| Sistema | Gioco |
|---|---|
| Mega Drive | Old-Towers |
| NES | 2048 |
| SNES | Donkey Kong Classic (Shiru) |
| PC Engine | Reflectron, Santatlantean (aetherbyte) |
| GBA | SpaceTwins |
| C64 | The Great Giana Sisters, Super Mario Bros 64 |
| Doom (prboom) | Doom (shareware) |

**Aggiunti da noi — ScummVM (avventure freeware ufficiali, giocabili col touch/mouse):**

| Gioco | gameid | Fonte | Setup |
|---|---|---|---|
| Beneath a Steel Sky | `sky` | scummvm.org (BASS-Floppy-1.3.zip) | `roms/scummvm/BeneathASteelSky/` + `sky.scummvm` |
| Flight of the Amazon Queen | `queen` | scummvm.org (FOTAQ_Talkie-1.1.zip) | `roms/scummvm/AmazonQueen/` + `queen.scummvm` |

Formato ScummVM su Batocera: una **cartella per gioco** coi file dati, più un file vuoto **`<gameid>.scummvm`** (ES lancia `scummvm -p <cartella> <gameid>`). Nomi visualizzati definiti in [`config/scummvm-gamelist.xml`](../config/scummvm-gamelist.xml) → deploy in `/userdata/roms/scummvm/gamelist.xml`.

> I dati dei giochi ScummVM (`sky.dsk`, `queen.1c`, …) NON sono nel repo (troppo grandi e meglio scaricarli dalla fonte ufficiale). Per l'Asem #2: riscaricali da scummvm.org con gli stessi URL.

## Doom completo: Freedoom (open source)

Installato **Freedoom** v0.13.0 in `/userdata/roms/prboom/`: `freedoom1.wad` (Fase 1, stile Doom 1) e `freedoom2.wad` (Fase 2, stile Doom 2) — FPS **completo e gratuito** (licenza BSD) sul motore Doom. Non è il Doom *originale* (commerciale): chi possiede `DOOM.WAD`/`DOOM2.WAD` (~12-14 MB) può aggiungerli da sé.

Download ufficiale: https://github.com/freedoom/freedoom/releases → estrai i due `.wad` in `roms/prboom/`. (Stessa cosa per Asem #2; i WAD non sono nel repo perché rigenerabili.)

## Locandine / box art (scraping)

Su Asem #1 le immagini (copertina, miniatura, marquee) sono state scaricate con lo **scraper integrato** di Batocera (ScreenScraper): **tutti** i giochi hanno la grafica. Stanno in `/userdata/roms/<sistema>/images/`, collegate nelle `gamelist.xml` (ES le scrive alla chiusura). NON versionate nel repo (rigenerabili).

**Per l'Asem #2** (dopo aver caricato i giochi): `MENU → SCRAPER → ScreenScraper → All Games → Scrape Now`. Serve UI Mode = **Full** (lo scraper è nascosto in Kiosk → vedi sblocco in [docs/05](../docs/05-kiosk-e-controlli.md)); poi si rimette Kiosk.

## Aggiungere giochi
- **Liberi (homebrew/PD/shareware):** ok inserirli, ma **annota la licenza** in un `README` o `LICENSE.txt` nella relativa cartella.
- **Propri (dump di cartucce che possiedi):** copiali direttamente su `/userdata/roms/<sistema>/` dell'Asem — **non** nel repo.

## BIOS
Alcuni sistemi richiedono BIOS (es. Neo Geo, PS1, alcuni Amiga) in `/userdata/bios/`. I BIOS proprietari NON sono inclusi: procurarli dal proprio hardware.
