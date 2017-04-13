from bs4 import BeautifulSoup
import urllib
import csv

def findInfo(row, className):
    return row.find('div', {'class':className}).string.encode('utf-8')

def main():
    # Soupify URL
    pages = ["http://appshopper.com/bestsellers/games/paid/?device=iphone",
            "http://appshopper.com/bestsellers/games/gros/?device=iphone"]
    for url in pages:
        request = urllib.urlopen(url).read()
        soup = BeautifulSoup(request, "html.parser")
        
        # Isolate rows in table
        table = soup.find('div', {'class':'top-chart-table'}).find_all('div', attrs={'class':'row'})
        
        # Write CSV and file
        headers = ['Rank', 'Name', 'Price']
        filename = url.split('/')[5] + "_apps.csv"
        with open(filename, "w") as file:
            w = csv.writer(file)
            w.writerow(headers)
            for row in table[1:]:
                information = [findInfo(row, 'rank'), findInfo(row, 'name'), findInfo(row, 'price')]
                w.writerow(information)
main()