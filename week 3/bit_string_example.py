'''Example: Bit string
Task

You are given a bit string consisting of the characters 0 and 1.
How many ways can you select two positions in the bit string,
 so that the left position contains the bit 0 and the right position contains the bit 1?

Consider the following situation:

Position	0	1	2	3	4	5	6	7
Bit	        0	1	0	0	1	0	1	1'''


def count_ways(bits):
    n = len(bits)
    count = 0
    possible_ways = 0
    for i in range(n):
        if bits[i] == 0:
            count += 1
        if bits[i] == 1:
            possible_ways = possible_ways + count

    return possible_ways


bits = [0, 1, 0, 0, 1, 0, 1, 1]
print(count_ways(bits))