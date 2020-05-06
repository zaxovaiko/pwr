# Wszystko bedzie lowercasem
.data
  o:   .asciiz "Wprowadz numer operacji (1-S, 2-D): "
  next:   .asciiz "\nContynuowac wykonanie programu? (1-Tak, 2-Nie): "
  key:   .asciiz "Wprowadz klucz: "
  text:   .asciiz "Wprowadz tekst (max 50): "
  r:   .asciiz "Wynik: "
  
  s: .space 50
  k: .word
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
  
  # read and store key to memory
  li $v0, 5
  syscall
  sw $v0, k
  
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
# s1 - w, wyrazenie
# s3 - w[i]
# s5 = k
# s6 = (w[i] + k) % 26, (s3 + s5) % 26
encode:
  la $s1, s
  
  e.loop:
    lb $s3, 0($s1)
    add $t1, $s3, 0
    
    beq $s3, 10, e.endloop
    blt $s3, 65, e.continue  # char < 'A' && char > 'Z'
    bgt $s3, 90, e.continue

    lw $s5, k
    li $t0, 26
    
    subi $s3, $s3, 65
    
    add $s6, $s3, $s5    # w[i] + k
    div $s6, $t0       # (w[i] + k) % 26
    
    mfhi $t1
    addi $t1, $t1, 65
    
    move $a0, $t1    # don't encode some
    li $v0, 11         # print decoded
    syscall
    
    e.continue:
      addi $s1, $s1, 1
      j e.loop
  e.endloop:
    j exit

# Deszyfrowanie  
# s0 - len(k), dlugosc klucza
# s1 - w, wyrazenie
# s3 - w[i]
# s6 = (w[i] - k) % 26, (s2 - s5) % 26
decode:    
  la $s1, s
  
  d.loop:
    lb $s3, 0($s1)
    addi $t1, $s3, 0

    beq $s3, 10, d.endloop
    blt $s3, 65, d.continue  # char < 'a' && char > 'z'
    bgt $s3, 90, d.continue
    
    subi $s3, $s3, 65 
    
    lw $s5, k
    li $t0, 26
    
    subu $s6, $s3, $s5  # w[i] - k
	blt $s6, 0, add_t
	
	cont: 
    div $s6, $t0       # (w[i] - k) % 26 (4 - 5) % 26
    
    mfhi $t1
    addi $t1, $t1, 65
    
    move $a0, $t1    # don't encode some
    li $v0, 11         # print decoded
    syscall
    
    d.continue:
      addi $s1, $s1, 1
      j d.loop

  d.endloop:
    j exit
    
add_t:
	addi $s6, $s6, 26
	j cont