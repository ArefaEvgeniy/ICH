from functools import partial


def say(a, b, c='!'):
    print(a, b, c)


say('Bye', 'Mike')
say('Hello', 'world', c='.')
new_say = partial(say, 'Hello', c='?', b='Jack')
new_say()
