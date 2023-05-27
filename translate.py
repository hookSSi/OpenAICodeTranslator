#!/usr/bin/env python3

# This code uses OpenAI Codex to translate between computer languages.
# Adjust your settings in settings.py
# Drop code in the input folder and translated versions will be created in the output folder

import utils
import storagehelper as sh
from settings import *
import inquirer
import os
import progressbar


class Main:
    def __init__(self) -> None:
        pass

    def run(self):
        print("Files to Process")

        answers = inquirer.prompt(questions)

        outputstorage = sh.Storage(OUTPUT_FOLDER)
        inputstorage = sh.Storage(INPUT_FOLDER)

        files = inputstorage.list_files(answers['source_language'])
        files = list(files)
        
        bar = progressbar.ProgressBar(maxval=len(files)).start()
        for i, file in enumerate(files, start=0):
            # To continue from where you stopped
            if os.path.exists(file.replace(INPUT_FOLDER, OUTPUT_FOLDER)):
                continue
                
            bar.update(i)
            if os.path.isfile(file):
                content = inputstorage.read_file(file)

                # use ChatGPT to convert te file
                translator = utils.CodeTranslator(ChatGPTAPIkey, answers['model'])

                translated_code = translator.translate_code(content, answers['source_language'], answers['target_language'])
                translated_file = outputstorage.change_file_extension(file, answers['target_language'])

                # write to the output folder
                translated_file = translated_file.replace(INPUT_FOLDER, OUTPUT_FOLDER)
                outputstorage.write_file(translated_file, translated_code)
        bar.finish()


if __name__ == '__main__':
    w = Main()
    w.run()
