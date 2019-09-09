# encoding=utf8
import sys


import csv
import urllib.parse # for il_adi to encoded url urllib.quote(str)
#roww = "sasasa"            
from flask import Flask, request, jsonify
app = Flask(__name__) 

# csv to mySQL for wordpresss veteriner-ilaclari

@app.route("/csv_to_wp_veteriner_ilaclari")
def csv_to_wp_veteriner_ilaclari():
    csv_icin_satir = ""
    with open('/home/wwwoakzg/python-vet_ilac/database/ilacSheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ilac_list = []
        for row in csv_reader:
            line_count += 1
            dok_il_adi = row[1]
            dok_yerli_yab = row[3]
            dok_firma = row[2]
            dok_em = row[9]
            dok_uyg = row[11]
            dok_turler = row[12]
            dok_takdim = row[8]
            
            
            
            # aynisi degilse yaz
            
            if dok_il_adi not in ilac_list:
                
                ilac_list.append(dok_il_adi)
                csv_html = """<p>&nbsp;&nbsp;</p><table class=""tablo"" border=""0"" cellspacing=""0" cellpadding=""0"><tbody><tr class=""even""><td weigh=""50%%""><strong>%s Yerli mi İthal mi?<br /></strong></td><td weigh=""50%%"">%s</td></tr><tr><td weigh=""50%%""><strong>%s Nasıl Kullanılır?<br /></strong></td><td weigh=""50%%"">%s</td></tr><tr class=""even""><td weigh=""50%%""><strong>%s Hangi Hayvanlarda Kullanılır?<br /></strong></td><td weigh=""50%%"">%s</td></tr><tr><td weigh=""50%%""><strong>%s Hangi Firmanın?<br /></strong></td><td weigh=""50%%"">%s</td></tr><tr class=""even""><td weigh=""50%%""><strong>%s İ&ccedil;inde Ne Var? Bileşimi Nedir?</strong></td><td weigh=""50%%"">%s</td></tr><tr><td weigh=""50%%""><strong>%s Ka&ccedil; mLlik &Uuml;retilir?<br /></strong></td><td weigh=""50%%"">%s</td></tr></tbody></table><p>&nbsp;</p>""" % (dok_il_adi, dok_yerli_yab, dok_il_adi, dok_uyg, dok_il_adi, dok_turler, dok_il_adi, dok_firma, dok_il_adi, dok_em, dok_il_adi, dok_takdim)
                csv_icin_satir = csv_icin_satir+"\"\";\"1\";\"2019-05-01 09:07:40\";\"2019-05-01 09:07:40\";\"%s\";\"%s\";\"%s\";\"publish\";\"open\";\"open\";;\"%s\";;;\"2019-05-01 09:07:40\";\"2019-05-01 09:07:40\";;\"0\";;\"0\";\"post\";;\"0\"\r\n" % (csv_html, dok_il_adi, dok_em, 100+line_count)
                            
                if row[1] == row[1]:
                    dok_il_adi = row[1]
                    dok_yerli_yab = row[3]
                    dok_firma = row[2]
                    dok_em = row[9]
                    dok_uyg = row[11]
                    dok_turler = row[12]    
                    
                    
    return  csv_icin_satir # kac tane var: str(len(ilac_list))



# csv to mySQL for wordpresss noted that: ayni olanlari tek yaz

@app.route("/csv_to_wp")
def csv_to_wp():
    csv_icin_satir = ""
    with open('/home/wwwoakzg/python-vet_ilac/database/ilacSheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ilac_list = []
        for row in csv_reader:
            line_count += 1
            dok_il_adi = row[1]
            dok_yerli_yab = row[3]
            dok_firma = row[2]
            dok_em = row[9]
            dok_uyg = row[11]
            dok_turler = row[12]
            
            
            
            # aynisi degilse yaz
            
            if dok_il_adi not in ilac_list:
                
                ilac_list.append(dok_il_adi)            
                csv_icin_satir = csv_icin_satir+"\"\";\"1\";\"2019-05-01 09:07:40\";\"2019-05-01 09:07:40\";\"<iframe name=\"\"I1\"\" id=\"\"if1\"\" width=\"\"100%%\"\"  height=\"\"100%%\"\" style=\"\"visibility:visible\"\"  src=\"\"http://python.vet-ilac.ozguruygulama.com/get_ilac?ilac=%s\"\"></iframe>\";\"%s\";\"%s\";\"publish\";\"open\";\"open\";;\"%s\";;;\"2019-05-01 09:07:40\";\"2019-05-01 09:07:40\";;\"0\";;\"0\";\"post\";;\"0\"\r\n" % (urllib.parse.quote(dok_il_adi), dok_il_adi, dok_em, 100+line_count)
                            
                if row[1] == row[1]:
                    dok_il_adi = row[1]
                    dok_yerli_yab = row[3]
                    dok_firma = row[2]
                    dok_em = row[9]
                    dok_uyg = row[11]
                    dok_turler = row[12]    
                    
                    
    return  csv_icin_satir # kac tane var: str(len(ilac_list))


# statics index.html

f = open('statics/index.html', 'r')
stat_read = f.read()
f.close()

# statics whenenter.html

f = open('statics/whenenter.html', 'r')
stat_read_whenenter = f.read()
f.close()

@app.route("/")
def greeting():
    return ""

@app.route("/index")
def index():
    return stat_read

@app.route("/whenenter")
def whenenter():
    return stat_read_whenenter

#not_submitted_yet page

@app.route("/not_submitted_yet")
def not_submitted_yet():
    
    # statics whenenter.html
    
    f = open('statics/not_submitted_yet.html', 'r')
    stat_read_not_submitted_yet = f.read()
    f.close()
    return stat_read_not_submitted_yet




@app.route("/get_ilac",  methods=['GET'])
def get_ilac():
    dok_il_adi = ""
    dok_yerli_yab = ""
    dok_firma = ""
    dok_em = ""
    dok_uyg = ""
    dok_turler = ""  
    return_son = ""
    img_sig_int = 0
    img_at_int = 0
    img_kedi_int = 0
    img_kop_int = 0    
    img_tot_names = ["cow","at","cat","dog"]
    img_tot_list = [img_sig_int, img_at_int, img_kedi_int, img_kop_int] 
    ilac_req = str(request.args.get('ilac'))
    with open('database/ilacSheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ilac_list = []
        for row in csv_reader:
            
            if ilac_req == row[1]:
                dok_il_adi = row[1]
                dok_yerli_yab = row[3]
                dok_firma = row[2]
                dok_em = row[9]
                dok_uyg = row[11]
                dok_turler = row[12]

    
    if len(dok_il_adi) > 0:
        return_son = return_son + "İlaç adı:<b>" + dok_il_adi + "</b>\r\n<br />"
        return_son = return_son + "Yerli/İthal:<b>" + dok_yerli_yab + "</b>\r\n<br />"
        return_son = return_son + "Firma:<b>" + dok_firma + "</b>\r\n<br />"
        return_son = return_son + "Etken Madde:<b>" + dok_em + "</b>\r\n<br />"
        return_son = return_son + "Uygulama Şekli:<b>" + dok_uyg + "</b>\r\n<br />"
        return_son = return_son + "Kullanılan Türler:<b>" + dok_turler + "</b>\r\n<br />"
        img_sig_int = 0
        img_at_int = 0
        img_kedi_int = 0
        img_kop_int = 0
        # list is below
        img_tot_names = ["cow","at","cat","dog"]
        if dok_turler.find("Sığır") > -1:
            img_sig_int = 1
            
        if dok_turler.find("At") > -1:
            img_at_int = 1
        
        if dok_turler.find("Kedi") > -1:
            img_kedi_int = 1
            
        if dok_turler.find("Köpek") > -1:
            img_kop_int = 1
          
    img_tot_list = [img_sig_int, img_at_int, img_kedi_int, img_kop_int]         
    # add img src for from img_tot_list
    i_img_line = ""
    for i_img in range(len(img_tot_list)):
        i_img_line = i_img_line + '<img src="/static/images/%s-%d.png">' % (img_tot_names[i_img], img_tot_list[i_img]) 
        
    back_ground_html = ''' <html>
<body background="/static/images/g13.png">'''    
        
    return back_ground_html+return_son+"<br/>"+i_img_line

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    

    
    roww = ""
    
    ilac_say=0
    
    with open('database/ilacSheet1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        ilac_list = []
        for row in csv_reader:
            if line_count == 0:            
                
                line_count += 1
            else:
                #find if there is stg in ilac(1-csv)
                
                
                if row[1].upper().find(str(search).upper()) > -1 or row[9].upper().find(str(search).upper()) > -1:     
                    ilac_list.append(ilac_list)
                    
                    ilac_list[ilac_say] = row[1]
                    ilac_say += 1
                    line_count += 1
       
    print(ilac_list    )
    
    #query = db_session.query(Movie.title).filter(Movie.title.like('%' + str(search) + '%'))
    results = ilac_list
    
    return jsonify(matching_results=results)

if __name__ == "__main__":
    app.run(host='127.0.0.1')
