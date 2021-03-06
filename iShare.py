def controller(data=None):    
    while data == None:
        data = interface()
    return main(*data)
        

def interface():
    total_control = 0
    buddies_shares = []
    buddies = str(input("Enter names of buddies name1, name2, so on: "))
    buddies = [x.strip().title() for x in buddies.split(',') if x.isspace() is False and x!='']
    if len(buddies) < 2:
        print("\nThere's no one to count\n")
        return
    total = float(input("What is the total sum? "))
    if total <= 0:
        print("\nTotal cannot be negative!\n")
        return
    for i in range(len(buddies)):
        share = float(input("How much {} paid? ".format(buddies[i])))
        if share < 0:
            print("\nThe share cannot be negative. Try again\n")
            return
        total_control += share
        if total_control > total:
            print("\nInput error! This share is exceeding the total sum!\n")
            return
        else:
            buddies_shares.append([buddies[i], share])
    if total_control != total:
        print("\nSum of all shares doesn't meet the total given. Try again\n")
        return
    else:
        return buddies_shares, total


def main(buddies_shares, total):
    guys_who_pay = []
    guys_who_get = []
    results_container = []
    equal_share = (total/len(buddies_shares)) if len(buddies_shares) > 0 else None
    
    for buddy in buddies_shares:
        if buddy[1] == 0:
            guys_who_pay.append([buddy[0], equal_share])       
        elif buddy[1] < equal_share:
            guys_who_pay.append([buddy[0], equal_share - buddy[1]])
        elif buddy[1] > equal_share:
            guys_who_get.append([buddy[0], buddy[1] - equal_share])
    guys_who_get = sorted(guys_who_get, key=lambda x: x[1], reverse=True)
    guys_who_pay = sorted(guys_who_pay, key=lambda x: x[1], reverse=True)
    
    for lender in guys_who_get:
        for debter in guys_who_pay:
            if lender[1] == debter[1]:
                results_container.append([debter[0], debter[1], lender[0]])
                guys_who_pay.remove(debter)         
                break
            elif lender[1] > debter[1]:
                results_container.append([debter[0], debter[1], lender[0]])
                lender[1] -= debter[1]
                guys_who_get.append(lender)
                guys_who_pay.remove(debter)
                break               
            elif lender[1] < debter[1]:
                results_container.append([debter[0], lender[1], lender[0]])
                debter[1] -= lender[1]
                break
    if len(guys_who_pay) == len(guys_who_get) == 0:
        return "\nEveryone equally contributed with {:.2f} each".format(equal_share)
    
    results_rounded = [[x[0], round(x[1], 2), x[2]] for x in results_container]
    
    output = "\n>>>Equal share is {:.2f}<<<".format(round(equal_share,2))
    for debter, cash, lender in results_rounded:
        line = '{} pays {:.2f} to {}'.format(debter, cash, lender)
        output += "\n{}".format("".join(line))
    return output
        

##################
#  TESTING AREA  #
##################


def test_1():
    data = ([["Den", 20], ["Fox", 40], ["Zoe", 0], ["Andy", 0], ["Bron", 40]], 100)
    output = main(*data)
    assert output == "\n>>>Equal share is 20.00<<<\nZoe pays 20.00 to Fox\nAndy pays 20.00 to Bron"
    return output


def test_2():
    data = ([["Den", 5], ["Fox", 0], ["Zoe", 15], ["Andy", 30], ["Bron", 50]], 100)
    output = main(*data)
    assert output == "\n>>>Equal share is 20.00<<<\nFox pays 20.00 to Bron\nDen pays 10.00 to Andy\nDen pays 5.00 to Bron\nZoe pays 5.00 to Bron"
    return output


def test_3():
    data = ([["Den", 0], ["Fox", 85], ["Zoe", 0], ["Andy", 15], ["Bron", 0]], 100)
    output = main(*data)
    assert output == "\n>>>Equal share is 20.00<<<\nDen pays 20.00 to Fox\nZoe pays 20.00 to Fox\nBron pays 20.00 to Fox\nAndy pays 5.00 to Fox"
    return output


def test_4():
    data = ([["Harry", 0], ["Den", 180], ["Fox", 400], ["Chad", 23], ["Elena", 900], ["July", 77]], 1580)
    output = main(*data)
    assert output == "\n>>>Equal share is 263.33<<<\nHarry pays 263.33 to Elena\nChad pays 136.67 to Fox\nChad pays 103.67 to Elena\nJuly pays 186.33 to Elena\nDen pays 83.33 to Elena"
    return output


def test_5():
    data = ([["Den", 45], ["Fox", 0], ["Zoe", 75]], 120)
    output = main(*data)
    assert output == "\n>>>Equal share is 40.00<<<\nFox pays 35.00 to Zoe\nFox pays 5.00 to Den"
    return output


def test_6():
    data = ([["Ed", 1083.12], ["Den", 70], ["Artem", 600], ["Dasha", 0]], 1753.12)
    output = main(*data)
    assert output == "\n>>>Equal share is 438.28<<<\nDasha pays 438.28 to Ed\nDen pays 161.72 to Artem\nDen pays 206.56 to Ed"
    return output


def test_7():
    data = ([["Ed", 1000], ["Den", 1000], ["Artem", 1000], ["Dasha", 1000]], 4000)
    output = main(*data)
    assert output == "\nEveryone equally contributed with 1000.00 each"
    return output

    
def test_8():
    data = ([["Елена", 187], ["Таня", 1500], ["Алекс", 400], ["Толя", 0], ["Оля", 1000], ["Денис", 950], ["Вася", 1950]], 5987)
    output = main(*data)
    assert output == "\n>>>Equal share is 855.29<<<\nТоля pays 855.29 to Вася\nЕлена pays 644.71 to Таня\nЕлена pays 23.57 to Оля\nАлекс pays 94.71 to Денис\nАлекс pays 239.43 to Вася\nАлекс pays 121.14 to Оля"
    return output


if __name__ == "__main__":
    print(controller())


##    print(test_1())
##    print(test_2())
##    print(test_3())
##    print(test_4())
##    print(test_5())
##    print(test_6())
##    print(test_7())
##    print(test_8())

