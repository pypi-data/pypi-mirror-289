import numpy as np
import string
import inspect
import re
import typing
from typing import Literal
import sys
import math
import time

variable = "A"
global_label = "AA"

xor = "xor"

global_vars = {}
function_code = {}
file_lines = {} # all the lines in the child script
indentations = {} # the indentation (leading whitespace) of each line in the child script
pb_import_name = "" # whatever this module is referred to in the child script 
math_import_name = "" # whatver the math module is referred to in the child script

# The str class is used as the way of manipulating strings in Basic
class Str():
    name = "" # can be Str[0-9]
    value = "" # whatever the string's value is

    def __init__(self, name):
        self.name = name

    def set(self, value):
        self.value = value

    def get_string(self):
        return self.value

# A dictionary to store all the custom lists of the user (this DOESN'T include L1-L6, which are built-in)
user_created_lists = []

class List():
    global user_created_lists, pb_import_name

    name = "" # either L₁-L₆ or a custom name
    object_name = "" # whatever the variable name is of this list when it is declared

    def __init__(self, name, value = None):
        stack_info = inspect.getframeinfo(inspect.stack()[1][0])

        calling_line = stack_info.code_context
        calling_script = stack_info.filename

        print(f"calling line: {calling_line}")
        print(f"calling_script: {calling_script}")

        if calling_script == __file__:
            # The list is being created from this module, i.e., it's L1-L6
            object_name_regex = rf"(\w+)\s*=\s*List\("
        else:
            # The list is being created from the child module
            object_name_regex = rf"(\w+)\s*=\s*\w+\.List\("
        re_result = re.search(object_name_regex, calling_line[0])
        if(re_result):
            self.object_name = re_result.groups()[0]
            user_created_lists.append(self)

        self.name = name

        if not value is None:
            # This means a default value for the list has been provided
            # The list will be set to this value at the beginning of the program
            basic_append(f"{value}→⌊{self.get_name()}")
        user_created_lists.append(self)

    def contains_number(self, number):
        '''Checks if the list contains the specified number. This command only works with lists of numbers.'''
        return f"max(not(⌊{self.get_name()}-{number}))"

    def get_list(self):
        return f"⌊{self.get_name()}"

    def get_object_name(self):
        return self.object_name
    
    def get_name(self):
        return self.name

    def set_list(self, value):
        '''Sets the entire list equal to value'''
        return f"{value}→⌊{self.get_name()}"

    def set_index(self, index, item):
        '''Sets the specified index in the list to be equal to the item specified'''
        self.value[index] = item
    
    def append(self, item):
        '''Appends the given item to the end of the list'''
        return f"{item}→⌊{self.get_name()}(1+dim(⌊{self.get_name()}))"

    def pop(self):
        '''Removes the last item from the list'''
        return f"⌊{self.get_name()}(X),X,1,dim(⌊{self.get_name()})-1)"
    
    def get_index(self, index):
        '''Returns the list item at the specificed index. Note that in TI-Basic, lists start at index 1, NOT 0.'''
        return f"⌊{self.get_name()}({index})"

    def remove_index(self, index):
        '''Removes the list item at the specificed index, shifting every indice after it down by one. The new list is returned. Note that in TI-Basic, lists start at index 1, NOT 0.'''
        return f"seq(⌊{self.get_name()}(X+(X≥{index})),X,1,dim(⌊{self.get_name()})+-1)→⌊{self.get_name()}"

SETUP_OPTIONS = Literal["FUNCTION", "MENU"]

'''Some useful literals'''
COLORS = Literal["BLUE", "RED", "BLACK", "MAGENTA", "GREEN", "ORANGE", "NAVY", "LTBLUE",
                 "YELLOW", "WHITE", "LTGRAY", "MEDGRAY", "GRAY", "DARKGRAY"]

# just so i can index the colors
COLOR_LIST = ["BLUE", "RED", "BLACK", "MAGENTA", "GREEN", "ORANGE", "NAVY", "LTBLUE",
              "YELLOW", "WHITE", "LTGRAY", "MEDGRAY", "GRAY", "DARKGRAY"]

MARKS = Literal["▫", "•", "·"] #  "⁺" was giving me issues for some reason, sorry :(
TAIL_DIRECTIONS = Literal["LEFT", "CENTER", "RIGHT", "BLANK"] # select blank if your model doesn't support tail direction
ALTERNATIVES = Literal["NOT_EQUAL", "LESS", "GREATER"]

FIXED_MARKS = {
    "Â·" : "·",
    "â€¢" : "•",
    "â–«" : "▫",
}

L1 = List("L₁")
L2 = List("L₂")
L3 = List("L₃")
L4 = List("L₄")
L5 = List("L₅")
L6 = List("L₆")

STR1 = Str("Str1")
STR2 = Str("Str2")
STR3 = Str("Str3")
STR4 = Str("Str4")
STR5 = Str("Str5")
STR6 = Str("Str6")
STR7 = Str("Str7")
STR8 = Str("Str8")
STR9 = Str("Str9")
STR0 = Str("Str0")

X = "X"
Y = "Y"
Z = "Z"

i = ""
'''The imaginary number i''' # (it's there - use your imagination)


'''End of literals'''

# These lines are used to help translate if/while statements
in_indented_block = False
statement_indentations = []

ti_basic = ""

screen_width = 24 # usually 16 or 24 - how many characters can fit horizontally across the screen
labels = [] # a dictionary list with info on every label in the program
all_menus = []

class Menu():
    title = "" # what is displayed to the user
    options = [] # a list of MenuOption objects
    function = "" # name of function that stores the menu's code
    parameter = "" # the parameter that the function takes
    label = "" # the label we can run Goto on to get back to this menu

    def __init__(self, title, function, options):
        self.title = title
        self.function = function
        self.parameter = re.search(r"^def " + function.__name__ + r"\s*\((.*)\):.*$", 
                                        str(inspect.getsource(self.function)).splitlines()[0]).groups()[0]
        self.options = options
        self.label = generate_label()
        for option in self.options:
            option.set_menu(self)

            start_end = get_option_start_end_lines(self, option)
            option.set_start_line(start_end[0])
            option.set_end_line(start_end[1])

        labels.append({
            "title": self.title,
            "label": self.label,
            "type": Menu
        })
        all_menus.append(self)

    def get_title(self):
        return self.title
    
    def get_options(self):
        return self.options
    
    def get_function(self):
        return self.function

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_parameter(self):
        return self.parameter

class MenuOption():
    option_name = "" # name of option
    label = "" # Will be generated by the computer
    menu = Menu # Whatever menu this MenuOption is a part of

    start_line = 0 # whatever line in the menu's function this option's code block begins and ends on
    end_line = 0

    def __init__(self, option_name):
        self.option_name = option_name
        self.label = generate_label()

        labels.append({
            "title": self.option_name,
            "label": self.label,
            "type": MenuOption
        })

    def get_option_name(self):
        return self.option_name
    
    def get_label(self):
        return self.label
    
    def get_menu(self):
        return self.menu

    def set_label(self, label):
        self.label = label
    
    def set_menu(self, menu):
        self.menu = menu

    def set_start_line(self, start_line):
        self.start_line = start_line

    def get_start_line(self):
        return self.start_line
    
    def set_end_line(self, end_line):
        self.end_line = end_line

    def get_end_line(self):
        return self.end_line
   
def generate_label(): # goes from AB to ZZ, over 600 combinations 
    global global_label
    alphabet = list(string.ascii_uppercase)

    index = alphabet.index(global_label[1]) # Will return 0-25, for A-Z, respectively
    if index == 25: # the second letter in the label is Z, so we increment the first letter
        global_label = alphabet[alphabet.index(global_label[0]) + 1] + "A"
    else:
        global_label = global_label[0] + alphabet[alphabet.index(global_label[1]) + 1]
    
    return global_label

