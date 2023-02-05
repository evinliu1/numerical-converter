# Numerical Conversion Application
# Personal Project
# 1/02/23 -
# Evin Kai Liu

from dotenv import load_dotenv,find_dotenv
import PySimpleGUI as sg

load_dotenv(find_dotenv())
layout = [
    [sg.Text('Numeric Converter')],
    [
        sg.Input('',key = '-INPUT_FIELD-'),
        sg.Combo([
                'binary to decimal',
                'decimal to binary',
                'decimal to octal',
                'octal to decimal',
                'hexidecimal to binary',
                'binary to hexidecimal'
                ],key = '-CONVERSION_SELECTOR-', size=(30,6)
                )],
    [sg.Button('Convert', key="-CONVERT_BUTTON-"), sg.Text('Converted Value   ->'), sg.Input('', key='-VALUE_FIELD-', size=(51,None))]
]

window = sg.Window('Converter Application', layout)

def binToDec(val):
    converted_value = 0
    error_message = '[ something doesn\'t seem right with your input ]'

    # increment power 
    counter = 0

    # splits string input into a list by character
    checker = [val for val in val]
    condition = True

    # if input is blank return error
    if val == '':
        sg.popup_error(error_message)
        return 'error'

    # checks if each element in checker is 0 or 1
    for x in checker:
        if x != '0' and x != '1':
            sg.popup_error(error_message)
            return 'error'


    val = int(val)
    while val != 0:
        digit = val % 10
        converted_value = converted_value + (digit * pow(2,counter))
        counter += 1
        val = val//10
    

    # returns converted value
    return converted_value

def decToBin(val):
    converted_value = ''
    error_message = '[ something doesn\'t seem right with your input ]'

    # return error message if inputed value is empty
    if val == '':
        sg.popup_error(error_message)
        return 'error'
    
    # if input value is only numbers, we can continue with code
    if val.isnumeric():
        val = int(val)
        while val != 0:
            digit = val % 2
            converted_value = str(digit) + converted_value
            val = val // 2
    else:
        sg.popup_error(error_message)
        return 'error'
    
    return converted_value

def decToOct(val):
    converted_value = ''
    error_message = '[ something doesn\'t seem right with your input ]'

    # return error message if inputed value is empty
    if val == '':
        return error_message
    
    # if input value is only numbers, we can continue with code
    if val.isnumeric():
        val = int(val)
        while val != 0:
            digit = val % 8
            converted_value = str(digit) + converted_value
            val = val // 8
    else:
        return error_message
    
    return converted_value

def octToDec(val):
    converted_value = 0
    error_message = '[ something doesn\'t seem right with your input ]'
    
    # increment power 
    counter = 0

    # splits string input into a list by character
    checker = [val for val in val]

    # if input is blank return error
    if val == '' or val.isnumeric() is not True:
        sg.popup_error(error_message)
        return 'error'

    # checks if each element in checker between 0 and 8
    for x in checker:
        if int(x) not in range(8):
            sg.popup_error(error_message)
            return 'error'

    # if input is in range(8) we convert from binary to decimal   
    val = int(val)
    while val != 0:
        digit = val % 10
        converted_value = converted_value + (digit * pow(8,counter))
        counter += 1
        val = val//10
    
    # if there is something wrong with input, we throw an error message
    else:
        sg.popup_error(error_message)
        return 'error'

    # returns converted value or error message
    return converted_value

def hexToBin(val):
    # initializing variables
    error_message = '[ something doesn\'t seem right with your input ]'

    unconverted_list = [val for val in val]
    converted_value_list = []
    converted_value = ""
    incorrect_input = False

    # dictory to hold ASCII -> Binary
    dict = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
    }

    # check if there is input errors 
    for val in unconverted_list:
        if val not in dict:
            incorrect_input = True 

    # throw error message if input errors
    if val.isalnum() is not True or incorrect_input is True:
        sg.popup_error(error_message)
        return 'error'

    # iterate through unconverted list and append correct values from dictionary to converted value list
    for val in unconverted_list:
        converted_value_list.append(dict.get(val))
        converted_value_list.append(' ')
    
    # iterate through converted list and append to return string
    for num in converted_value_list:
        converted_value = converted_value + num
    
    converted_value = converted_value.rstrip()
    return converted_value

def binToHex(val):
    # initialize variables
    mod_value = 4
    input_error = False
    error_message_binary = '[ something doesn\'t seem right with your input - try only inputting 0\'s and 1\'s ]'
    error_message_mod = '[ something doesn\'t seem right with your input - try inputting values in groups of 4 ]'
    reader = ''
    converted_value = ''
    val = val.strip()
    val_list = [val for val in val]
    dict = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    # check if user input consists only of numbers 0 or 1
    if val.isnumeric() is not True:
        sg.popup_error(error_message_binary)
        return 'error'
    
    # check if each char in val is 0 or 1
    for str in val_list:
        if str is not ('0' or '1'):
            sg.popup_error(error_message_binary)
            return 'error'

    # check if user input
    checker = val.toInt()
    if checker % 4 != 0:
        sg.popup_error(error_message_mod)
        return 'error'
    

    for num in val:
        for i in range(4):
            reader = reader + num
        
        converted_value = converted_value + dict.get(reader)
        reader = ''
    
    return converted_value


# MAIN APPLICATION LOOP
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT_BUTTON-':
        # val holds value in the input field
        val = values['-INPUT_FIELD-']
        if values['-CONVERSION_SELECTOR-'] == 'binary to decimal':
            # call our conversion method
            converted_value = binToDec(val)
        elif values['-CONVERSION_SELECTOR-'] == 'decimal to binary':
            converted_value = decToBin(val)
        elif values['-CONVERSION_SELECTOR-'] == 'octal to decimal':
            converted_value = octToDec(val)    
        elif values['-CONVERSION_SELECTOR-'] == 'decimal to octal':
            converted_value = decToOct(val)
        elif values['-CONVERSION_SELECTOR-'] == 'hexidecimal to binary':
            converted_value = hexToBin(val)
        elif values['-CONVERSION_SELECTOR-'] == 'binary to hexidecimal':
            converted_value = binToHex(val)

        window['-VALUE_FIELD-'].update(converted_value)

window.close()