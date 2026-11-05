try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File not found")



    #File not found
