def func(a='shout'):
    def shout(word='Yes'):
        return word + '!'

    def whisper(word='Yes'):
        return word.lower() + '...'

    if a == 'shout':
        return shout
    else:
        return whisper


talk = func('WW')
print(talk())

print(func('uu')('Andry'))
