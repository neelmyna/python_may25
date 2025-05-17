s = 'a t m e'
characters = s.split(' ')
print(characters) # ['a', 't', 'm' 'e']

s = 'm y s u r u'
characters = s.split()
print(characters)

s = 'a@t@m e'
characters = s.split('@')
print(characters) # ['a', 't', 'm e']

s2 = ''.join(characters)
print(s2) # 'at m e'

s3 = ''.join(characters)
print(s2) # 'atm e'