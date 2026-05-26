# 05 — Kiosk, lockdown e controlli (touch + joypad)

Obiettivo: **accendi → menu giochi → gioca**. Niente desktop, niente impostazioni rompibili dall'utente, niente uscite accidentali.

## Modalità Kiosk (lockdown)

EmulationStation (Batocera) ha tre **UI Mode**:

| Modalità | Cosa vede l'utente |
|---|---|
| **Full** | Tutto (per noi, in fase di setup) |
| **Kiosk** ✅ | Solo i giochi e poche opzioni; menu di configurazione **nascosto** |
| **Kid** | Ancora più ristretta (solo giochi marcati "kid") |

Usiamo **Kiosk** sui cabinati. ✅ **Attivo su Asem #1.**

- Impostazione (GUI): `MENU → UI SETTINGS → UI MODE → Kiosk`.
- In `es_settings.cfg`: `<string name="UIMode" value="Kiosk" />` (file reale in [`config/es_settings.cfg`](../config/es_settings.cfg)).
- ⚠️ ES **riscrive** `es_settings.cfg` quando si chiude: per modificarlo via SSH bisogna **fermare ES, editare, riavviare ES** (vedi sblocco sotto).

### 🔧 Sblocco per manutenzione (tornare a Full)
In Kiosk il menu impostazioni è nascosto. Per rientrare in Full mode, via SSH dal portatile:
```sh
ssh root@<ip-asem>            # password: linux
/etc/init.d/S31emulationstation stop
sed -i 's/value="Kiosk"/value="Full"/' /userdata/system/configs/emulationstation/es_settings.cfg
/etc/init.d/S31emulationstation start
```
Finita la manutenzione, stesso giro al contrario (`Full` → `Kiosk`). Questo è il "backdoor" affidabile del cabinato.

### Altri accorgimenti di lockdown
- **Avvio diretto** su EmulationStation (default Batocera, nessun desktop).
- Disabilitare lo spegnimento accidentale / esporre solo un menu "Spegni" controllato.
- (Opzionale) Password sul BIOS dell'Asem per impedire il boot da USB esterne.
- Sistema Batocera **read-only**: anche se l'utente combina guai, un riavvio ripristina il sistema; solo `userdata` è scrivibile.

## Attract mode (effetto "cabinato vivo")

Batocera può mostrare uno **screensaver/attract** con video o immagini dei giochi quando il cabinato è inattivo — molto "sala giochi".
- `MENU → UI SETTINGS → SCREENSAVER SETTINGS` → tipo `Random Video` o `Slideshow`, timeout es. 90s.

## Controlli: touch + joypad USB

Strategia decisa: **touch per navigare i menu, joypad USB per giocare.**

### Fase di test: solo tastiera + mouse (joypad non ancora acquistati)

Per testare tutto lo stack prima di comprare i joypad, **tastiera e mouse bastano**.

- **EmulationStation:** frecce per navigare, **Invio** per selezionare. Al primo avvio, se non c'è joypad, tieni premuto un tasto e parte "CONFIGURE A CONTROLLER": mappa la tastiera (modo più affidabile).
- **Mapping tastiera predefinito (RetroArch):** D-pad = frecce, B = `Z`, A = `X`, Y = `A`, X = `S`, Start = `Invio`, Select = `Shift destro`, L/R = `Q`/`W`. Rimappabile in *CONTROLLER SETTINGS*.
- **Mouse/touch:** utili per i sistemi "puntatore" (DOS punta-e-clicca, Amiga/C64). Per arcade/console 2D meglio la tastiera.

> La tastiera consente di provare menu, emulatori e prestazioni sulla GMA 3150. I joypad servono solo per il feeling "cabinato".

### Acquisto joypad (target 2D)

Conta più il **d-pad** degli stick: pad stile **SNES-USB** (economici) o **8BitDo** (SN30/M30). Per il vero cabinato, in futuro: joystick + pulsanti arcade con **encoder USB** (Zero-Delay), che Batocera vede come un normale joypad.

### Joypad USB
- Batocera riconosce automaticamente la maggior parte dei joypad USB.
- Prima configurazione: `MENU → CONTROLLER SETTINGS → CONFIGURE A CONTROLLER` e segui il mapping guidato.
- Le mappe risultanti le salviamo in [`config/controllers/`](../config/) per riapplicarle identiche sul secondo Asem.
- Consigliati: pad stile SNES-USB (D-pad ottimo per i 2D) o pad stile Xbox.

### Touch
- Serve a **navigare** (scorrere lista giochi, selezionare). EmulationStation non è nativamente touch-first, quindi:
  - touch come puntatore/scroll dove supportato;
  - in alternativa, un **joypad sempre collegato** garantisce la navigazione completa anche se il touch è limitato.
- Touchscreen **resistivi** possono richiedere calibrazione (vedi [01 — Hardware](01-hardware.md)).
- Alcuni core hanno **overlay touch** a schermo per i giochi: utile se un cabinato dovesse restare solo-touch.

> Nota di design: per un'esperienza "cabinato" pulita, l'ideale è **un joypad collegato fisso** + touch come comodità. Se in futuro si aggiungessero veri controlli arcade (joystick + pulsanti via encoder USB tipo Zero-Delay), Batocera li vede come un normale joypad e il mapping è lo stesso.

## File coinvolti (li versioniamo in `config/`)
- `es_settings.cfg` → UI Mode, screensaver, opzioni ES.
- `batocera.conf` → opzioni globali/per-sistema (core, shader off, rewind off…).
- mappe controller → riproducibili sui due PC.
