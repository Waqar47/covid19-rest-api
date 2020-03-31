from bs4 import BeautifulSoup
import requests


def get_json_covid():
    #response = requests.get('https://www.worldometers.info/coronavirus/')
    
    
    soup = BeautifulSoup(open('out.html',encoding="utf-8"))
    
    
    table = soup.find_all(id='main_table_countries_today')[0]
    rows = table.find_all('tr')
    
    
    covid_records = []
    
    for i in range(1,len(rows)):
        
        td_s = rows[i].find_all('td')
        
        if(len(td_s) == 0):
            continue
        
        #for td in td_s:
            #print(td.text + ' ',end='')
        
        td = td_s
        
        covid_tr = {
        
        'country':td[0].text.strip(),
        'total_cases':td[1].text.strip(),
        'new_cases':td[2].text.strip(),
        'total_deaths':td[3].text.strip(),
        'new_deaths':td[4].text.strip(),
        'total_recovered':td[5].text.strip(),
        'active_cases':td[6].text.strip(),
        'serious_critical':td[7].text.strip(),
        'total_cases_per_million':td[8].text.strip(),
        'total_deaths_per_million':td[9].text.strip(),
        'reported_first_case':td[10].text.strip()
        
        }
        
        covid_records.append(covid_tr)
#        print(covid_tr)   
    #html = soup.prettify("utf-8")
    return covid_records
    #with open('out.html','wb') as file:
        #file.write(html)




