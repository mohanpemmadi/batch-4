
# file_name
# mode - read,write and append

''' Read '''

'''
# fp = open('sample.txt','r')

fp = open('sample.txt')

print(fp.name)
print(fp.mode)

print(fp.read())
print(type(fp.read()))
print(fp.read(11))
print(fp.readlines())

print(fp.closed)
print('#########')
fp.close()
print(fp.closed)

'''

''' write '''

# wp = open('sample2.txt','w')
# wp.write('hi abc\n')
# wp.write('hi xyzq')
# wp.writelines(['python\n','java\n','php'])


''' append '''

ap = open('sample3.txt','a')
# # ap.write('hello python')
ap.write('\nhello php')




