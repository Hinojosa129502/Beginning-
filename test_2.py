import string
trans = string.maketrans('ae', 'bx')
text = 'abcdef'
print text.translate(trans)

trans_2 = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
test_string = 'fcjjm fmu ypc wms'
print test_string.translate(trans_2)

trans_3 = string.maketrans(string.digits, string.digits[3:] + string.digits[:3])
test_string_2 = '137263'
print test_string_2.translate(trans_3)
