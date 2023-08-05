# https://adventofcode.com/2021/day/16

import sys

hextobin = { "0": "0000", "1": "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111" }

def update_packet_value(typeid, current, new_item):
    if current == None:
        return new_item
    match typeid:
        case 0:
            return current + new_item
        case 1:
            return current * new_item
        case 2:
            return min(current, new_item)
        case 3:
            return max(current, new_item)
        case 5:
            return 1 if current > new_item else 0
        case 6:
            return 1 if current < new_item else 0
        case 7:
            return 1 if current == new_item else 0

def read_bits(a, b, bits):
    result = 0
    for i in range(a, b):
        result = 2 * result + bits[i]
    return result

def read_packet(i, bits):
    version = read_bits(i, i+3, bits)
    typeid = read_bits(i+3, i+6, bits)
    version_sum = version
    if typeid == 4:
        val = 0
        k = i + 6
        while bits[k]:
            val = val * 16 + read_bits(k+1, k+5, bits)
            k += 5
        val = val * 16 + read_bits(k+1, k+5, bits)
        return (k + 5, val, version_sum)
    result = None
    j = 0
    if bits[i+6] == 0:
        length = read_bits(i+7, i+22, bits)
        j = i+22
        while j < i+22+length:
            (j, intermediate, v_sum) = read_packet(j, bits)
            result = update_packet_value(typeid, result, intermediate)
            version_sum += v_sum
        return (i+22+length, result, version_sum)
    else:
        length = read_bits(i+7, i+18, bits)
        j = i+18
        for _ in range(length):
            (j, intermediate, v_sum) = read_packet(j, bits)
            result = update_packet_value(typeid, result, intermediate)
            version_sum += v_sum
        return (j, result, version_sum)

for line in sys.stdin:
    bits = [ int(bit) for symbol in line.strip() for bit in hextobin[symbol]  ]
    _, value, version_sum = read_packet(0, bits)
    print("Part 1")
    print(version_sum)
    print("Part 2")
    print(value)
