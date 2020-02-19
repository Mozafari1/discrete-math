import random
from math import floor, sqrt
 # Importerer pakken som jeg skal bruke i koden

 # Stater med random verdi og slutter med random verdi
random_start = 384745734068465
random_end = 974957434853634

# Definerer funksjonen og sjekker om det PRIM TALL
#
def is_the_num_prime(number):
    
    def swtich_if():
        option = number
        if option <= 2: # sjekker om tall er mindre enn 2 og hvis det er så det kan ikke være prim tall
            return False
        if option %2 ==0: # sjekker om det om tallet er odd og oddetall er ikke prim tall
            return False

        for i in range(3,floor(sqrt(option)),2):
            if option %i ==0:
                return False
        return True

def invers_of_mod(a,remainder):
    remaindr_ = remainder
    y = 0
    x = 1
    if remainder ==1:
        return 0
    
    while a >1:
        quotient = a//remainder
        t = remainder

        remainder = a %remainder
        a = t
        t = y
        
        y = x -quotient *y
        x = t


    if x <0:
        x = x+remaindr_
    return x

def gcd (a,b):
    while b!=0:
        a, b = b, a %b
    return a

def generate_l_prime(start = random_start, end = random_end):
    number = random.int(random_start, random_end)

    while not is_the_num_prime(number):
        number = random.randint(random_start, random_end)
    return number

def generate_rsa_key():
    random_prime_number_1 = generate_l_prime()
    random_prime_number_2 = generate_l_prime()

    multi_1_2 = random_prime_number_1 * random_prime_number_2

    phi_function = (random_prime_number_1 -1)*(random_prime_number_2 -1)
     
    e = random.randrange(1,phi_function)

    while gcd(e, phi_function)!=1:  
        e = random.randrange(1,phi_function)
    inverse_of_e  = invers_of_mod(e, phi_function)

    return((inverse_of_e,multi_1_2),(e, multi_1_2))

def encrypt(public_key, plaintext):
    e, n = public_key
    chipertext = []

    for char in plaintext:
        a = ord(char)
        chipertext.append(pow(a,e,n))
    return chipertext

def decrypt(private_key, chipertext):
    decr, n = private_key
    plaintext = ''

    for char in chipertext:
        a = pow(char,decr,n)
        plaintext = plaintext+str(chr(a))
    return plaintext

if __name__ == "__main__":
    private_key, public_key= generate_rsa_key()
    plaintext = input("enter text: ")
    print("The original text: %s" % plaintext)
    chipertext = encrypt(public_key, plaintext)
    print("Ciphertext: %s"%chipertext)
    origitext = decrypt(private_key,chipertext)
    print("Decrypted text is: %s" %origitext)

