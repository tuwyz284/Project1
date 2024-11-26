from collections import defaultdict

import csv
k = 0
tlist = []
mlist = defaultdict(list)
with open(r'C:\Users\Admin\Desktop\ds_dirty_fin_202410041147.csv', encoding='utf_8_sig') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        row1= row[0].split(',')
        row2 = row1[0]
        mlist[row2].append(row)
        if len(mlist[row2])>1:
            tlist.append(mlist[row2])
            mlist.pop(row2)

idlist = []
fs = []
for el in tlist:
    idlist.append(el[0][0])
    f = el[0]
    for tel in el[1:]:
        if f!=tel:
            s = []
            for i in range(len(f)):
                if f[i]!=tel[i]:
                    s.append(max(f[i], tel[i]))
                else:
                    s.append(f[i])

            fs.append(s)

        else:
            fs.append(f)



s = fs+list(mlist.values())
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(s)