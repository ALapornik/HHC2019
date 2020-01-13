import hashlib

money=1500
distance=7999
day=3
month=9

reindeer=2
runners=2
ammo=10
meds=2
food=84

hash="2cb6b10338a7fc4117a80da24b582060"

hashvalue = money + distance + day + month
hashvalue += reindeer + runners + ammo + meds + food

def md5it(x):
    m = hashlib.md5(x.encode())
    return  m.hexdigest()

print(md5it(str(hashvalue)) + " : Our HASH")

print(hash + " : Original HASH")

