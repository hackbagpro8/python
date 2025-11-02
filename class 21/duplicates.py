student={
    "id1":
    {
        "name":"sara",
        "age":"13",
        "subjects":["Maths","Science","english"]
    },
    "id2":
    {
        "name":"sourash",
        "age":"16",
        "subjects":["Japanese","Social Science","english"]
    },
    "id3":
    {
        "name":"sara",
        "age":"13",
        "subjects":["Maths","Science","english"]
    },
    "id4":
    {
        "name":"Mathew",
        "age":"16",
        "subjects":["Accountance","Maths","english"]
    }
}

result={}
for key,value in student.items():
    if value not in result.values():
        result[key] = value

print("without duplication")
print(result)
