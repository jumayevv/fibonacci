# fibonacci
lst = [1,1]
n = 5
for i in range(n):
    lst.append(sum(lst[i:]))
print(lst)