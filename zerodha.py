#geting content from the bse site
import urllib.request
from urllib.request import urlopen
html = urlopen("https://www.bseindia.com/markets/equity/EQReports/Equitydebcopy.aspx")
content = html.read()

#converion of byte object to string
string = content.decode("utf-8")

#identification of the equity file through the anchor id and class on the source code of bse site
pos = string.index('<a id="btnhylZip" class="tablebluelink" href="')

#start position of slicing after occurance of anchor id
start_pos = pos+46

#end position of slicing at first occurance of target after start position
end_pos = string.find('" target="_self">',pos)

#URL of the equity file
file = string[start_pos:end_pos]

#splitting filename from file
file_name = file.split('/')[-1]

#downloading file 
testfile = urllib.request.URLopener()
testfile.retrieve(file, file_name)

#extracting the downloaded file
import zipfile
zip_ref = zipfile.ZipFile('C:\\Users\\Prafful Mishra\\AppData\\Local\\Programs\\Python\\Python36-32\\'+file_name,'r')
zip_ref.extractall('C:\\Users\\Prafful Mishra\\AppData\\Local\\Programs\\Python\\Python36-32')
zip_ref.close()

import csv
import redis

#redis connection
r = redis.Redis(host='localhost',port=6379,db=0)

#opening the csv file
with open(file_name, 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        r.set(row['SC_NAME'],{'code': row['SC_CODE'],'name': row['SC_NAME'],'open' :row['OPEN'], 'high' : row['HIGH'],'low' : row['LOW'],'close' : row['CLOSE']})
csvFile.close()

