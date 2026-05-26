# 01 — Hardware

## I due target: Panel PC Asem

Asem S.p.A. (Italia) produce PC industriali e panel PC con touchscreen. I nostri due esemplari montano:

| Componente | Specifica nota | Da verificare |
|---|---|---|
| CPU | Intel **Atom**, **64-bit** | modello esatto (es. N2600, D2550, E38xx, x5-Z83xx…) |
| RAM | **2 GB** | confermare, ev. espandibilità |
| Storage | **128 GB+** | tipo (SSD SATA / mSATA / eMMC) |
| Display | Touchscreen | risoluzione + tecnologia touch (resistivo/capacitivo) |
| Video | Integrata Intel (GMA / HD Graphics) | — |
| I/O | USB (per joypad), eventuale seriale/LAN | n° porte USB libere |

> ⚠️ **2 GB di RAM è il vincolo principale** di tutto il progetto. Determina quali sistemi possiamo emulare (arcade + console fino a 4ª/5ª gen) e impone core leggeri. Vedi [04 — Giochi consigliati](04-giochi-consigliati.md).

## Verificare le specifiche reali

Le specifiche esatte cambiano scelte fini (driver video, core consigliati). Le scopriamo al **primo avvio** di Batocera da chiavetta, prima ancora di installare.

In Batocera apri un terminale (tasto **F1** dal menu → *Applications* → terminale, oppure SSH) e lancia lo script:

```sh
sh check-hardware.sh
```

Vedi [`scripts/check-hardware.sh`](../scripts/check-hardware.sh) — riporta CPU, architettura (32/64 bit), RAM, dischi, GPU, schede audio e dispositivi USB/input collegati.

In alternativa, comandi singoli:

```sh
lscpu              # modello CPU + architettura
free -h            # RAM
lsblk              # dischi e partizioni
lspci | grep VGA   # GPU
lsusb              # joypad / encoder collegati
```

## Note touchscreen

- Il touch capacitivo è plug-and-play su Linux; quello **resistivo** a volte richiede calibrazione (`xinput`, o tool di Batocera).
- EmulationStation non è pensato primariamente per il touch: nel nostro setup il **touch serve a navigare**, il **joypad a giocare**. Dettagli in [05 — Kiosk e controlli](05-kiosk-e-controlli.md).

## Macchina di sviluppo vs target

- **Sviluppo:** portatile Windows (questo repo). Qui scriviamo tema, script e config.
- **Target:** i due Asem, dove installiamo Batocera e deployamo il contenuto del repo.

Vedi il flusso completo in [03 — Installazione](03-installazione.md).
