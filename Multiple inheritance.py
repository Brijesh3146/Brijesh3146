#base class 1
class employee:
    raise_amt=1.04
    def __init__(self, first, last,pay ):
        self.first=first 
        self.last=last 
        self.email=first+'.'+last+'@bollywood.com'
        self.pay=pay
#base class 2
class developer:
    def __init__(self,prog_lang):
        self.prog_lang=prog_lang
#derived class 
class Manager(developer, employee):
    def __init__(self, first,last,pay,prog_lang,time):
        employee.__init__(self,first, last,pay)
        developer.__init__(self,prog_lang)
        self.time=time
mgr1=Manager('kabir','rana',25000,'python',10)
print('name=',mgr1.first)
print(mgr1.email)
print(mgr1.pay)
print(mgr1.prog_lang)
print(mgr1.time)
        
