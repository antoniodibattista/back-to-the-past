# scripts/

Script di setup, deploy e diagnostica per i cabinati.

| Script | Stato | Descrizione |
|---|---|---|
| `check-hardware.sh` | ✅ pronto | Ricognizione hardware sull'Asem al primo boot di Batocera (CPU, bit, RAM, dischi, GPU, USB, input). Vedi [docs/01](../docs/01-hardware.md). |
| `deploy.sh` | 🔜 da fare | Push di `theme/`, `config/`, `games/` su `/userdata` dell'Asem via SSH/rsync. |
| `backup-userdata.sh` | 💡 idea | Backup della partizione `userdata` (config + salvataggi). |

## Note
- Gli script `.sh` girano su **Batocera/Linux** (shell BusyBox `sh`), non su Windows.
- Dal portatile Windows si lanciano i deploy via SSH (`ssh root@<ip-asem>`, password default `linux`) o via la share di rete di Batocera.
