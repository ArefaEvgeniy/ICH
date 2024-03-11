name = 'Adam'
balance = 1234.56

string = f"Hello, {name:*^10}, your balance is {balance:10.1f}. Byu, {name}"
string_2 = "Hello, {:*^10}, your balance is {:10.1f}. Byu, {}".format(name, balance, name)
print(string)
print(string_2)
