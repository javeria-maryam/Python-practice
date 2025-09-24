# Add a new key "city",update marks, then delete age.

thisdict = {"name" : "Ali",
            "age"  : 23,
            "marks" : 89

}

thisdict.update({"city" : "lahore"})
 
del thisdict["age"]

print(thisdict)