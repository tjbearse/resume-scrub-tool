
def getChoice(labels, values=None):
    if(not values):
        values = labels
    elif(len(labels) != len(values)):
        raise 'error len(labels) != len(values)'
    while True:
        for i, label in enumerate(labels):
            print("{0}) {1}".format(i+1, label))
        print("q) quit\n")
        choice = raw_input()
        try:
            if(choice[0] == 'q'):
                quit()
            print('\n')
            return values[int(choice) - 1]
        except SystemExit:
            raise
        except:
            print('oops! try again')
