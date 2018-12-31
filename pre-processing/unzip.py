import zipfile

def extract(in_zip, out_path):
    """
    :param in_zip: file path of zip to extract
    :param out_path: dir path of extracted output
    """
    with zipfile.ZipFile(in_zip, 'r') as file:
        file.extractall(out_path)