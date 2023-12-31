import re
import operator
from rpn_io import *

sym_tab={}
stack = []
pc=-1

scanner = re.Scanner([(r"[ \t\n]", lambda s, t: None),
                        (r"-?(\d*)?\.\d+", lambda s, t:stack.append(float(t))),
                        (r"-?\d+", lambda s, t: stack.append(int(t))),
                        (r"[a-zA-Z_][a-zA-Z_0-9]*", lambda s, t:stack.append(t)),
                        (r"[+]", lambda s, t: bin_op(operator.add)),
                        (r"[-]", lambda s, t: bin_op(operator.sub)),
                        (r"[*]", lambda s, t: bin_op(operator.mul)),
                        (r"[/]", lambda s, t: bin_op(operator.truediv)),
                        (r"[\^]", lambda s, t: bin_op(operator.pow)),
                        (r"[=]", lambda s, t: assign_op()),
])

def assign_op():
    '''Assignment Operator function: Pop off a name
    and a value, and make a symbol-table entry.
    '''
    op2, op1 = stack.pop(), stack.pop()
    # print(op2,op1)
    if type(op2) == str: # Source may be another var!
        op2 = sym_tab[op2]
    sym_tab[op1] = op2
def bin_op(action):
    '''Binary Operation evaluator: If an operand is
    a variable name, look it up in the symbol table
    and replace with the corresponding value, before
    being evaluated.
    '''
    op2, op1 = stack.pop(), stack.pop()
    if type(op1) == str:
        op1 = sym_tab[op1]
    if type(op2) == str:
        op2 = sym_tab[op2]
    stack.append(action(op1, op2))

# def main():
#     a_list = open_rpn_file()
#     if not a_list:
#         print('Bye!')
#         return
#     for a_line in a_list:
#         a_line = a_line.strip()
#         if a_line.startswith('PRINTS'):
#             do_prints(a_line[7:])
#         elif a_line.startswith('PRINTLN'):
#             do_println(a_line[8:])
#         elif a_line.startswith('PRINTVAR'):
#             do_printvar(a_line[9:], sym_tab)
#         elif a_line.startswith('INPUT'):
#             do_input(a_line[6:], sym_tab)
#         elif a_line:
#             tokens, unknown = scanner.scan(a_line)
#             if unknown:
#                 print('Unrecognized input:',unknown)

def main():
    global pc
    a_list = open_rpn_file()
    if not a_list:
        print('Bye!')
        return
    pc = -1
    while True:
        pc += 1
        if pc >= len(a_list):
            break
        a_line = a_list[pc]
        try:
            a_line = a_line.strip()
            if a_line.startswith('PRINTS'):
                do_prints(a_line[7:])
            elif a_line.startswith('PRINTLN'):
                do_println(a_line[8:])
            elif a_line.startswith('PRINTVAR'):
                do_printvar(a_line[9:], sym_tab)
            elif a_line.startswith('INPUT'):
                do_input(a_line[6:], sym_tab)
            elif a_line:
                tokens, unknown =scanner.scan(a_line)
                if unknown:
                    print('Unrecognized input:',unknown)
                    break
        except KeyError as e:
            # print(e)
            print('Unrecognized symbol', e.args[0],'found in line', pc)
            print(a_list[pc])
            break
main()