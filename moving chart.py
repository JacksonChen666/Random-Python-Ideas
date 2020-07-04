import json

import matplotlib.pyplot as plt

with open("covid-19_cases.json", encoding='utf-8') as f:
    data = json.load(f)

processed_data = {}
print(data)
print(processed_data)

for item in data:
    processed_data[int("".join(item["Date"].split("-")[:2]))
    ] = item["Cases"]
x_data = []
y_data = []

cnt = 0
temp = 0
for i in range(0, 200000):
    if processed_data.get(i) is not None and processed_data.get(i) != ' ':
        cnt += 1
        temp += processed_data.get(i)
        if cnt >= 12:
            x_data.append(i)
            y_data.append(processed_data.get(i))
            cnt = 0
            temp = 0

print(x_data)
print(y_data)
plt.ion()
index_list = range(len(x_data))
for i in index_list:
    plt.clf()
    plt.plot(index_list[:i + 1], y_data[:i + 1])
    plt.pause(0.01)

plt.ioff()
plt.show()
