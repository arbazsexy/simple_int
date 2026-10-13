import sys  # 1. Import sys at the top

def simint(p, i, t):
    return (p * i * t) / 100

# 2. Only run command-line execution if this file is run directly
if __name__ == "__main__":
    if len(sys.argv) >= 4:
        p = int(sys.argv[1])
        i = float(sys.argv[2])
        t = float(sys.argv[3])
        print("simple intrest:", simint(p, i, t))