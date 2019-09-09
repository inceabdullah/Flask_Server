import mysql.connector #

from flask import Flask, redirect, request
import urllib3
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def hello():
    
    url_req = "https://usa.inquirer.net/files/2019/06/800-620x413.jpeg"
    return redirect(url_req, code=302) 


@app.route("/kac_adet")
def kac_adet():
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")   
    # kac tane bugun tarihi var, ++versiyonlar: tarih degiskeni
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="***", passwd="**", database="***")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    row_say = 0
    for row in rows:    
        if bugun_date == row[0]:
            row_say += 1  # kac adet oldugudur, satir olarak versiyon 1 en fazla 5 
    
    if row_say > 5:
        row_say = 5
    
    url_req = "redirect?adet=%d" % row_say
    url_son = "&gated&"
    url_req = url_req+url_son
    return redirect(url_req, code=302) 
    
    
@app.route("/kac_keywords", methods=['GET', 'POST'])
def kac_keywords_():
    # kac adet keyword, maximum 20 adet app verdiyon 1 icin. genelli,kte dbde cok fazla var 
    
    url_req = str(request.args.get('url')) # app 1den gelip tinyDB ye yazan
    
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")       
    
    # mysql cift arama hem tarih hem de url tutarsa
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="***", passwd="***", database="***")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    row_say = 0
    for row in rows:    
        if bugun_date == row[0]:
            if url_req == row[1]:
                split_the_hashes = row[3].split(';')              #row_say += 1  # kac adet oldugudur, satir olarak, versiyon 1 icin en fazla 20dir
                len_split_TH = len(split_the_hashes)# edit: yanlis. satir degil, split il olmali row[3] de
                
    
    if len_split_TH > 20:
        len_split_TH = 20
    
    url_req = "redirect?adet=%d" % len_split_TH
    url_son = "&gated&"
    url_req = url_req+url_son
    return redirect(url_req, code=302) 
    
    
    
@app.route("/url_al")
def url_al_():
    
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")     
    
    # mysql cift arama hem tarih hem de url tutarsa
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="***", passwd="***", database="***")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    
    # url listesi
    
    URLs = []
    
    row_say = 0
    for row in rows:    
            if bugun_date == row[0]:
                row_say += 1
                if not row_say > 5:
                    URLs.append(row[1])

    getnamed_URLs = []
    toplamali_GURL = ""
    
    for z in range(len(URLs)):
        getnamed_URLs.append('')
        getnamed_URLs[z] = "url%d=%s&" % ((z+1), quote(URLs[z]))
        toplamali_GURL = toplamali_GURL + getnamed_URLs[z]
        

    
    url_req = "redirect?%s" % (toplamali_GURL)
    url_son = "gated&"
    url_req = url_req+url_son
    return redirect(url_req, code=302)     

@app.route("/resim_al", methods=['GET', 'POST'])
def resim_al():
    
    resimid_req = int(request.args.get('resimid')) # for icin integer
    url_req = str(request.args.get('url'))
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")     
    
    # mysql cift arama hem tarih hem de url tutarsa
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="**", passwd="***", database="**")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    
    # url listesi
    
    
    
    row_say = 0
    for row in rows:    
            if bugun_date == row[0]:
                row_say += 1
                if row_say == resimid_req:
                    thumb_resmi = row[2]
                      
    

    thumb_url = "http://apps.ozguruygulama.com/ingilizce-haber-oku/static/thumbs/%s" % thumb_resmi
    return redirect(thumb_url, code=302)
    
    
@app.route("/keyword_al", methods=['GET', 'POST'])
def keyword_al_():
    
    url_req = str(request.args.get('url'))
    sirasi_req = str(request.args.get('sirasi'))
    
    resimid_req = int(request.args.get('resimid')) # array icin integer
    url_req = str(request.args.get('url'))
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")     
    
    # mysql cift arama hem tarih hem de url tutarsa
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="**", passwd="**", database="***")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    
   
    
    
    
    row_say = 0
    for row in rows:    
            if bugun_date == row[0]:
                if url_req == row[1]:
                    line_the_hashed = row[3]
    

    line_the_hasheds = line_the_hashed.split(';')    

    keyword_url = "http://apps.ozguruygulama.com/ingilizce-haber-oku/static/words/%s.png" % line_the_hasheds[(resimid_req-1)]
    return redirect(keyword_url, code=302)  
    
    
