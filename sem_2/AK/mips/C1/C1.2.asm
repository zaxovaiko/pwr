# Second program
# Basic operations with numbers
.data
	welcome: .asciiz "\nCzy wykonac kolejne dzialanie? (0/1)(Nie/Tak): "
.text

while:	
	# Read operation
	li $v0, 5
	syscall
	move $s0, $v0
	
	# Read b
	li $v0, 5
	syscall
	move $s1, $v0

	# Read c
	li $v0, 5
	syscall
	move $s2, $v0
	
	# Read d
	li $v0, 5
	syscall
	move $s3, $v0
	
	# Compare each expression with input
	beq $s0, 1, fexp
	beq $s0, 2, sexp
	beq $s0, 3, texp

# a = (b + c) ? d
fexp: 
	add $a0, $s1, $s2
	sub $a0, $a0, $s3
	j exit

# a = b - (c + d)
sexp:	
	add $a0, $s2, $s3
	sub $a0, $s1, $a0
	j exit

# a = (b - c) + d
texp: 
	sub $a0, $s1, $s2
	add $a0, $s3, $a0
	j exit
	
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