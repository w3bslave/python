#Basic Python Program for a countdown timer.
import time
def countDown(n):
    if n!=-1:
        print(n)
        time.sleep(1)
        countDown(n-1)
    
def main():
    n=int(input("Countdown starting value: "))
    countDown(n)
main()
