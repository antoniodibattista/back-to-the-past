# 05 — Kiosk, lockdown e controlli (touch + joypad)

Obiettivo: **accendi → menu giochi → gioca**. Niente desktop, niente impostazioni rompibili dall'utente, niente uscite accidentali.

## Modalità Kiosk (lockdown)

EmulationStation (Batocera) ha tre **UI Mode**:

| Modalità | Cosa vede l'utente |
|---|---|
| **Full** | Tutto (per noi, in fase di setup) |
| **Kiosk** ✅ | Solo i giochi e poche opzioni; menu di configurazione **nascosto** |
| **Kid** | Ancora più ristretta (solo giochi marcati "kid") |

Useremo **Kiosk** sui cabinati.

- Impostazione: `MENU → UI SETTINGS → UI MODE → Kiosk`.
- In `es_settings.cfg`: `<string name="UIMode" value="Kiosk" />`.
- Per **rientrare** in Full mode (manutenzione) c'è una sequenza/passphrase di sblocco (es. inserire un codice col joypad). La documenteremo in `config/`.

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
