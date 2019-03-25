##############################
# Arabs <-> Romans Converter #
#     by Denys Lozinskyi     #
##############################

tab = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I']
    ]

def arabs2romans(number):
    '''
        converts arabic numbers into the romans
    '''
    
    if not 0 < number < 4000:
        return "!Число должно быть в диапазоне от 0 до 3999!"
    
    
    result = ''
    for arab, roman in tab:
        while number >= arab:
            result += roman
            number -= arab
    return result


# def romans2arabs(string="XX"):
#     '''
#         converts roman numbers back to the arabics
#     '''
#     result = 0
#     initial_point = 0
#     while initial_point < len(string):
#         for arab, roman in tab:
#             if string[initial_point:initial_point+2] == roman:
#                 result += arab
#                 initial_point +=2
#                 break 
#             elif string[initial_point] == roman:
#                 result += arab
#                 initial_point += 1
#                 break
#         else:
#             return "Введенное число содержит ошибки"
#     return result

        

def main_script():
    
    print("КОНВЕРТЕР АРАБСКИХ ЧИСЕЛ В РИМСКИЕ")
    print("для завершения работы введите 'n'")
    while True:
        arab = input("\nВведите число: ")
        if arab.lower() == "n":
            print("\nРабота программы завершена")
            break
        try:
            number = int(arab)
        except:
            print("!Неверный ввод!")
            continue
        print("\n%s -> %s" %(arab, arabs2romans(int(arab))))


if __name__ == '__main__':
    main_script()
    