def reformat_equation(equation):
    variable = ""

    equation_divider = re.search(r"^(\w*)\s*\+=|^(\w*)\s*=|^(\w*)\s*-=|^(\w*)\s*\*=|^(\w*)\s*\/=", equation)
    equation = math_convert(equation) # to replace "math." with calculator commands

    
    negative_sequence = re.findall(r"[-+=/*][\s]*-\d*", equation)
    negatives = []

    if(negative_sequence):
        for sequence in negative_sequence:
            #print(f"sequence {sequence}")
            negatives.append(int(str(sequence[1:]).strip()))

        characters = list(equation)
        for negative in negatives:
            print(f"negative! {negative}")
            i = equation.index(str(negative))
            characters[i] = "­"
        equation = "".join(characters)
    
    if(equation_divider):
        variable = [i for i in equation_divider.groups() if i is not None][0]
        divider = equation_divider.group().split(variable)[1].strip()
        print(f"var: {variable, divider}")
    else:
          # this isn't a valid equation, so we just return the line and use it as is
          return(equation)

    equation = equation.replace(" ", "") # remove spaces

    if(len(divider) == 2): # it's either += -= *= or /=
        equation = f"{variable.upper()}{divider[0]}{equation.split(variable + divider)[1]}→{variable.upper()}"
    else:
        equation = f"{equation.split(variable + divider)[1]}→{variable.upper()}"
    return equation

def superscript_number(number):
    sups = {u'0': u'\u2070',
            u'1': u'\xb9',
            u'2': u'\xb2',
            u'3': u'\xb3',
            u'4': u'\u2074',
            u'5': u'\u2075',
            u'6': u'\u2076',
            u'7': u'\u2077',
            u'8': u'\u2078',
            u'9': u'\u2079'}

    return ''.join(sups.get(char, char) for char in number)  # lose the list comprehension

def power(var, exponent):
    '''
    Raises *var* to the *exponent* power
    '''
    return f"{var}{superscript_number(exponent)}"

def math_convert(line):
    fixed_line = str(line)
    fixed_line=fixed_line.replace("math.sqrt(","√(")
    fixed_line=fixed_line.replace("math.fabs(","abs(")
    fixed_line=fixed_line.replace("math.sin(","sin(")
    fixed_line=fixed_line.replace("math.cos(","cos(")
    fixed_line=fixed_line.replace("math.tan(","tan(")
    fixed_line=fixed_line.replace("math.asin(","asin(")
    fixed_line=fixed_line.replace("math.acos(","acos(")
    fixed_line=fixed_line.replace("math.atan(","atan(")
    fixed_line=fixed_line.replace("math.sinh(","sinh(")
    fixed_line=fixed_line.replace("math.cosh(","cosh(")
    fixed_line=fixed_line.replace("math.tanh(","tanh(")
    fixed_line=fixed_line.replace("math.asinh(","asinh(")
    fixed_line=fixed_line.replace("math.acosh(","acosh(")
    fixed_line=fixed_line.replace("math.atanh(","atanh(")
    fixed_line=fixed_line.replace("math.log(","ln(")
    fixed_line=fixed_line.replace("math.exp(","e^(")
    fixed_line=fixed_line.replace("math.floor(","int(")
    fixed_line=fixed_line.replace("math.log10(","log(")
    
    #same, but without "math." They might use
    #from math import sqrt etc...
    fixed_line=fixed_line.replace("sqrt(","√(")
    fixed_line=fixed_line.replace("fabs(","abs(")
    #(Redundant fixed_lines deleted)
    fixed_line=fixed_line.replace("log(","ln(")
    fixed_line=fixed_line.replace("exp(","e^(")
    fixed_line=fixed_line.replace("floor(","int(")
    fixed_line=fixed_line.replace("log10(","log(")

    if not (fixed_line == line):
        math_convert(fixed_line)
    
    return fixed_line

def basic_append(input):
    '''Appends the input to the existing TI-Basic code.\n
    NOTE: You don't call this function! This is automatically called by the module after a line is translated to Basic.'''
    global ti_basic
    ti_basic += str(input) + "\n"

def get_option_start_end_lines(menu, option): # automatically finds where each option's code starts and ends in its function
    function_lines = get_function_code(menu)
    parameter = menu.get_parameter()
    option_name = option.get_option_name()
    start = 0
    end = 0

    for line in function_lines:
        regex_result = re.search("if.*" + str(parameter) + r"\s*==\s*\"" + str(option_name) + "\".*:", line)
        if(regex_result):
            start = function_lines.index(line) + 1
            break
    
    i = start
    while i < len(function_lines):
        if(i == len(function_lines) - 1):
            # this is the end of the function, so this is also the end of the option's code
            end = i
            break
        
        line = function_lines[i + 1]
        regex_result = re.search(r"if.*" + str(parameter) + r".*==.*\".*\".*:", line)
        if(regex_result):
            end = i
            break
        i += 1

    return [start, end]

def get_function_code(menu): # returns the code of a menu's function
    try:
        return function_code[menu.get_function().__name__]
    except KeyError:
        function_code[menu.get_function().__name__] = str(inspect.getsource(menu.get_function())).splitlines()
        return function_code[menu.get_function().__name__]

def get_option_code(menu, option):
    function_lines = get_function_code(menu)
    option_lines = []

    i = option.get_start_line()
    while i <= option.get_end_line():
        option_lines.append(function_lines[i].strip())
        i += 1
    return option_lines

def fix_negatives(line):
    '''
    Gives negative numbers the negation symbol instead of just the - sign, preventing negation errors in the calculator
    '''
    line = str(line)

    # my best attempt at a regex that identifies all negative numbers in a line
    negative_search_regex = r"(?:[-+*=].*?(-\d+))|^\s*(-\d+)|\(\s*(-\d+)|,\s*(-\d+)"
    re_result = re.finditer(negative_search_regex, line)
    re_result_groups = re.findall(negative_search_regex, line)

    negatives = []
    indices = []

    for count, match in enumerate(re_result, 0):
        match_groups = re_result_groups[count]
        for group in match_groups:
            negatives.append(group)
            indices.append(match.group().rfind("-") + match.start())

    #print(f"{line}\n{negatives}\n{indices}\n")

    line_chars = list(line)
    for index in indices:
        line_chars[index] = "­"
    line = "".join(line_chars)

    return line

def string_insert(source_str, insert_str, pos):
    '''
    Inserts the "insert_str" at index "pos" in "source_str"
    '''
    return source_str[:pos] + insert_str + source_str[pos:]

def identify_line(line):
    '''Uses regex to look at each line and categorize it. The line is then translated differently depending on its type.'''

    global pb_import_name

    # Define the dictionary that will be returned with the line identification
    line_values = {
        "empty_line" : False,
        "string_object" : False,
        "list_object" : False,
        "pb_function" : False,
        "math_module" : False,
        "variable_set" : False,
        "if_while" : False
    }

    # 1. Check if the line is a comment (begins with #) or is blank
    # NOTE: If this is true, we skip over the rest of identification.
    if line.startswith("#") or not line: # "not line" checks for a blank line
        line_values["empty_line"] = True
        return line_values

    # 2. Check if the line uses a string object
    pb_string_regex = f"{pb_import_name}\.STR\d"
    if(re.search(pb_string_regex, line)):
        line_values["string_object"] = True

    # 3. Check if the line uses a list object
    pb_list_regex = rf"([\w]+)\s*\.\s*(set_list|set_index|get_list|append|pop|contains_number|get_index|remove_index|remove_value)\s*\(.*\)"
    if(re.search(pb_list_regex, line)):
        line_values["list_object"] = True

    # 4. Check if the line calls a function from this module
    pb_function_regex = f"{pb_import_name}\."
    if(re.search(pb_function_regex, line)):
        line_values["pb_function"] = True
    
    # 5. Check if the line uses the math module
    math_regex = rf"{math_import_name}\."
    if(re.search(math_regex, line)):
        line_values["math_module"] = True

    # 6. Check if the line sets the value of a variable (i.e., x = 4)
    variable_set_regex = r"^([\w\d]+)\s*(?!==)(?:(?:=|\+=|-=|\/=))\s*(.*)"
    if (re.search(variable_set_regex, line)):
        line_values["variable_set"] = True

    # 7. Check if the line initializes an if statement or a for/while loop
    if_while_regex = r"^(?:(?:if)|(?:while))"
    if(re.search(if_while_regex, line)):
        line_values["if_while"] = True

    return line_values

