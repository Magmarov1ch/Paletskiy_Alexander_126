import random
def magic(num_list,x):
    sum_nums = sum (num_list)
    if sum_nums % x == 0:
        return True
    else:
        return False
num_list = random.sample(range(0, 10000), random.randint(5,101))
x = random.randint(1, 101)
print(num_list)
print(x)
print(magic(num_list, x))