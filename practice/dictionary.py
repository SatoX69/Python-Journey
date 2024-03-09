# JSON

registrar = {
    "name": "Andrew",
    "age": 16,
    "nationality": "German",
    "ageIssue": None
}

print(registrar)
registrar["sex"] = "male"

if registrar['age'] < 18:
    registrar['ageIssue'] = "Too young"
    
print(registrar)