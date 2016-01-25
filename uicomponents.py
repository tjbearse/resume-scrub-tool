
def getChoice(labels):
    while True:
        for i, label in enumerate(labels):
            print("{0}) {1}".format(i+1, label))
        print("q) quit\n")
        choice = raw_input()
        try:
            if(choice[0] == 'q'):
                quit()
            return labels[int(choice) - 1]
        except SystemExit:
            raise
        except:
            print('oops! try again')
