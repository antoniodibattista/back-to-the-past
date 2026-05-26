# 03 — Installazione

Flusso completo: dal portatile di sviluppo ai due cabinati Asem.

```
[ Portatile Windows ]                 [ Asem #1 e #2 ]
  - questo repo            ── deploy ──▶  - Batocera installato su disco
  - scrive img su USB                     - /userdata popolato col nostro contenuto
```

---

## Fase 1 — Procurarsi Batocera (sul portatile)

1. Vai su https://batocera.org/download e scarica la build **"Intel Atom and old low-powered devices (V5.25)"** (file `.img.gz`).
   - ⚠️ **NON** la build x86_64 "standard/ultima": sul nostro Atom **D525 / GMA 3150** non parte (vedi [02](02-sistema-operativo.md)).
2. Scarica uno scrittore di immagini:
   - **balenaEtcher** (consigliato, semplice) — oppure **Rufus**.
3. Inserisci una chiavetta USB (≥ 8 GB; verrà **cancellata**).

## Fase 2 — Creare la chiavetta avviabile

Con balenaEtcher:
1. *Flash from file* → seleziona `batocera-5.25-x86-*.img.gz` (non serve scompattarlo).
2. *Select target* → la chiavetta USB.
3. *Flash!* e attendi.

> Se balenaEtcher si blocca: usa **USBImager** (gestisce direttamente il `.img.gz`) o **Rufus** (in modalità **DD**). Eseguilo come amministratore e usa una porta USB 2.0.

## Fase 3 — Primo avvio LIVE sull'Asem (senza installare)

1. Inserisci la chiavetta nell'Asem, accendi ed entra nel **boot menu** (di solito `F12`/`F11`/`ESC` — varia per BIOS).
2. Avvia da USB. Batocera parte in modalità live.
3. **Verifica l'hardware reale** con [`scripts/check-hardware.sh`](../scripts/check-hardware.sh) (vedi [01 — Hardware](01-hardware.md)). Annota CPU, RAM, dischi, touch, USB.
4. Verifica che **touchscreen** e **joypad USB** vengano riconosciuti.

> Se i 2 GB rendessero EmulationStation troppo pesante, qui valutiamo il piano B (Lakka). Vedi [02](02-sistema-operativo.md).

## Fase 4 — Installazione su disco interno (procedura testata su Asem #1)