def get_arguments(function_call):
    '''
    Returns the arguments in the outmost function in the string. Nested functions' arguments are ignored.
    '''

    # First, regex is used to determine if the parentheses are empty/contains only whitespace. This means there are no arguments within them
    
    argument_search = rf"^{pb_import_name}\.[\w\d]+\(\s*\)" # returns a match if the outtermost function has NO arguments
    re_result = re.search(argument_search, function_call)
    if re_result:
        return []

    index = function_call.index("(") + 1 # so we start at where the arguments begin as opposed to the beginning of the line
    closing_left = 1 # goes up for each opening parentheses, down for each closing parentheses
    argument_count = 1 # at least one exists because the regex matched
    splitters = [] # where each comma that splits the arguments lies in the string
    splitters.append(index)

    #TODO: realize that parentheses in strings will eff this up
    while index < len(function_call):
        if function_call[index] == "," and closing_left == 1: # because commas separate arguments
            argument_count += 1
            splitters.append(index)
        if function_call[index] == "(":
            closing_left += 1
        if function_call[index] == ")":
            closing_left -= 1
        index += 1

    raw_args = [function_call[i:j] for i,j in zip(splitters, splitters[1:]+[None])] # dunno what the hell this does but thank you stackoverflow
    arguments = []
    for argument in raw_args:
        # clean everything up before returning
        
        if argument.endswith(")") and argument == raw_args[-1]:
            argument = argument[:len(argument) - 1]

        if argument.startswith(","):
            argument = argument.replace(",", "", 1)
        argument = argument.strip()
        arguments.append(argument)

    return arguments

def translate_pb_function(line):
    '''
    Translates the leftmost Python Basic function in the given line into its corresponding calculator command,
    then returns the line with the translation applied
    '''

    print(f"Translate PB Function called! Line: {line}")

    pb_function_identifier = f"(?:{pb_import_name}\.([\w\d]*?)\()"
    re_result = re.search(pb_function_identifier, line)
    if(re_result):
        # Identify the function name (Output, Prompt, normalCdf, etc)
        pb_function_name = re_result.groups()[0]

        start_index = line.index(re_result.group())
        splitters = []
        splitters.append(str(line).index("(", start_index))
        
        # While loop gets the substring containing this specific function within the line
        open_parentheses = 0
        index = start_index
        while index < len(line):
            if line[index] == "," and open_parentheses == 1: # because commas separate arguments
                splitters.append(index)
            if line[index] == "(":
                open_parentheses += 1
            if line[index] == ")":
                open_parentheses -= 1

                if open_parentheses == 0:
                    # We just encountered the closing parentheses that corresponds to the opening parentheses for this function
                    # So, we break the loop
                    break
            index += 1
        end_index = index + 1 # +1 so we actually include the final closing parentheses in the substring

        # NOTE: function_call is the substring within the line that has the specific PB function to translate.
        # Also note that the function_call substring could be the whole line, if the line is just a single PB command
        # Example: function_call = "pb.output(5,1,"Hey there!")"
        function_call = line[start_index:end_index]
        function_arguments = get_arguments(function_call)
        
        print(f"function call is {function_call}\narguments are {function_arguments}\nfunction name is {pb_function_name}")
        
        if len(function_arguments) > 1:
            function_arguments.insert(0, pb_function_name)
            translated_function_call = list_input(function_arguments)
            translated_line = line.replace(function_call, translated_function_call)
            return translated_line
        elif len(function_arguments) == 1:
            translated_function_call = globals()[pb_function_name](function_arguments[0])
            translated_line = line.replace(function_call, translated_function_call)
            return translated_line
        elif len(function_arguments) == 0:
            translated_function_call = globals()[pb_function_name]()
            translated_line = line.replace(function_call, translated_function_call)
            return translated_line
        
    else:
        # no PB functions were found, but this function was still called
        # this must mean a PB literal is being used, so it is translated here

        pb_literal_finder = rf"{pb_import_name}\.([\w\d]+)\s*(?=,|\)|$)"
        re_matches = re.finditer(pb_literal_finder, line)
        re_groups = re.findall(pb_literal_finder, line)

        for count, match in enumerate(re_matches, 0):
            line = line.replace(match.group(), globals()[re_groups[count]])

        return line

def translate_pb_string(line):
    '''
    Translates string objects (STR[0-9]) into calculator commands
    '''
    global pb_import_name

    string_set_regex = f"{pb_import_name}\.STR(\d)\.set\((.*)\)"
    re_result = re.search(string_set_regex, line)
    if re_result:
        # STR.set is used
        match = re_result.group()
        groups = re_result.groups()

        line = line.replace(match, f"{remove_spaces(f"{groups[1]}→Str{groups[0]}")}")
        print(f"RETURNING LINE {line}")
        return line
    
    string_get_regex = f"{pb_import_name}\.STR(\d)\.get_string\(\)"
    re_result = re.search(string_get_regex, line)
    if re_result:
        # STR.get is used
        match = re_result.group()
        groups = re_result.groups()

        line = line.replace(match, f"Str{groups[0]}")
        return line
    
def translate_pb_list(line): # This turned out so much better than it should've
    global pb_import_name, user_created_lists, global_vars

    pb_list_regex = r"([\w]+)\s*\.\s*(set_list|set_index|get_list|append|pop|contains_number|get_index|remove_index|remove_value)"
    re_result = re.search(pb_list_regex, line)
    if re_result:
        re_groups = re_result.groups()

        selected_list = next((x for x in user_created_lists if x.get_object_name() == re_groups[0]), None)
        command = re_groups[1]
        variable = get_outermost_parentheses(line, re_result.start())
        print(f"Variable for {line} is {variable}")

        string_to_replace = f"{re_result.group()}({variable})"

        
        if variable:
            print(f"Replacing {string_to_replace} in {line} with {str(getattr(selected_list, command)(variable))}")
            line = line.replace(string_to_replace, str(getattr(selected_list, command)(variable)))
        else:
            print(f"Replacing {string_to_replace} in {line} with {str(getattr(selected_list, command)())}")
            line = line.replace(string_to_replace, str(getattr(selected_list, command)()))
        
    return line

def get_outermost_parentheses(line, start_index):
    '''Takes the line, and, starting from start_index, finds the first open parentheses and returns everything in THAT pair of parentheses, including any nested parentheses.'''
    line_chars = list(line)

    i = start_index
    parentheses_level = 0
    in_quotes = False # if true, we ignore parentheses, as they are inside of a string
    returning_chars = [] # the characters in the parentheses to be returned

    print(f"String: {line}  Start index: {start_index}")
    while i < len(line_chars):
        char = line_chars[i]

        if char != "(" and parentheses_level == 0:
            i += 1
            continue
        if char == '"':
            in_quotes = not in_quotes # inverting the value
            i += 1
            returning_chars.append(char)
            continue
        if char == "(" and not in_quotes:
            parentheses_level += 1
            i += 1
            if parentheses_level != 1:
                returning_chars.append(char)
            continue
        elif char == ")" and not in_quotes:
            parentheses_level -= 1
            if parentheses_level == 0:
                break
            else:
                i += 1
                returning_chars.append(char)
                continue
        else:
            i += 1
            returning_chars.append(char)
            continue

    returning_chars = "".join(returning_chars) # to turn it into a string

    print(f"Returning chars: {returning_chars}")
    return returning_chars

def translate_one_function(function):
    '''
    Used when the user only wants to translate one function instead of a menu structure
    '''
    global in_indented_block, statement_indentations, indentations, file_lines

    translated_lines = []
    current_index = 1 # to skip the line beginning with "def xxx():"

    # This line finds the line number in the child script that this function begins on
    function_start_line = list(file_lines.keys())[list(file_lines.values()).index(function_code[function.__name__][0].strip())]
    
    # This line gives us the list of strings representing the lines of the chosen function
    function_lines = function_code[function.__name__]

    while current_index < len(function_lines):
        # We start on the first line of this option's code within its function, and current_index ensures we increment by one line each iteration
        master_index = function_start_line + current_index
        
        # In simplier terms, master_index is the line number of this line in the child script

        current_line = file_lines[master_index]
        line_index = master_index
        line_indentation = indentations[master_index]

        #print(f"line: {current_line}, index: {line_index}")
        # Check if this line is part of an indented segment. If not, append the End statement
        if in_indented_block and line_indentation <= statement_indentations[-1] and current_line:
            print(f"Difference in indents is {indentations[master_index - 1] - line_indentation}")
            if current_line == "else:" and line_indentation == statement_indentations[-1]:
                translated_lines.append("Else")
                current_index += 1
                continue
            else:
                statement_indentations.pop()
                translated_lines.append("End")

                if not statement_indentations:
                    # if there are no more indented blocks that we are within, reset the boolean
                    in_indented_block = False
                
                continue

        translated_line = translate_line(current_line, line_index)
        translated_lines.append(translated_line)
        
        if translated_line.startswith("If"):
            translated_lines.append("Then")
        
        current_index += 1
    
    return translated_lines

