"""
File: testhashing.py
"""

def main(arrayLength = 10, numberOfItems = 5):
    print("Array length:    ", arrayLength)
    print("Number of items:  ", numberOfItems)
    print("%s  %20s  %20s" % ("Item", "hash code", "array index"))
    for i in range(1, numberOfItems + 1):
        item = "Item" + str(i)
        code = hash(item)
        index = abs(code) % arrayLength
        print("%-6s  %25d  %8d" % (item, code, index))

if __name__ == "__main__":
    main()

