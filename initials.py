def get_initials(fullname):
    name = fullname.split(" ") # takes the input and splits into a list marked by a space " "
    new_string = "" # creating an empty string to put the initials in for output
    for initials in name: # created a loop for each name in the list
        initial = initials[0] # grabs the first initial from each name
        new_string = new_string + initial # adds each initial into the new string
    new_string =  new_string.upper() # makes each letter in the new string uppercase
    return new_string # returns the new string
def main():
    name = input("What is your name?") #requesting the name
    print(get_initials(name)) # calling the function with print()

if __name__ == '__main__':
    main()       
