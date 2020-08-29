def calpi(time):
    numerator = 1
    denominator = 1
    ans = 0

    for x in range(time):
        if x == 0:
            ans += denominator
            print("4 x ( " + str(denominator) + " ", end='')
        else:
            denominator += 2 
            if x % 2 == 0:
                ans += (numerator / (denominator))
                if(x == (time-1)):
                    print("+ 1 / " + str(denominator) + " ) = ", end='')
                else:
                    print("+ 1 / " + str(denominator) + " ", end='')
            else:
                ans -= (numerator / (denominator))
                if(x == (time-1)):
                    print("- 1 / " + str(denominator) + " ) = ", end='')
                else:
                    print("- 1 / " + str(denominator) + " ", end='')
    print(4*ans)
                
def main():
    calpi(6)
    calpi(8)

if __name__ == "__main__":
    main()