#Assume a file containing a series of integers is named numbers.txt and exists on the computer’s disk.
#Write a program that displays all of the numbers in the file.

def main():
    random_numbers_file = open('numbers.txt','r')
    print("The numbers found in 'numbers.txt' are:")
    #iterate for loop for all lines in 'file'
    for line in random_numbers_file:
        number = (line)
        print(number)
main()