def translate_option_code(option):
    '''
    Accepts a menuOption passed from setup(), and returns a translated list of strings
    '''
    global in_indented_block, statement_indentations, indentations, file_lines

    translated_option_code = [] # the translated list of strings to be returned

    # 1. Get the lines that make up this specific menuOption object
    option_code = get_option_code(option.get_menu(), option)
    
    # 2. This line finds the line number in the child script that the function of this specified option begins on
    function_start_line = list(file_lines.keys())[list(file_lines.values()).index(get_function_code(option.get_menu())[0])]
    
    current_index = 0

    while current_index < len(option_code):
        # We start on the first line of this option's code within its function, and current_index ensures we increment by one line each iteration
        master_index = function_start_line + option.get_start_line() + current_index
        
        # In simplier terms, master_index is the line number of this line in the child script

        current_line = file_lines[master_index]
        line_index = master_index
        line_indentation = indentations[master_index]

        #print(f"line: {current_line}, index: {line_index}")
        # Check if this line is part of an indented segment. If not, append the End statement
        if in_indented_block and line_indentation <= statement_indentations[-1] and current_line:
            if current_line == "else:" and line_indentation == statement_indentations[-1]:
                translated_option_code.append("Else")
                current_index += 1
                continue
            else:
                statement_indentations.pop()
                translated_option_code.append("End")

                if not statement_indentations:
                    # if there are no more indented blocks that we are within, reset the boolean
                    in_indented_block = False

        translated_line = translate_line(current_line, line_index)
        translated_option_code.append(translated_line)
        
        if translated_line.startswith("If"):
            translated_option_code.append("Then")
        
        current_index += 1
    
    return translated_option_code

def remove_spaces(input):
    '''
    Returns a copy of the input string with spaces removed, except for spaces that are contained within strings
    '''
    input = str(input)

    new_string_chars = []
    in_quotes = False

    index = 0
    while index < len(input):
        char = input[index]

        if char == '"':
            if not in_quotes:
                in_quotes = True
            else:
                in_quotes = False
        
        if char != " " or in_quotes:
            new_string_chars.append(char)
        
        index += 1

    return "".join(new_string_chars)

def translate_if_while(line):
    line = str(line)
    condition = "" # the entire substring after the if/while
    conditions = "" # condition split by and/or

    line = line.replace("!=", "≠")
    line = line.replace(">=", "≥")
    line = line.replace("<=", "≤")
    line = line.replace("==", "=")

    condition_grabber = r"(?:if|while|for)(?:\(|\s+)\(?(.*?)\s*\)?\s*:"
    re_result = re.search(condition_grabber, line)
    if(re_result):
        condition = re_result.groups()[0]

        and_or_regex = r"(.*?)(\s*(?:and|or|$)\s*)"
        conditions = re.findall(and_or_regex, condition)
        
        translated_condition = ""
        for match in conditions:
            for text in match:
                if not " and " in text and not " or " in text:
                    translated_condition += remove_spaces(text)
                else:
                    translated_condition += text

    if line.startswith("if"):
        return f"If {translated_condition}"
    if line.startswith("while"):
        return f"While {translated_condition}"

def translate_line(line, line_index): # actually not so bad anymore
    global pb_import_name, in_indented_block, statement_indentations, indentations

    # 1. Before translating, we call identify_line() to get an overview of the line
    line_info = identify_line(line)

    print(f"Attempting to translate: {line}")
    print(f"Line info: {line_info}")
    
    # 2. Look at each value in the dictionary and translate whatever is needed

        # 2(a): If the line is a comment / empty, an empty string is returned, as there is nothing to be done
    if line_info["empty_line"]:
        return ""
    
        # 2(b): If a string is used, we translate_pb_string is called
    if line_info["string_object"]:
        line = translate_pb_string(line)

        # 2(c): If a list is used, translate_pb_object is used
    if line_info["list_object"]:
        line = translate_pb_list(line)

        # 2(d): If the line contains a PB function, translate_pb_function is called
    if line_info["pb_function"]:
        line = translate_pb_function(line)

        # 2(e): If the line uses the math module, we convert it into the corresponding calculator commmand
    if line_info["math_module"]:
        line = math_convert(line)

        # 2(f): A variable is set (i.e., x = 4)
    if line_info["variable_set"]:
        line = reformat_equation(line)

        # 2(g): An if, for, or while statement is defined
    if line_info["if_while"]:
        # Declare that we're now in an indented code block
        in_indented_block = True
        statement_indentations.append(indentations[line_index])
        #print(f"Line: {line}\tIndent: {statement_indentations[-1]}")

        line = translate_if_while(line)
        

    # End of function checks
    done_translating = True
    for attr in line_info.values():
        if attr:
            done_translating = False
            break
    
    if done_translating:
        return line
    else:
        return translate_line(line, line_index) # recursion baby

def list_input(input): # for when we need to make a call with globals() but we have multiple parameters
    for item in input:
        # loop through each item in list to fix formatting
        index = input.index(item)
        fixed_item = str(item).replace("'", "").strip()
        input[index] = fixed_item
    print("fixed list " + str(input))

    # first item in list is the TI operation to perform
    function_name = input[0]
    if(len(input) == 3):
        return globals()[function_name](input[1], input[2])
    if(len(input) == 4):
        return globals()[function_name](input[1], input[2], input[3])
    if(len(input) == 5):
        return globals()[function_name](input[1], input[2], input[3], input[4])
    if(len(input) == 6):
        return globals()[function_name](input[1], input[2], input[3], input[4], input[5])

def read_file_lines(filename):
  '''Reads a Python file and returns a dictionary mapping line numbers to indentation levels.'''
  global file_lines, indentations

  current_indent = 0

  with open(filename, 'r') as file:
    for line_number, line in enumerate(file, 1):
        # Strip the line and put it into the line dictionary
        file_lines[line_number] = line.strip()

        # Remove trailing whitespace
        stripped_line = line.rstrip()

        # Count leading spaces for indentation
        line_indent = 0
        for char in stripped_line:
            if char == "\t": # \t is a tab break
                line_indent += 4
                continue
            if char != ' ' and char != "\t":
                break
            line_indent += 1

        # Update indentation based on braces
        if line.endswith(':'):
            current_indent += line_indent
        elif line.startswith('}') and current_indent > 0:
            current_indent = max(0, current_indent - line_indent)

        indentations[line_number] = line_indent

        #print(f"{line_number}: ({line_indent}) {line.strip()}")

