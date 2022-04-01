

IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4 = [2, 4, 3, 1]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]

S0 = [['01', '00', '11', '10'],
      ['11', '10', '01', '00'],
      ['00', '10', '01', '11'],
      ['11', '01', '11', '10']]

S1 = [['00', '01', '10', '11'],
      ['10', '00', '01', '11'],
      ['11', '00', '01', '00'],
      ['10', '01', '00', '11']]

dict = {
    '00': 0,
    '01': 1,
    '10': 2,
    '11': 3
}


def str_to_bin(str):
    a = bin(ord(str))
    print(a)
    a = '0'+a[2:]
    return a


def permutate(original, permutation):
    new = ''
    for i in permutation:
        new += original[i-1]
    return new


def left_halff(original):
    return original[:int((len(original)/2))]


def right_halff(original):
    return original[int((len(original)/2)):]


def left_shift(original):
    return original[1:] + original[0]


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new

def lookup_s(s, ss):
    s0 = dict[s[:2]]
    s1 = dict[s[2:]]
    ss0 = dict[ss[:2]]
    ss1 = dict[ss[2:]]
    return S0[s0][s1] + S1[ss0][ss1]




if __name__ == "__main__":
    
    encrypt_str=[]
    print('**** KEY GENERATION ****')
    # step1
    KEY = '1001001110'
    print('Original Key: ', KEY)
    updated_key = ''

    # step2
    print('After P10:', permutate(KEY, P10))
    updated_key = permutate(KEY, P10)

    # step3
    left_half = left_halff(updated_key)
    right_half = right_halff(updated_key)

    print('Left Half:', left_half)
    print('Left Half:', left_half)
    print('Right Half:', right_half)

    # step4
    LS1_LH = left_shift(left_half)
    LS1_RH = left_shift(right_half)

    # step5
    KEY1 = LS1_LH + LS1_RH
    KEY1 = permutate(KEY1, P8)
    print('Key1:', KEY1)

    # step6
    LS2_LH = left_shift(LS1_LH)
    LS2_LH = left_shift(LS2_LH)
    LS2_RH = left_shift(LS1_RH)
    LS2_RH = left_shift(LS2_RH)

    # step7
    KEY2 = LS2_LH + LS2_RH
    KEY2 = permutate(KEY2, P8)
    print('Key2:', KEY2)




    print('\n\n**** ENCRYPTION ****\n')
    print(' # Cycle1 #')

    stri = input('Enter Your message: ')
    for i in stri:
        print(i)
        message = str_to_bin(i)

        # message = '10100001'

        # step1
        updated_message = permutate(message, IP)
        print('After IP:', updated_message)

        # step2
        left_half1 = left_halff(updated_message)
        right_half1 = right_halff(updated_message)
        print('Left Half:', left_half1)
        print('Right Half:', right_half1)

        # step3
        updated_right_half1 = permutate(right_half1, EP)
        print('After EP:', updated_right_half1)

        # step4
        xor_val = xor(updated_right_half1, KEY1)
        print('XOR:', xor_val)

        # step5
        s0 = left_halff(xor_val)
        s1 = right_halff(xor_val)
        print('After Substitution:', lookup_s(s0, s1))
        s = lookup_s(s0, s1)

        # step6
        p4 = permutate(s, P4)
        print('After P4:', p4)

        # step7
        xor_val = xor(left_half1, p4)
        
        # step8
        updated_message = right_half1 + xor_val
        print('After 1st Cycle:', updated_message)

        
        print('\n # Cycle2 #')
        # step2
        left_half1 = left_halff(updated_message)
        right_half1 = right_halff(updated_message)
        print('Left Half:', left_half1)
        print('Right Half:', right_half1)

        # step3
        updated_right_half1 = permutate(right_half1, EP)
        print('After EP:', updated_right_half1)

        # step4
        xor_val = xor(updated_right_half1, KEY2)
        print('XOR:', xor_val)

        # step5
        s0 = left_halff(xor_val)
        s1 = right_halff(xor_val)
        print('After Substitution:', lookup_s(s0, s1))
        s = lookup_s(s0, s1)

        # step6
        p4 = permutate(s, P4)
        print('After P4:', p4)

        # step7
        xor_val = xor(left_half1, p4)
        
        # step8
        updated_message = right_half1 + xor_val
        print('After 2nd Cycle:', updated_message)

        # step9
        encrypted_message = permutate(updated_message, IP_INVERSE)
        print('\nEncrypted Bits:', encrypted_message)
        aaa = chr(int(encrypted_message, 2))
        encrypt_str.append(aaa)

    
    print('bits to text:', encrypt_str)


