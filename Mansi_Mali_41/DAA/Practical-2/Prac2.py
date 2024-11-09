#Name : Mansi Mali
#Roll No. 41
#Sub : DAA
#Experiment No : 2
import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Return the root of the tree

def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

def huffman_encoding(text):
    if not text:
        return "", None

    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)

    # Encode the text
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, codes

# User input
if __name__ == "__main__":
    user_input = input("Enter a string to encode using Huffman encoding: ")
    encoded_text, huffman_codes = huffman_encoding(user_input)

    print("Encoded Text:", encoded_text)
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
