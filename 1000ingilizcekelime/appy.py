from urllib.parse import quote
import mysql.connector
from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/get10', methods=['GET'])
def get10():
    total = ""
    total_say = 0
    sayi_req = request.args.get('sayi')
    mydb = mysql.connector.connect(host="localhost", user="**", passwd="**", database="**")
    sql_select_Query = "select * from 1KKelime"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        if (int(row[0]) >= int(sayi_req)+1) and int(row[0]) <= int(sayi_req)+10:
            total_say += 1
            total = total+"__word__"+str(total_say)+"="+(str(row[1]))+"&"+"__anlami__"+str(total_say)+"="+(str(row[2]))+"&"
    cursor.close()
    total = total+"geted_get10"
    redirect2 = "/redirect?%s" % (total)
    return redirect(redirect2, code=302)
    
    
@app.route('/redirect')
def redirect_():
    return ""
    