

def LCM(num1, num2):
    
    maximum = max(num1, num2)
    i = maximum
    while True:
        if (i % num1 == 0  and i % num2 == 0):
            lcm = i
            break
        i += maximum

    return lcm
if __name__ == '__main__':
    input1 = int(input('Enter first number: '))
    input2 = int(input('Enter second number: '))
    print('''LCM of {} and {} is {}'''.format( input1, input2, LCM(input1, input2)))