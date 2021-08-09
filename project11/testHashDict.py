"""
File: testhashdict.py
A program for testing rehasing of a hash dictionary.
"""

from modules.dict.hashDict import HashDict

def main(dictionaryType):
    d = dictionaryType()
    print("Adding 1-40:")
    for key in range(1, 40):
        d[key] = "Value" + str(key)
        print("Length: %3d, Load factor: %5.3f, ArraySize: %3d" % (len(d), d.loadFactor(), len(d._array)))
        
    
    print("Removing 1-40:")
    for key in range(1, 40):
        print("popped:", d.pop(key))
        print("Length: %3d, Load factor: %5.3f, ArraySize: %3d" % (len(d), d.loadFactor(), len(d._array)))
    
if __name__ == "__main__":
    main(HashDict)

