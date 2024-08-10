import re


class FilePathUtilities:

    @classmethod
    def extract_file_extension(cls, path: str) -> str:
        pattern = r"\.([a-zA-Z0-9]+)$"
        match = re.search(pattern, path)
        if match:
            file_extension = match.group(1)
            return file_extension