
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("An error occurred")
else:
    print("Everything went well")
finally:
    print("The execution completed")
    
x = -1

if x < 0:
    raise Exception("Negative value not allowed")
