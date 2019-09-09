from PIL import Image, ImageDraw

W, H = (360, 150)
msg = "94.54.60.74"
im = Image.new("RGBA", (W, H), "black")
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg)
draw.text(((W-w)/2,(H-h)/2), msg, fill ="white")
im.save("static/rsm.png","PNG")
