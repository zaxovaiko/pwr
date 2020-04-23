# First program
# Basic math operations
.data
	welcome: .asciiz "\nCzy wykonac kolejne dzialanie? (0/1)(Nie/Tak): "
.text

# While loop
while:	
	# Read operation's number
	li $v0, 5
	syscall
	move $s0, $v0
	
	# Read first number
	li $v0, 5
	syscall
	move $s1, $v0

	# Read second number
	li $v0, 5
	syscall
	move $s2, $v0
	
	# Compare each op's number with input
	beq $s0, 1, addnum
	beq $s0, 2, minnum
	beq $s0, 3, mulnum
	beq $s0, 4, divnum

# Multiply nums
mulnum: 
	mul $a0, $s1, $s2
	j exit
	
# Divide nums
divnum:	
	div $a0, $s1, $s2 
	j exit
	
# Substract nums
minnum: 
	sub $a0, $s1, $s2
	j exit

# Add two nums
addnum:	
	add $a0, $s1, $s2
	j exit
	
# Use exit to stop program
exit:
	# Print result
	li $v0, 1
	syscall	
	
	# Write 'do you want to continue?'
	li $v0, 4
	la $a0, welcome
	syscall
	
	# Read user's response
	li $v0, 5
	syscall
	
	# Check if user want to continue
	# If not then stop program
	beq $v0, 1, while
	
	li $v0, 10
	syscall
	
