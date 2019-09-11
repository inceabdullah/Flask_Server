import mysql.connector

def exe():

    selfcon = mysql.connector.connect(host="localhost", user = "****", passwd="***", database = "****")
    
    selfcur = selfcon.cursor()
    
    sql = """SELECT * FROM wp_posts"""
    
    selfcur.execute(sql)
    
    
    rows = selfcur.fetchall()
    
    for row in rows:
        
        raw_id = row[0]
        raw_row = row[4]
        replaced_row = raw_row.replace('src="http://', 'src="https://')
        
        sql = """UPDATE wp_posts SET `%s` = '%s' WHERE `%s` = %d""" % ("post_content", replaced_row, "ID", raw_id)
        
        selfcur.execute(sql)
        selfcon.commit() # shoul be written. otherwise, it won't update.
        
        #print(row[4], file=open("frameler-yaz.txt", "a"))
        #print(sql)
        
        
