from urllib.parse import quote

cus_ip = "4.42.42.4"

qut_str = quote("http://apps.ozguruygulama.com/ip-adresi-ogrenme/static/")

redir_url = "redirect?img_url=%s.png&geted" % (qut_str)

print(redir_url)