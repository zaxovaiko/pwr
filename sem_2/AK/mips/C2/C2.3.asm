# Wszystko bedzie lowercasem
.data
	o: 	.asciiz "Wprowadz numer operacji (1-S, 2-D): "
	next: 	.asciiz "\nContynuowac wykonanie programu? (1-Tak, 2-Nie): "
	key: 	.asciiz "Wprowadz klucza (max 8): "
	text: 	.asciiz "Wprowadz tekst (max 50): "
	r: 	.asciiz "Wynik: "
	
	s: .space 50 # attackatdawn
	k: .space 8  # lxfopvefrnhr | lemon
.text

# Czytamy dane
read:
	li $v0, 4
	la $a0, o	
	syscall
	
	li $v0, 5 # czytamy operacje
	syscall
	move $t8, $v0
	
	li $v0, 4
	la $a0, key
	syscall
	
	li $v0, 8 # czytamy klucza
	la $a0, k
	la $a1, 8
	syscall
	
	li $v0, 4
	la $a0, text
	syscall
	
	li $v0, 8 # czytamy wyrazenie
	la $a0, s
	la $a1, 50
	syscall
		
	li $v0, 4
	la $a0, r
	syscall
	
	# Szukamy dlugosc klucza
	keylen:
		la $t0, k
		
		keylen.loop:
    			lb $t1, 0($t0) 		# t1 = next	
    			beq $t1, 10, keylen.end # next == null ? break		
    			beq $t1, 0, keylen.end  # next == '\n' ? break
    			addi $t0, $t0, 1 	# address++
    				
    			j keylen.loop
    			
		keylen.end:
			la $t1, k
			sub $s0, $t0, $t1
	
	beq $t8, 1, encode
	beq $t8, 2, decode
		
	j exit
			
# Contuonowac?
exit:
	li $v0, 4
	la $a0, next
	syscall 
	
	li $v0, 5 # czytamy odpowiedz
	syscall
		
	beq $v0, 1, read
	beq $v0, 2, stop
	
# Exit
stop:
	li $v0, 10
	syscall
	
# Szyfrowanie
# s0 - len(k), dlugosc klucza
# s1 - w, wyrazenie
# s2 - i, indeks
# s3 - w[i]
# s4 = i % len(k), s2 % s0
# s5 = k[i % len(k)], k[s4]
# s6 = (w[i] + k[i % len(k)]) % 26, (s2 + s5) % 26
encode:
	la $s1, s
	addi $s2, $zero, 0 # potrzebno dla formuly, i = 0
	
	e.loop:
		lb $s3, 0($s1)
		add $t1, $s3, 0
		
		#beq $s3, 0,  d.endloop
		beq $s3, 10,  e.endloop
		blt $s3, 97,  e.continue	# char < 'a' && char > 'z'
		bgt $s3, 122, e.continue
		
		# i % len(k)
		div $s2, $s0
		mfhi $s4
		
		# s5 = k[i % len(k)]
		# indeks dla klucza, j = 0
		la $t0, k
		addi $t1, $zero, 0 
		
		e.get.loop:
			lb $s5, k($t1) 		# k[i]
			beq $t1, $s4, e.get.end # j == i % len(k) ? break
    			addi $t1, $t1, 1	# j++
			j e.get.loop
				
		e.get.end:
			subi $s5, $s5, 97 	# ord() - 97
		
		subi $s3, $s3, 97
		
		li $t0, 26
		add $s6, $s3, $s5		# w[i] + k[i % len(k)]
		div $s6, $t0 			# (w[i] + k[i % len(k)]) % 26
		
		mfhi $t1
		addi $t1, $t1, 97
		
		move $a0, $t1		# don't encode some
		li $v0, 11 		# print decoded
		syscall
		
		e.continue:
			addi $s2, $s2, 1
			addi $s1, $s1, 1
			j e.loop
	e.endloop:
		j exit

# Deszyfrowanie	
# s0 - len(k), dlugosc klucza
# s1 - w, wyrazenie
# s2 - i, indeks
# s3 - w[i]
# s4 = i % len(k), s2 % s0
# s5 = k[i % len(k)], k[s4]
# s6 = (w[i] - k[i % len(k)] + 26) % 26, (s2 - s5 + 26) % 26
decode:		
	la $s1, s
	addi $s2, $zero, 0 # potrzebno dla formuly, i = 0
	
	d.loop:
		lb $s3, 0($s1)
		addi $t1, $s3, 0
		
		#beq $s3, 0,  d.endloop
		beq $s3, 10,  d.endloop
		blt $s3, 97,  d.continue	# char < 'a' && char > 'z'
		bgt $s3, 122, d.continue
		
		# i % len(k)
		div $s2, $s0
		mfhi $s4
		
		# s5 = k[i % len(k)]
		# indeks dla klucza, j = 0
		la $t0, k
		addi $t1, $zero, 0 
		
		d.get.loop:
			lb $s5, k($t1) 		# k[i]
			beq $t1, $s4, d.get.end # j == i % len(k) ? break
    			addi $t1, $t1, 1	# j++
			j d.get.loop
				
		d.get.end:
			subi $s5, $s5, 97 	# ord() - 97
		
		subi $s3, $s3, 97
		
		li $t0, 26
		sub $s6, $s3, $s5		# w[i] - k[i % len(k)]  + 26
		add $s6, $s6, 26
		div $s6, $t0 			# (w[i] - k[i % len(k)] + 26) % 26
		
		mfhi $t1
		addi $t1, $t1, 97
		
		move $a0, $t1		# don't encode some
		li $v0, 11 		# print decoded
		syscall
		
		d.continue:
			
		
			addi $s2, $s2, 1
			addi $s1, $s1, 1
			j d.loop
	d.endloop:
		j exit	
