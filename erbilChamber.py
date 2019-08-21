import requests
import bs4
import urllib.parse
import csv


preURL = "https://www.erbilchamber.org"
csvFile = open('ErbilChamber.csv', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['ManagingDirector','CompanyActivity','RegistrationNumber','DateOfRegistration','MobileNumber','Address','NameOfShareholders'])
try:
    for i in range(0, 8620, 20):
        page = requests.get("http://erbilchamber.org/en/companies.html?start="+str(i))
        soup = bs4.BeautifulSoup(page.content, 'lxml')
        for companiesLink in soup.find_all('h3', class_="catItemTitle"):
            companiesURL = preURL + urllib.parse.quote(companiesLink.a['href'])

            companiesPage = requests.get(companiesURL)
            companiesSoup = bs4.BeautifulSoup(companiesPage.content, 'lxml')
            csvArray = ['','','','','','','']
            j = 0
            for companiesInfo in companiesSoup.find_all('span', class_="itemExtraFieldsValue"):
                print (companiesInfo.text)
                csvArray[j] = companiesInfo.text
                j += 1
            csvWriter.writerow(csvArray)
except:        
    print(i)
csvFile.close()