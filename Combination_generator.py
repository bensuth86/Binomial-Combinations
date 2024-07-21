# Commented for example nCr = 6C3
# Will NOT work for r < 2 i.e. nC1

##%INPUT%##

from timeit import default_timer as timer

def rev_seq(sequence):
    return list(reversed(sequence))  # (3,2,1)

## After 3 iterations (combination (1,2,6)), reset sequence returns the following:

def reset_sequence(sequence):
    for revindex, elem in enumerate(rev_seq(sequence)):  # index position for reversed sequence order

        x = elem - rev_seq(sequence)[revindex + 1]  # difference between adjacent terms
        if x != 1 or revindex >= len(sequence) - 2:  # or statement to prevent 'list index out of range' error
            break

    index = ((revindex + 1) * -1) - 1  # returns corresponding index postion within sequence before its reversal

    current_term = sequence[index]
    current_term += 1
    # [2,6]

    (sequence[index:]) = list(range(current_term, current_term + len((sequence[index:]))))
    # [2,6] = [3,4]

    return sequence  # new sequence: (1,3,4)


##%PROCESS%##

def main(n, r):

    # n = int(input("Enter n: "))
    # r = int(input("Enter r: "))

    cbn = 1
    sequence = list(range(1, r + 1))  # (1,2,3)
    # print("%s : %s" % (cbn, sequence))
    yield sequence  # yield 1st combination

    # start = timer()

    while sequence[0] < (n - r) + 1:  # final combination (4,5,6)

        c = 0
        while sequence[-1] < n:
            c += 1
            cbn += 1

            sequence[-1] += 1
            yield sequence
            # print("%sa : %s" % (cbn, sequence))

        ##    print ("\n count %s" %c)
        sequence = reset_sequence(sequence)
        cbn += 1
        # print("\n %sb : %s" % (cbn, sequence))
        yield sequence

        # After 3 + 2 + 1 iterations, combination = (1,5,6)
        #                             c == 1
        if c == 1 and sequence[0] < (n - r) + 1:
            sequence = reset_sequence(sequence)

            cbn += 1
            # print("\n %sc : %s" % (cbn, sequence))
            yield sequence
            # sequence reset to (2,3,4)

    # ...
    end = timer()

    ##%OUTPUT%##

    # elapsed_time = (end - start)
    # elapsed_time = round(elapsed_time, 3)
    # # print("%s : %s" % (cbn, sequence))
    #
    # print("\n%s combinations for %sC%s" % (cbn, n, r))
    #
    # print("Solution converged in %s seconds" % elapsed_time)

# main(6, 3)


##12C7
##792 cbn's
##elapsed time: 0.01 seconds

##20C15
##15504 cbn's
##elapsed time: 0.14 seconds

##30C20
##30 million+ cbn's
##elapsed time: 212 seconds

