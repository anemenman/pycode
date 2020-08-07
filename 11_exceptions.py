# try-except-finally
try:
    b = 1 / 0
except Exception as e:
    print(e)
finally:
    print("Finally!")

# raise exception
try:
    raise Exception("Some exception")
except Exception as e:
    print("Exception exception " + str(e))
