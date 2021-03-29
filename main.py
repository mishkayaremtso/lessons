
def create(name, telephone, address):
    record = {
        'name' : name,
        'phone': telephone,
        'address': address

    }
    return record

user1 = create("petro","+124143414","kek")
user2 = create("sf","sg2342414","erer")

print(user2,"\n",user1)


def award(medal, *persons):
    for person in persons:
        print("kret " + person.title() +" medal "+ medal)


award("shlyapa","petro","gfg")