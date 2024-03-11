string = "{:{fill}{align}{width}}"
print(string.format('cat', fill='*', align='^', width=5))

print("{:*^5}".format('cat', fill='*', align='^', width=5))
print("{:{fill}{align}{width}}}".format('cat', fill='*', align='^', width=5))
