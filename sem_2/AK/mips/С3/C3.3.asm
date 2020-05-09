.data
	enter:  .asciiz "Wprowadz instrukcji: "
	wrong:  .asciiz "Instrukcja jest niepoprawna."
	help: 	.asciiz "\nDostepne instrukcji: \nMULT $1, $2\nNOOP\nJ label\nADD $1, $2, $3\nADDI $1, $2, value\nJR $1\nJAL label"
	number: .asciiz "\nWprowadz ilosc instrukcji (1-5): "
	stack: 	.asciiz "\nStos z instrukcjami: \n"
	memory: .asciiz "Uzyta pamiec: "

	_add: 	.asciiz "ADD $*, $*, $*"
	_addi: 	.asciiz "ADDI $*, $*, &"
	_j: 	.asciiz "J #"
	_noop: 	.asciiz "NOOP"
	_mult: 	.asciiz "MULT $*, $*"
	_jr: 	.asciiz "JR $*"
	_jal: 	.asciiz "JAL #"
	buffer: .space 30

.text

# Zaczynamy program
start:
  move $s6, $sp # Tworzymy stos
  li $v0, 4
  la $a0, help
  syscall

# Czytamy ilosc instrukcji
readNum:
    li $v0, 4
    la $a0, number
    syscall
    
    li $v0, 5
    syscall
    
    blt $v0, 1, readNum
    bgt $v0, 5, readNum
    
    move $s7, $v0
    j read
   
# Czytamy instrukcje
read:
    beq $s7, $zero, end

    li $v0, 4
    la $a0, enter
    syscall

    li $v0, 8
    la $a0, buffer
    li $a1, 30
    syscall
    
    li $v0, 0
    
    # Sprawdzamy poprawnosc instrukcji
    la $a1, _j
    jal match
    beq $v0, 1, next

    la $a1, _add
    jal match
    beq $v0, 1, next

    la $a1, _addi
    jal match
    beq $v0, 1, next
    
    la $a1, _noop
    jal match
    beq $v0, 1, next
    
    la $a1, _mult
    jal match
    beq $v0, 1, next
    
    la $a1, _jr
    jal match
    beq $v0, 1, next
    
    la $a1, _jal
    jal match
    beq $v0, 1, next
    
    j wrongInstuction

	# Idziemy do nastepnego
    next:
      sub $s7, $s7, 1
      jal push
      j read

	# Wyswietlamy niepoprawnosc instrukcji
    wrongInstuction:
       li $v0, 4
       la $a0, wrong
       syscall
       j read

# Wyswietlamy stos i konczymy program
end:
    la $a0, stack
    li $v0, 4
    syscall

    move $a0, $s6
    jal print
    li $v0, 10
    syscall
 
