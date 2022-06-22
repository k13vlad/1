import csv

word1 = 'WARNING'
word2 = 'rpc.statd'
result = []
time = []
text = []
final_text = []


with open('syslog', "r") as file:
    lines = file.readlines()


for line in lines:
    if word1 in line and word2 in line:
        a = line.replace('WARNING rpc.statd:', '')
        b = a.split(' ')
        c = b[0].split(',')
        del(c[1])
        d = ''.join(c)
        del(b[0])
        b.insert(0,d)
        result.append(b)


for x in result:
    a = x[0]
    time.append(a)
    del x[0]
    text.append(x)


for x in text:
    a = ' '.join(x)
    final_text.append(a)


with open('file_with_end_data.csv', "w") as f:
    writer = csv.writer(f)
    writer.writerows(zip(time, final_text))
f.close()

