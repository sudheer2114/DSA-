def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
def main():
    num = int(input("enter number: "))
    print("digits count: ", count_digits(num))
main()