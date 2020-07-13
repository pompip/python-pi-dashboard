D = dict()
D['hello'] = dict()
D["hello"]["world"] = 10
print(D["hello"]["world"])

def rf(name):
    
    with open(name,'r') as f:
        l = f.readlines()
    return "".join(l).split(" ")

rf("C:\\Users\\bonreeKC\\Desktop\\hell.log")