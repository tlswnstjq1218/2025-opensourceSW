# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import time
print(' 로켓 발사 카운트 다운')
for number in range (10,0,-1):
    print (f'발사 {number}초 전!')
    time.sleep(1)
print('로켓 발사')

print('비행기 이륙합니다')
height = 0
while height < 10000:
    print(f'고도 {height:05d}km')
    height = height + 1000
print(f'고도 {height:05d}km 도달')

x=int(input('입력:'))
print(f'{x}를 2로 나누어봅시다')
while True:
    x= x // 2
    print(f'x = {x}')
    if x < 10:
        print('x가 10보다 작아졌으므로 종료합니다')
        break
    else:
        print ('x가 아직 10보다 크므로 계속합니다')

###

num = input('정수 혹은 소수를 입력하세요:')

float_num=float(num)
print(f'입력한 숫자의 소수형:{float_num}')

int_num = int(float(num))
print(f'입력한 숫자의 정수형:{int_num}')

string = input('영어로 아무거나 입력하세요 (5자 이상):')

print(f'str.upper():{string.upper()}')
print(f'str.lower():{string.lower()}')
print(f'str[2:4]:{string[2:4]}')

l = list()

l.append(4)
print(l)

l.append('string')
print(l)

l.append(10.44)
print(l)

l.remove('string')
print(l)

y = set()
for n in range(0,20):
    y.add(n)
print(y)

d = dict()
d['key'] = 'value'
print(d)

d[4] = 'string'
print(d)

d[20.2] = 99.4

print(d)

d.pop(4)
print(d)
x= {'K':'V',10:20}

x= {'K':'V',10:20}

x= int(input())
y= int(input())
print(f'{x}+{y} = {x+y}')
 ##수# 정x = int(input('첫번째 인자를 입력하세요:'))y=int(input('두번쨰 인자를 입력하세요:'))
print(f'[x] + [y] = [x + y]:
print('프로그램을 종료합니다')
