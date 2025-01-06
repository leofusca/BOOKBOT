
def main():
    with open("books/Frankestein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    
def wordcount():
    with open("books/Frankestein.txt") as f:
        file_contents = f.read()
    number_of_words = len(file_contents.split())  
    return number_of_words

def charactercount():
    with open("books/Frankestein.txt") as f:
        file_contents = f.read()
    lowered_text = file_contents.lower()

    charactercount_dictionary = {} 

    for x in lowered_text:
        if x.isalpha():
            if x in charactercount_dictionary:
                charactercount_dictionary[x] += 1
            else:
                charactercount_dictionary[x] = 1
        
    print(charactercount_dictionary)  
    
    


main()
print("--- Begin report of books/frankenstein.txt ---") 
print(f"{wordcount()} words found in the document")



charactercount()