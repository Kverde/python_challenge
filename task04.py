import urllib.request
import re

base_url = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

# fist = 12345
# second = 25357
# trhird = 63579
# resut = peak.html

cur_ident = '63579'
for i in range(400):
    url = base_url + cur_ident
    print(url)

    response = urllib.request.urlopen(url)
    text = str(response.read())
    print(text)

    cur_ident = re.findall(r'\d+', text)
    if len(cur_ident) == 0:
        break
    cur_ident = cur_ident[0]

# 16044
# b'Yes. Divide by two and keep going.'
# 16044 / 2 = 8022