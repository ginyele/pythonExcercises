# 1. Write a program that prints your name 100 times.
# name = input("Enter your name ")
# for i in range(100):
#     print(name)


'''
2. Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
option end='' into the print function to fill the screen horizontally.]
'''
# name = input("Enter your name ")
# for i in range(100):
#     print(name, end=' ')


'''
3. Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
output should look like the output below.
1 Your name
2 Your name
3 Your name
4 Your name
...
100 Your name
'''

name = input("Enter your name: ")
for i in range(1, 101):
    print(i, name)