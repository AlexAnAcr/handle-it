owrt = []
with open('ToH_dump_tab_separated.csv','r') as f:
    owrt = f.readlines()

appripriate = []
for i in owrt:
    appripriate.append([i.split('\t')[2].lower(), i.split('\t')[3].lower()])

def goodrouter(vendor, router):
    for i in appripriate:
        if i[0] == vendor.lower() and (i[1].startswith(router.lower()) or router.lower().startswith(i[1])):
            return True
    return False
    
lines = []
with open('citi.txt','r', encoding='utf-8') as f:
    lines = f.readlines()

good = []

prev = ''
for i in lines:
    if (i.startswith('Wi-Fi роутер') and prev != i):
        prev = i
        
        rstr = i.strip()[13:]
        rvendor = rstr.split(' ')[0]
        rmodel = " ".join(rstr.split(' ')[1:]).split(',')[0]

        if (goodrouter(rvendor, rmodel)):
            good.append(rvendor + " : " + rmodel)

for i in good:
    print(i)
        
