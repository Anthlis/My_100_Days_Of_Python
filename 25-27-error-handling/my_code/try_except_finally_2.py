def log(msg):
    # pretend cloud server is down
    # raise SystemError("Logging not up")
    print(msg)

def divide_work(x, y):
    try:
        return x/y
    except ZeroDivisionError as ex:
        log("System is down")
        raise ArithmeticError("Bad maths") from ex
    

try:
    divide_work(6, 0)
except Exception as e:
    print(f"Exception: {str(e.__class__)}")
    print(f"context: {e.__context__}")
    print(f"cause: {e.__cause__}")
    print(f"tb: {e.__traceback__}")
    
    

# >>> divide_work(7, 0)
# System is down
# Traceback (most recent call last):
#   File "C:\Users\ListerA\OneDrive\macfiles\Thonny\try_except_finally_2.py", line 8, in divide_work
#     return x/y
# ZeroDivisionError: division by zero

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<pyshell>", line 1, in <module>
#   File "C:\Users\ListerA\OneDrive\macfiles\Thonny\try_except_finally_2.py", line 11, in divide_work
#     raise ArithmeticError("bad maths") from ex
# ArithmeticError: bad maths

# ---------------------

# run output:

# >>> %Run try_except_finally_2.py
# System is down
# Exception: <class 'ArithmeticError'>
# context: division by zero
# cause: division by zero
# tb: <traceback object at 0x03E8C6E8>