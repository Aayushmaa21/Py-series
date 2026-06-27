def alphabetize_lists(list1, list2):

    new_list = []          # Initialize a new list
    
    new_list = list1 + list2   # Combine the lists
    
    new_list.sort()            # Sort the combined list
    
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Ninja", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

print(alphabetize_lists(Aniyahs_list, Imanis_list))