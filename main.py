import vslist as vs
'''
names=['s','p','y']
vchi=vs.vstrlist()
vs1= vs.vstr('11','14:22','47', 'Tom','Igor','Alex')
vs2= vs.vstr('11','14:00','45', 'Tom','Alex')

print(vchi.appoint(vs1))
print(vchi.appoint(vs2))
'''

vstrl=vs.vstrlist()
zapr='''7
APPOINT 1 12:30 30 2 andrey alex
APPOINT 1 12:00 30 2 alex sergey
APPOINT 1 12:59 60 2 alex andrey
PRINT 1 alex
PRINT 1 andrey
PRINT 1 sergey
PRINT 2 alex'''

zstr=zapr.split('\n')
for sdl in zstr:
    s = sdl.split(' ')
    if s[0] == 'APPOINT':
        day = s[1]
        time = s[2]
        dur = s[3]
        namelist = s[5:]
        vsnew = vs.vstr(day,time,dur,s[5:])
        print(vstrl.appoint(vsnew))
    elif s[0] == 'PRINT':
        print(vstrl.printn(s[1],s[2]))