def setup(child_globals, filename, chosen_function = None): # Called from child script to begin the heavy lifting
    global global_vars, file_lines, pb_import_name, math_import_name, ti_basic, indentations

    # 1. Get all file info for later
    global_vars = child_globals
    read_file_lines(filename)

    # 2. Get the shorthand for the modules in the child script
    for line in file_lines.values():
        if "import pythonbasic" in line:
            if(" as " in line):
                pb_import_name = line.split("import pythonbasic as ")[1].strip()
                print(f"imported as {pb_import_name}")
            else:
                pb_import_name = "pythonbasic"
            
            if math_import_name:
                break
        if "import math" in line:
            if(" as " in line):
                math_import_name = line.split("import math as ")[1].strip()
            else:
                math_import_name = "math"
            
            if pb_import_name:
                break
    
    if not chosen_function is None:
        function_code[chosen_function.__name__] = str(inspect.getsource(chosen_function)).splitlines()
        
        translated_function = translate_one_function(chosen_function)
        for line in translated_function:
            basic_append(line)
    else:
        # 3. Go through each menu that the user created and translate it to Basic
        for menu in all_menus:
            menuOptions = menu.get_options()

            basic_append(f"Lbl {menu.get_label()}")
            menu_syntax = f"Menu(\"{menu.get_title().upper()}\"" # starting syntax for the menu option in Basic

            for option in menuOptions:
                menu_syntax += f",\"{option.get_option_name().upper()}\",{option.get_label()}"
            
            basic_append(menu_syntax) # writes the line in Basic that declares the menu

            for option in menuOptions:
                basic_append(f"Lbl {option.get_label()}")
                
                translated_option_code = translate_option_code(option)
                for line in translated_option_code:
                    #translated_line = translateLine(line)
                    #print(f"TRANSLATION: {line}")
                    basic_append(line)
                
                basic_append(Stop())

    # 4. Check translated lines for negative numbers and fix them
    split_ti_basic = []
    for line in ti_basic.splitlines():
        line = line.replace("âˆŸ", "⌊").replace("âŒŠ", "⌊").replace("â†’", "→")
        split_ti_basic.append(fix_negatives(line))
    ti_basic = "\n".join(split_ti_basic)

    # 5. Write output to file
    filename = input("Enter the output file name. Omit .txt\n")
    filename += ".txt"
    file = open(filename, "w", encoding="utf-8")
    file.writelines(ti_basic)
    file.close()
    print("\nTI-Basic:\n" + ti_basic)

# Above are the functions that translate the module into Basic.
# Except for setup(), they should not be called by the user; rather, they should only be called from this module.















# Below are the functions to be called by the user, AKA, the actual calculator commands.

def abs(value):
	'''Returns the absolute value of a real number, and the complex absolute value of a complex number.'''
	return f"abs({value})"

def angle(z):
	'''Returns the complex argument of a complex number.'''
	return f"angle({z})"

def AsmComp(original,result):
    '''Compresses an assembly program in hexadecimal form into binary form.'''
    return f"Asm(prgm{original.replace('"', "")},prgm{result.replace('"', "")})"

def binomcdf(trials,probability,value=-1):
    '''Calculates the binomial cumulative probability, either at a single value or for all values'''
    if value == -1:
        return f"binomcdf({trials},{probability})"
    else:
        return f"binomcdf({trials},{probability},{value})"

def binompdf(trials,probability,value=-1):
    '''Calculates the binomial probability, either at a single value or for all values'''
    if value == -1:
        return f"binompdf({trials},{probability})"
    else:
        return f"binompdf({trials},{probability},{value})"

def ClrHome():
    '''Returns a *ClrHome* command.'''
    return "ClrHome"

def dim(list):
    '''The dim( command is used to find the size of an existing list or matrix. It takes only one argument - the list or matrix you want the size of. For a list, it returns the number of elements; for a matrix, it returns a two-element list of the number of rows and the number of columns.'''
    return f"dim({list})"

def checkTmr(Variable):
	'''Returns the number of seconds since the timer was started.'''
	return f"checkTmr({Variable})"

def Circle(X,Y,r):
	'''Draws a circle.'''
	return f"Circle({X},{Y},{r})"

def conj(value):
	'''Calculates the complex conjugate of a complex number.'''
	return f"conj({value})"

def cos(angle):
	'''Returns the cosine of a real number.'''
	return f"cos({angle})"

def cosh(value):
	'''Calculates the hyperbolic cosine of a value.'''
	return f"cosh({value})"

def cumSum(listormatrix):
	'''Calculates cumulative sums of a list or of the columns of a matrix.'''
	return f"cumSum({listormatrix})"

def dayOfWk(year,month,day):
	'''Returns an integer from 1 to 7, each representing a day of the week, given a date.'''
	return f"dayOfWk({year},{month},{day})"

def dbd(date1,date2):
	'''Calculates the number of days between two days.'''
	return f"dbd({date1},{date2})"

def DelVar(variable):
    '''The DelVar command deletes the contents of a variable (and thus the variable itself) from memory. You can use the DelVar command with any variable: reals, lists, matrices, strings, pictures, etc. However, you cannot use DelVar on specific elements of a matrix or string; it will actually throw a ERR:SYNTAX error. (It also does not work on programs, unfortunately.)'''
    return f"DelVar {variable}"

def det(matrix):
	'''Calculates the determinant of a square matrix.'''
	return f"det({matrix})"

def Disp(input):
    '''Displays the given input.'''
    return f"Disp {remove_spaces(input)}"

def End():
    '''Returns an *End* statement'''
    return "End"

def eval(string):
    '''The eval( command, given an expression that evaluates to a real number, returns the string representation of that number.'''
    return f"eval({string})"

def Exit():
    '''The Exit command immediately exits from a For..EndFor, Loop..EndLoop, or While..EndWhile loop. The program continues running from the instruction after the EndFor, EndLoop, or EndWhile.'''
    return "Exit"

def expr(string):
	'''Returns the value of a string that contains an expression.'''
	return f"expr({string})"

def Fill(value,matrix):
	'''Fills a list or matrix with one number.'''
	return f"Fill({value},{matrix})"

def floor(number):
    '''The floor() command rounds a number down to the nearest integer less than or equal to the number. For instance, floor(π) returns 3, while floor(-π) returns -4'''
    return f"floor({number})"

def fMax(function,var,min,max):
    '''fMax(f(var),var,lo,hi[,tol]) finds the value of var between lo and hi at which the maximum of f(var) occurs. tol controls the accuracy of the maximum value computed. The default value of tol is 10-5. fMax( only works for real numbers and expressions. Brent's method for optimization is used for approximating the maximum value.
    \nfMax(sin(X)cos(X),X,0,3)
    \n.7853995667'''
    return f"fMax({remove_spaces(function.strip('"').strip("'"))},{var},{min},{max})"

def fMin(function,var,min,max):
    '''fMin(f(var),var,lo,hi[,tol]) finds the value of var between lo and hi at which the minimum of f(var) occurs. tol controls the accuracy of the minimum value computed. The default value of tol is 10-5. fMin( only works for real numbers and expressions. Brent's method for optimization is used for approximating the minimum value.
    \nfMin(cos(sin(X)+Xcos(X)),X,0,2)
    \n1.076873875'''
    return f"fMin({remove_spaces(function.strip('"').strip("'"))},{var},{min},{max})"

def fnInt(function,var,a,b):
    '''fnInt(f(var),var,a,b[,tol]) computes an approximation to the definite integral of f with respect to var from a to b. tol controls the accuracy of the integral computed. The default value of tol is 10-5. fnInt( returns exact results for functions that are polynomials of small degree. fnInt( only works for real numbers and expressions. The Gauss-Kronrod method is used for approximating the integral. Tip: Sometimes, to get an answer of acceptable accuracy out of fnInt(, substitution of variables and analytic manipulation may be needed.'''
    return f"fnInt({remove_spaces(function.strip('"').strip("'"))},{var},{a},{b})"

def For(variable, start, end, step=1):
    '''
    Executes some commands many times, with a variable increasing from start to end by step, with the default value step=1.\n
    NOTE: After you've written the code to be contained in the For loop, put an End() function after it! Otherwise your loop will never close.
    '''
    return f"For({variable},{start},{end},{step})"

def fPart(value):
	'''Returns the fractional part of a value.'''
	return f"fPart({value})"

def Fpdf(x,numeratordf,denominatordf):
	'''Evaluates the F-distribution probability density function at a point.'''
	return f"Fpdf({x},{numeratordf},{denominatordf})"

def gcd(value1,value2):
	'''Finds the greatest common divisor of two values.'''
	return f"gcd({value1},{value2})"

def geometcdf(probability,trials):
	'''Calculates the cumulative geometric probability for a single value'''
	return f"geometcdf({probability},{trials})"

def geometpdf(probability,trials):
	'''Calculates the geometric probability for a single value'''
	return f"geometpdf({probability},{trials})"

def Get(variable):
	'''Gets a variable's value from a connected calculator or CBL device.'''
	return f"Get({variable})"