# Sprawdzamy poprawnosc instrukcji 
match:
    li $t1, 0 # iterator dla stringa
    li $t2, 0 # iterator dla schematu
  
  matchNext:
    add $t3, $a0, $t1 # addresses
    add $t4, $a1, $t2

    lb $t5, 0($t3) # str[i]
    lb $t6, 0($t4) # regex[i]
    lb $t7, 1($t3) # str[i + 1]
    
    # Koniec stringow
    seq $s0, $t5, 0
    seq $s0, $t5, 10
    seq $s1, $t6, 0
    and $s0, $s0, $s1
    beq $s0, 1, matchSuccess
   
    beq $t5, 0, matchfail # Jezeli len(str) < len(reg)
    beq $t6, 0, matchfail # Jezeli len(str) > len(reg)
    
    beq $t6, 42, regnum   # *
    beq $t6, 38, immedval # &
    beq $t6, 35, oneword  # #
    j dirmatch

    regnum:
      beq $t7, 44, onedigit  # == ','
      beq $t7, 0, onedigit # == null
      beq $t7, 10, onedigit   # == '\n'
      j twodigits

      # in [0..9]
      onedigit:
        sgt $s0, $t5, 47
        slti $s1, $t5, 58
        and $s0, $s0, $s1
        bne $s0, 1, matchfail
        add $t1, $t1, 1
        add $t2, $t2, 1
        j matchNext
      
      # in [0..31]
      twodigits:
        # num[0] < 3
        sgt $s0, $t5, 48
        slti $s1, $t5, 52
        and $s0, $s0, $s1
        bne $s0, 1, matchfail
        
        # num[1]
        sgt $s0, $t7, 47
        slti $s1, $t7, 58
        and $s0, $s0, $s1
        bne $s0, 1, matchfail
        
        seq $s0, $t5, 51 # num[0] == 3
        sgt $s1, $t7, 49 # num[1] > 1
        and $s0, $s0, $s1
        beq $s0, 1, matchfail # num > 31
        
        add $t1, $t1, 2
        add $t2, $t2, 1
        j matchNext

    immedval:
      sgt $s0, $t5, 47
      slti $s1, $t5, 58
      and $s0, $s0, $s1
      bne $s0, 1, matchfail
      
      beq $t7, 0, endImmedval
      beq $t7, 10, wordend
      
      add $t1, $t1, 1 # do not increment pattern iterator to check next digit
      j matchNext
      
      endImmedval:
        add $t1, $t1, 1
        add $t2, $t2, 1
        j matchNext

    oneword:
      # allow only a-z
      sgt $s0, $t5, 96
      slti $s1, $t5, 123
      and $s0, $s0, $s1
      bne $s0, 1, matchfail
      
      beq $t7, 0, wordend
      beq $t7, 10, wordend
      # do not increment pattern iterator to check next char
      add $t1, $t1, 1
      j matchNext
      
     wordend:
        	add $t1, $t1, 1
        	add $t2, $t2, 1
        	j matchNext
    
    # Sprawdzamy
	dirmatch:
      	bne $t5, $t6, matchfail
      	add $t1, $t1, 1
      	add $t2, $t2, 1
      	j matchNext

# Jezeli instrukcja jest poprawna
matchSuccess:
    li $v0, 1
    jr $ra
    
# Jezeli instrukcja jest niepoprawna
matchfail:
    li $v0, 0
    jr $ra
    
# Dodajemy instrukcje do stosu
# a0 - inst address?
push:
    li $t0, 0 # length
    li $t2, 0 # inst 

# Bierzemy dlugosc instrukcji
length:
    add $t3, $a0, $t0  # char address
    lb $t4, 0($t3)     # inst[i]

    beq $t4, 0, pushChar  # inst[i] == null
    beq $t4, 10, pushChar # inst[i] == '\n'

    add $t0, $t0, 1
    j length

pushChar:
    sub $t0, $t0, 1
    blt $t0, 0, pushEnd
    add $t3, $a0, $t0 # char address
    lb $t4, 0($t3)    # char

    beq $t4, 32, pushNextPart # if ' ' don't push

    add $t6, $sp, $t2  # byte address
    sb $t4, 0($t6)     # store chr  
 
    add $t2, $t2, 1
    j pushChar

	# Resetujemy $t2
    pushNextPart:
        add $sp, $sp, 4 # $sp += 4
        li $t2, 0       # reset
        
        j pushChar

    pushEnd:
        add $sp, $sp, 4
        jr $ra

# Wyswietlamy instrukcje
# a0 - koniec stosa
print:
    move $t0, $a0      # cp stack bot
	addi $t3, $zero, 0 # counter for memory

    printNextWord:
    	blt $sp, $t0, printEnd

    	# Wyswietlamy kazde wyrazenie
    	li $v0, 11
    	lb $a0, -1($sp)
    	syscall
    	lb $a0, -2($sp)
    	syscall
    	lb $a0, -3($sp)
    	syscall
    	lb $a0, -4($sp)
    	syscall

    	li $a0, 10 # \n
    	li $v0, 11
    	syscall

		add $t3, $t3, 1
    	add $sp, $sp, -4
    	j printNextWord

# Wyswietlamy koniec programu
printEnd:
	li $v0, 4
	la $a0, memory
	syscall

	mul $t3, $t3, 4
	li $v0, 1
	move $a0, $t3
	syscall
	
    jr $ra
