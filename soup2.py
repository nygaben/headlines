import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import pandas as pd
import json 
import codecs
import time
from datetime import date



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

c = Counter(word_count)

print(c)

#top = c.most_common(200)

#df = pd.DataFrame(c, columns =['WORD', 'FREQUENCY'])

#df = pd.DataFrame.from_dict(c, orient='index').reset_index()
#df = df.rename(columns={'index':'WORD', 0:'FREQUENCY'})
#df.sort_values(by=['FREQUENCY'], inplace=True, ascending=False)


#print(df) 

#print(top)


#print(type(dictionaryObject))

#timestr = time.strftime("%Y%m%d-%H%M%S")

#with codecs.open(timestr+ '.json', 'a+', 'utf-8') as fp:
    #fp.write(json.dumps(c, ensure_ascii=False))