> ⚠️ **Lezione dall'Asem #1:** il classico **MENU → SYSTEM SETTINGS → INSTALL ON A NEW DISK** (e il comando `batocera-install`) **non va bene** per noi:
> 1. su V5.25 quel comando **scarica da internet l'ultima Batocera** (che sul D525/GMA 3150 non funziona), non installa la V5.25 che stai usando;
> 2. se il disco interno ha già un OS e `sharedevice=INTERNAL`, Batocera **monta il disco interno come `/userdata`**: l'installer non riesce a smontarlo e fallisce con *"AN ERROR OCCURED: check the system/logs directory"* (exit 256).
>
> Il metodo affidabile è **scrivere la stessa immagine V5.25 sul disco con `dd`** (è esattamente ciò che l'installer fa internamente: `zcat img.gz | dd of=/dev/sdX`).

**Accesso:** SSH `root@<ip-asem>`, password `linux` (IP in MENU → NETWORK SETTINGS). Su Windows si passa la password con `sshpass`, es.:
`sshpass -p linux ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=NUL root@<ip>`

1. **Libera il disco interno**: rendi scrivibile `/boot`, metti `sharedevice=RAM`, riavvia.
   ```sh
   mount -o remount,rw /boot
   sed -i s/sharedevice=INTERNAL/sharedevice=RAM/ /boot/batocera-boot.conf
   reboot
   ```
2. **Smonta il disco interno** se auto-montato come drive esterno (verifica con `grep /dev/sda /proc/mounts`, dev'essere vuoto):
   ```sh
   umount /dev/sda1
   ```
3. **Porta l'immagine V5.25 sull'Asem** (in `/boot`, che ha spazio):
   ```sh
   # dal portatile:
   scp batocera-5.25-x86-*.img.gz root@<ip>:/boot/
   ```
4. **Scrivi l'immagine sul disco** — ⚠️ CANCELLA TUTTO (anche un OS preesistente):
   ```sh
   zcat /boot/batocera-5.25-x86-*.img.gz | dd of=/dev/sda bs=4M
   sync
   ```
5. **Abilita l'auto-espansione** dell'area dati sul disco appena scritto:
   ```sh
   mkdir -p /tmp/sb && mount /dev/sda1 /tmp/sb
   sed -i s/#autoresize=true/autoresize=true/ /tmp/sb/batocera-boot.conf
   sync && umount /tmp/sb
   ```
6. **Spegni, togli la chiavetta, riaccendi.** Parte da disco; il primo avvio **espande `/userdata`** a tutto il disco (può riavviarsi una volta da solo).

> ⚠️ Identifica bene il disco: `/dev/sda` = SSD interna (`TRAN=ata`), `/dev/sdb` = chiavetta USB (`TRAN=usb`). Controlla con `lsblk -o NAME,SIZE,TRAN,MODEL`.

Al riavvio Batocera parte dal disco. Lo storage è diviso in:
- partizione **BATOCERA** (sistema, read-only)
- partizione **SHARE → `/userdata`** ← qui vivono ROM, configurazioni, salvataggi, temi → **è ciò che deployamo noi**.

## Fase 5 — Deploy del nostro livello "Back To The Past"

Il contenuto di questo repo va in `/userdata` dell'Asem. Mappatura cartelle:

| Repo | Destinazione su Asem |
|---|---|
| `theme/back-to-the-past/` | `/userdata/themes/back-to-the-past/` |
| `config/batocera.conf` (chiavi) | `/userdata/system/batocera.conf` |
| `config/es_settings.cfg` | `/userdata/system/configs/emulationstation/es_settings.cfg` |
| `config/controllers/` | mappe joypad (in `batocera.conf` / ES) |
| `games/<sistema>/` | `/userdata/roms/<sistema>/` |

Metodi di deploy (uno qualsiasi):

- **Rete (consigliato):** Batocera espone una share di rete (SMB) `\\BATOCERA\share` e il **SSH** (utente `root`, password default `linux`). Dal portatile si copia con `scp`/`rsync` o trascinando nella share.
- **Chiavetta USB:** copia le cartelle e poi sposta in `/userdata`.

> Gli script in [`scripts/`](../scripts/) automatizzeranno questo deploy (es. `deploy.sh` via SSH/rsync). Vedi [ROADMAP](ROADMAP.md).

## Fase 6 — Kiosk & finalizzazione

1. Imposta la modalità **Kiosk** in EmulationStation (lockdown).
2. Abilita l'**avvio diretto** sul menu (già default) ed eventuale **attract mode**.
3. Configura touch (navigazione) + joypad (gioco).
4. Vedi [05 — Kiosk e controlli](05-kiosk-e-controlli.md).

## Fase 7 — Ripeti sul secondo Asem

Stessa procedura. Il bello del repo è che il deploy è **identico e riproducibile** sui due PC.

---

## Checklist rapida

**Asem #1:**
- [x] Immagine Batocera V5.25 (x86) scaricata
- [x] Chiavetta USB creata
- [x] Boot live su Asem #1 OK
- [x] Hardware verificato (Atom D525, GMA 3150, SSD 32 GB, eth0)
- [x] Installazione su disco interno (metodo `dd`, area dati espansa a ~26 GB)
- [ ] Deploy tema/config/giochi
- [ ] Kiosk + controlli configurati

**Asem #2:**
- [ ] Ripetere installazione (stessa procedura `dd`)
- [ ] Deploy + kiosk
