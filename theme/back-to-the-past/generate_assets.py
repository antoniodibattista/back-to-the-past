#!/usr/bin/env python3
"""
Genera gli asset grafici del tema "Back To The Past" (stile synthwave/arcade).
Richiede: Pillow (PIL). Font: Press Start 2P (OFL) in ./art/.
Output: ./art/background.png (1366x768) e ./art/logo.png (trasparente).
Eseguire dalla cartella del tema:  python generate_assets.py
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "art")
FONT = os.path.join(ART, "PressStart2P-Regular.ttf")
W, H = 1366, 768

# Palette neon
CYAN = (0, 229, 255)
MAGENTA = (255, 45, 149)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def make_background():
    bg = Image.new("RGB", (W, H), (7, 6, 15))
    d = ImageDraw.Draw(bg)
    horizon = int(H * 0.62)
    # cielo: nero-blu in alto -> viola verso l'orizzonte
    sky_top, sky_bot = (9, 8, 22), (58, 18, 68)
    for y in range(horizon):
        t = (y / horizon) ** 2
        d.line([(0, y), (W, y)], fill=lerp(sky_top, sky_bot, t))
    # pavimento: viola scuro -> quasi nero
    flr_top, flr_bot = (22, 7, 30), (5, 4, 11)
    for y in range(horizon, H):
        t = (y - horizon) / (H - horizon)
        d.line([(0, y), (W, y)], fill=lerp(flr_top, flr_bot, t))

    cx = W // 2
    # sole/alone magenta all'orizzonte
    sun = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sun)
    r = 230
    sd.ellipse([cx - r, horizon - r, cx + r, horizon + r], fill=(255, 70, 150, 130))
    sun = sun.filter(ImageFilter.GaussianBlur(70))
    bg = Image.alpha_composite(bg.convert("RGBA"), sun)

    # griglia neon in prospettiva
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    # linee verticali che convergono al punto di fuga (cx, horizon)
    nv = 22
    for i in range(-nv, nv + 1):
        xb = cx + i * (W / nv) * 1.6
        gd.line([(cx, horizon), (xb, H)], fill=(*MAGENTA, 70), width=1)
    # linee orizzontali sempre piu' fitte verso l'orizzonte
    nh = 18
    for i in range(nh + 1):
        t = i / nh
        y = horizon + int((H - horizon) * (t ** 1.9))
        a = int(150 * (1 - t * 0.5))
        gd.line([(0, y), (W, y)], fill=(*CYAN, a), width=2)
    grid = grid.filter(ImageFilter.GaussianBlur(0.6))
    bg = Image.alpha_composite(bg, grid)

    # vignettatura ai bordi
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-W * 0.25, -H * 0.25, W * 1.25, H * 1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(150))
    dark = Image.new("RGBA", (W, H), (0, 0, 0, 170))
    bg = Image.composite(bg, Image.alpha_composite(bg, dark), vig)

    bg.convert("RGB").save(os.path.join(ART, "background.png"))
    print("background.png OK")


def make_logo():
    lines = ["BACK TO", "THE PAST"]
    fs = 86
    font = ImageFont.truetype(FONT, fs)
    tmp = ImageDraw.Draw(Image.new("RGBA", (4, 4)))
    widths = [tmp.textbbox((0, 0), s, font=font)[2] for s in lines]
    pad = 90
    lh = fs + 30
    LW = max(widths) + pad * 2
    LH = lh * len(lines) + pad

    def draw_text(color):
        im = Image.new("RGBA", (LW, LH), (0, 0, 0, 0))
        dd = ImageDraw.Draw(im)
        for idx, s in enumerate(lines):
            w = tmp.textbbox((0, 0), s, font=font)[2]
            dd.text(((LW - w) // 2, pad // 2 + idx * lh), s, font=font, fill=color)
        return im

    core = draw_text((255, 255, 255, 255))
    glow_c = draw_text((*CYAN, 255)).filter(ImageFilter.GaussianBlur(26))
    glow_m = draw_text((*MAGENTA, 255)).filter(ImageFilter.GaussianBlur(13))

    out = Image.new("RGBA", (LW, LH), (0, 0, 0, 0))
    for layer in (glow_c, glow_m, glow_m, core):
        out = Image.alpha_composite(out, layer)
    out.save(os.path.join(ART, "logo.png"))
    print("logo.png OK (%dx%d)" % (LW, LH))


if __name__ == "__main__":
    make_background()
    make_logo()
    print("Asset generati in", ART)
