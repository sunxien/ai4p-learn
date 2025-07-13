import os


def validate_filetype(filetype: str):
    if filetype != "pdf" and filetype != "txt":
        raise RuntimeError(f"filetype: {filetype} is unsupported")
    return filetype


def validate_filepath(filepath: str):
    if not filepath or filepath.strip() == "":
        raise RuntimeError(f"filetype: {filepath} is invalid")
    if not os.path.exists(filepath):
        raise RuntimeError(f"filetype: {filepath} is not exists")
    return filepath


class KnowledgeFile:

    filetype: str
    filepath: str

    def __init__(self, filetype: str, filepath: str):
        self.filetype = validate_filetype(filetype)
        self.filepath = validate_filepath(filepath)


