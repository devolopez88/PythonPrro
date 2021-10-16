def div(num):
    divisor = []
    for i in range(1, num +1):
        if num % i == 1:
            divisor.append(i)
    return divisor
    

def run():
    n = int(input("Tape a value : "))
    print(div(n))

if __name__ == "__main__":
    run()
