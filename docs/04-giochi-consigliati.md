# 04 — Giochi consigliati & tuning per Atom + 2 GB

La regola d'oro (Atom D525 / GMA 3150): **arcade 2D anni 80/90 e console fino alla 4ª generazione**. Niente 3D — la GPU non lo accelera.

## ✅ Sistemi che girano bene

| Sistema | Core libretro consigliato (leggero) | Note |
|---|---|---|
| **Arcade (MAME)** | `mame2003_plus` o `fbneo` | I classici 80s (Pac-Man, Galaga, Donkey Kong, Bubble Bobble…) sono leggerissimi. FBNeo è molto efficiente. |
| **Arcade CPS1/CPS2** | `fbneo` | Street Fighter II, Final Fight, ecc. |
| **Neo Geo** | `fbneo` | Richiede BIOS `neogeo.zip`. Metal Slug, KOF… girano. |
| **NES / Famicom** | `fceumm` o `nestopia` | Perfetto. |
| **SNES / Super Famicom** | `snes9x2005` / `snes9x2002` | Usa le versioni "200x" (leggere), NON `snes9x` pieno. Evita giochi con chip SuperFX (Star Fox). |
| **Mega Drive / Genesis** | `genesis_plus_gx` o `picodrive` | Ottimo. |
| **Master System / Game Gear** | `genesis_plus_gx` / `smsplus` | Leggeri. |
| **Game Boy / GBC** | `gambatte` | Leggerissimo. |
| **Game Boy Advance** | `gpsp` (leggero) o `mgba` | `gpsp` è più veloce su Atom; `mgba` più preciso ma più pesante. |
| **PC Engine / TurboGrafx-16** | `mednafen_pce_fast` | Bene. |
| **Atari 2600 / 7800** | `stella` / `prosystem` | Banali da far girare. |
| **Commodore 64** | `vice_x64` | Bene. |
| **Amiga** | `puae` | OK per titoli classici; alcuni richiedono kickstart BIOS. |
| **MS-DOS** | `dosbox_pure` | Ottimo per i classici DOS (Prince of Persia, Doom shareware, Commander Keen…). |

## ❌ Fuori portata su Atom D525 + GMA 3150 + 2 GB

- **PlayStation 1** — escluso: senza accelerazione 3D (GMA 3150) `pcsx_rearmed` non regge. *(Era "al limite" finché non sapevamo la GPU.)*
- N64, PSP, Dreamcast, Sega Saturn, PS2, GameCube/Wii, Naomi, e qualsiasi sistema 3D. **Non installarli**: frustrazione garantita.

> La GMA 3150 fa il rendering 2D in modo dignitoso ma il 3D è praticamente assente: la regola è **2D sì, 3D no**.

---

## 🔧 Tuning prestazioni (impostazioni Batocera/RetroArch)

Da applicare globalmente e/o per sistema. Le mettiamo nei nostri file in [`config/`](../config/).

- **Shader: OFF** (gli shader CRT pesano molto sull'Atom). Eventualmente solo `scanlines` leggero.
- **Rewind: OFF** (mangia RAM e CPU). Su 2 GB è la prima cosa da disattivare.
- **Run-ahead: OFF.**
- **Integer scale / smooth: OFF** se causa cali; preferire scaling semplice.
- **VSync: ON** per evitare tearing (ma se cala, valutare OFF + frameskip).
- **Frameskip auto**: utile su arcade pesanti.
- **Audio**: latency standard, evitare resampler costosi.
- **Threaded video: ON** dove disponibile.
- **Scraper immagini**: scaricare poche immagini/box art per non riempire la RAM con anteprime; niente video snap nelle gamelist.

> Obiettivo: **60 fps stabili** sui sistemi della tabella "verde". Se un gioco non ci sta, è il gioco/sistema sbagliato per questo hardware, non un problema da forzare.

---

## 🎮 Selezione "cabinato" suggerita

Per un cabinato anni 80/90 punterei su una **collezione curata** (non 10.000 ROM a caso): più "magia arcade", meno paralisi da scelta.

- **Arcade hall of fame:** Pac-Man, Ms. Pac-Man, Galaga, Donkey Kong, Frogger, Dig Dug, Bubble Bobble, Bombjack, 1942/1943, Street Fighter II, Metal Slug, Bomberman.
- **Console icone:** Super Mario Bros, Sonic, Tetris, Mega Man, Castlevania, Contra, Zelda, Street of Rage.
- **DOS:** Prince of Persia, Doom (shareware), Commander Keen, Lemmings.

I giochi **non li distribuiamo** noi (vedi [06 — Legale](06-legale.md)); in [`games/`](../games/) prepariamo la struttura e includiamo solo titoli liberi/homebrew.
