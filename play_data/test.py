from collections import Counter
lst = [1,2,2,2,3,3,3,4,4]
temp = Counter(lst).most_common()
if temp[0][1] == temp[1][1]:
    print(-1)
else:
    print(temp[0][0])