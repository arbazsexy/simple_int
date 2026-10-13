def simint(principle,intrest,time):
    return (principle*intrest*time)/100

if __name__ == "__main__":
    p = int(input("Enter principle amount"))
    i = int(input("Enter intrest:"))
    t = int(input("Enter time:"))

print("simple intrest:",simint(p,i,t))
