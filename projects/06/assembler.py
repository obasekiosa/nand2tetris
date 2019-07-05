import string


file_name = NULL
file_extention = NULL

if file_extention != '.asm':
    exit()
# open file XXX.asm
source_file = open(file_name)
# create  destination file XXX.hack
destination_file = open(file_name + ".hack", "w+")

# read each line
line = True
while line:
    line = source_file.readline()
    # process each line
    instruction_code = ProcessLine(line)
    # write each line to destination file
    if instruction_code:
        destination_file.write(instruction_code)

# close files
destination_file.close()
source_file.close()
# end program
exit()


# process each line
def ProcessLine(line):
    new_line = line[:]
    if new_line:
        # remove comments
        new_line = RemoveComments(line)
        if new_line
            # remove white space
            new_line = RemoveWhiteSpace(new_line)
            if new_line:
                # parse instructions
                instruction, instruction_type = ParseInstruction(new_line)
                if instruction_type == 1 or instruction_type == 0:
                    # translate instructions
                    return TranslateInstruction(instruction, instruction_type)
                else:
                    return ''
            else:
                return ''
        else:
            return ''
    else:
        return ''

# remove comments
def RemoveComments(line):
    # search for '//' in input string
    loc = line.find(line)
    # remove all strings strating from position of '//'
    new_line = line[:loc]
    # return proccessed string
    return new_line

# remove white space
def RemoveWhiteSpace(line):
    new_line = ''
    # replace all nonalphanumeric characters with ''
    for e in line:
        if e.isalphanun():
            new_line += e
    # return proccessed string
    return new_line

# parse instructions
def ParseInstruction(line):
    # check if strings begins with @
    tokens = line.split('@', 1)
    if tokens[0] == '' and len(tokens) > 1:
        # return (instruction, comandtype)
        return (tokens[1], 0)
    else
        # split string into left and right of '=' (destinaton, computation)
        token_eq = line.split('=', 1)
        # split string into left and right of ';' (computation, jump)
        token_semicolon = tokens[1].split(';', 1)
        # (destination, computation, jump)
        tokens = token_eq[0] + token_semicolon
        instruction = tuple(tokens)
        # return (instruction, comandtype)
        return (instruction, 1)

# translate instructions
def TranslateInstruction(instruction, instruction_type):
    CODE = {
        'comp': { '0':'0101010',
                  '1':'0111111',
                  '-1':'0111010',
                   'D':'0001100',
                   'A':'0110000',
                   '!D':'0001101',
                    '!A':'0110001',
                    '-D':'0001111',
                    '-A':'0110011',
                    'D+1':'0011111',
                    '1+D':'0011111',
                    'A+1':'0110111',
                    '1+A':'0110111',
                    'D-1':'0001110',
                    'A-1':'0110010',
                    'D+A':'0000010',
                    'A+D':'0000010',
                    'D-A':'0010011',
                    'A-D':'0000111',
                    'D&A':'0000000',
                    'A&D':'0000000',
                    'D|A':'0010101',
                    'A|D':'0010101',
                    'M':'1110000',
                    '!M':'1110001',
                    '-M':'1110011',
                    '1+M':'1110111',
                    'M+1':'1110111',
                    'M-1':'1110010',
                    'D+M':'1000010',
                    'M+D':'1000010',
                    'D-M':'1010011',
                    'M-D':'1000111',
                    'D&M':'1000000',
                    'M&D':'1000000',
                    'D|M':'1010101',
                    'M|D':'1010101'
        },

        'dest': {'A':'100',
                 'D':'010', 
                 'M':'001',
                 'AD':'110', 
                 'AM':'101', 
                 'MD':'011', 
                 'AMD':'111', 
                 '':'000'
        },

        'jump': {'JMP':'111', 
                 'JGT':'001', 
                 'JGE':'011', 
                 'JLT':'100', 
                 'JLE':'110', 
                 'JEQ':'010', 
                 'JNE':'101', 
                 '':'000'
        }
    }
    # if A-instruction
    if instruction_type == 0:
        # convert numeric value to 15 bit binary
        # append '0' to the beginning of 15 bit result
        # return result
        return '0' + str(bin(int(instruction))

    # if C-instruction
    if instruction_type == 1
    # get computation code
    CODE['comp'][instruction[1]]
    # get destination code
    # get jump code
    # append all together with '111' at the beginning
    # return result
    return '111' + CODE['comp'][instruction[1]] + CODE['dest'][instruction[0]] + CODE['jump'][instruction[2]]


101010
111111
111010
001100
110000
001101
110001
001111
110011
011111
110111
001110
110010
000010
010011
000111
000000
010101