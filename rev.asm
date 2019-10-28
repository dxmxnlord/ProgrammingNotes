# data declaration section of code
.data 

# reserve space for the input string of max 12 bytes or characters
# the same will be used for the output string
input: .space 12 
# message to display
output: .asciiz "Enter the string between 0 and 11 characters: "

# actual code 
.text

# this section makes the inital steps like input/output and 
# pushing a marker to the mips stack and storing the string base address
main:
        # make a system call to print the output message
        la $a0, output 
        li $v0, 4
        syscall
        # make a system call to read the input 
        li $v0, 8
        la $a0, input
        li $a1, 12
        syscall
        # add a marker to the bottom of the mips stack to signify the end of the string.
        li $t0, 0
        subu $sp, $sp, 4
        sw $t0, ($sp)
        # load base address of string
        la $t1, input

# this section is to push each letter of the string into the mips stack
push:
        # load the character into the t0 register (byte for a character )
        lbu $t0, 0($t1)
        # if the end of the string is reached, go to reset 
        beqz $t0, reset
        # shift stack ponter to accomodate the character
        subu $sp, $sp, 4
        # store the character
        sw $t0, ($sp)
        # increment address
        addu $t1, $t1, 1
        # repeat
        j push
        
# reset the t1 register to contain the base address again
reset: la $t1, input

# pop characters from the stack to make a string
pop:
        # load character from the stack
        lw $t0, ($sp)
        # shift the stack pointer to point to previous ( but now next ) character
        addu $sp, $sp, 4
        # if the base marker is reached, go to exit
        beqz $t0, exit
        # replace the character in the input string
        sb $t0, 0($t1)
        # increment address
        addu $t1, $t1, 1
        # repeat
        j pop
        
exit: 
        # system call to print string
        li $v0, 4
        la $a1, input
        syscall
        # system call to exit program
        li $v0, 10
        syscall