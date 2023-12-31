from bs4 import BeautifulSoup
import re
import json


#Functions

def desciption(link):
    link1 = str(link)
    if "advance" in link1:
      dict = {'description':'JUDGE_MISCELLANEOUS_ADVANCE'}
    elif "M_J_1" in link1:
      dict = {'description':'JUDGE_MISCELLANEOUS_MAIN'}
    elif "M_J_2" in link1:
        dict = {'description':'JUDGE_MISCELLANEOUS_SUPPL'}
    elif "F_J_1" in link1:
        dict = {'description':'JUDGE_REGULAR_MAIN'}
    elif "F_J_2" in link1:
        dict = {'description':'JUDGE_REGULAR_SUPPL'}
    elif "M_C_1" in link1:
        dict = {'description': 'CHAMBER_MAIN'}
    elif "M_C_2" in link1:
        dict = {'description': 'CHAMBER_SUPPL'}
    elif "M_S_1" in link1:
        dict = {'description': 'SINGLE JUDGE_MAIN'}
    elif "M_S_2" in link1:
        dict = {'description': 'SINGLE JUDGE_SUPPL'}
    elif "M_CC_1" in link1:
        dict = {'description': 'REVIEW & CURATIVE_MAIN'}
    elif "M_CC_2" in link1:
        dict = {'description': 'REVIEW & CURATIVE_SUPPL'}
    elif "M_R_1" in link1:
        dict = {'description': 'REGISTRAR_MAIN'}
    elif "M_R_2" in link1:
        dict = {'description': 'REGISTRAR_SUPPL'}
    return dict
  

def Date_of_Hearing(link):
    pattern = r"\d...[-]\d+[-]\d+"
    match = re.findall(pattern, link)
    date = None
    if len(match) > 0:
        date = str(match[0])
    dict = {'Date_of_Hearing': date}
    return dict


#main code starts

with open("Supreme_court_causelist.html", "r", encoding="utf8") as f:
    html_doc = f.read()
    f.close()
    
soup = BeautifulSoup(html_doc, "html.parser")

t1 = soup.find("div", {'align':'center'})
t2 = t1.find("table", {'class':'mobview'})
t3 = t2.find_all("tr")
#print(t3)
Links = []

for link in t2.find_all('a'):
    address = "https://main.sci.gov.in"
    data = str(link.get('href'))
    data1 = address + data
    Links.append(data1)
    #print(data1)

'''
dict ={
    'date_of_hearing':''
    'pdf_link': ''
    'description': ''
}
'''

Final_list = []

for link in Links:
    dict1 = Date_of_Hearing(link)
    dict2 = desciption(link)
    dict3 = {'Pdf_link': link}
    dict4 = dict1|dict2
    dict5 = dict4|dict3
    Final_list.append(dict5)


print(Final_list)

with open("Final_list.json", "w") as final:
 final.write(json.dumps(Final_list, indent=2))

final.close()


