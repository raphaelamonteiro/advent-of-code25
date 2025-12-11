
def main():
    #Open the file
    file = open("input.txt", "r")

    lines = file.readlines()
    file.close()
    #Close the file

    currentPosition = 50
    zeroCount = 0

    # Process each line
    for line in lines:
        line = line.strip()
        direction = line[0]
        value = int(line[1:])

        
        if direction == "R":
            newPosition = (currentPosition + value) % 100
        
        else:
            newPosition = (currentPosition - value) % 100


        if newPosition == 0:
            zeroCount += 1

        currentPosition = newPosition

    print(f"Password: {zeroCount}")


if __name__ == "__main__":
    main()