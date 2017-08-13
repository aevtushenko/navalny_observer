# -*- coding: utf-8 -*-
import csv,copy,random,math
 
with open('res4.csv', 'rb') as f:
    reader = csv.reader(f)
    data0 = map(list, reader)
# print l
del data0[0]  
data = copy.deepcopy(data0)
#print data

nav_col = "FF3300"
put_col = "2721D6"
zug_col = "057A09"
zhi_col = "FF8000"
tie_col = "707070"
total_votes = 0
total_unspoiled_votes = 0
total_nav = 0
total_put = 0
total_zug = 0
total_zhi= 0
total_sp = 0
out = open('points4.json','w')

def get_proc(res,votes):
    res_proc = []
    s = 0
    for i in range(len(res)-1):
        to_add = round(float(100*res[i])/votes,2)
        res_proc.append(to_add)
        s += to_add
    res_proc.append(100 - s)
    return res_proc
    

for l in data:
    votes = random.randint(2000,5000)
    col = ""
    num = l[0]
    address = l[1].replace('"','\\"').replace("'","\\'")
    lat = l[2]
    lng = l[3]
    if lat == "" or lng == "":
        continue
    p50 = math.floor(float(votes*0.5))
    p40 = math.floor(float(votes*0.4))
    p20 = math.floor(float(votes*0.2))
    nav = random.randint(p20,p50)
    put = random.randint(p20,p40)
    zug = random.randint(0,votes-nav-put)
    zhi = random.randint(0,votes-nav-put-zug)
    sp = votes-nav-put-zug-zhi
    res = [nav,put,zug,zhi,sp]
    res_proc = get_proc(res,votes)
    nav_proc = res_proc[0]
    put_proc = res_proc[1]
    zug_proc = res_proc[2]
    zhi_proc = res_proc[3]
    sp_proc = res_proc[4]
    m = max(res_proc[:-1])
    lst = [i for i, j in enumerate(res_proc[:-1]) if j == m]
    if len(lst) > 1:
        col = tie_col
    else:
        which = lst[0]
        if which == 0:
            col = nav_col
        elif which == 1:
            col = put_col
        elif which == 2:
            col = zug_col
        elif which == 3:
            col = zhi_col
        else:
            print "error"
    fire = ""
    if random.randint(0,10) < 3:
        fire = ",'marker-symbol': 'fire-station'"
    out.write('{type: \'Feature\',geometry: {type: \'Point\',coordinates:['+
                lng+
                ','+
                lat+
                ']},properties:{"description": "<b>'+
                num+
                '</b><br><i>'+
                address+
                '</i><hr>Навальный '+
                str(nav_proc)+
                '%<br>Путин '+
                str(put_proc)+
                '%<br>Зюганов '+
                str(zug_proc)+
                '%<br>Жириновский '+
                str(zhi_proc)+
                '%<br>Испорчено '+
                str(sp_proc)+
                '%",\'marker-color\': \'#'+
                col+
                '\',\'marker-size\': \'small\''+
                fire+
                '}},\n')
    total_votes += votes
    total_unspoiled_votes += votes - sp
    total_nav += nav
    total_put += put
    total_zug += zug
    total_zhi += zhi
    
out.close()
print total_votes
print total_unspoiled_votes
print total_nav
print total_put
print total_zug
print total_zhi
