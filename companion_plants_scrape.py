from bs4 import BeautifulSoup
import requests
import re
import json
import time

all_my_data = []

url = "https://en.wikipedia.org/wiki/List_of_companion_plants"

results_page = requests.get(url)
results_page_html = results_page.text
soup = BeautifulSoup(results_page_html, "html.parser")
tables = soup.find_all('tbody')
time.sleep(10)

column_map = {
	1: "Common name",
	2: "Scientific name",
	3: "Helps",
	4: "Helped by",
	5: "Attracts",
	6: "-Repels/+distracts",
	7: "OP",
	8: "Avoid",
	9: "Comments",
}

data = soup.find_all('tr')
vegetables = data[1:45]
fruit = data[46:56]
herbs = data[57:90]
flowers = data[91:112]
other = data [113:117]


for veg in vegetables:

	data = veg.find_all('td')

	counter = 0

	print('--------------')

	for row in data:
		my_data = {}
		counter = counter + 1 
		labels = column_map[counter]
		table_rows = row.text
		my_data[labels] = table_rows
		# x = row.text
		print(my_data)