@app.route("/anlam_al", methods=['GET', 'POST'])
def anlam_al_():
    
    url_req = str(request.args.get('url'))
    sirasi_req = int(request.args.get('resimid'))
    
    
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")     
    
    # mysql cift arama hem tarih hem de url tutarsa
    import  mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="**", passwd="**", database="**")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM table_ingilizce")
    rows = mycursor.fetchall()
    
   
    
    
    
    row_say = 0
    for row in rows:    
            if bugun_date == row[0]:
                if url_req == row[1]:
                    line_the_hashed = row[3]
    

    line_the_hasheds = line_the_hashed.split(';')        
    


    anlam_url = "http://apps.ozguruygulama.com/ingilizce-haber-oku/static/anlamlar/%s.png" % line_the_hasheds[(sirasi_req-1)]
    return redirect(anlam_url, code=302)    



@app.route("/redirect")
def redirect_():
    
    
    
    
    return "" 
    
    
    

# liste icin input


@app.route("/listeicininput")
def listeicininput_():
    
    html = """
    
    <form action="listelendi" method="post">URL: <input name="url" type="text" /><br /> 
  
  
  
    <input type="submit" value="Submit" /></form>
    """
    
    
    
    return html
    
    
    
@app.route("/listelendi", methods=['GET', 'POST'])
def listelendi_():
    
    import news_url_to_thumb_img
    import fetch_words_from_news
    
    
    
    url_req = str(request.form['url'])  

    geted_img_filename = news_url_to_thumb_img.news_url_to_thumb_img(url_req) # return [img, filename(....png)]
    
    geted_words = fetch_words_from_news.fetch_words_from_news(url_req) # return [[],[]] 0: en, 1:tr
    
    geted_en = geted_words[0]
    geted_tr = geted_words[1]
    
    # make pic_path
    
    file_name_mh5ed = geted_img_filename[1]
    
    pic_path = "static/thumbs/%s" % file_name_mh5ed
    
    # save the pic
    
    geted_img_filename[0].save(pic_path, "PNG")
    
    toplam_geted = len(geted_words[0])
    
    img_html = """
     <img src="%s"> 
     """ % pic_path
     
    html_checkbox = "" 
     
    for i in range(toplam_geted):
        html_checkbox = html_checkbox+"""<input type="checkbox" name="chckbx%d" value="True"><input name="word%d" value="%s"><input name="anlam%d" value="%s"><br>
        """ % ((i+1), (i+1), geted_en[i], (i+1), geted_tr[i])
        
        
        
        
        
        
        
        
    
    html = """<form action="liste_duzeldi_before" method="post">
    URL: <input name="url" type="text" value="%s" /><br />
    MD5: <input name="md5_url" type="text" value="%s" /><br /> 
    Adet: <input name="adet" type="text" value="%d" /><br />    
  
    %s

  
  
  
    <input type="submit" value="Submit" />
    
    
    </form>
    
    %s
    """ % (url_req, file_name_mh5ed, toplam_geted, html_checkbox, img_html)
    
    
    
    
    
    return html    
    
    
    
