from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
from datetime import timedelta, date, datetime
from openpyxl.workbook import Workbook

#Download and parse the html file
start_url = 'https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm'

#Download teh HTML from start_url
downloaded_html = requests.get(start_url)

#parse the HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.content, "html.parser") #.encode('utf-8', 'ignore')

table = soup.select('table')[5]

#select the th and tr tags
table_head = table.select('tr th')
print(table_head)

#convert element to text
print('---------')
for element in table_head:
    print(element.text)

regex = re.compile("_\[\w\]")

#use for loop to iterate to the values and append to a list
table_columns = []
for element in table_head:
    column_label = element.get_text(separator=' ', strip=True)
    column_label = column_label.replace(" ", "_")
    column_label = regex.sub("", column_label)
    table_columns.append(column_label)
    print(column_label)

print('---------')
print(table_columns)

#select the tr tags
table_rows = table.select('tr')

#use for loop to iterate to the values in each row and append to a list
table_data = []
for index, element in enumerate(table_rows):
    if index > 0:
        row_list = []
        values = element.select('td')

        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)


#convert to a dataframe
df = pd.DataFrame(table_data, columns=table_columns, index=None)

#function to create date time object for weekdays from start date to end date
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(1997,1,6)
end_dt = date(2021,2,19)

date=[]
weekdays = [6,7]
for dt in daterange(start_dt, end_dt):
    if dt.isoweekday() not in weekdays:
        date.append(dt.strftime("%Y-%m-%d"))


#drop columns not needed, convert list to series and merge with dataframe
df = df.drop(['Week_Of'], axis=1)
df = pd.concat([df, df.stack().reset_index(drop=True).rename('Price')], axis=1)
date_series = pd.Series(date).rename('Date')
df_comb = pd.concat([df, date_series], axis=1)
df_comb = df_comb.drop(['Mon', 'Tue', 'Wed', 'Thu', 'Fri'], axis=1)


#save as csv file
#df_comb.to_csv("output.csv", index=False)

df = pd.read_csv('output.csv')

df.dropna()
#df_new = pd.concat([new_df, date_series], axis=1)

df_comb.to_csv("output2.csv", index=False)
