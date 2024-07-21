import Combination_generator
import prime_factors

def main(num):  ### for example factorise 147 ###

    factors = []
    # cbns = 0

    ## Return list of prime factors ##
    primefactors = prime_factors.main(num)  # (3,7,7)
    # print(primefactors)

    ## Find all combinations of prime factors and therefore all factors ##
    n = len(primefactors)  # 3

    for r in range(2, n+1):  # 3C2 & 3C3, 1st & 2nd loop respectively

        allseq = Combination_generator.main(n, r)
        for seq in allseq:

            factor = 1
            for i in seq:

                factor = factor * primefactors[i-1]  # {(3x7), (3x7), (7x7)}; (3x3x7)
                factors.append(factor)

    all_factors = [1] + primefactors + factors

    all_factors = sorted(set(all_factors)) # sorts numerically and removes duplicates

    # print(all_factors)
    return all_factors

# f = main(21)
