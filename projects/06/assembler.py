# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:02:46 2019

@author: Obaseki Osakpolor
"""
import sys

def ConvertToBinary15(number):
    bin_num = ''
    while number != 0:
        if number % 2 == 0:
            bin_num += '0'
        else:
            bin_num += '1'
        number = number // 2
        
    zero_padding = ''
    for i in range(15 - len(bin_num)):
        zero_padding += '0'
        
    return zero_padding + bin_num[::-1]
    
        
def RemoveComments(line):
    # search for '//' in input string
    loc = line.find("//")
    if loc == -1:
        new_line = line
    else:
        # slice string up to position of '//'
        new_line = line[:loc]
    # return proccessed string
    return new_line
    
def RemoveWhiteSpace(line):
    new_line = ''
    # replace all nonalphanumeric characters with ''
    nonallowable = " \n\t\r"
    for e in line:
        if e not in nonallowable:
            new_line += e
    # return proccessed string
    return new_line

def ParseInstruction(line):
    # check if strings begins with @
    tokens = line.split('@', 1)
    if tokens[0] == '' and len(tokens) > 1:
        # return (instruction, comandtype)
        return (tokens[1], 0)
    else:
        # split string into left and right of '=' (destinaton, computation)
        token_eq = line.split('=', 1)
        # split string into left and right of ';' (computation, jump)
        token_semicolon = token_eq[len(token_eq) - 1].split(';', 1)
        # (destination, computation, jump)
        if len(token_eq) > 1:
            tokens = [token_eq[0]] + token_semicolon
        else:
            tokens = [''] + token_semicolon
        if len(token_semicolon) == 1:
            tokens += ['']
        instruction = tuple(tokens)
        # return (instruction, comandtype)
        return (instruction, 1)
    

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
        instruction = int(instruction)
        if instruction < 0:
            print("Invalid command: negative address")
            exit()
        else:
            binary_instruction = ConvertToBinary15(instruction)
        
        if len(binary_instruction) > 15:
            print("Invalid command: address out of range")
            exit()
        # append '0' to the beginning of 15 bit result
        # return result
        return '0' + binary_instruction

    # if C-instruction
    if instruction_type == 1:
        # get computation code
        try:
            comp_code = CODE['comp'][instruction[1]]
        except:
            print("Invalid command: invalid computation code")
            exit()
        # get destination code
        try:
            dest_code = CODE['dest'][instruction[0]]
        except:
            print("Invalid command: invalid destination code")
            exit()
            
        # get jump code
        try:
            jump_code = CODE['jump'][instruction[2]]
        except:
            print("Invalid command: invalid jump code")
            exit()
        
        # append all together with '111' at the beginning
        # return result
        return '111' + comp_code + dest_code + jump_code
#
# process each line
def ProcessLine(line):
    new_line = line[:]
    if new_line:
        # remove comments
        new_line = RemoveComments(new_line)
        if new_line:
            # remove white space
            new_line = RemoveWhiteSpace(new_line)
            if new_line:
                # parse instructions
                instruction, instruction_type = ParseInstruction(new_line)
                if instruction_type == 1 or instruction_type == 0:
                    # translate instructions
                    return TranslateInstruction(instruction, instruction_type)
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None

if len(sys.argv) != 2:
    print("1 argument needed")
    exit()
    
if '.' not in sys.argv[1]:
    print("file extention needed")
    exit()
    
file_full_name = sys.argv[1].split(".", 1)
file_name = file_full_name[0]
file_extention = file_full_name[1]

if file_extention.lower() != 'asm':
    print("non assembly file give, provide a .asm file")
    exit()
    
    
# open file XXX.asm
try:
    source_file = open(file_name + "." + file_extention, "r")
except:
    print("No such file in directory.")
    exit()
#create  destination file XXX.hack
try:
    destination_file = open(file_name + ".hack", "w+")
except:
    print("Could not create Destination file")
    exit()

# read each line 
read = True
line = source_file.readline()
while read:
    if line:
        # process each line
        instruction_code = ProcessLine(line)
        # write each line to destination file
        if instruction_code:
            destination_file.write(instruction_code)
        line = source_file.readline()
        if line and instruction_code:
            destination_file.write('\n')
    else:
        read = False
    
# close files
try:
    destination_file.close()
    source_file.close()
except:
    print("could not close files")
finally:
    # end program
    exit()

