import random    
def private_key (prime_number, prim_root):
    n = 1
    Alice_rand_num = random.randint(n, prime_number) # Alice_ran_num <prime_number -n 
    Bob_rand_num  = random.randint(n, prime_number) 
    # mathematical formula (prim_root ** Alice_rand_num mod prime_number)
    key_Alice = pow(prim_root, Alice_rand_num, prime_number) 
    key_Bod = pow(prim_root, Bob_rand_num, prime_number)
    #Python number method pow() returns x to the power of y. 
    #If the third argument (z) is given, it returns x to the power of y modulus z, i.e. pow(x, y) % z
    print("Key_Alice : %s"% (pow(key_Bod, Alice_rand_num, prime_number)))
    print("key_Bod   : %s"%(pow(key_Alice, Bob_rand_num, prime_number)))

if __name__ == "__main__":
    pn = random.randint(2934845,35767465)
    pr = random.randint(2643766,568789678)
    pn_pow = pow(pr, pn)
    pr_pow = pow(pn,pr)
    prime_number = pn_pow
    prim_root = pr_pow
    private_key( prime_number, prim_root)