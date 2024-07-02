"""Cats With Hats Problem"""
cats = []
for i in range(100):
    cats.append((f"cat #{i+1}", "off"))
cats = dict(cats)

for i in range(1, 101):
    for j in range(i, 100, i):
        if cats[f"cat #{j}"] == 'off':
            cats[f"cat #{j}"] = 'on'
        else:
            cats[f"cat #{j}"] = 'off'

for i in range(1, 100):
    if cats[f"cat #{i}"] == "on":
        print(f"cat #{i}")
print("have hats on.")
