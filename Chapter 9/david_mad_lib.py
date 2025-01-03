import re

def mad_libs(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    pattern_adjective = re.compile(r'ADJECTIVE')
    pattern_noun = re.compile(r'NOUN')
    pattern_adverb = re.compile(r'ADVERB')
    pattern_verb = re.compile(r'VERB')

    text = pattern_adjective.sub(input('Enter an adjective: \n'), text)
    text = pattern_noun.sub(input('Enter a noun: \n'), text)
    text = pattern_verb.sub(input('Enter a verb: \n'), text)
    text = pattern_noun.sub(input('Enter a noun: \n'), text)

    print(text)

    with open('mad_libs_result.txt', 'w') as file:
        file.write(text)

def user_file_location():
    file_path = input('Enter the file path containing the Mad Libs text: \n')
    mad_libs(file_path)

user_file_location()

