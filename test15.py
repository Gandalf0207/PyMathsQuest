import json
dico = {
    "nv1" : {
        "aaa" : 1,
        "bbb" : 2,
        "ccc" : 3154
    },

    "nv2" : {
        "aaa" : 1,
        "bbb" : 2,
        "ccc" : 3
    },

    "nv3" : {
        "aaa" : 1,
        "bbb" : 2,
        "ccc" : 3
    },

    "nv4" : {
        "aaa" : 1,
        "bbb" : 2,
        "ccc" : 3
    },
}

def loadAllDialogues():
    with open("Dialogues.json", 'r') as file:
        data = json.load(file)
        print(data["Niveau0"]["PNJ1"])
        return data

print(dico["nv1"]["ccc"])
print(loadAllDialogues())