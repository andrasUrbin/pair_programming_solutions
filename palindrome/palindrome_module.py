def palindrome(str):
    bString = str.strip().lower().replace(" ", "")
    cString = bString[::-1]
    print(cString)
    if bString == cString:
        print("It's a palindrome!")
        return True
    else:
        print("It's not a palindrome!")
        return False


def main():
    aString = input("What's your word?")
    palindrome(aString)


if __name__ == '__main__':
    main()
