def is_even(no):
    if no % 2==0:
        return True
    else:
        return False

for i in range(101):
    if is_even(i)==True:
        print(i)
