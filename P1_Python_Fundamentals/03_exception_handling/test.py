def test(x):

    try:
        y = int(x)
    except ValueError:
        print("failed")
    else:
        print("success")
    finally:
        print("done")


test('123')
#The try-catch-else-finally block structure (commonly used in Python) controls how errors are handled in code execution:
#try: Code you want to attempt running that might throw an error.
#catch / except: Code that runs only if an error occurs in the try block.
#else: Code that runs only if no errors occurred in the try block.
#finally: Code that always runs, regardless of whether an error happened or not (used for cleanup like closing files or connections).

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("Success: File read successfully.")
finally:
    print("Cleanup: Closing operations.")
