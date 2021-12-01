#File Writer
#Ask the user the number of words need to be entered
#Save the words in the txt file

def main():
    words = int(input("How many words you want to write? "))
    f = open("writtenwords.txt","w")
    i=0
    while (i < words):
        word=input("Enter a word: ")
        f = open('writtenwords.txt', 'a')
        f.write(word)
        f.write('\n')
        i+=1
        f.close()
main()
