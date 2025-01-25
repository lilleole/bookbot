def wordCount(text):
    return len(text.split())

def totalChar(text):
    return len(text)

def charCount(text):
    dictionary = {}
    for char in text:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary


def printOutput(path: str, totalChar: int, wordCount: int, charCount: dict) -> None:
    dictlist = []
    for key, value in charCount.items():
        temp = [key, value]
        dictlist.append(temp)
    sortedlist = sorted(dictlist, key=lambda x: x[1], reverse=True)


    print(f"--- Begin report of {path} ---")
    print(f"{wordCount} words found in the document")
    print(f"{totalChar} characters found in the document\n")

    for item in sortedlist:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")

def main():
    path = "frankenstein.txt"
    f = open(path,"r")
    text = f.read()

    printOutput(path, totalChar(text), wordCount(text.lower()), charCount(text.lower()))



if __name__ == '__main__':
    main()
