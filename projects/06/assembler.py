# open file XXX.asm
# create  destination file XXX.hack

# read each line
# process each line
# write each line to destination file

# close files
# end program


# process each line
    # remove comments
    # remove white space
    # parse instructions
    # translate instructions
    # return translation

# remove comments
    # search for '//' in input string 
    # remove all strings strating from position of '//'
    # return proccessed string

# remove white space
    # replace all nonalphanumeric characters with ''
    # return proccessed string

# parse instructions
    # check if strings begins with @
    # check if string after @ is numeric
    # return numeric string (instruction, comandtype)

    # check for '='
    # split string into left and right of '=' (destinaton, computation)
    # check for ';'
    # split string into left and right of ';' (computation, jump)
    # return (instruction, comandtype)

# translate instructions
    # check for instruction type
    # if A-instruction
    # convert numeric value to 15 bit binary
    # append '0' to the beginning of 15 bit result
    # return result

    # if C-instruction
    # get computation code
    # get destination code
    # get jump code
    # append all together with '111' at the beginning
    # return result
