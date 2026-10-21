
sentance = "Python is easy and Python is powerful"
result = {}
word = []

for i in range(0, len(sentance)):
    if sentance[i]!=" ":
        word.append(sentance[i])
    else:
        tem = "".join(word)
        result[tem] = result.get(tem, 0)+1
        word = []
    if i==len(sentance)-1:
        tem = "".join(word)
        result[tem] = result.get(tem, 0)+1
print(result)