def GetCalc(variable):
	'''Gets a variable from another calculator.'''
	return f"GetCalc({variable})"

def getKey():
    '''The getKey() command returns the key code of the last keypress. If no key was pressed since the program, function, or expression started running, or since the last getKey() command, getKey() returns 0. It's important to note that once getKey() is used, the keypress is forgotten — even if it's used in the same line! So most of the time you want to store the result of getkey to a variable to use it.'''
    return "getKey"

def get_color_number(color: COLORS = "BLUE"):
    '''Returns the numeric value of the given color string. Ranges from 10-24.'''
    color = color.strip('"').strip("'")
    if color not in COLOR_LIST:
        print(f"Unaccepted color {color}")
    else:
        return str(10 + COLOR_LIST.index(color))

def getDtStr(value):
	'''Returns the current date of the clock on the TI-84+/SE/CE as a string.'''
	return f"getDtStr({value})"

def getTmStr(value):
	'''Returns the current time of the clock on the TI-84+/SE as a string.'''
	return f"getTmStr({value})"

def goto_label(label):
    global global_vars

    if(".get_label()" in label): # a literal string was not given
        label = global_vars[f"{label.split(".")[0]}"].get_label()

    return f"Goto {label.strip('"')}"

def goto_menu(menu):
    '''Takes a menu object and returns a Goto command pointing to that menu's label.'''
    global global_vars, all_menus

    menu = global_vars[menu]

    for m in all_menus:
        if m == menu:
            try:
                return f"Goto {m.get_label()}"
            except:
                print(f"No label found for {m}")

def goto_menu_title(menu_title):
    global global_vars, all_menus
    
    if(".get_title()" in menu_title): # a literal string was not given
        menu_title = global_vars[f"{menu_title.split(".")[0]}"].get_title()

    for menu in all_menus:
        if menu.get_title() == menu_title:
            return f"Goto {menu.get_label()}"
    # if no match
    print("No label found for " + menu_title)

# def GraphStyle(equation#,style#):
# 	'''Sets the graphing style of a graphing equation in the current mode.'''
# 	return f"GraphStyle({equation#},{style#})"

def identity(n):
	'''Creates an n by n identity matrix.'''
	return f"identity({n})"

def imag(value):
	'''Returns the imaginary part of a complex number.'''
	return f"imag({value})"

def inString(haystack,needle,startingpoint):
	'''Finds the first occurrence of a search string in a larger string.'''
	return f"inString({haystack},{needle},{startingpoint})"

def Int(value):
    '''Rounds a value down to the nearest integer.'''
    return f"int({value})"

def invNorm(probability,mean=0,sd=1,tail_direction: TAIL_DIRECTIONS = "BLANK"):
    '''invNorm( is the inverse of the cumulative normal distribution function: given a probability, it will give you a z-score with that tail probability. The probability argument of invNorm( is between 0 and 1; 0 will give -1E99 instead of negative infinity, and 1 will give 1E99 instead of positive infinity.'''
    if tail_direction != "BLANK":
        return f"invNorm({probability},{mean},{sd},{tail_direction})"
    else:
        return f"invNorm({probability},{mean},{sd})"
    
def invT(probability,ν):
	'''Calculates the inverse of the cumulative Student's t-distribution function with degrees of freedom ν.'''
	return f"invT({probability},{ν})"

def iPart(value):
	'''Returns the integer part of a value.'''
	return f"iPart({value})"

def Lbl(label):
    '''Using Lbl is simple: just put it (on a line by itself) at a point in the program you might want to jump to later, and add an identifier. The identifiers TI-Basic allows are one or two characters long, and made up of letters and numbers (so Lbl 0, Lbl XY, Lbl A5, and Lbl 99 are all valid labels). When the program is running normally, the calculator will just skip over a label as though it weren't there.'''
    return f"Lbl {label.replace('"', "").replace("'", "")}"
    
def lcm(value1,value2):
	'''Finds the least common multiple of two values.'''
	return f"lcm({value1},{value2})"

def length(string):
	'''Returns the length of a string.'''
	return f"length({string})"

def Line(x1,y1,x2,y2):
    '''The Line( command is used to draw lines at any angle, as opposed to only drawing vertical or horizontal lines. Line(X1,Y1,X2,Y2) will draw a line from (X1,Y1) to (X2,Y2). Line( is affected by the window settings, although you can use a friendly window so there is no impact on the command.'''
    return f"Line({x1},{y1},{x2},{y2})"

def literal_tibasic(input):
    '''
    Whatever is passed as input will be put into the final output file without any translation.\n
    This may be useful if you need an especially complex line that this module isn't capable of creating automatically.
    '''
    return input.strip('"').strip("'")

def ln(value):
	'''Computes the (principal branch of the) natural logarithm.'''
	return f"ln({value})"

def log(value,base=-1):
    '''The log( command computes the base 10 logarithm of a value — the exponent to which 10 must be raised, to get that value. This makes it the inverse of the 10^( command. log( is a real number for all positive real values. For negative numbers, log( is an imaginary number (so taking log( of a negative number will cause ERR:NONREAL ANS to be thrown in Real mode), and of course it's a complex number for complex values. log( is not defined at 0, even if you're in a complex mode.'''
    if(base == -1):
        return f"log{value}"
    else:
        return f"log{value},{base}"

def max(value1,value2 = None):
    '''max(X,Y) returns the largest of the two numbers X and Y. max(list) returns the largest element of list. max(list1,list2) returns the pairwise maxima of the two lists. max(list1,X) (equivalently, max(X,list1)) returns a list whose elements are the larger of X or the corresponding element of the original list.'''
    if value2 is None:
        return f"max({remove_spaces(value1)})"
    else:
        return f"max({remove_spaces(value1)},{remove_spaces(value2)})"
    
def mean(list,frequency_list = None):
    '''The mean( command finds the mean, or the average, of a list. It's pretty elementary. It takes a list of real numbers as a parameter.'''
    if frequency_list is None:
        return f"mean({list})"
    else:
        return f"mean({list},{frequency_list})"
    
def median(list,frequency_list = None):
    '''The median( command finds the median of a list. It takes a list of real numbers as a parameter.'''
    if frequency_list is None:
        return f"median({list})"
    else:
        return f"median({list},{frequency_list})"
    
def min(value1,value2 = None):
    '''min(x,y) returns the smallest of the two numbers x and y. min(list) returns the smallest element of list. min(list1,list2) returns the pairwise minima of the two lists. min(list1,x) (equivalently, min(x,list1)) returns a list whose elements are the smaller of x or the corresponding element of the original list.'''
    if value2 is None:
        return f"min({remove_spaces(value1)})"
    else:
        return f"min({remove_spaces(value1)},{remove_spaces(value2)})"
    
def ncr(int1,int2):
    '''nCr is the number of combinations function (or binomial coefficient), defined as a nCr b = a!/(b!*(a-b)!), where a and b are nonnegative integers. The function also works on lists.'''
    return f"{int1} nCr {int2}"

def nDeriv(function,var,value,h=.001):
    '''nDeriv(f(var),var,value[,h]) computes an approximation to the value of the derivative of f(var) with respect to var at var=value. h is the step size used in the approximation of the derivative. The default value of h is 0.001.'''
    return f"nDeriv({remove_spaces(function)},{var},{value},{h})"

def normalcdf(lower,upper,mean=0,sd=1):
    '''normalcdf( is the normal (Gaussian) cumulative density function. If some random variable follows a normal distribution, you can use this command to find the probability that this variable will fall in the interval you supply. There are two ways to use normalcdf(. With two arguments (lower bound and upper bound), the calculator will assume you mean the standard normal distribution, and use that to find the probability corresponding to the interval between "lower bound" and "upper bound". You can also supply two additional arguments to use the normal distribution with a specified mean and standard deviation.'''
    return f"normalcdf({lower},{upper},{mean},{sd})"

