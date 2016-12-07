# from string import maketrans
# intab = "aeiou"
# outtab = "12345"
# transtab = maketrans(intab, outtab)
#
# str = "Testing, Testing; One, Two, Three"
# print str.maketrans(transtab)

import string
trans = string.maketrans('ae', 'bx')
text = 'abcdef'
print text.translate(trans)
