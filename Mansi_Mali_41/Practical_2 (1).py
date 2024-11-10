'''
NAME: UGALE GANESH DHONDIRAM
CLASS: BE (COMP)
ROLL NO: 35
SUB: DAA
EXPERIMENT NO: 02
'''

import heapq

# Characters and their frequencies
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

# Build heap with (frequency, character) tuples
heap = [(freq[i], chars[i]) for i in range(len(chars))]
heapq.heapify(heap)

# Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    heapq.heappush(heap, (left[0] + right[0], [left, right]))

# Generate Huffman codes
def huffman_codes(tree, code=""):
    if type(tree[1]) is str:
        print(f"{tree[1]} -> {code}")
    else:
        huffman_codes(tree[1][0], code + "0")
        huffman_codes(tree[1][1], code + "1")

# Print the codes
huffman_codes(heap[0])

'''
OUTPUT:
f -> 0
c -> 100
d -> 101
a -> 1100
b -> 1101
e -> 111

'''