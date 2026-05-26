#!/bin/sh
# check-hardware.sh — Back To The Past
# Ricognizione hardware del PC Asem al primo avvio di Batocera (live USB).
# Uso:  sh check-hardware.sh
# Funziona su Batocera/Linux (BusyBox). Non richiede installazione.

line() { printf '\n===== %s =====\n' "$1"; }

printf '### Back To The Past — ricognizione hardware ###\n'
printf 'Data: %s\n' "$(date 2>/dev/null)"

line "CPU"
if command -v lscpu >/dev/null 2>&1; then
  lscpu | grep -Ei 'model name|architecture|cpu\(s\)|vendor|mhz'
else
  grep -Ei 'model name|flags' /proc/cpuinfo | head -2
fi
# Architettura 32/64 bit: 'lm' nei flags indica supporto 64-bit
if grep -q ' lm ' /proc/cpuinfo 2>/dev/null || grep -q ' lm$' /proc/cpuinfo 2>/dev/null; then
  printf 'Architettura: 64-bit supportato (flag lm presente)\n'
else
  printf 'Architettura: 64-bit NON rilevato (flag lm assente) -> probabile 32-bit\n'
fi

line "RAM"
if command -v free >/dev/null 2>&1; then
  free -h
else
  grep -i memtotal /proc/meminfo
fi

line "DISCHI / STORAGE"
if command -v lsblk >/dev/null 2>&1; then
  lsblk -o NAME,SIZE,TYPE,MODEL,TRAN 2>/dev/null || lsblk
else
  cat /proc/partitions
fi

line "GPU / VIDEO"
if command -v lspci >/dev/null 2>&1; then
  lspci | grep -Ei 'vga|display|graphics'
else
  printf 'lspci non disponibile\n'
fi

line "AUDIO"
if command -v aplay >/dev/null 2>&1; then
  aplay -l 2>/dev/null | grep -i card
elif command -v lspci >/dev/null 2>&1; then
  lspci | grep -i audio
fi

line "USB (joypad / encoder / touch)"
if command -v lsusb >/dev/null 2>&1; then
  lsusb
else
  printf 'lsusb non disponibile\n'
fi

line "INPUT DEVICES (touch / joystick)"
if [ -d /proc/bus/input ]; then
  grep -Ei 'name=' /proc/bus/input/devices 2>/dev/null
fi
ls /dev/input/ 2>/dev/null

line "RETE"
ip addr 2>/dev/null | grep -E 'inet |link/ether' || ifconfig 2>/dev/null | grep -E 'inet |HWaddr'

printf '\n### Fine ricognizione. Annota questi dati in docs/01-hardware.md ###\n'
