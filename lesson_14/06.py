name = 'Adam'
balance = 1234.56

string = "Hello, %s, your balance is %d. Byu, %s" % (name, balance, name)
string_2 = "Hello, %(name)s, your balance is %(balance)d. Byu, %(name)s" % {'name': name, 'balance': balance}
print(string)
print(string_2)
