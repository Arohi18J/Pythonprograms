

def checkGreater(number):
    
    original = [1,2,3,4,5,6,7,8,9,10]
    original.sort()
    if number > original[-1]:
        print('the entered number is greater than those in the list')
    else:
        print('the entered number is less than those in the list')

if __name__ == '__main__':
    userInput = int(input('Enter the number to check: '))
    checkGreater(userInput)