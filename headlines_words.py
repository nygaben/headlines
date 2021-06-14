import requests
from bs4 import BeautifulSoup
import pandas as pd
import json 

blank = []
new_items = []

r = requests.get("http://telex.hu")

soup = BeautifulSoup(r.content, "lxml")
ps = soup.find_all("a", class_="cl-title")
#print(soup)
for p in ps:
	a = p.get_text().strip()
	blank.append(a)

#print(blank)

for words in blank:
	new_items.extend(words.split())

#print(new_items)


word_count = {}
 
#print(new_items)
for its in new_items:
	#print(its)
	#if 'a' in its:
		#continue
	if its in word_count:
		word_count[its] += 1
	else:
		word_count[its] = 1

#print(word_count)

keys_to_remove = [
"egy", "A", "és", "nem", "hogy", "egyik", "még",
'–', "Az", "meg", "is", "mert", "mindig", "kell",
"most", "történt", "Egy", "első", "után", #"elleni",
"fel", "már", "utáni", "ember", "Nem", "jó", "ki",
"neki", "ne", "de", "be", "mind", "volt", "így",
"előtti", "a", "az", "jobb", "szerint", "csak", "miatt",
"kis", "szóló"
]


for key in keys_to_remove:
	word_count.pop(key, None)

#print(word_count)


df = pd.DataFrame.from_dict(word_count, orient='index').reset_index()
df = df.rename(columns={'index':'WORD', 0:'FREQUENCY'})
df.sort_values(by=['FREQUENCY'], inplace=True, ascending=False)


#print(df) 



with open('telexwords.json', "w") as file_write:
	json.dump(word_count, file_write)

with open('telexwords.json') as file_object:
        last_scrape = json.load(file_object)
#print(last_scrape)

# ALL_SCRAPE : az összes, frissített adat megy ide

all_scrape = {
	
}

for k, v in last_scrape.items():
    if k not in last_scrape.items():
        all_scrape[k] = 0
    all_scrape[k] += v

#print(all_scrape)

#with open("all.json", "w") as outfile: 
    #json.dump(alltime, outfile)