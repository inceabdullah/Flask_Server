import urllib.parse 
import csv
from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_folder='static')


@app.route("/")
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
            csv_icin_satir = csv_icin_satir + urllib.parse.quote(dok_il_adi) + "\n\r"
            
            
            # aynisi degilse yaz
            
            
    return  csv_icin_satir # kac tane var: str(len(ilac_list))
