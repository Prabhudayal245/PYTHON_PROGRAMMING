def main():
    try:
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        print(a+b)
        return
    except Exception as e:
        print(e)
        return
    
    finally:
        print("thakyou finally keyword to print me even fuction is return")

main()