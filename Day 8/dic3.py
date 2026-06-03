#changing value by using key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


#changing key
dictionary = {"cat": "chat", "dog": "chien"}

dictionary["kitty"] = dictionary["cat"]  # add new key
del dictionary["cat"]                    # remove old key

print(dictionary)
