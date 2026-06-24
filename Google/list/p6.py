filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

new_filenames = [
    filename.replace(".hpp", ".h") if filename.endswith(".hpp") else filename
    for filename in filenames
]

print(new_filenames)