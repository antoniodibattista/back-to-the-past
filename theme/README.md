# theme/

Il tema **EmulationStation** "Back To The Past" — l'identità visiva del cabinato. È il principale deliverable di sviluppo del progetto.

## Obiettivo estetico
Look da **cabinato arcade anni 80/90**: colori al neon, font pixel/retro, eventuale effetto CRT/scanline leggero (senza appesantire l'Atom), logo "Back To The Past", marquee per ogni sistema.

## Destinazione su Asem
`/userdata/themes/back-to-the-past/` → poi selezionato in `MENU → UI SETTINGS → THEME SET`.

## Come si costruisce
Un tema EmulationStation è una cartella di **XML + immagini**:
```
back-to-the-past/
├── theme.xml            # definizione globale (view system/gamelist)
├── colors / fonts       # palette e font retro
├── _inc/                # frammenti riusabili
└── <sistema>/           # asset per ogni sistema (logo, sfondo, marquee)
    ├── nes/ snes/ mame/ ...
```

## Strategia consigliata
- Partire da un tema leggero esistente (es. famiglia *Carbon* o un tema "arcade" minimale) e **rebrandizzarlo** "Back To The Past": più rapido che partire da zero e più gentile con l'Atom.
- Evitare video-snap e animazioni pesanti nelle gamelist (RAM/CPU limitate).
- Riferimento formato temi: https://wiki.batocera.org/themes

> Stato: **da fare** (Fase 3 della [ROADMAP](../docs/ROADMAP.md)). Cartella segnaposto.