@app.route("/liste_duzeldi_before", methods=['GET', 'POST'])
def liste_duzeldi_before_():
    
    # liste duzeldiden:
    
    url_req = str(request.form['url'])  
    md5_url_req = str(request.form['md5_url'])
    adet_req = int(str(request.form['adet']))
    
    # not splitted en ve tr
    
    ok_words = []
    topla_words = ""
    ok_anlamlar = []
    topla_anlamlar = ""
    topla_satirlar = ""
    
    gecerli_word_say = 0
    for j in range(adet_req):
        inside_arg_get = 'chckbx%d' % (j+1)
        inside_word_get = 'word%d' % (j+1)
        inside_anlam_get = 'anlam%d' % (j+1)
        if str(request.form.get(inside_arg_get)) == "True":
            gecerli_word_say += 1
            ok_words.append(str(request.form.get(inside_word_get)))
            
            

        
        toplam_words_sayisi = gecerli_word_say
        
        

  



    
    # make pic_path
        
    img_html = """
     <img src="static/thumbs/%s"> 
     """ % md5_url_req
     
    
    
    #get tr_from_en_list()
    
    import tr_from_en_list
    geted_tr_list = tr_from_en_list.tr_from_en_list(ok_words)
    
    
       
    # save the pic
    
    html_checkbox = "" 
     
    for i in range(toplam_words_sayisi):
        html_checkbox = html_checkbox+"""<input type="checkbox" name="chckbx%d" value="True"><input name="word%d" value="%s"><input name="anlam%d" value="%s"><br>
        """ % ((i+1), (i+1), ok_words[i], (i+1), geted_tr_list[i])
        
        
        
        
        
        
        
        
    
    html = """<form action="liste_duzeldi" method="post">
    URL: <input name="url" type="text" value="%s" /><br />
    MD5: <input name="md5_url" type="text" value="%s" /><br /> 
    Adet: <input name="adet" type="text" value="%d" /><br />    
  
    %s

  
  
  
    <input type="submit" value="Submit" />
    
    
    </form>
    
    %s
    """ % (url_req, md5_url_req, toplam_words_sayisi, html_checkbox, img_html)
    
    
    
    
    return html
    
    
    
@app.route("/liste_duzeldi", methods=['GET', 'POST'])
def liste_duzeldi_():
    
    
    url_req = str(request.form['url'])  
    md5_url_req = str(request.form['md5_url'])
    adet_req = int(str(request.form['adet']))
    
    # not splitted en ve tr
    
    ok_words = []
    topla_words = ""
    ok_anlamlar = []
    topla_anlamlar = ""
    topla_satirlar = ""
    
    gecerli_word_say = 0
    for j in range(adet_req):
        inside_arg_get = 'chckbx%d' % (j+1)
        inside_word_get = 'word%d' % (j+1)
        inside_anlam_get = 'anlam%d' % (j+1)
        if str(request.form.get(inside_arg_get)) == "True":
            gecerli_word_say += 1
            ok_words.append(str(request.form.get(inside_word_get)))
            topla_words = topla_words+";"+str(request.form.get(inside_word_get))
            ok_anlamlar.append(str(request.form.get(inside_anlam_get)))
            topla_anlamlar = topla_anlamlar+";"+str(request.form.get(inside_anlam_get))
            topla_satirlar = topla_satirlar+str(gecerli_word_say)+". "+str(request.form.get(inside_word_get))+"   -   "+str(request.form.get(inside_anlam_get))+"<br />"
        
        toplam_words_sayisi = gecerli_word_say
        
        
    img_html = """
     <img src="static/thumbs/%s"> 
     """ % md5_url_req
     
    
    
    
    hiddens = """
    
    URL: <input name="url" type="text" value="%s" /><br />
    MD5: <input name="md5_url" type="text" value="%s" /><br /> 
    Adet: <input name="adet" type="text" value="%d" /><br />
    ENs : <input name="ens" type="text" value="%s" /><br />
    TRs : <input name="trs" type="text" value="%s" /><br />
    
    
    """ % (url_req, md5_url_req, toplam_words_sayisi, topla_words, topla_anlamlar)
    
    
    
    html = """
    
    <form action="make_text_img" method="post">
    
    %s
  
    %s
  
    <input type="submit" value="Submit" /></form>
    
    %s
    
    """ % (hiddens, topla_satirlar, img_html)
    
    
    
    return html    
    
    
    
