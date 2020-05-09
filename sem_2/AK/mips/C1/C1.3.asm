.data
	next:   .asciiz "\nCzy wykonac kolejne dzialanie? (0/1)(Nie/Tak): "
	enterO: .asciiz "Wprowadz opecje (1/2) (x^n, x): "
	enterX:	.asciiz "Wprowadz x: "
	enterN:	.asciiz "Wprowadz n: "
	less: 	.asciiz "Stopien jest mniejszy od zera."
	error: 	.asciiz "Overflow. Sproboj mniejsza liczbe."
.text

main:
	li $v0, 4
	la $a0, enterO
	syscall

	li $v0, 5
	syscall
	move $s0, $v0
	
	li $v0, 4
	la $a0, enterX
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	beq $s0, 1, exp
	beq $s0, 2, fac

fac: 
	li $t1, 1
	
	factorial: 
		mulu $t1, $t1, $t0	  # x * (x - 1) * ...
	 	subi $t0, $t0, 1 	  # -1, 
 		bge $t0, 1, factorial # powtorzac dopoki $t0 >= 1
	 
	move $a0, $t1
	j result

showError:
	li $v0, 4
	la $a0, error
	syscall
	j exit

exp:
	li $v0, 4
	la $a0, enterN
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0
	
	bltz $t1, lessZero
	li $t3, 1
	
	pow: 
		mulo $t3, $t3, $t0 # x * x
		subi $t1, $t1, 1   # -1
 		bge $t1, 1, pow    # powtorzac dopoki $t1 >= 1
	
	move $a0, $t3
	j result

errorMsg:
	li $v0, 4
	la $a0, error
	syscall
	j exit

lessZero:
	li $v0, 4
	la $a0, less
	syscall
	j exit

result:
	li $v0, 1
	syscall	
	j exit

exit:
	li $v0, 4
	la $a0, next
	syscall
	
	li $v0, 5
	syscall
	
	beq $v0, 1, main
	li $v0, 10
	syscall