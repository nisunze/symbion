#!/usr/bin/env python

def format_address(address_string):
    # Declare variables
    splits = address_string.split(' ')
    # Separate the address string into parts
    num = splits[0]
    name = ' '.join(splits[1:])
    # Traverse through the address parts
    result = "house number {} on street named {}".format(num, name)
    # Determine if the address part is the
    # house number or part of the street name

    # Does anything else need to be done 
    # before returning the result?

    # Return the formatted string  
    return result

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