# make_text_img

    
@app.route("/make_text_img", methods=['GET', 'POST'])
def make_text_img_():
    
    import make_fittedFRAMED_textIMG
    import text_2_md5_hash
    import datetime
    
    # today like 19-7-13
    
    today = datetime.date.today()
    bugun_date = today.strftime("%y-%m-%d")
    
    
    url_req = str(request.form['url'])  
    md5_url_req = str(request.form['md5_url'])
    adet_req = int(str(request.form['adet']))
    ens_req = str(request.form['ens'])
    trs_req = str(request.form['trs'])
    
    # spitted ens ve trs:
    
    ens_all = ens_req.split(";")
    trs_all = trs_req.split(";")
    
    word_hasheds = []

    adet_words = len(ens_all)

    img_html = """
     <img src="static/thumbs/%s"> 
     """ % md5_url_req
     
    for k in range(adet_words):
        #for word:
        word_name = ens_all[k]
        word_textIMG = make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG(word_name, True, 24, "bg_320x50.png")
        #save the word to static/words
        word_file_name_hash = text_2_md5_hash.text_2_md5_hash(word_name)
         
        save_word_path = "static/words/%s.png" % word_file_name_hash
        word_textIMG[0].save(save_word_path, "PNG")
         
        word_hasheds.append(word_file_name_hash)
         
        anlam_name = trs_all[k]
        anlam_textIMG = make_fittedFRAMED_textIMG.make_fittedFRAMED_textIMG(anlam_name, True, 24, "bg_320x50.png")
        
        # hash almaya gerek yok.
        
        #save anlamlar to static/anlamlar
        
        save_anlam_path = "static/anlamlar/%s.png" % word_file_name_hash
         
        anlam_textIMG[0].save(save_anlam_path, "PNG") 
        
        #appende gerek yok
        
        
    toplanmis_word_hasheds = ""
    
    for l in range(len(word_hasheds)):
        toplanmis_word_hasheds = toplanmis_word_hasheds+";"+word_hasheds[l]
        
        
        
    
            
    
    
    hiddens = """
    
    URL: <input name="url" type="text" value="%s" /><br />
    MD5: <input name="md5_url" type="text" value="%s" /><br /> 
    Adet: <input name="adet" type="text" value="%d" /><br />
    ENs : <input name="ens" type="text" value="%s" /><br />
    TRs : <input name="trs" type="text" value="%s" /><br />
    WordHashes : <input name="wordhashes" type="text" value="%s" /><br />
    Date : <input name="date" type="text" value="%s" /><br />
    
    
    """ % (url_req, md5_url_req, adet_req, ens_req, trs_req, toplanmis_word_hasheds, bugun_date)    
    
    
    words_imgs = ""
    
    for m in range(len(word_hasheds)):
        
        word_hashed_name = word_hasheds[m]
        words_imgs = words_imgs+"""
        
        <img src="static/words/%s.png"><img src="static/anlamlar/%s.png"><br />
        
        """ % (word_hashed_name, word_hashed_name)
        
        
    html = """
    
    <form action="add_to_mysql" method="post">
    
    %s
  
    %s
  
    <input type="submit" value="Submit" /></form>
    
    %s
    
    """ % (hiddens, words_imgs, img_html)
    
    return html
    
    
    
@app.route("/add_to_mysql", methods=['GET', 'POST'])
def add_to_mysql_():
    
    import  mysql.connector
    
    mydb = mysql.connector.connect(host="localhost", user="**", passwd="**", database="**")
    
    
    mycursor = mydb.cursor()
    
    
    

    
    url_req = str(request.form['url'])  
    md5_url_req = str(request.form['md5_url'])
    adet_req = int(str(request.form['adet']))
    ens_req = str(request.form['ens'])
    trs_req = str(request.form['trs'])
    wordhashes_req = str(request.form['wordhashes'])
    date_req = str(request.form['date'])
    
    sql = "INSERT INTO table_ingilizce (`DATE`, `URL`, `MD5URL`, `WORDHASHES`) VALUES (%s, %s, %s, %s)"
    
    val = (date_req, url_req, md5_url_req, wordhashes_req)
    
    
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    
    
    
    return "check the db"
        
    
    


if __name__ == "__main__":

    app.run(debug=True, threaded=True)
