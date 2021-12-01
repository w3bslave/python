#Word List File Reader

#Open the file to be evaluated:
file = open("writtenwords.txt", "rt")

#Function for the longest words in the txt file:
def longestWords(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

#Count the number of words:
data = file.read()
words = data.split()

#Average of Words in the txt file:
wordCount = len(words)
ch = 0
for word in words:
    ch += len(word)  
    avg = ch /wordCount

print('The total number of words in text file is:', len(words))
print("The longest of words in text file is/are: ",longestWords('writtenwords.txt'))
print ("The average length of all of the words in the file is: ", avg)
