import math

n = int(input("Enter the numerator (must be greater than 0): "))

while True:
    if n > 0:
        d = eval(input("Enter the denominator (must be greater than 0): "))
        while True:
            if d > 0:
                g = math.gcd(n, d)
                if n < d:
                    print(f'{n} / {d} is a proper function.')
                    if g > 1:
                        n = int(n / g)
                        d = int(d / g)
                        print(f'This proper function can be reduced to: {n} / {d}')
                        break
                    else:
                        print('This fraction cannot be reduced any further')
                        break
                else:
                    print(f'{n} / {d} is an improper function.')
                    if g > 1:
                        n = int(n / g)
                        d = int(d / g)
                        print(f'This improper function can be reduced to: {n} / {d}')
                        whole_number = n // d
                        proper_function = n - (whole_number * d)
                        if proper_function == 0:
                            print(f'The whole number is {whole_number}')
                            break
                        else:
                            print(f'The mixed number is {whole_number} and {proper_function} / {d}')
                            break
                    else:
                        print(f'This improper function cannot be reduced any further')
                        whole_number = n // d
                        proper_function = n - (whole_number * d)
                        if proper_function == 0:
                            print(f'The whole number is {whole_number}')
                            break
                        else:
                            print(f'The mixed number is {whole_number} and {proper_function} / {d}')
                            break

            else:
                d = eval(input("Please re-enter the denominator. Value must be greater than 0: "))
        break

    else:
        n = int(input("Please re-enter the numerator. Value must be greater than 0: "))











