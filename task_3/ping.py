import  os
os.system('clear')

print('#' * 100)
ip_to_check = input('IP to check: ')

print('-' * 60)
os.system('ping {}'.format(ip_to_check))
print('-' * 60)
input("Press any Key to Exit...")