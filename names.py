def names_part2(sadie):
    for group,meep in sadie.iteritems(): # group is the key, meep is the value
        print group #prints Students and Instructors
        
        for place,individual in enumerate(meep): #enumerate gets back index and value. place is index, individual is value
            loo = str(place + 1)
            loo += " - "
            loo += individual["first_name"].upper()
            loo += " "
            loo += individual["last_name"].upper()
            loo += " - "
            loo += str(len(individual["first_name"]) + len(individual["last_name"]))
            print loo

def names_part1(sadie):
    for deedle in sadie:
        print deedle["first_name"],deedle["last_name"]


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

names_part2(users)
names_part1(students)
