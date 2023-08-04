import sqlite3
import json

conn = sqlite3.connect('pdf_Links_with_Description.db')

cur = conn.cursor()


Final_list_json = json.load(open('Final_list.json'))


cur.execute("""CREATE TABLE IF NOT EXISTS pdf_links(
    Date_of_hearing DATATYPE,
    description DATATYPE,
    pdf_link DATATYPE
)""")

for i in Final_list_json:
    #print(i)
    cur.execute("INSERT INTO pdf_links VALUES(?,?,?)", (i['Date_of_Hearing'], i["description"], i['Pdf_link']))

cur.execute("SELECT * FROM pdf_links")
print(cur.fetchall())
conn.commit()
conn.close()

