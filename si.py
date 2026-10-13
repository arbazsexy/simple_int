import sys 

def simint(p, i, t):
    return (p * i * t) / 100


if __name__ == "__main__":
        p = int(sys.argv[1])
        i = float(sys.argv[2])
        t = float(sys.argv[3])
        print("simple intrest:", simint(p, i, t))