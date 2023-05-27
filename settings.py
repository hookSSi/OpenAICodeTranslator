import inquirer

# App Settings
INPUT_FOLDER = "INPUT_FOLDER"
OUTPUT_FOLDER = "OUTPUT_FOLDER"

ChatGPTAPIkey = "WRITE API KEY HERE"

questions = [
    inquirer.List('model', message="'What\'s your model to use?'", choices=['gpt-3.5-turbo']),
    inquirer.List('source_language', message="What languages do you want to translate? (Source Language)",
                  choices=['TypeScript']),
    inquirer.List('target_language', message="What languages do you want to translate to? (Target Language)",
                  choices=['C#']),
]
