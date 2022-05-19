
"""

Set is a collection of unique elements

* mutable
* unordered
* unindexed
* unchangeable - values in the set are immutables

"""

# sample_set = {1,2,3}
# sample_set = set((1,2,3))
# print(type(sample_set))
lst = [5,4,1,2,3,1,2,1,1,4]
# print(lst)
st = {5,4,1,2,3,1,2,1,1,4}

# print(lst[0])
# lst[0] = 500
# print(lst)
# print(st[0])

# print(dir(st))

''' add '''

st.add('abc')
st.add('xyz')
# print(st)

''' update '''

st1 = {100, 200}

st.update(st1)
# print(st)

''' discard '''

# st.discard(100)
# st.discard(1000)
#
# print(st)


''' remove '''

# st.remove(100)
# st.remove(1000)
#
# print(st)

''' pop - removes random value'''

st.pop()

# print(st)
# st.pop()
# print(st)
# st.pop()
# print(st)
# st.pop()
# print(st)

# print(dir(st))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

''' union '''
# print('A-',A)
# print('B-',B)
#
# print(A.update(B))
# print(B.union(A))
#
# print('A-',A)
# print('B-',B)

''' intersection '''

# print(A.intersection(B))


lst = [5,1,2,3,4,1,2,3]

# print(set(lst))


num = 4

for i in range(2,num):
    if num%i == 0:
        print('not a prime number')
        break
else:
    print('prime number')


