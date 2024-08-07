import json

def read_json(filePath: str) -> dict:
    """
    # func > read_json

    Returns the contents of the json file given as a dict

    :param filePath: str
    :return: dict
    """

    with open(filePath, 'r') as f: return json.load(f)

def write_json(filePath: str, data: dict, indent: int = 4) -> None:
    """
    # func > read_json

    Returns the contents of the json file given as a dict

    :param filePath: str
    :param data: dict
    :param indent: int = 4
    :return: None
    """

    with open(filePath, 'w') as f: json.dump(data, f, indent=indent)

