def word_multiply(string: str, repeat: int = 1) -> str:
    return string * repeat


text = 'python'
print(word_multiply(text, 2))  # => pythonpython
print(word_multiply(text, 0))  # =>
print(word_multiply(text))  # => 'python'