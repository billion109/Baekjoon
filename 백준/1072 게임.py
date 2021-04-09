import math
if __name__ == "__main__":
    while True:
        try:
            X, Y = map(int,input().split())
            Z = (100*Y)//X


            if Z >= 99:
                print(-1)
                exit(0)


            #print(math.ceil((0.01*X*(Z+1)-Y)/(0.99-0.01*Z)))
            print(math.ceil((X*(Z+1)-100*Y)/(99-Z)))
        except:
            break