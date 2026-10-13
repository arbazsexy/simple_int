def simint(principle,intrest,time):
    return (principle*intrest*time)/100

if __name__ == "__main__":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

print("simple intrest:",simint(p,i,t))
