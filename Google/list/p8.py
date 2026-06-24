def biography_list(people):
    # Iterate over each person
    for person in people:

        # Separate the tuple values
        name, age, profession = person

        # Print the formatted sentence
        print("{} is {} years old and works as {}.".format(name, age, profession))

# Call to the function
biography_list([
    ("Ira", 30, "a Chef"),
    ("Raj", 35, "a Lawyer"),
    ("Maria", 25, "an Engineer")
])