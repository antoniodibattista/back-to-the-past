# 🕹️ Back To The Past

> Far rivivere due PC Touch industriali **Asem** trasformandoli in **cabinati arcade** con giochi anni 80/90.

Progetto personale di retro-gaming: due panel PC industriali Asem (CPU Intel **Atom 64-bit**, **2 GB di RAM**, storage 128 GB+, schermo touch) vengono convertiti in postazioni "cabinato" che si avviano direttamente su un menu giochi, in modalità **kiosk** (niente desktop, niente distrazioni), con controllo via **touch** (navigazione) e **joypad USB** (gioco).

## 🎯 Obiettivi

- ✅ Avvio diretto sul menu giochi (nessun desktop visibile, "accendi e gioca")
- ✅ Esperienza da cabinato: tema dedicato, grafica arcade, attract mode
- ✅ Giochi anni 80/90 che girano **fluidi su Atom + 2 GB** (arcade + console fino alla 4ª/5ª gen)
- ✅ Modalità kiosk/lockdown: l'utente non può rompere il sistema
- ✅ Touch per i menu + joypad USB per giocare
- ✅ Setup ripetibile e documentato per entrambi i PC

## 🧠 Decisione architetturale chiave

**Non scriviamo un emulatore da zero (tipo MAME).** Sarebbe un lavoro enorme (anni-uomo) e su un Atom sarebbe comunque più lento degli emulatori esistenti, già ottimizzati in C/assembly. Vedi [docs/02 — Sistema operativo](docs/02-sistema-operativo.md) per il ragionamento completo.

La strategia è: **base collaudata + nostro livello "kiosk" su misura**.

| Livello | Cosa usiamo | Chi lo fa |
|---|---|---|
| Sistema operativo + emulatori | **Batocera.linux (x86_64)** | Pronto, open source |
| Frontend / menu giochi | EmulationStation (incluso in Batocera) | Pronto, lo personalizziamo |
| Motore emulazione | RetroArch + core libretro | Pronto |
| **Tema "cabinato", lockdown, script di setup, selezione giochi** | **Questo repo** | **Noi** 👈 |

In pratica Batocera ci dà la macchina; noi costruiamo l'**esperienza "Back To The Past"** sopra di essa.

## 🖥️ Hardware target

| Componente | Specifica |
|---|---|
| Marca/modello | Panel PC industriale Asem (×2) |
| CPU | Intel **Atom** (64-bit) |
| RAM | 2 GB |
| Storage | 128 GB+ |
| Display | Touchscreen |
| Controlli | Touch (menu) + joypad USB (gioco) |

> ⚠️ 2 GB di RAM è il **minimo**: si punta su arcade e console leggere. Console pesanti (N64, PSP, Dreamcast, PS2…) sono fuori portata. Dettagli in [docs/04 — Giochi consigliati](docs/04-giochi-consigliati.md).

Per verificare le specifiche esatte (modello Atom, bit, RAM, dischi) c'è lo script [`scripts/check-hardware.sh`](scripts/check-hardware.sh) da lanciare al primo boot.

## 📚 Documentazione

| Doc | Contenuto |
|---|---|
| [01 — Hardware](docs/01-hardware.md) | Specifiche, come verificarle, note sui PC Asem |
| [02 — Sistema operativo](docs/02-sistema-operativo.md) | Perché Batocera, alternative valutate, perché NON scrivere un emulatore |
| [03 — Installazione](docs/03-installazione.md) | Guida passo-passo: creare la chiavetta, installare, primo avvio |
| [04 — Giochi consigliati](docs/04-giochi-consigliati.md) | Sistemi/emulatori che girano su Atom + core consigliati + tuning |
| [05 — Kiosk e controlli](docs/05-kiosk-e-controlli.md) | Lockdown, autostart, touch + joypad, attract mode |
| [06 — Legale](docs/06-legale.md) | ROM e copyright: cosa distribuiamo e cosa no |
| [ROADMAP](docs/ROADMAP.md) | Fasi del progetto e stato |

## 🗂️ Struttura del repo

```
back-to-the-past/
├── docs/        → progettazione e guide
├── scripts/     → script di setup, deploy, diagnostica
├── config/      → file di configurazione (batocera.conf, mappe joypad…)
├── theme/       → tema EmulationStation "Back To The Past"
└── games/       → giochi legali (homebrew/PD) + struttura cartelle
```

## 🚦 Stato

Progetto in fase di **progettazione/setup**. Vedi [ROADMAP](docs/ROADMAP.md).

## 📄 Licenza

Codice e configurazioni di questo repo: [MIT](LICENSE).
I giochi NON sono inclusi salvo quelli esplicitamente liberi/homebrew — vedi [docs/06 — Legale](docs/06-legale.md).
