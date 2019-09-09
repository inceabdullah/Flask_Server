from PIL import Image, ImageDraw
from flask import Flask, request, redirect   
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    cus_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    
    W, H = (360, 150)
    msg = "94.54.60.74"
    im = Image.new("RGBA", (W, H), "black")
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg)
    draw.text(((W-w)/2,(H-h)/2), msg, fill ="white")
    img_adi = "static/%s.png" % cus_ip
    im.save(img_adi,"PNG")
    qut_url = quote("http://apps.ozguruygulama.com/ip-adresi-ogrenme/static/")
    
    redir_url = "redirect?img_url=%s.png&geted" % (qut_url+cus_ip)
    
    return redirect(redir_url, code=302) 
    
    
@app.route('/redirect')
def redirect_():

    
    return ""