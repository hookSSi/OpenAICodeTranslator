import os
import glob
import errno

extensions = {
    'C#': 'cs',
    'TypeScript': 'ts'
}


class Storage:
    def __init__(self, folder_path):
        self.root_folder = os.path.dirname(os.path.abspath(__file__))
        self.folder_path = os.path.join(self.root_folder, folder_path)

    def list_files(self, source_language):
        source_file_extension = extensions[source_language]
        return glob.iglob(f'{self.folder_path}\\**\\*.{source_file_extension}', recursive=True)

    def read_file(self, filename):
        if os.path.isfile(os.path.join(self.folder_path, filename)):
            with open(os.path.join(self.folder_path, filename), 'r', encoding="utf-8") as file:
                return file.read()

    def write_file(self, filename, content):
        self.mkdir_p(os.path.dirname(filename))
        with open(os.path.join(self.folder_path, filename), 'w', encoding="utf-8") as file:
            file.write(content)

    # Taken from https://stackoverflow.com/a/600612/119527
    def mkdir_p(self, path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def get_file_name(self, filename):
        return os.path.basename(filename)

    def change_file_extension(self, file, target_language):
        file_name, file_ext = os.path.splitext(file)

        # new file name and extension
        new_file_extension = extensions[target_language]
        new_file_name = f"{file_name}.{new_file_extension}"

        # join the new file name and extension
        return os.path.join(self.folder_path, new_file_name)
