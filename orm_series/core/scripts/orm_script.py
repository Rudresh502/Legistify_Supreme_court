from core.models import Final_list
import json
from django.db import connection

Final_list_json = json.load(open('Final_list.json'))

def run():
    for i in Final_list_json:
     Final_list.objects.create(
         date_of_hearing = i['Date_of_Hearing'],
         description = i['description'],
         pdf_link = i['Pdf_link']
     )
    print(connection.queries)
