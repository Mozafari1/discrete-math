#----------------------------------------------------------
# Hjemmeeksamen i diskret matematikk høst 2019. Kandidat nr: 22
# ---------------------------------------------------------------
# Koden er skrevet i python3. Programmet kan kjøre ved å skrive "python + filnavnet"
# Det tar litt tid for programmet er klar for kryptering og dekrypting av tekster. Programmet støtter alle språkene.
# Programmet tar input fra brukeren
# ---------------------------------------------------------
# Importerer noen pakker som jeg trenger videre i programmet
# -----------------------------------------
# Steg 1       Importerer pakker 
#-----------------------------------------

import math
import random

#--------------------------------------------
# Steg 2    Sjekker primtallet 
#-------------------------------------------
def primtall(tall):
    #sjekker om tallet er mindre enn 2 og primtall kan ikke være mindre enn 2
    if (tall <=2 ):
        return False
    # sjekker om tallet partall og et partall kan ikke være primtall 
    if tall%2==0:
        return False

    # Nå har jeg sjekket om tall er mindre 3
    # Nå finner primtallet og det gjør jeg ved å tallet opp til kvadrat av (N)
    # Øker med 2 
    for i in range(3, math.floor(math.sqrt(tall)),2):
        if (tall %i ==0):
            return False
       
    return True

#-----------------------------------------------------------------------------------
# Steg 3   Extended Euclids Algoritme  (EEA)
#------------------------------------------------------------
# Bruker EEA for å finne modulær  invers i O(log (m)), altså linear
# Finner verdien til d som er modulær invers av e i RSA 
# funksjonen tar to helltall og finner modulær inversen 

def m_invers(a,m):

    mod = m
    y = 0
    x = 1
    if (m ==1):
        return 0;
    while (a >1):
        #kvotient = k
        k = a // m 
        temp = m 
        # r = remainder
        # dette like som gcd 
        m = a % m
        a = temp
        temp = y
        # oppdaterer x og y verdiene
        y = x - k * y 
        x = temp
        # sjekker om x større en 0 og at det er positivt
    if x <0:
        x =x+mod
    
    return x

# --------------------------------------------------------
# steg 4 gcd algoritmen
#---------------------------------------------------------
#This is a simple code to compute gcd numbers
# Verifiserer om (e, phi) er komprimer med gcd 

def gcd(x,y):
    while (y!=0):
        x, y = y, x%y
    return  x

#--------------------------------------------------------------
# Steg 5 lage primtall 
#---------------------------------------------------------------
# 
x = pow(20, 12) # => 2000^4
y = pow(99,8)  # => 9999^4 

def produsere_primtall (start =x, end=y ):
    tall = random.randint(x,y) # primtallet skal være mellom x og y verdi og det er tilfeldig 
    # sjekker om det er primtall eller ikke
    while (not primtall(tall)):
        # hvis det er ikke primtall så genererer primtall på nytt 
        tall = random.randint(x,y)
    # returnerer primtallet
    return tall

#--------------------------------------------------------------------
# Steg 6 : Produserer RSA nøkkeler
#----------------------------------------------------------------------

def RSA_nokkel():
     # produserer den første primtallet 
     primtall_1 = produsere_primtall()
     # produserer den andre primtallet
     primtall_2 = produsere_primtall()
     # Ganger primtall_1 med primtall_2 for å få n. 
     # Å gjøre det motsatte for å få primtall_1 og primtall_2 fra n så tar den litt tid for n er en exponential 
     n = primtall_1 * primtall_2
     # Reginer ut phi og bruker Euler sin phi funksjonen
     phi = (primtall_1-1)*(primtall_2-1)
     # verdien til e skal være mellom 1 og phi
     e = random.randrange(1,phi)
     # dobbel sjekker om gcd(e, phi) =1 og at de er komprimer hvis de ikke er komprimer så kan jeg ikke finne d
     while gcd(e,phi)!=1:
         # produserer e på nytt hvis det gcd er ikke 1
         e = random.randrange(1,phi)
     # d  er modulær invers av e
     d =m_invers(e,phi)
     # returnerer både privat og offentlige nøkkler
     return ((d,n),(e,n))

#-----------------------------------------------------------------------
# Steg 7 : krypterer meldingen 
#------------------------------------------------------------------------
# Funksjonen tar to paramter som er offentlige nøkkelen og meldingen og krypterer meldingen ved å bruke den offentlige nøkkelen
# offentlig_nøkkel = on
# meldingen = m
def krypter(on, m):
    # her trenger vi e og n for å krypterer meldingen og de er offentlig
    e, n = on
    # Jeg bruker ascii verdiene for tegn og omformingen lagres i en array, arrayet er tomt i starten
    krypterte_meldingen = []
    # vurderer alle bokstavene i en rekkefølge
    for i in m:
        temp = ord(i)
        krypterte_meldingen.append(pow(temp,e,n)) # Her temp er grunntallet og e er exponenten og n er modulo
    return krypterte_meldingen

#-------------------------------------------------------------------
# Steg 8 : Dekrypterer meldingen 
#---------------------------------------------------------------------

# dekrypterer meldingen ved å bruke privat nøkkelen
# funksjonen tar to parameter som p-nøkkelen og krypterte meldingen
# privat nøkkelen = pn
# krypterte_meldingen = kn
def dekrypterer(pn, kn):
    # vi trenger d og n for dekryptere meldingen og det er privat
    d , n = pn
    m = ''
    # vurderer alle bokstavene i en rekkefølge
    for i in kn:
        temp = pow(i,d,n)
        m = m + str (chr(temp))
    return m
#--------------------------------------------------------------------
# Siste steg: printer ut resultater 
#---------------------------------------------------------------------
# Hoved funksjon
# privat nøkkelen = pn
# offentlig_nøkkel = on
# meldingen = m
# krypterte_meldingen = kn

if __name__ == "__main__":
    pn,on = RSA_nokkel()
    m = input("Skriv en melding som du vil kryptere: ")
    kn = krypter(on, m)
    print("Dette er din krypterte meldingen: %s" %kn)
    opprinnelige_meldingen = dekrypterer(pn, kn)
    print("Dette er din opprinnelige meldingen: %s" %opprinnelige_meldingen)


