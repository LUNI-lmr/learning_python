# how to use loops in a dictionary:
info = {"name": "LUNI", "followers": 5000, "category": "dev"}

for c, v in info.items(): # "c" stands for "chave" (key) and "v" stands for valor (value).

    print (f"{c}: {v}")

for v in info.values(): # print only the values

    print (f"{v}")

for c in info.keys(): # print only the keys

    print(f"{c}")
