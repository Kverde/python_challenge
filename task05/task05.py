import pickle
import urllib.request

url = r'http://www.pythonchallenge.com/pc/def/banner.p'

response = urllib.request.urlopen(url)
banner = response.read()

file_name = r'.\banner.p'

with open(file_name, 'wb') as f:
    f.write(banner)

with open(file_name, 'rb') as f:
    obj = pickle.load(f)

for line in obj:
    for item in line:
        print(item[0] * item[1], end='')
    print()

# channel