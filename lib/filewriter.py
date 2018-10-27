import os
import sys
import json

def create_directory(directory_name):
    try:
        cwd = os.getcwd()
        path_for_file = os.path.join(cwd, directory_name)

        if not os.path.exists(path_for_file):
            os.makedirs(path_for_file)
    except OSError:
        print('Error creating path: {}'.format(directory_name))

def write_to_file(result_dict):
    text = json.dumps(result_dict)
    create_directory("scrapes")
    content_file = './scrapes/webscrape.txt'
    print('Writing result to {}'.format(content_file))
    try:
        with open(content_file, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print("Error downloading file; ", e)
        sys.exit(1)
    print("Result written to file.")        