import sys
import numpy as np

if(len(sys.argv) < 2):
    print("You need at least the size of the array you want to create.")
    print("Command: python int_array_gen.py <array_length> [<max_value> <delimiter>]")
    sys.exit(0)

if(not sys.argv[1].isdigit()):
    print("Second argument must be a integer.")
    print("Command: python int_array_gen.py <array_length> [<max_value> <delimiter>]")
    sys.exit(0)

array_size = int(sys.argv[1])

if(len(sys.argv) > 2):
    if(not sys.argv[2].isdigit()):
        print("Third argument must be a integer.")
        print("Command: python int_array_gen.py <array_length> [<max_value> <delimiter>]")
        sys.exit(0)
    else:
        max_value = int(sys.argv[2])
else:
    max_value = 20

result = ""

if(len(sys.argv) > 3):
    delimiter = sys.argv[4]
else:
    delimiter = " "

# Generate de array
result = np.random.randint(max_value, size=array_size).tolist()
# Writing the result
print(delimiter.join(str(e) for e in result))