def normalpdf(x,mean=0,sd=1):
    '''normalpdf( is the normal (Gaussian) probability density function. Since the normal distribution is continuous, the value of normalpdf( doesn't represent an actual probability - in fact, one of the only uses for this command is to draw a graph of the normal curve. You could also use it for various calculus purposes, such as finding inflection points. The command can be used in two ways: normalpdf(x) will evaluate the standard normal p.d.f. (with mean at 0 and a standard deviation of 1) at x, and normalpdf(x,μ,σ) will work for an arbitrary normal curve, with mean μ and standard deviation σ.'''
    return f"normalpdf({x},{mean},{sd})"

def NormProbPlot(plot_number,data_list,data_axis,mark: MARKS = "▫"):
    '''Plot#(NormProbPlot, data list, data axis, mark) defines a normal probability plot. The mean and standard deviation of the data are calculated. Then for each point, the number of standard deviations it is from the mean is calculated, and the point is plotted against this number using mark. data axis can be either X or Y: it determines whether the value of a point determines it's x-coordinate or y-coordinate. The point behind this rather convoluted process is to test the extent to which the data is normally distributed. If it follows the normal distribution closely, then the result will be close to a straight line - otherwise it will be curved.'''
    mark = FIXED_MARKS[mark.strip("'").strip('"')]
    return f"Plot{plot_number}(NormProbPlot,{data_list},{data_axis},{mark})"

def Not(value):
    '''Flips the truth value of its argument.'''
    return f"not({value})"

def npr(int1,int2):
    '''nPr is the number of permutations function, defined as a nPr b = a!/(a-b)!, where a and b are nonnegative integers. The function also works on lists.'''
    return f"{int1} nPr {int2}"

def npv(interest_rate,cf0,cf_list,cf_freq=None):
    '''The npv( command computes the net present value of money over a specified time period. If a positive value is returned after executing npv(, that means it was a positive cashflow; otherwise it was a negative cashflow. The npv( command takes four arguments, and the fourth one is optional:\n\ninterest rate — the percentage of the money that is paid for the use of that money over each individual period of time.\n\nCF0 — the initial amount of money that you start out with; this number must be a real number, otherwise you will get a ERR:DATA TYPE error.\n\nCFList — the list of cash flows added or subtracted after the initial money.\n\nCFFreq — the list of frequencies of each cash flow added after the initial money; if this is left off, each cash flow in the cash flow list will just appear once by default.'''
    if cf_freq is None:
        return f"npv({interest_rate},{cf0},{cf_list})"
    else:
        return f"npv({interest_rate},{cf0},{cf_list},{cf_freq})"

def OnePropZInt(x,n,c_level):
    '''The 1-PropZInt( command calculates a confidence interval for a proportion, at a specific confidence level: for example, if the confidence level is 95%, you are 95% certain that the proportion lies within the interval you get. The command assumes that the sample is large enough that the normal approximation to binomial distributions is valid: this is true if, in the sample you take, the positive and negative counts are both >5. The 1-PropZInt( command takes 3 arguments. The first, x, is the positive count in the sample. The second, n, is the total size of the sample. (So the sample proportion is equal to x out of n). The third argument is the confidence level, which defaults to 95. The output gives you a confidence interval of the form (a,b), meaning that the true proportion π is most likely in the range a<π<b, and the value of x/n.'''
    return f"1-PropZInt({x},{n},{c_level})"

def OnePropZTest(null,x,n,prop: ALTERNATIVES = "NOT_EQUAL",draw=0):
    '''1-PropZTest performs an z-test to compare a population proportion to a hypothesis value. This test is valid for sufficiently large samples: only when the number of successes (x in the command syntax) and the number of failures (n-x) are both >5.\n\nThe logic behind the test is as follows: we want to test the hypothesis that the true proportion is equal to some value p0 (the null hypothesis). To do this, we assume that this "null hypothesis" is true, and calculate the probability that the (usually, somewhat different) actual proportion occurred, under this assumption. If this probability is sufficiently low (usually, 5% is the cutoff point), we conclude that since it's so unlikely that the data could have occurred under the null hypothesis, the null hypothesis must be false, and therefore the true proportion is not equal to p0. If, on the other hand, the probability is not too low, we conclude that the data may well have occurred under the null hypothesis, and therefore there's no reason to reject it.\n\nCommonly used notation has the letter π being used for the true population proportion (making the null hypothesis be π=p0). TI must have been afraid that this would be confused with the real number π, so on the calculator, "prop" is used everywhere instead.\n\nIn addition to the null hypothesis, we must have an alternative hypothesis as well - usually this is simply that the proportion is not equal to p0. However, in certain cases, our alternative hypothesis may be that the proportion is greater or less than p0.\n\n\nThe arguments to 1-PropZTest( are as follows:\n\np0 - the value for the null hypothesis (the proportion you're testing for)\n\nx - the success count in the sample\n\nn - the total size of the sample (so the sample proportion would be x/n)\n\nalternative (optional if you don't include draw?) - determines the alternative hypothesis\n\n0 (default value) - prop≠p0\n\n-1 (or any negative value) - prop<p0\n\n1 (or any positive value) - prop>p0\n\ndraw? (optional) set this to 1 if you want a graphical rather than numeric result'''

    alternative = 0
    if prop == "NOT_EQUAL": alternative = 0
    if prop == "LESS": alternative = -1
    if prop == "GREATER": alternative = 1

    return f"1-PropZTest({null},{x},{n},{alternative},{draw})"

def OpenLib(library):
	'''Sets up a compatible Flash application library for use with ExecLib'''
	return f"OpenLib({library})"

def Output(row,column,expression):
	'''Displays an expression on the home screen starting at a specified row and column. Wraps around if necessary.'''
	return f"Output({row},{column},{expression})"

def Pause():
    ''''Returns a *Pause* command.'''
    return "Pause "

def PlotBoxplot(plot_number,x_list,frequency_list):
    '''Plot#(Boxplot, x-list, freq list) defines a box plot. A rectangular box is drawn whose left edge is Q1 (the first quartile) of the data, and whose right edge is Q3 (the third quartile). A vertical segment is drawn within the box at the median, and 'whiskers' are drawn from the box to the minimum and maximum data points. The box plot ignores the Ymax and Ymin dimensions of the screen, and any plots that aren't box plots or modified box plots. Each box plot takes approximately 1/3 of the screen in height, and if more than one are plotted, they will take up different areas of the screen.'''
    return f"Plot{plot_number}(Boxplot,{x_list},{frequency_list})"

def PlotHistogram(plot_number,x_list,frequency_list):
    '''Plot#(Histogram, x-list, freq list) defines a Histogram plot. The x-axis is divided into intervals that are Xscl wide. A bar is drawn in in each interval whose height corresponds to the number of points in the interval. Points that are not between Xmin and Xmax are not tallied. Xscl must not be too small - it can divide the screen into no more than 47 different bars.'''
    return f"Plot{plot_number}(Histogram,{x_list},{frequency_list})"

def PlotModBoxplot(plot_number,x_list,frequency_list,mark: MARKS = "▫"):
    '''Plot#(ModBoxplot, x-list, freq list, mark) defines a modified box plot. This is almost entirely like the normal box plot, except that it also draws outliers. Whiskers are only drawn to the furthers point within 1.5 times the interquartile range (Q3-Q1) of the box. Beyond this point, data points are drawn individually, using mark. The box plot ignores the Ymax and Ymin dimensions of the screen, and any plots that aren't box plots or modified box plots. Each box plot takes approximately 1/3 of the screen in height, and if more than one are plotted, they will take up different areas of the screen.'''
    mark = FIXED_MARKS[mark.strip("'").strip('"')]
    return f"Plot{plot_number}(ModBoxplot,{x_list},{frequency_list},{mark})"

def PlotScatter(plot_number,x_list,y_list,mark: MARKS = "▫"):
    '''Plot#(Scatter, x-list, y-list, mark) defines a scatter plot. The points defined by x-list and y-list are plotted using mark on the graph screen. x-list and y-list must be the same length.'''
    mark = FIXED_MARKS[mark.strip("'").strip('"')]
    return f"Plot{plot_number}(Scatter,{x_list},{y_list},{mark})"

def PlotxyLine(plot_number,x_list,y_list,mark: MARKS = "▫"):
    '''Plot#(xyLine, x-list, y-list, mark) defines an xyLine plot. Similarly to a scatter plot, the points defined by x-list and y-list are plotted using mark on the graph screen, but with an xyLine plot they are also connected by a line, in the order that they occur in the lists. x-list and y-list must be the same length.'''
    mark = FIXED_MARKS[mark.strip("'").strip('"')]
    return f"Plot{plot_number}(xyLine,{x_list},{y_list},{mark})"

