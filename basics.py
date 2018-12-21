# string interpolation
testString = "Hello World {}".format('my master') ### 'my master' gets inserted for {} in the string -- interpolation of multiple variables possible


#joining and loops 
strings = []

for i in range(0,5):
    string = "Das ist das {}. Element".format(i+1)
    strings.append(string)
joined = ' -- '.join(strings)
#print joined

## iterate over all array-elements
for elem in strings:
    print elem

## enumerate enables a counter / index to be accessible
for i, elem in enumerate(strings):
    print i