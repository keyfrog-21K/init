# generate_gitignore.py
# Generate .gitignore file for Project.
# Using https://www.toptal.com/developers/gitignore

import requests

def generate(path: str, args: list):
    """
    Generate .gitignore file using toptal.com's gitignore.io
    
    :param path: Path for file (Example: './MyProject/.gitignore')
    :type path: str
    :param args: Arguments (Example: ['python', 'macos'])
    :type args: list
    """
    
    target_url = 'https://www.toptal.com/developers/gitignore/api/' # Example: https://www.toptal.com/developers/gitignore/api/macos,python
    
    for i in range(len(args)):
        target_url += args[i]
        if not i == len(args):
            target_url += ','
    
    response = requests.get(target_url)
    with open(path, 'w') as f:
        f.write(response.text)

