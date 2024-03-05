n = int(input("enter size of fibonacci numbers: "))
lst = [1, 1]
[lst.append(sum(lst[i:])) for i in range(n-2)] # we decreased n because we already has two number which is fibonacci number starts with
print(lst)
