"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
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