def poissoncdf(mean,value):
	'''Calculates the Poisson cumulative probability for a single value'''
	return f"poissoncdf({mean},{value})"

def poissonpdf(mean,value):
	'''Calculates the Poisson probability for a single value'''
	return f"poissonpdf({mean},{value})"

def prod(list,start=-1,end=-1):
    '''The prod( command calculates the product of all or part of a list. When you use it with only one argument, the list, it multiplies all the elements of the list. You can also give it a bound of start and end and it will only multiply the elements starting and ending at those indices (inclusive).'''
    if start == -1 and end == -1:
        return f"prod({list})"
    elif start != -1 and end != -1:
        return f"prod({list},{start},{end})"
    elif start != -1 and end == -1:
        return f"prod({list},{start})"
    else:
        return f"prod({list})"

def Prompt(variable):
    '''Prompts the user for a variable. Make sure you follow Basic's rules for variable names!'''
    return f"Prompt {variable}"

def PtChange(X,Y):
	'''Toggles a point on the graph screen.'''
	return f"Pt-Change({X},{Y})"

def Pt_Off(x,y):
    '''The Pt-Off( command is used to turn off a point (a pixel on the screen) on the graph screen at the given (X,Y) coordinates. Pt-Off( is affected by the window settings, which means you have to change the window settings accordingly, otherwise the point won't show up correctly on the screen.'''
    return f"Pt-Off({x},{y})"

def Pt_On(x,y):
    '''The Pt-On( command is used to draw a point on the graph screen at the given (X,Y) coordinates. Pt-On( is affected by the window settings Xmin, Xmax, Ymin, and Ymax. Make sure to change these accordingly when using it in a program, otherwise, you don't know where the point will show up.'''
    return f"Pt-On({x},{y})"

def PxlChange(row,column):
	'''Toggles a pixel on the graph screen.'''
	return f"Pxl-Change({row},{column})"

def PxlOff(row,column):
	'''Turns off a pixel on the graph screen.'''
	return f"Pxl-Off({row},{column})"

def PxlOn(row,column):
	'''Turns on a pixel on the graph screen.'''
	return f"Pxl-On({row},{column})"

def pxlTest(Y,X):
	'''Tests a pixel on the graph screen to see if it is on or off.'''
	return f"pxl-Test({Y},{X})"

def randBin(n,p,simulations):
	'''Generates a random number with the binomial distribution.'''
	return f"randBin({n},{p},{simulations})"

def randInt(lower,upper,amount=-1):
    '''randInt(min,max) generates a uniformly-distributed pseudorandom integer between min and max inclusive. randInt(min,max,n) generates a list of n uniformly-distributed pseudorandom integers between min and max.'''
    if amount == -1:
        return f"randInt({lower},{upper})"
    else:
        return f"randInt({lower},{upper},{amount})"

def randM(rows,columns):
	'''Creates a matrix of specified size with the entries random integers from -9 to 9.'''
	return f"randM({rows},{columns})"

def randNorm(mean,sd,amount):
    '''randNorm(µ,σ) generates a normally-distributed pseudorandom number with mean µ and standard deviation σ. The result returned will most probably be within the range µ±3σ. randNorm(µ,σ,n) generates a list of n normally-distributed pseudorandom numbers with mean µ and standard deviation σ.'''
    if amount == -1:
        return f"randInt({mean},{sd})"
    else:
        return f"randInt({mean},{sd},{amount})"

def ref(matrix):
	'''Puts a matrix into row-echelon form.'''
	return f"ref({matrix})"

def Repeat(condition):
    '''A Repeat loop executes a block of commands between the Repeat and End commands until the specified condition is true. The condition is tested at the end of the loop (when the End command is encountered), so the loop will always be executed at least once. This means that you sometimes don't have to declare or initialize the variables in the condition before the loop. After each time the Repeat loop is executed, the condition is checked to see if it is true. If it is true, then the loop is exited and program execution continues after the End command. If the condition is false, the loop is executed again.\n\n NOTE: After you've written all the lines to be contained in the repeat loop, make sure to end the loop with the End() command!'''
    return f"Repeat {remove_spaces(condition)}"

def rowSwap(matrix,row1,row2):
	'''Swaps two rows of a matrix.'''
	return f"rowSwap({matrix},{row1},{row2})"

def rref(matrix):
	'''Puts a matrix into reduced row-echelon form.'''
	return f"rref({matrix})"

def Select(xlistname,ylistname):
	'''Allows the user to select a subinterval of any enabled Scatter or xyLine plots.'''
	return f"Select({xlistname},{ylistname})"

def Send(variable):
	'''Sends data or a variable to a connected CBL device.'''
	return f"Send({variable})"

def setDate(year,month,day):
	'''Sets the date of the clock on the TI-84+/SE.'''
	return f"setDate({year},{month},{day})"

def setDtFmt(value):
	'''Sets the date format of the clock on the TI-84+/SE.'''
	return f"setDtFmt({value})"

def setTime(hour,minute,second):
	'''Sets the time of the clock on the TI-84+/SE.'''
	return f"setTime({hour},{minute},{second})"

def setTmFmt(value):
	'''Sets the time format of the clock on the TI-84+/SE.'''
	return f"setTmFmt({value})"

def ShadeF(lower,upper,numeratordf,denominatordf):
	'''Finds the probability of an interval of the <em>F</em>-distribution, and graphs the distribution with the interval's area shaded.'''
	return f"ShadeF({lower},{upper},{numeratordf},{denominatordf})"

def sin(angle):
	'''Returns the sine of a real number.'''
	return f"sin({angle})"

def sinh(value):
	'''Calculates the hyperbolic sine of a value.'''
	return f"sinh({value})"

def SortA(list):
    '''The SortA( command sorts a list in ascending order. It does not return it, but instead edits the original list variable (so it takes only list variables as arguments).'''
    return f"SortA({list})"

def SortD(list):
    '''The SortD( command sorts a list in descending order. It does not return it, but instead edits the original list variable (so it takes only list variables as arguments).'''
    return f"SortD({list})"

def stdDev(list,frequency_list = None):
    '''The stdDev( command finds the sample standard deviation of a list, a measure of the spread of a distribution. It takes a list of real numbers as a parameter.'''
    if(frequency_list is None):
        return f"stdDev({list})"
    else:
        return f"stdDev({list},{frequency_list})"

def Stop():
    '''Returns a *Stop* statement'''
    return "Stop"

def sub(string,start,length):
	'''Returns a specific part of a given string, or divides by 100.'''
	return f"sub({string},{start},{length})"

def tan(angle):
	'''Returns the tangent of a real number.'''
	return f"tan({angle})"

def Tangent(expression,value):
	'''Draws a line tangent to an expression at the specified value.'''
	return f"Tangent({expression},{value})"

def tanh(value):
	'''Calculates the hyperbolic tangent of a value.'''
	return f"tanh({value})"

def tcdf(lower,upper,ν):
	'''Calculates the Student's t probability betwen lower and upper for degrees of freedom ν.'''
	return f"tcdf({lower},{upper},{ν})"

def timeCnv(value):
	'''Converts seconds into the equivalent days, hours, minutes, and seconds.'''
	return f"timeCnv({value})"

def toString(input):
    '''The toString( command, given any value including real numbers, complex numbers, lists, or matrices, returns the string representation of the value of the input.'''
    return f"toString({input})"

def tpdf(t,ν):
	'''Evaluates the Student's t probability density function with degrees of freedom ν.'''
	return f"tpdf({t},{ν})"

def variable_set(variable, expression):
    '''An alternative to typing out a variable's value\n
    Instead of x = 4, you could type pythonbasic.variable_set(x, 4)'''
    translated_line = translate_line(expression)
    #print("translation of " + str(expression) + " is " + str(translated_line))
    if(translated_line == ""):
        return str(expression) + "→" + str(variable)
    else:
        return str(translated_line) + "→" + str(variable)