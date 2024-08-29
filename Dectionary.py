bscit={"fyit":{"sem1":{"sub1":"cpp","sub2":"java","sub3":"python"},
     "sem2":{"sub1":"dbms","sub2":"oops"}},
     "syit":{"sem3":{"sub1":"wad","sub2":"nm"},
    "sem4":{"sub1":"ds","sub2":"cn"}},
    "tyit":{"sem5":{"sub1":"hs","sub2":"gi"},
    "sem6":{"sub1":"English","sub2":"Hindi"}}}
print(bscit["syit"]["sem4"].values())
del bscit["tyit"]["sem6"]
bscit["fyit"]["sem1"]["sub"]="c++"
print(bscit)
