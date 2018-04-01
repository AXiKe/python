
打印九九乘法表


```python
for i in range(1,10):
    for j in range(0+i,10):
        print(str(i)+'X'+str(j)+'='+str(i*j),end='\t')
    print()
```

    1X1=1	1X2=2	1X3=3	1X4=4	1X5=5	1X6=6	1X7=7	1X8=8	1X9=9	
    2X2=4	2X3=6	2X4=8	2X5=10	2X6=12	2X7=14	2X8=16	2X9=18	
    3X3=9	3X4=12	3X5=15	3X6=18	3X7=21	3X8=24	3X9=27	
    4X4=16	4X5=20	4X6=24	4X7=28	4X8=32	4X9=36	
    5X5=25	5X6=30	5X7=35	5X8=40	5X9=45	
    6X6=36	6X7=42	6X8=48	6X9=54	
    7X7=49	7X8=56	7X9=63	
    8X8=64	8X9=72	
    9X9=81	



```python
for i in range(1,10):
    print((i-1)*("        "),end='')
    for j in range(0+i,10):
        print(str(i)+'X'+str(j)+'='+str(i*j),end='\t')
    print()
```

    1X1=1	1X2=2	1X3=3	1X4=4	1X5=5	1X6=6	1X7=7	1X8=8	1X9=9	
            2X2=4	2X3=6	2X4=8	2X5=10	2X6=12	2X7=14	2X8=16	2X9=18	
                    3X3=9	3X4=12	3X5=15	3X6=18	3X7=21	3X8=24	3X9=27	
                            4X4=16	4X5=20	4X6=24	4X7=28	4X8=32	4X9=36	
                                    5X5=25	5X6=30	5X7=35	5X8=40	5X9=45	
                                            6X6=36	6X7=42	6X8=48	6X9=54	
                                                    7X7=49	7X8=56	7X9=63	
                                                            8X8=64	8X9=72	
                                                                    9X9=81	



```python
for i in range(1,10):
    line =''
    for j in range(1,10):
        if i > j:
            line ='{}   {}   {:<3}'.format(' ',' ',' ')
        else:
            line ='{} * {} = {:<3}'.format(i,j,i*j)
        print(line,end=' ')
    print()
```

    1 * 1 = 1   1 * 2 = 2   1 * 3 = 3   1 * 4 = 4   1 * 5 = 5   1 * 6 = 6   1 * 7 = 7   1 * 8 = 8   1 * 9 = 9   
                2 * 2 = 4   2 * 3 = 6   2 * 4 = 8   2 * 5 = 10  2 * 6 = 12  2 * 7 = 14  2 * 8 = 16  2 * 9 = 18  
                            3 * 3 = 9   3 * 4 = 12  3 * 5 = 15  3 * 6 = 18  3 * 7 = 21  3 * 8 = 24  3 * 9 = 27  
                                        4 * 4 = 16  4 * 5 = 20  4 * 6 = 24  4 * 7 = 28  4 * 8 = 32  4 * 9 = 36  
                                                    5 * 5 = 25  5 * 6 = 30  5 * 7 = 35  5 * 8 = 40  5 * 9 = 45  
                                                                6 * 6 = 36  6 * 7 = 42  6 * 8 = 48  6 * 9 = 54  
                                                                            7 * 7 = 49  7 * 8 = 56  7 * 9 = 63  
                                                                                        8 * 8 = 64  8 * 9 = 72  
                                                                                                    9 * 9 = 81  


打印如下菱形


```python
n=3
w=5
j=1
while w <6:
    for i in range(1,8,2):
        print((" ")*n,end='')
        print("*"*i)
        n -=1
    w +=1
else:
    for i in range(5,0,-2):
        print((" ")*j,end='')
        print("*"*i)
        j +=1
```

       *
      ***
     *****
    *******
     *****
      ***
       *



```python
for i in range(-3,4):
    if i<0:
        prespace = -i
    else:
        presapce = i
    print(' '*prespace+'*'*(7-prespace*2))
```

       *
      ***
     *****
     *****
     *****
     *****
     *****



```python
n=3
w=5
j=3
while w <6:
    for i in range(1,5):
        print((" ")*n,end='')
        print("*"*i)
        n -=1
    w +=1
else:
    for i in range(5,0,-2):
        print((" ")*3,end='')
        print("*"*i)
```

       *
      **
     ***
    ****
       *****
       ***
       *



```python
j = "*"
for i in range(-3,4):
    if i==0:
        print(j*7)
    print(" "*(-i) + j*(i+4)) if i<0 else print(3*" " + j*(3-i))
```

       *
      **
     ***
    *******
       ***
       **
       *
       


斐波那契数列，100以内


```python
i = 1
j = 1
while i < 100:
    i, j = j, i+j
    print(i,end=" ")
```

    1 2 3 5 8 13 21 34 55 89 144 


```python
i = 1
j = 1
while i < 100:
    print(i)
    i, j = j, i+j
```

    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89


求斐波那契数列第101项


```python
i = 1
j = 1
count = 0
while True:
    i, j = j,i+j
    count += 1
    if count == 100:
        break
print(i)
```

    573147844013817084101


求10万内的所有素数


```python
for i in range(1,100,2):
    for j in range(2,i-1):
        if i%j == 0:
            break
    else:
        print(i,end=" ")
```

    1 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 


```python
import datetime
start = datetime.datetime.now()
print(start)
```

    2018-04-01 16:19:01.629587



```python
import datetime
datetime.datetime.now()
```




    datetime.datetime(2018, 4, 1, 16, 19, 18, 437480)



解决猴子吃桃问题


```python
num=1
for i in range(2,11):
    num=  (num + 1)*2
print(num)
```

    1534



```python

```




    datetime.datetime(2018, 4, 1, 16, 19, 18, 437480)


