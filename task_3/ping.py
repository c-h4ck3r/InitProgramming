import  os
os.system('clear')

print('#' * 100)
ip_to_check = input('IP to check: ')
n = int(input("Enter the interval: "))
print('-' * 60)
for i in range(n):
    os.system('ping {} -c 1'.format(ip_to_check))

input("Press any Key to Exit...")
