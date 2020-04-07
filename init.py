import os
import subprocess
from datetime import datetime
from string import Template
from typing import Dict


def get_repo_root() -> str:
    return subprocess.Popen(
        ['git', 'rev-parse', '--show-toplevel'],
        stdout=subprocess.PIPE,
    ).communicate()[0].rstrip().decode('utf-8')


def replace_content(
    root: str,
    filename: str,
    template_dict: Dict[str, str],
) -> None:
    with open(os.path.join(root, filename), 'r+') as f:
        content = f.read().replace('\\', '').split('---')[0]
        updated_content = Template(content).safe_substitute(repo_info)
        f.seek(0)
        f.truncate()
        f.write(updated_content)


if __name__ == "__main__":
    root = get_repo_root()
    name = os.path.basename(root)
    module_name = name.replace('-', '_')
    title = module_name.replace('_', ' ').capitalize()
    repo_info = {
        'year': str(datetime.now().year),
        'name': name,
        'title': title,
    }
    files = ['README.md', 'LICENSE']
    for filename in files:
        replace_content(root, filename, repo_info)
    os.rename(
        os.path.join(root, 'src'),
        os.path.join(root, module_name),
    )
