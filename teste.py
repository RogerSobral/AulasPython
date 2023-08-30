lista=[1,2,3,4,"A"]

listas=[lista,
        [1,45,22,60,"A"],
        [12,5,2,0,"A"],
        {"Nome":"Carlos", "Idade":45}
]


for lis in listas:
    if isinstance(lis,dict):
        print(lis["Nome"])
    else:
        print(lis[0])

