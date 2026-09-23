"""Derive transparent logo variants from the supplied black-on-white master.

No drawing or generative changes are applied to the signature geometry.
"""
from pathlib import Path
from PIL import Image, ImageOps

root = Path(__file__).resolve().parent
source = root.parent / "Logomarca" / "Gemini_Generated_Image_vv0l6hvv0l6hvv0l.jpg"
gray = Image.open(source).convert("L")
alpha = ImageOps.invert(gray)
# Remove JPEG noise from the white background while retaining soft stroke edges.
alpha = alpha.point(lambda value: 0 if value < 9 else min(255, round((value - 9) * 255 / 246)))
bounds = alpha.getbbox()
if not bounds:
    raise RuntimeError("A assinatura não foi encontrada na imagem de origem")
padding = 24
left, top, right, bottom = bounds
box = (max(0, left - padding), max(0, top - padding), min(gray.width, right + padding), min(gray.height, bottom + padding))
alpha = alpha.crop(box)
for name, color in (("signature-light.png", (255, 255, 255)), ("signature-dark.png", (32, 45, 58))):
    out = Image.new("RGBA", alpha.size, (*color, 0))
    out.putalpha(alpha)
    out.save(root / "assets" / "images" / name, optimize=True)
    print(name, out.size)
