def registrar(first=None, last=None, **userInfo):
    userInfo["first_name"] = first
    userInfo["last_name"] = last
    return userInfo

def code(code, *ref):
    msg = f'Your code: {code}'
    for x in ref:
        msg += f"\nYou have a referral from {x.title()}"
    return msg

# Exported functions must not have any other additional code like in function_1.py