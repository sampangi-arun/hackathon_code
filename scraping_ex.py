import requests
from bs4 import BeautifulSoup
import pandas as pd



if __name__=='__main__':
    response = requests.get('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(response.content)
    tr_section = soup.findAll('tr')
    df = None
    for idx, row in enumerate(tr_section):
        temp=[]
        if df is None:
            for row_values in row.findAll('th'):
                temp.append(row_values.text)
                #print(temp)
            df = pd.DataFrame(columns=temp)
        else:
            for row_values in row.findAll('td'):
                temp.append(row_values.text.strip())
            if(len(temp) < 6):
                temp.insert(0, idx)
            df.loc[idx] = temp
    df.to_csv('Corona_stats.csv', index=False)
