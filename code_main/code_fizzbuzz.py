def super_fizz_buzz(number):
    word = []
    if number % 3 == 0 :
        word.append('Fizz')
        if number % 9 == 0:
            word.append('Fizz')
            if number % 25 == 0:
                word.append('BuzzBuzz')
        elif number % 5 == 0:
            word.append('Buzz')
    elif number % 5 == 0 :
        word.append('Buzz')
        if number % 25 == 0:
           word.append('Buzz')
    else:
        word = ['NoFizzBuzz']
    tmp = ''.join(map(str, word))
    
    return (tmp)