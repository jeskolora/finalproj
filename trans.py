langDict = {}
langDict = {"jawn":"person, place, or thing", "ocky":"not authentic","drawlin":"acting out of character or being bad","wack":"corney or dumb","outta pocket":"acting out of line" }
# infinite loop till user chooses to exit
while True:
    print(
        "Main Menu\n1 - translate a word\n2 - add word to dict\n3 - print dictionary\n4 - test yourself\n5 - "
        "exit\nPLEASE MAKE A SELECTION:")
    choice = input()
    # check if the input is a number or not
    if choice.isdigit():
        # if it is a number convert to int
        choice = int(choice)
        # translate a word
        if choice == 1:
            word = input("Provide the Philly term:")
            if word in langDict:
                print(langDict[word])
            else:
                print("Sorry no translation for that word")
        # add word to dict
        elif choice == 2:
            word = input("What language is the translated word in:")
            if word in langDict:
                print("The word already exists:{0} - {1}".format(word, langDict[word]))
            language= input("What Eng word are you providing a translation for:")
            translated = input("What is the translated word:")
            if word in langDict:
                langDict[word][translated] = language
            else:
                langDict[word] = {translated: language}
        # print current translation dictionary
        elif choice == 3:
            print(langDict)
        #quiz
        elif choice ==4:
            print("How Philly Are You?\nFind out now by taking this quiz!")
            print('Word blank : - ocky -jawn - wack - drawlin - outta pocket')
            QA = [
                "Pass me that ___","jawn",
                "Those shoes appear to be a knock-off. Therefore, it's ___.","ocky",
                "Chad knew kicking his friend out would be _____","outta pocket",
                "Anytime her mother leaves the house, Ciara starts ___","drawlin"
                ]
            points = 0
            current = 0
            quiz= 1

            while quiz <3:
                question = input(QA[current])
                if question ==QA[current + 1]:
                    print("That's right")
                    points = points + 1
                    current = current + 2
                quiz = quiz + 1
            #Scoring
            if points <=1:
                print('We can tell you are not from Philly.')
            elif points ==2:
                print("Wow!\nYou must know how to get to Center City on your own.")
            else:
                print('Good job!\nYou must be a Philly native.')
 # exit
        elif choice == 5:
            print("See you later")
            break
        else:
            print("**Invalid input")
    else:
        print("**Invalid input - type a number above only")
