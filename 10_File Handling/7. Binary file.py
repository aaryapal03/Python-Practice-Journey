
"A binary file stores data in the form of bytes (0s and 1s)."
"Examples:- Images (.jpg, .png),  PDF files (.pdf), Audio files (.mp3), Video files (.mp4)"

'''
Modes:
rb -> Read Binary
wb -> Write Binary
ab -> Append Binary
'''

# Writing bytes to a binary file
with open("binary_file.bin", "wb") as file:
    file.write(b"Hello Python")

print()


#reading bytes to a binary file
with open("binary_file.bin", "rb") as file:
    data = file.read()
    print(data)

print()


# Make sure "image.jpg" exists in the same folder.

try:
    with open("image.jpg", "rb") as source:
        data = source.read()

    with open("image_copy.jpg", "wb") as destination:
        destination.write(data)

    print("Image copied successfully.")

except FileNotFoundError:
    print("image.jpg not found.")

print()


#End of Program
