def square(n):
    return n * n

if __name__  ==  '__main__':
    
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square(2), 4)
        test.assert_equals(square(50), 2500)
        test.assert_equals(square(1), 1)