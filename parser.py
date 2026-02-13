def convert(inputfile):
    outputfile = open('pythonCode.py', "a")
    indent = 0
    outputTxt= []
    for line in inputfile:
        outputTxt.append("\t"*indent)
        list1 = line.strip().split(" ")
        list1 = [item for item in list1 if item != ""]
        # See if line starts with key word
        if not (len(list1)):
            outputTxt.append("\n")
            continue
        keyword = list1[0]
        startIndex = 1
        addNL = True
        if keyword == "PROCEDURE":
            outputTxt.append("def ")
        elif keyword == "FOR" and list1[1] == "EACH":
            outputTxt.append("for ")
            startIndex = 2
        elif keyword == "REPEAT":
            if list1[1] == "UNTIL":
                outputTxt.append("while not ")
                startIndex = 2
            elif list1[2] == "TIMES":
                num = list1[1]
                outputTxt.append("for i in range(" + num + ") ")
                startIndex = 3
        elif keyword == "DISPLAY":
            toPrint = " ".join(list1[1:])
            outputTxt.append("print" + toPrint + "\n")
            continue
        else:
            startIndex = 0

        for word in list1[startIndex:]:
            if word == "NOT":
                outputTxt.append("!= ")

            # Change operators
            elif word == "=":
                     outputTxt.append("== ")
            elif word == "←":
                outputTxt.append("= ")
            elif word == "MOD":
                outputTxt.append("% ")
            
            # Control indentation
            elif word == "{":
                indent += 1
                outputTxt.pop()
                outputTxt.pop()
                outputTxt[-1] = outputTxt[-1][:-1]
                outputTxt.append(":")

            elif word == "}":
                indent -=1
                outputTxt.pop()
                addNL = False
                # outputTxt[-1] = outputTxt[-1][:-1]

            # Handle booleans
            elif word == "true" or word == "false":
                outputTxt.append(word.capitalize())
            elif word == "(true)" or word == "(false)":
                outputTxt.append(word[1:-1].capitalize())

            # Other cases
            else:
                outputTxt.append(word.lower() + " ")
        if addNL:
            outputTxt.append("\n")


    outputTxt = ''.join(outputTxt)
    outputfile.write(outputTxt)

if __name__ == "__main__":
    filename = input("Your AP Pseudocode should be in a .txt file.\nWhat is the name of the file? ")
    #filename = "myfile"
    try:
        file = open(filename+".txt", 'r')
    except FileNotFoundError:
        #try:
        file = open(filename, 'r')
        
    convert(file)