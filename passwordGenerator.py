import string, random

print('***Password Generator***')

#func for a weak password
def weakPass():
    weakPasswordsList = ['Password', '1234', 'qwerty', '00000', '1111', 'user', 'Iloveu', 'myBirthday']
    return random.choice(weakPasswordsList)

#func for strong password
def strongPass(x = string.ascii_letters + string.digits + string.punctuation, N = random.randint(12,20)):
    return ''.join(random.choice(x) for _ in range(N))

def userChoice():
    print('Would you like a weak or strong password?')
    while True:
        print('Please enter \'weak\' or \'strong\'.')
        userInput = input()
        if userInput == 'weak':
            print('Weak password: ', weakPass())
            break
        elif userInput == 'strong':
            print()
            print('Password: ', strongPass())
            print('Length: ', len(strongPass()))
            break
        else:
            print()
            continue



userChoice()