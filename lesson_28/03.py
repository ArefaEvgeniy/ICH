from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["apple"] = 5
ordered_dict[99] = 99
ordered_dict["banana"] = 2
ordered_dict[5] = 55
ordered_dict["orange"] = 8
ordered_dict[1] = 11

print(ordered_dict)

for item in ordered_dict.values():
    print(item)
