def registrar(first=None, last=None, **userInfo):
    userInfo["first_name"] = first
    userInfo["last_name"] = last
    return userInfo
    
register = registrar("Joe", "Biden", field="Clown", occupation="President", age= '> 50')
print(register)

def cook(code, *ref):
    msg = f'Your code: {code}'
    for x in ref:
        msg += f"\nYou have a referral from {x.title()}"
    return msg
        
x = cook(1001, "User_10", "User_20", "User_30")
print(x)