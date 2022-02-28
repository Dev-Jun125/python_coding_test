from typing import Counter

a = input()
A = a.upper()
A_count_values = Counter(A).values()
print(A.count('A'))

count = 0
for i in A_count_values:
    if i == max(A_count_values):
        count = count + 1
if count > 1:
    print('?')
else:
    print(Counter(A).most_common()[0][0])