# 01 — Hardware

## I due target: Panel PC Asem

Asem S.p.A. (Italia) produce PC industriali e panel PC con touchscreen. I nostri due esemplari montano:

| Componente | Specifica | Note |
|---|---|---|
| CPU | **Intel Atom D525** ✅ confermato | Pineview (2010), dual-core 1.8 GHz, 4 thread (HT), 64-bit |
| GPU | **Intel GMA 3150** (integrata nel D525) | ⚠️ niente accelerazione 3D utilizzabile su Linux moderno → vincola la scelta dell'OS |
| RAM | **2 GB** | confermare ev. espandibilità |
| Storage | **SSD SanDisk U100 — 32 GB** (29.8 GiB) ✅ confermato | disco unico, SATA; ~26 GB liberi per i giochi dopo l'OS |
| Display | Touchscreen | risoluzione + tecnologia touch (resistivo/capacitivo) da verificare |
| I/O | USB (per joypad), eventuale seriale/LAN | n° porte USB libere da verificare |

> ⚠️ **Due colli di bottiglia, non uno:**
> 1. **GPU GMA 3150** — senza 3D moderno. Impone la build **Batocera "Intel Atom / old low-powered (V5.25)"** (vedi [02](02-sistema-operativo.md)) e l'uso di soli sistemi **2D** (no PlayStation 1, no 3D). Anche il tema dev'essere leggero (no video-snap, no shader pesanti).
> 2. **2 GB di RAM** — impone core leggeri.
>
> Risultato: target = arcade 2D + console fino alla 4ª gen. Vedi [04 — Giochi consigliati](04-giochi-consigliati.md).

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
