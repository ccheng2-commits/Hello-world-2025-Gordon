import math
from tkinter import *
from PIL import Image, ImageDraw, ImageTk

# --- Basic settings ---
WIDTH, HEIGHT = 600, 300
SCALE = 4  # for anti-aliasing (smooth edges)
BG_COLOR = (255, 255, 255, 255)

def strength_color(level):
    """Return RGBA color based on wind level (0-5)."""
    if level <= 0:
        return (0, 0, 0, 0)
    t = level / 5
    r = int(40 + 200 * t)
    g = int(120 * (1 - t) + 30 * t)
    b = int(220 * (1 - t) + 50 * t)
    a = int(80 + 160 * t)
    return (r, g, b, a)

def draw_wind(level):
    """Generate the wind pattern image."""
    big_w, big_h = WIDTH * SCALE, HEIGHT * SCALE
    img = Image.new("RGBA", (big_w, big_h), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")

    if level == 0:
        from PIL import ImageFont
        try:
            font = ImageFont.truetype("Arial.ttf", 48 * SCALE)
        except:
            font = None
        draw.text((big_w//2 - 50*SCALE, big_h//2 - 20*SCALE),
                  "calm", fill=(140,140,140,180), font=font)
    else:
        color = strength_color(level)
        base_y = big_h // 2
        n_lines = level * 6
        amplitude = 8 * SCALE + level * 3 * SCALE
        spacing = int(10 * SCALE)
        line_w = int(1.5 * SCALE + level)

        for i in range(n_lines):
            offset = i - n_lines // 2
            y0 = base_y + offset * spacing
            phase = i * math.pi / 10
            pts = []
            for x in range(0, big_w, 4 * SCALE):
                y = y0 + amplitude * math.sin((2 * math.pi * x) / (150 * SCALE) + phase)
                pts.append((x, y))
            draw.line(pts, fill=color, width=line_w)

    return img.resize((WIDTH, HEIGHT), Image.LANCZOS)

# --- Main program ---
if __name__ == "__main__":
    level = int(input("Enter wind level (0–5): "))

    root = Tk()
    root.title(f"Wind Level {level}")
    img = draw_wind(level)
    tk_img = ImageTk.PhotoImage(img)

    canvas = Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    canvas.create_image(0, 0, image=tk_img, anchor="nw")

    root.mainloop()