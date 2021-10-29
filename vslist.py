class vstr(object):
    #Сохранить дату, время и список людей
    def __init__(self,day, time, dur, *namelist):
        self.day = day
        self.time=time
        self.dur=dur
        self.time1 = int(time[0:2]) * 60 + int(time[3:5])
        self.time2 = self.time1 + int(dur)
        self.namelist = namelist
        pass
    #проверка, что этот человек будет на встрече.
    def istherename(self, name):
        for somename in self.namelist[0]:
            if somename==name:
                return True
        return False


class vstrlist(object):


    def __init__(self):
        self.vstrlist = []
        pass

    # превратить время и продолжительность в начало и конец в минутах
    # искать совпадение по группам и вывести, успешно ли все, и внести встречу в список.
    def appoint(self,vstrecha):

        if self.vstrlist==[]:
            self.vstrlist.append(vstrecha)
            return 'OK'
        pernames=""
        for newname in vstrecha.namelist[0]:
            for n in self.vstrlist:
                if (vstrecha.day == n.day) and (n.istherename(newname)):
                    if ( n.time1<vstrecha.time1 and n.time2>vstrecha.time1 ) or ( n.time1<vstrecha.time2 and n.time2>vstrecha.time2):
                        pernames +=" " + str(newname)
        if pernames =="":
            self.vstrlist.append(vstrecha)
            ret="Ok"
        else:
            ret = 'FAIL\n'+ pernames[1:]

        return (ret)


    # искать совпадение по группам для print и вывести список параметров

    def printn(self,day,name):
        if self.vstrlist==[]:
            return ''
        resnames=''

        for n in self.vstrlist:

            if n.day == day and n.istherename(name):
                resnames = '\n'+n.time + ' ' + n.dur + ' '
                for names in n.namelist[0]:

                    resnames+=str(names+' ')
                #print(resnames)
        return resnames


