## 12- factors: 12/( 2,4/2,6/2 )
## 15- factors: 15/( 3,5 )
## 45- factors: 45/( 3,5,9,15 )


def find_next_prime(n):
    return find_prime_in_range(n, 2*n)

def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p
    return None

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def main(fac_num):

    
    divisor = fac_num
    currentprime = 2
    primefactors = []
  
    while isprime(divisor) == False: #while not a prime nos

##        print (divisor)       
        while divisor % currentprime == 0: # (leaves no remainder)
            
            divisor = divisor/currentprime
            primefactors.append(currentprime)
##            print (divisor)
        
        currentprime += 1
        next_prime = find_next_prime(currentprime)
##        print("prime- %s" % next_prime)

    if divisor != 1:
        primefactors.append(int(divisor))

    return primefactors
