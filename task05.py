import pickle

with open(r'.\task05.txt', 'rb') as f:
    data_new = pickle.load(f)

print(data_new)
