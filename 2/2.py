import matplotlib.pyplot as plt
import re

with open("2/file.txt", "r") as f:
    text = f.read()
    
def wordCount(text):
    words = re.sub(r'[^A-Za-z ]', '', text).split(" ")
    freq = dict()
    for word in words:
        if (word in freq):
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq

data = wordCount(text)
plt.bar(list(data.keys()),  list(data.values()))

plt.xlabel('Слова')
plt.ylabel('клкст')
plt.title('Гістограма')
plt.xticks(rotation=90)

plt.show()
