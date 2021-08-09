"""
File: testdict.py

Authors: Laurie Jones, Harry Pinkerton, James Lawson
Project: 11

A test harness for dictionaries.
"""
from modules.dict.arrayDict import ArrayDict
from modules.dict.hashDict import HashDict

def main(dictionaryType = ArrayDict):
    print("Testing", dictionaryType)
    d = dictionaryType()
    pairs = [("name", "Ken"), ("hair-color", "grey"),
             ("hobbies", ["movies", "dancing"]), ("age", 66)]
    for (key, value) in pairs:
        d[key] = value
    print("\nLength is 4: ", len(d))
    print("\nThe dictionary:", d)
    print("\nThe keys:", end = " ")
    for key in d.keys(): print(key, end = " ")
    print("\n\nThe values:", end = " ")
    for key in d.values(): print(key, end = " ")
    print("\n\nKey Value (using [])")
    for key in d:
        print(key, d[key])
    print("\nKey Value (using get)")
    for key in d:
        print(key, d.get(key))
    keys = list(d.keys())
    values = list(d.values())
    for key in keys:
        d[key] = str(d[key]) + " replaced"
    print("\nValues replaced: " + str(d))
    print("\nDelete all keys, printing the values:")
    for key in keys:
        print(d.pop(key))
    
    print("values are:", values)
    print("\nLength is 0: ", len(d))
    d = dictionaryType(keys, values)
    print("\nCreate with keys and values:", d)
    d2 = dictionaryType(["occupation", "citizenship", "age"], ["teacher", "USA", 67])
    print("\nA second dictionary:", d2)
    print("\nAdd (+) the two dictionaries:", d + d2)
    

# Include your dictionary type as an argument to main
if __name__ == "__main__":
    main(HashDict)
