# To read the contents of the file
with open("my_file.txt",mode='r') as f:
    contents = f.read()

# Append the new content in the file
with open("my_file.txt",mode='a') as f:
    # contents = f.read()
    f.write("\nNew Text")

# Delete and write new content in the file
with open("my_file.txt",mode='w') as f:
    f.write("New Text")

my_file_path = "../../../Desktop/my_file.txt"
with open(my_file_path) as file:
    contents = file.read()
    print(contents)
