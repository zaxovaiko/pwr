.data

help_msg: .asciiz "\nAvailable instructions:\nADD $1, $2, $3\nADDI $1, $2, value\nJ label\nNOOP\nMULT $1, $2\nJR $1\nJAL label"
enter_inst_msg: .asciiz "\nEnter your instruction: "
wrong_inst_msg: .asciiz "\nInstruction you've enterd is incorrect" 
number_of_inst_msg: .asciiz "\nNumber of instructions (1-5): "
stack_msg: .asciiz "\nStack of instructions and their args: \n"

# instrcutions patters
add_inst: .asciiz "ADD $*, $*, $*"
addi_inst: .asciiz "ADDI $*, $*, &"
j_inst: .asciiz "J #"
noop_inst: .asciiz "NOOP"
mult_inst: .asciiz "MULT $*, $*"
jr_inst: .asciiz "JR $*"
jal_inst: .asciiz "JAL #"
instruction_buffer: .space 30


.text
program_start:
  move $s6, $sp     # store stack bottom
  li $v0, 4
  la $a0, help_msg
  syscall

  read_num_of_instructions:
    li $v0, 4
    la $a0, number_of_inst_msg
    syscall
    
    li $v0, 5
    syscall
    
    blt $v0, 1, read_num_of_instructions
    bgt $v0, 5, read_num_of_instructions
    
    move $s7, $v0
    j read_instruction

  read_instruction:
    beq $s7, $zero, program_end

    li $v0, 4
    la $a0, enter_inst_msg
    syscall

    li $v0, 8
    la $a0, instruction_buffer
    li $a1, 30
    syscall
    
    li $v0, 0
    
    # check instruction validity
    la $a1, j_inst
    jal check_match
    beq $v0, 1, next_iter

    la $a1, add_inst
    jal check_match
    beq $v0, 1, next_iter

    la $a1, addi_inst
    jal check_match
    beq $v0, 1, next_iter
    
    
    la $a1, noop_inst
    jal check_match
    beq $v0, 1, next_iter
    
    la $a1, mult_inst
    
    jal check_match
    beq $v0, 1, next_iter
    
    la $a1, jr_inst
    jal check_match
    beq $v0, 1, next_iter
    
    la $a1, jal_inst
    jal check_match
    beq $v0, 1, next_iter

    j wrong_inst

    next_iter:
      sub $s7, $s7, 1
      jal push_instruction_to_stack
      j read_instruction

     wrong_inst:
       li $v0, 4
       la $a0, wrong_inst_msg
       syscall
       j read_instruction
 
  program_end:
    la $a0, stack_msg
    li $v0, 4
    syscall

    move $a0, $s6
    jal print_instructions_from_stack
    li $v0, 10
    syscall
