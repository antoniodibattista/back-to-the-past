# 02 — Sistema operativo & motore di emulazione

## TL;DR

- **Sistema scelto:** [**Batocera.linux**](https://batocera.org) — edizione **x86_64**, installata sul disco interno dell'Asem.
- **Frontend:** EmulationStation (incluso) — lo personalizziamo col nostro tema.
- **Emulazione:** RetroArch + core libretro (inclusi).
- **NON** scriviamo un emulatore da zero. Vedi sotto il perché.

---

## Perché NON scrivere un emulatore tipo MAME

Era una delle opzioni sul tavolo. La scartiamo per motivi concreti:

1. **Effort enorme.** Un emulatore accurato è un progetto da anni-uomo: bisogna replicare CPU, chip video/audio, timing, quirk hardware. MAME ha ~30 anni di sviluppo e centinaia di contributori.
2. **Prestazioni.** Gli emulatori esistenti sono scritti in C/C++ con ottimizzazioni spinte (a volte assembly). Una nostra versione in linguaggio "comodo" sarebbe **più lenta** — proprio ciò che non possiamo permetterci su un **Atom**.
3. **Compatibilità.** Far girare un gioco è un conto; far girare *migliaia* di giochi con tutti i loro casi limite è un altro. È esattamente il valore che MAME/RetroArch già offrono gratis.
4. **Manutenzione.** Sarebbe codice nostro da mantenere per sempre, invece di sfruttare progetti vivi e collaudati.

> **Dove mettiamo il nostro lavoro di sviluppo:** nel **livello kiosk** — tema "cabinato", lockdown, autostart, script di setup riproducibili, selezione e organizzazione dei giochi. Lì creiamo valore reale e l'effort è proporzionato all'hardware. (Se in futuro volessimo programmare *un* gioco originale per il cabinato, quello sì sarebbe un bel sotto-progetto — ma è diverso dallo scrivere un emulatore.)

---

## Distro retro valutate

| Distro | Frontend | RAM minima | Pro | Contro per noi |
|---|---|---|---|---|
| **Batocera.linux** ✅ | EmulationStation | ~2 GB | Tema-abile, kiosk integrato, joypad auto, x86_64, sistema read-only + dati separati, enorme community | 2 GB è il minimo: serve scegliere bene i core |
| Recalbox | EmulationStation | ~2 GB | Molto simile a Batocera, semplice | Community/personalizzazione leggermente minori |
| Lakka | RetroArch (XMB) | ~1 GB | Leggerissima, ottima per HW debole | Niente EmulationStation: estetica meno "cabinato", meno tema-abile |
| ChimeraOS / Bazzite | Steam Big Picture | 8 GB+ | Moderne | **Fuori portata** su Atom 2 GB |

### Perché Batocera (e non Lakka)

Lakka è più leggera, ed è il **piano B** se i 2 GB si rivelassero troppo stretti. Ma Batocera vince perché:

- **EmulationStation è temabile**: è lì che costruiamo l'identità "Back To The Past" (il nostro valore aggiunto).
- Ha **modalità Kiosk/Kid** integrate per il lockdown.
- Sistema **read-only** + partizione `userdata` separata → difficile da rompere, facile da ripristinare.
- Auto-riconoscimento **joypad** e gestione **touch**.
- Si installa sul disco interno (abbiamo 128 GB+).

> Su 2 GB di RAM useremo **core leggeri** (es. `snes9x2005` invece di `snes9x`, `fbneo` per l'arcade) e disattiveremo shader/rewind. Tutto il tuning è in [04 — Giochi consigliati](04-giochi-consigliati.md).

---

## Architettura a livelli

```
┌─────────────────────────────────────────────┐
│  TEMA "Back To The Past" + LOCKDOWN + SETUP   │ ← questo repo (NOI)
├─────────────────────────────────────────────┤
│  EmulationStation (frontend / menu giochi)    │ ← Batocera
├─────────────────────────────────────────────┤
│  RetroArch + core libretro (emulatori)        │ ← Batocera
├─────────────────────────────────────────────┤
│  Batocera.linux (kernel, driver, audio/video) │ ← Batocera
├─────────────────────────────────────────────┤
│  Asem Panel PC — Atom 64-bit, 2 GB RAM        │ ← hardware
└─────────────────────────────────────────────┘
```

## Riferimenti

- Batocera: https://batocera.org
- Wiki Batocera (x86): https://wiki.batocera.org
- RetroArch / libretro: https://www.libretro.com
- Lakka (piano B): https://www.lakka.tv
