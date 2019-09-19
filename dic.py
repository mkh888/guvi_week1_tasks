lst={1:'a', 2: 'b' , 3: 'c'}
print(lst)
print([number for number, name in lst.items() if name=="a"])

num1 = 1.5
num2 = 6.3
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
