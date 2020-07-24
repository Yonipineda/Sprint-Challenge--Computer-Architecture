# 1. The CALL instruction doesn't allow you to pass any arguments. What are some ways to effectively get arguments to a subroutine?
# 2. What's the result of bitwise-AND between `0b110` AND `0b011`?
# 3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

'''Answer for Q #1'''

To effectively Pass params to a subroutine,  the Call pushes the params in a stack in reverse 
order. The last parameter to pass is the first one pushed and the first parameter to pass
is the last one pushed. 

This puts the first param at the top of the stack and the last param at the bottom of the 
stack.

This preferable compared to pass parameters via the registers or via a memory location because 
it is robust. For example, you avoid having to tell the CALL in what register the subroutine 
expects the parameters.


# NOTE

'''
A program is made up of instructions which implement the solution to a problem. In a given
program, it is often needed to perform a particular sub-task many times on different data
values. So,we split the program into smaller units which solve a particular part of the problem.
These task specific sub-units are termed as functions, procedures or subroutines. In assembly
language, we use the word subroutine for all subprograms to distinguish between functions used
in other programming languages and those used in assembly languages.

The block of instructions that constitute a subroutine can be included at every point in the main
program when that task is needed. However, this would result in unnecessary waste of memory
space. Rather, only one copy of the instructions that constitute the subroutine is placed in
memory and can be accessed repeatedly
'''

'''
To pass parameters to a subroutine, the calling program pushes them on the stack in the 
reverse order so that the last parameter to pass is the first one pushed, and the first 
parameter to pass is the last one pushed. This way the first parameter is on top of the stack 
and the last one is at the bottom of the stack.
'''

# the CALL function first pushes the address of the next instruction(the return address), 
# then the instruction pointer is modified to point to the start of the function

'''
The stack is usually the preferred way to pass arguments to a subroutine.  
Although this technique is a bit more involved once you get it right, it is bullet proof, 
and allows one to pass as many parameters to a subroutine as desired. 
Using this standard also has the advantage of hiding from the main program all the details 
of the subroutine (for example if passing via registers is implemented, then the calling
program needs to know in what registers does the subroutine expects its parameters.)
To pass parameters to a subroutine, the calling program pushes them on the stack in the 
reverse order so that the last parameter to pass is the first one pushed, 
and the first parameter to pass is the last one pushed.  
This way the first parameter is on top of the stack and the last one is at the bottom of 
the stack.  Most compilers exclusively pass parameters to a subroutines via the stack 
regardless of the number of parameters.  
''' 

###############################################################################################

'''Answer for Q #2'''
# binary-nums scale by base 2: means n^2

# suppose we have a decimal num: 45
## in binary, each bit to the left is an icrement of base 2.
## we start with 1, 2, 4, 8, 16, ..., n, etc.

## since our target is 45, the highest we can go for is 32, since 16*2 = 32.
## higher than that is not possible since 32*2 = 64
## we start with 32, we still have 13 digits left to go
## 32 + 8 = 40, that is okay and good! so we give a true, or 1 on the 8th n.
## now we have 40, we need 5 more. 
## 4 is allowable in is within our availability, since 40 + 4 = 44.
## now we need 1 more, and we can simply use 1 since 44 + 1 = 45. BOOM.

### We did, 32 + 8 + 4 + 1 == 45

# In binary:

## Below is an illustration of my solution

1 0 1 1 0  1  0   0   0   0  0
| | | | |  |  |   |   |   |  |      ==  45
1 2 4 8 16 32 64 128 256 ... n 

# We are solving for a AND logic gate.

A AND B:	1 if both bits 1
A OR B:		1 if at least one bit 1
A XOR B:	1 if exactly one bit 1  (Exclusive OR)
NOT A:		1 if bit is 0

## An AND gate needs both bits to be true
### our problem is as follow 

#### `0b110` and `0b011` == A = 110 and B = 011
A | B | A AND B
1 | 0 | 0  # False
1 | 1 | 1  # True because both A AND B are 1
0 | 1 | 0  # False


# NOTE: Programming annotation 

A AND B:	A & B
A OR B:		A | B
A XOR B:	A ^ B		(note: xor means exclusive OR)
NOT A:		~A


################################################################################################


'''Answer for Q #3'''
# 3. Convert the 8-bit binary number 0bXXXXXXXX (PM's choice) to hex.

## Thinking. . . 
'''

Ok, binary is a Base 2 system. Which means there are only two possible values to represent 
numbers. (1, 0)

As I described in Q#2, it increments by n^2.

Meaning, 0,1,2,4,8,16,24,32,...,etc.

Hex, or Hexadecimal, is a Base 16 system. 

It goes like this:

        0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F


0bXXXXXXXX == 1 2 4 8 16 32 64 128

Since the binary system is a Based 2 system and increases by n^2, which means each 
increment is multiplied by 2, and we have 8 X's, we do:

    [1], [2] * 2, [4] * 2, [8] * 2, [16] * 2, [32] * 2, [64] * 2, [128]

In the decimal system, which is a Base 10 system, this translates to:

    1 hundred, 2 tens, and 8 units == 128

In Hex, since its a Base 16 system, and our last symbol; F == 15, 
we go back in signify 16 as 10. 

So 10 == 16

or

0,1,2,4,5,6,7,8,9,A,B,C,D,E,F,10,11,12 where 10 == 16, 11 == 17, 12 == 18, etc.

With this info, since 10 == 16, 20 == 32.

Because 16 + 16 = 32 and 10 represents 16, so following the Hex system once more will have 
you iterate through the symbals once more as follows:

    ...f,10, 11, 12, ... , 1f, 20; where 20 == 32. 

Following the logic, we can keep skipping the steps from 10 by using the rule from the binary 
system, which is n^2.

10*2 = 20, 10 is 16 and 16*2 is 32, so 20 == 32. 

20*2 = 40, 20 is 32 and 32*2 is 64, so 40 == 64

40*2 = 80, 40 is 64 and 64*2 is 128, so 80 == 128.

Our binary is 0bXXXXXXXX or, for demonstration, 10000000 which is 128.
128 is our decimal and following the Hex Base 16 system, to get to that binary number 
we would get the result: 80.

so

0bXXXXXXXX == in hex: 0x80 


'''

