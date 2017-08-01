s1 = "fifty cha' 'emDaq De' mej vegh De' vegh 'emDaq wejmaHlogh mej"
s2 = "loSmaH loS 'emDaq De' mej vegh cha'maH Soch 'emDaq De' mej vegh"



d = {}
for i in range(len(s1)):
    d[s1[i]] = 0 

for i in range(len(s1)):
    d[s1[i]] += 1 

for i in range(len(s2)):
    d[s2[i]] = 0

for i in range(len(s2)):
    d[s2[i]] += 1 



print d
print len(d)

d2 = {}

s1w = s1.split(" ")
s2w = s2.split(" ")

for word in s1w:
    d2[word] = 0

for word in s1w:
    d2[word] += 1

for word in s2w:
    d2[word] = 0

for word in s2w:
    d2[word] += 1

print (d2)
