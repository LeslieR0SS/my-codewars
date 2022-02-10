def permute_a_palindorme(input):
    isunique = False
    for letter in input:
        letter_count = input.count(letter)
        if letter_count == 1 and not isunique:
            isunique = True 
        elif letter_count %2 != 0:
            return False
    return True 


if __name__ == '__main__':
    assert permute_a_palindorme('aa') == True
    assert permute_a_palindorme('baa') == True
    assert permute_a_palindorme('aab') == True
    assert permute_a_palindorme('baabcd') == False
    assert permute_a_palindorme('racecar') == True
    assert permute_a_palindorme('racecara') == False
