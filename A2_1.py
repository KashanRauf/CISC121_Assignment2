# Using a function to confirm validity of input.
def is_valid(num) :
    num = int(num)
    return bool(-20 < num & num < 20)

# Loop breaks once input is confirmed to be valid, gives the user a chance to correct
valid_input = False 
values = 0

while not valid_input :
    # Prompting users for input.
    values = input("Please enter two integers between -20 and 20: ").split()

    # Checking values and giving output.
    first_valid = is_valid(values[0])
    second_valid = is_valid(values[1])
    if first_valid and second_valid:
        print("Both numbers are valid")
        valid_input = True
    elif not first_valid and (not second_valid):
        print("Both numbers are invalid")
    elif not first_valid :
        print("First number (", values[0], ") is invalid", sep="")
    else :
        print("Second number (", values[1], ") is invalid", sep="")
    print("")

# Once valid input is given, skip counts by 5
if valid_input :
    val = int(values[0])
    while val + 5 < int(values[1]) :
        print (val + 5)
        val += 5

