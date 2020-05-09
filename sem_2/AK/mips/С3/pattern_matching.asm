.globl check_match
# FUNC - verifies if assembly instruction matches a specific pattern
# special chars: * - register number, & - immediate value, # - one word
# args: $a0 - address of string to verify, $a1 - address of pattern
check_match:
  li $t1, 0         # string iterator
  li $t2, 0         # pattern iterator
  
  c_i_m_next_iter:
    add $t3, $a0, $t1  # string char address
    add $t4, $a1, $t2  # pattern char address

    lb $t5, 0($t3)     # string char
    lb $t6, 0($t4)     # pattern char
    lb $t7, 1($t3)     # string next char
    
    # end of string & pattern
    seq $s0, $t5, $zero
    seq $s0, $t5, 0xa
    seq $s1, $t6, $zero
    and $s0, $s0, $s1
    beq $s0, 1, c_i_m_succ_end
 
    # string ended and pattern not
    beq $t5, $zero, c_i_m_fail_end
    # pattern ended and string not
    beq $t6, $zero, c_i_m_fail_end
    
    beq $t6, 0x2a, check_register_num   # *
    beq $t6, 0x26, check_immediate_val  # &
    beq $t6, 0x23, check_one_word       # #
    j check_direct_match

    check_register_num:
      beq $t7, 0x2c, check_one_digit_num  # if next char is comma
      beq $t7, $zero, check_one_digit_num # if end of string
      beq $t7, 0xa, check_one_digit_num   # if end of string
      j check_two_digit_num

      # check if number is in range 0..9
      check_one_digit_num:
        sgt $s0, $t5, 0x2f
        slti $s1, $t5, 0x3a
        and $s0, $s0, $s1
        bne $s0, 1, c_i_m_fail_end
        add $t1, $t1, 1
        add $t2, $t2, 1
        j c_i_m_next_iter
      
      # check if number is in range 0..31
      check_two_digit_num:
        # check first char (should be <= 3)
        sgt $s0, $t5, 0x30
        slti $s1, $t5, 0x34
        and $s0, $s0, $s1
        bne $s0, 1, c_i_m_fail_end
        
        # check second char
        sgt $s0, $t7, 0x2f
        slti $s1, $t7, 0x3a
        and $s0, $s0, $s1
        bne $s0, 1, c_i_m_fail_end
        
        seq $s0, $t5, 0x33 # if first char is 3
        sgt $s1, $t7, 0x31 # if second char is > 1
        and $s0, $s0, $s1
        beq $s0, 1, c_i_m_fail_end # num is > 31
        
        add $t1, $t1, 2
        add $t2, $t2, 1
        j c_i_m_next_iter

    check_immediate_val:
      sgt $s0, $t5, 0x2f
      slti $s1, $t5, 0x3a
      and $s0, $s0, $s1
      bne $s0, 1, c_i_m_fail_end
      
      beq $t7, $zero, end_of_immediate_val
      beq $t7, 0xa, end_of_one_word
      # do not increment pattern iterator to check next digit
      add $t1, $t1, 1
      j c_i_m_next_iter
      
      end_of_immediate_val:
        add $t1, $t1, 1
        add $t2, $t2, 1
        j c_i_m_next_iter
                

    check_one_word:
      # allow only a-z
      sgt $s0, $t5, 0x60
      slti $s1, $t5, 0x7b
      and $s0, $s0, $s1
      bne $s0, 1, c_i_m_fail_end
      
      beq $t7, $zero, end_of_one_word
      beq $t7, 0xa, end_of_one_word
      # do not increment pattern iterator to check next char
      add $t1, $t1, 1
      j c_i_m_next_iter
      
      end_of_one_word:
        add $t1, $t1, 1
        add $t2, $t2, 1
        j c_i_m_next_iter
    
    check_direct_match:
      bne $t5, $t6, c_i_m_fail_end
      add $t1, $t1, 1
      add $t2, $t2, 1
      j c_i_m_next_iter

  c_i_m_succ_end:
    li $v0, 1
    jr $ra
  
  c_i_m_fail_end:
    li $v0, 0
    jr $ra
