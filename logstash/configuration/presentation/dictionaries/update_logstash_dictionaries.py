import requests
import json

__doc__ = 'Requests the code translations for format codes, jus-classifications, iso-language codes and library ' \
          'union codes from vuFind github and library and region codes from libadmin and creates yaml files from them.'


def update_format_codes():
    file = requests.get('https://raw.githubusercontent.com/swissbib/vufind/master/local/languages/formats/de.ini')

    result = list()
    text = file.text.split("\n")
    for line in text:
        if line.startswith(';') or line == '':
            pass
        else:
            temp = line.split('=')
            code = temp[0].strip()
            value = temp[1].strip(' ')
            result.append([code, value])

    with open('swissbib_format_codes.yml', 'w', encoding='utf-8') as file:
        for item in result:
            file.write(' "' + item[0] + '": ' + item[1] + '\n')


def update_jus_classifcation_codes():
    file = requests.get('https://raw.githubusercontent.com/swissbib/vufind/master/local/languages/drsys/de.ini')

    result = list()
    text = file.text.split("\n")
    for line in text:
        if line.startswith(';') or line == '':
            pass
        else:
            temp = line.split('=')
            code = temp[0].strip()
            value = temp[1].strip(' ')
            result.append([code, value])

    with open('jus_classifications.yml', 'w', encoding='utf-8') as file:
        for item in result:
            file.write(' "' + item[0] + '": ' + item[1] + '\n')


def update_library_network_codes():
    file = requests.get('https://raw.githubusercontent.com/swissbib/vufind/master/local/languages/union/de.ini')

    result = list()
    text = file.text.split("\n")
    for line in text:
        if line.startswith(';') or line == '':
            pass
        else:
            temp = line.split('=')
            code = temp[0].strip()
            value = temp[1].strip(' ')
            result.append([code, value])

    with open('union_translations.yml', 'w', encoding='utf-8') as file:
        for item in result:
            file.write(' "' + item[0] + '": ' + item[1] + '\n')


def update_language_codes():
    file = requests.get('https://raw.githubusercontent.com/swissbib/vufind/master/local/languages/languagecodes/de.ini')

    result = list()
    text = file.text.split("\n")
    for line in text:
        if line.startswith(';') or line == '':
            pass
        else:
            temp = line.split('=')
            code = temp[0].strip()
            value = temp[1].strip(' ')
            result.append([code, value])

    with open('iso_639_2_language_codes.yml', 'w', encoding='utf-8') as file:
        for item in result:
            file.write(' "' + item[0] + '": ' + item[1] + '\n')


def update_libadmin_library_codes():
    libs = json.loads(requests.get('https://www.swissbib.ch/mapportal.json').text)

    lib_list = list()
    for item in libs['data']:
        temp = list()
        temp.append(item['group']['code'])
        temp.append(item['group']['label']['de'])
        lib_list.append(temp)
        for institutionen in item['institutions']:
            temp = list()
            temp.append(institutionen['bib_code'])
            temp.append(institutionen['label']['de'])
            lib_list.append(temp)

    with open('swissbib_libraries.yml', 'w', encoding='utf-8') as file:
        for item in lib_list:
            file.write(' "' + item[0] + '": "' + item[1] + '"\n')


if __name__ == '__main__':
    update_format_codes()
    update_jus_classifcation_codes()
    update_language_codes()
    update_libadmin_library_codes()
    update_library_network_codes()
