
def make_negative( number ):
    if number > 0:
        return number * -1
    return number
    if number == 0:
        return none 
    
    
    ### aaqui la linea 6y 7 se ven raras pero en el codewars me funciona:/??

def make_negative( number ):
    if number > 0 :
        return number * -1
    if number <= 0 :
        return number

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(make_negative(42),-42)
        test.assert_equals(make_negative(-9),-9)
        test.assert_equals(make_negative(0),0)
        