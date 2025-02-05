class bookbot:
    def __init__(self,file):
        self.path = file
        self.f = open(self.path, "r")
        self.text = self.f.read()
        self.dictionary = self.charCount()
        self.totalChar = self.totalChar()
        self.wordCount = self.wordCount()


    def wordCount(self):
        return len(self.text.split())
    
    def totalChar(self):
        return len(self.text)
    
    def charCount(self):
        self.dictionary = {}
        for char in self.text:
            if char not in self.dictionary:
                self.dictionary[char] = 1
            else:
                self.dictionary[char] += 1
        return self.dictionary
    
    
    def printOutput(self) -> None:
        dictlist = []
        for key, value in self.dictionary.items():
            temp = [key, value]
            dictlist.append(temp)
        sortedlist = sorted(dictlist, key=lambda x: x[1], reverse=True)
    
    
        print(f"--- Begin report of {self.path} ---")
        print(f"{self.wordCount} words found in the document")
        print(f"{self.totalChar} characters found in the document\n")
    
        for item in sortedlist:
            print(f"The '{item[0]}' character was found {item[1]} times")
    
        print("--- End report ---")

def main():
    frankenstein = bookbot("frankenstein.txt")

    frankenstein.printOutput()



if __name__ == '__main__':
    main()
