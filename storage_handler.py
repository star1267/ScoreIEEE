import json


def write_json(path, content):
    """This creates a json file and write the dict to that file."""
    #
    with open(path, "w") as output:
        json.dump(content, output, indent=2)

    ...
