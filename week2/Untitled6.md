
求100以内的素数


```python
prime=[1,2]
for i in range(3,100):
    if i % 2 == 0:
        continue
    else:
        for n in range(2,i//2+1):
            if i % n == 0:
                break
        else:
            prime.append(i)
print(prime)
```

    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

