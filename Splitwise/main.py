from splitwise.system import System
def main():
    rawInput = []
    while(True):
        temp = list(map(str, input().strip().split()))
        #print("temp",temp)
        if(temp[0] == "exit"):
            break
        rawInput.append(temp)
    print(rawInput)
    splitWise = System()
    for sysInput in rawInput:
        if(sysInput[0] == "SHOW"):
            if(len(sysInput) == 2):
                # show all users
                splitWise.getGroup(sysInput[1]).showAllUsers()
            elif len(sysInput) >= 3:
                # show specific user 
                splitWise.getGroup(sysInput[1]).showUser(sysInput[2])
            else:
                print("Invalid SHOW command format")
        elif(sysInput[0] == "EXPENSE"):
            for val in sysInput:
                if(val == "EQUAL"):
                    paidBy = sysInput[2]
                    totalAmount = int(sysInput[3])
                    paidTo = []
                    for i in range(0, int(sysInput[4])):
                        paidTo.append(sysInput[4 + 1 + i])
                    splitWise.getGroup(sysInput[1]).addExpenseByEqualSplit(paidBy, paidTo, totalAmount)
                elif(val == "PERCENT"):
                    paidBy = sysInput[2]
                    totalAmount = int(sysInput[3])
                    paidTo = []
                    percents = []
                    for i in range(0, int(sysInput[4])):
                        paidTo.append(sysInput[4 + 1 + i])
                        percents.append(int(sysInput[4 + 1 + i + 1 + int(sysInput[4])]))
                    splitWise.getGroup(sysInput[1]).addExpenseByPercentSplit(paidBy, paidTo, percents, totalAmount)
                elif(val == "EXACT"):
                    paidBy = sysInput[2]
                    totalAmount = int(sysInput[3])
                    paidTo = []
                    amounts = []
                    for i in range(0, int(sysInput[4])):
                        paidTo.append(sysInput[4 + 1 + i])
                        amounts.append(int(sysInput[4 + 1 + i + 1 + int(sysInput[4])]))
                    splitWise.getGroup(sysInput[1]).addExpenseByExactSplit(paidBy, paidTo, amounts)
        elif(sysInput[0] == "USER"):
            splitWise.registerUser(sysInput[1])
        elif(sysInput[0] == "GROUP"):
            # making grp by default with all users at once
            splitWise.registerGroup(sysInput[1], splitWise.users)
        else:
            print("Unsupported split")
        

# start off
main()