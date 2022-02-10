def to_camel_case(text):
    text = text.title()
    text = text.replace('_','')
    return text

if __name__ == '__main__':
    assert to_camel_case('The_stealth_warrior') == 'TheStealthWarrior'