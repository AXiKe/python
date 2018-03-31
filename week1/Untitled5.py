
# coding: utf-8

# 打印一个边长为n的正方形

# In[22]:


a = int(input(">>>"))
for j in range(a):
    for i in range(a):
        print("*",end=" ")
    print("")


# 求100以内所有奇数的和

# In[28]:


sum = 0
for i in range(100):
    if i%2:
        sum += i
else:
    print(sum)
# 计算次数更多


# In[27]:


sum = 0
for i in range(1,100,2):
    sum += i
else:
    print(sum)
# 计算次数更少


# 判断学生成绩，成绩等级A~E。其中，90分以上为A,80~89分为B,70~79分为C,60~69分为D,60分以下为E

# In[33]:


a = int(input(">>>"))
if a < 60:
    print("E")
elif a < 70:
    print("D")
elif a < 80:
    print("C")
elif a < 90:
    print("B")
else:
    print("A")


# 求1到5阶乘之和

# In[43]:


j = 1
sum = 0
while j < 6:
    c = 1
    for i in range(1,j+1):
        c *= i
    sum += c
    j += 1
print(sum)


# In[45]:


nums = 1
x = 0
for n in range(1,6):
    nums *= n
    x += nums
print(x)


# 给一个数，判断它是否是素数（质数）
#     质数：一个大于1的自然数只能被1和它本身整除

# In[53]:


a = int(input(">>>"))
for i in range(2,a):
    if a%i == 0:
        print("no prime")
        break
else:
    print("is prime")

