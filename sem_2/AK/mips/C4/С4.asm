.data
	welcome: 	.asciiz "\nWybierz operacje (1 +, 2 -, 3 *, 4 /): "
	aMsg: 		.asciiz "\nLiczba a: " 
	bMsg: 		.asciiz "Liczba b: "
	error: 		.asciiz "Niepoprawna liczba\n"
	zero: 		.asciiz  "Dzielenie przez zero\n"
	result: 	.asciiz "Wynik: "
	exit: 		.asciiz "\nWprowadz 0 zeby skonczyc program: "
	zeroD: 		.double 0

	# handle exceptions
	.ktext 0x80000180
	
	move $t0, $a0
	la $a0, error
	li $v0, 4
	syscall
	
	move $a0, $t0
	li $s7, 1
	mfc0 $k0, $14 		# get return address
	addiu $k0, $k0, 4   # jum to next opration (after syscall)
	jr $k0


.text
j start

# FUNC: reads double with excpetion handling
# args: $a0 - title msg
# return: $f0
read_double:
  	li $v0, 4
  	syscall
  	li $s7, 0  # reset exception indicator 
  	li $v0, 7
  	syscall
  	beq $s7, 1, read_double # exception occured
  	jr $ra

start:
  	la $a0, welcome
  	li $v0, 4
  	syscall

  	li $s7, 0  # reset exception indicator
  	li $v0, 5
  	syscall
  	beq $s7, 1, start  # exception occured
  	move $s0, $v0

  	blt $s0, 1, start
  	bgt $s0, 4, start

  	# read first argument
  	la $a0, aMsg
  	jal read_double
  	mov.d $f2, $f0
  
  	# read second argument
  	la $a0, bMsg
  	jal read_double

	# Operacji
  	beq $s0, 1, _add
  	beq $s0, 2, _sub
  	beq $s0, 3, _mul
  	beq $s0, 4, _div

  _add:
    add.d $f12, $f2, $f0
    j print

  _sub:
    sub.d $f12, $f2, $f0
    j print

  _mul:
    mul.d $f12, $f2, $f0
    j print
  
  _div:
    l.d $f4, zeroD
    c.eq.d $f0, $f4
    bc1f next
    
    la $a0, zero
    li $v0, 4
    syscall
    j start

    next:
      div.d $f12, $f2, $f0,
      j print

  print:
    la $a0, result
    li $v0, 4
    syscall
    li $v0, 3
    syscall
    
    la $a0, exit
    li $v0, 4
    syscall
    
    li $v0, 5
    syscall
    
    bne $v0, 0, start