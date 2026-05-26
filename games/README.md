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

## Aggiungere giochi
- **Liberi (homebrew/PD/shareware):** ok inserirli, ma **annota la licenza** in un `README` o `LICENSE.txt` nella relativa cartella.
- **Propri (dump di cartucce che possiedi):** copiali direttamente su `/userdata/roms/<sistema>/` dell'Asem — **non** nel repo.

## BIOS
Alcuni sistemi richiedono BIOS (es. Neo Geo, PS1, alcuni Amiga) in `/userdata/bios/`. I BIOS proprietari NON sono inclusi: procurarli dal proprio hardware.
