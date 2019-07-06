# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:02:46 2019

@author: Obaseki Osakpolor
"""
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
    if loc != -1:
        # remove all strings strating from position of '//'
        new_line = line[:loc]
        # return proccessed string
        return new_line
    else:
        return None
    
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
        if instruction < 0:
            print("Invalid command")
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
            print("Invalid command")
            exit()
        # get destination code
        try:
            dest_code = CODE['dest'][instruction[0]]
        except:
            print("Invalid command")
            exit()
            
        # get jump code
        try:
            jump_code = CODE['jump'][instruction[2]]
        except:
            print("Invalid command")
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
    
# Uncomment the code below go Generate and Test the vaious modules individually

        
#a = '// This file is @ ; part of www.nand2tetris.org\n'
#b = ' and the book "The Elements of Computing Systems"//'
#c = '// by Nisan and // Schocken,== MIT Press.'
#d = ' File name: //projects/06/max/Max.asm'
#tests = [a, b, c, d]
#for test in tests:
##    print(RemoveComments(test))
##    print(RemoveWhiteSpace(test))
    
#for i in range(100):
#    print(ConvertToBinary15(i))

## generate A-type instructions
#k = 100
#start = 2**14
#stop = start + k
#A_instructions = []
#for i in range(start, stop):
#    A_instructions.append((i, 0))
##print(A_instructions[0:10])
#
##generate C-type instruction
#CODE = {
#        'comp': { '0':'0101010',
#                  '1':'0111111',
#                  '-1':'0111010',
#                   'D':'0001100',
#                   'A':'0110000',
#                   '!D':'0001101',
#                    '!A':'0110001',
#                    '-D':'0001111',
#                    '-A':'0110011',
#                    'D+1':'0011111',
#                    '1+D':'0011111',
#                    'A+1':'0110111',
#                    '1+A':'0110111',
#                    'D-1':'0001110',
#                    'A-1':'0110010',
#                    'D+A':'0000010',
#                    'A+D':'0000010',
#                    'D-A':'0010011',
#                    'A-D':'0000111',
#                    'D&A':'0000000',
#                    'A&D':'0000000',
#                    'D|A':'0010101',
#                    'A|D':'0010101',
#                    'M':'1110000',
#                    '!M':'1110001',
#                    '-M':'1110011',
#                    '1+M':'1110111',
#                    'M+1':'1110111',
#                    'M-1':'1110010',
#                    'D+M':'1000010',
#                    'M+D':'1000010',
#                    'D-M':'1010011',
#                    'M-D':'1000111',
#                    'D&M':'1000000',
#                    'M&D':'1000000',
#                    'D|M':'1010101',
#                    'M|D':'1010101'
#        },
#
#        'dest': {'A':'100',
#                 'D':'010', 
#                 'M':'001',
#                 'AD':'110', 
#                 'AM':'101', 
#                 'MD':'011', 
#                 'AMD':'111', 
#                 '':'000'
#        },
#
#        'jump': {'JMP':'111', 
#                 'JGT':'001', 
#                 'JGE':'011', 
#                 'JLT':'100', 
#                 'JLE':'110', 
#                 'JEQ':'010', 
#                 'JNE':'101', 
#                 '':'000'
#        }
#}
#
#k = 100
#start = 2000
#stop =  start + k
#
#C_instructions = []
#for d in CODE['dest'].keys():
#    for c in CODE['comp'].keys():
#        for j in CODE['jump'].keys():
#            C_instructions.append(((d, c, j), 1))
#print(C_instructions[start:stop])
#
#
#
## Test Translate A-Instructions
#for i in range(start, stop):
#    print(TranslateInstruction(A_instructions[i%k][0], A_instructions[i%k][1]))
#
#print(TranslateInstruction(('D&A', '', ''), 1))
#            
## Translate C-Instructions
#for i in range(start, stop):
#    print(C_instructions[i][0], C_instructions[i][1])
#    print(TranslateInstruction(C_instructions[i][0], C_instructions[i][1]))


## Test PasrseInstruction
#instructions = ['@0','D=M','@23','D;JLE','@16','M=D','@16384','D=A','@17','M=D',
#                '@17', 'A=M','M=-1','@17','D=M','@32','D=D+A','@17','M=D','@16',
#                'MD=M-1','@10','D;JGT','@23','0;JMP', 'A', '-1', '0', '0JMP']
#
#for i in  instructions:
#    print(i)
#    print(ParseInstruction(i))