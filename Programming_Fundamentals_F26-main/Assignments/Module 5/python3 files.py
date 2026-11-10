with open("notes.txt", "x") as f:
    pass

with open("notes.txt", "w") as f:
    f.write("Buy dog food\n")
    f.write("Walk the dog\n")

with open("notes.txt", "a") as f:
    f.write("Brush the dog\n")

with open("notes.txt", "r") as f:
    contents=f.read()
print(contents)

with open("notes.txt", "r") as f:
    for line in f:
        print("To do:", line.strip())
