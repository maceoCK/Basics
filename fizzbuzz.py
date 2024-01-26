
def fizzbuzz(count):
    for i in range(1, count + 1):
        printed = False
        if i % 3:
            print("Fizz", end = "")
            printed = True
        if i % 5:
            print("Buzz", end = "")
            printed = True
        if not printed:
            print(i, end = "")
        print("")

fizzbuzz(20)
