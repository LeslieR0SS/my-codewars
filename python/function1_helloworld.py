

from cgi import test


def greet (test):
        
    return ("hello world!")
    
if __name__ == '__main__':
    assert greet("Greet function") == "hello world!"
