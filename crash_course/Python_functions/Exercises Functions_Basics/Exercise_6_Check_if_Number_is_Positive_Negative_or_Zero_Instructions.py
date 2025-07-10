
def check_sign(a:int):
    if a > 0:
        print('Positive')
    elif a < 0:
        print('Negative')
    else:
        print('Zero')

check_sign(10)  # Output: "Positive"
check_sign(-5)  # Output: "Negative"
check_sign(0)   # Output: "Zero"