import random    
def private_key (prime_number, prim_root):
    n = 1
    Alice_rand_num = random.randint(n, prime_number) # Alice_ran_num <prime_number -n 
    Bob_rand_num  = random.randint(n, prime_number) 
    # mathematical formula (prim_root ** Alice_rand_num mod prime_number)
    key_Alice = pow(prim_root, Alice_rand_num, prime_number) 
    key_Bod = pow(prim_root, Bob_rand_num, prime_number)
    print("Key_Alice : %s"% (pow(key_Bod, Alice_rand_num, prime_number)))
    print("key_Bod   : %s"%(pow(key_Alice, Bob_rand_num, prime_number)))

if __name__ == "__main__":
    prime_number =774647675834763765353857776346583475865476867346576573456878436587436873465874395256984657345436578347658743658345
    prim_root = 34524347586347567864358734856843758347568347657346575345763765847958436587456835874567349587583465887578743654
    private_key( prime_number, prim_root)