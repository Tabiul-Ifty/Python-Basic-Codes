# define a list
number = [1, 5, 7, 4, 6, 8]

# defining the push function
def push():
    value = int(input("value to push:"))
    number.append(value)
    print(number)

# defining the pop function
def pop():
    number.pop()
    print(number)

# defining the exit function
def exit():
    print(number)

# to continue infinite time
while True:
    # to command what to do
    print('''
1 for push
2 for pop
3 for exit''')

# taking input as command
    app = int(input(">"))
# 1 to push
    if app == 1:
        push()
# 2 to pop
    elif app == 2:
        pop()
# 3 to exit
    elif app == 3:
        exit()
#to break the loop
        break
