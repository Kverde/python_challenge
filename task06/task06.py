import re
import os
import zipfile


dir_name = r'.\channel'
file_templ = os.path.join(dir_name, '{}.txt')
zip_file_name = '.\channel.zip'


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def cut_ident(string):
    ident = re.findall(r'\d+', string)
    if len(ident) == 0:
        return None
    else:
        return ident[0]



zip = zipfile.ZipFile(zip_file_name)

file_id = '90052'

comments = b''

while file_id is not None:
    text = read_file(file_templ.format(file_id))
    comm = zip.getinfo('{}.txt'.format(file_id)).comment
    comments += comm

    if not 'Next nothing is ' in text:
        print(text)
    file_id = cut_ident(text)

print(comments)
print(comments.decode('utf-8'))

zip.close()

# HOCKEY
# OXYGEY
# oxygen



