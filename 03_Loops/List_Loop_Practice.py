Q1 Create a list of numbers    
Print:
first element
last element
list_num=[10, 20, 30, 40, 50]
print(list_num[0])
print(list_num[-1])


Q2 Add:
25 at the end
2 at the beginning
list_num=[5, 10, 15, 20]
list_num.insert(0 , 2)
list_num.append( 25 )
print(list_num)


Q3 Modify:
change 3 → 99
list_num = [1, 2, 3, 4, 5]
list_num[2] = 99
print(list_num)


Level 2 – Loop + Logic
Q4 Print all elements using loop
lst = [1, 2, 3, 4, 5]
for number in lst:
    print(number)
  
  
Q5 Print only even numbers from:
lst = [10, 13, 18, 21, 24]
for i in lst:
    if i % 2 == 0:
        print(i)


Q6 Find sum of all elements
lst = [10, 13, 18, 21, 24]
total=sum(lst)
print(total)


Q7 Adding a list
number = [10, 20, 30, 40]
total=0
for i in number:
    total += i
print(total)


Q8 Find SUM of only EVEN numbers
lst = [10, 13, 18, 21, 24]
total=0
for i in lst:
    if i % 2 == 0:
        total += i
print(total)


Q9 Count how many EVEN numbers are in the list
lst = [10, 13, 18, 21, 24]
count = 0
for i in lst:
    if i % 2 == 0:
        count += 1
print(count)


Q10 Find the LARGEST number in a list (without using max())
lst = [10, 55, 23, 89, 45]


max_num=lst[0]
for i in lst:
    if i > max_num:
        max_num = i
print(max_num)
