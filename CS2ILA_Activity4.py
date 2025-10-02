#Activity 4
#Ask the user for their full name
full_name = input("Enter your full name (First, Middle, Last): ")

#Extract the first name, middle name, and last name
extracted_names = [part.strip() for part in full_name.split(',')]

if len(extracted_names) != 3:
    print("Error Ocurred: invalid format.")
    
else:
    first_name, middle_name, last_name = extracted_names
    
    #Capitalize the first letter of each name.
    first_name = first_name.title()
    last_name = last_name.title()
    #Convert the middle name to a single initial followed by a period
    middle_initial = middle_name[0].upper() + "."

    #Rearrange the name into the format: LastName, FirstName M.
    formatted_name = f"{last_name}, {first_name} {middle_initial}"
    
    #Display the formatted name
    print("Formatted Name:", formatted_name)