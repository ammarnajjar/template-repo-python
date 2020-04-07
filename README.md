# \$title

## [![CI](https://github.com/ammarnajjar/$name/workflows/ci/badge.svg)](https://github.com/ammarnajjar/$name/actions)

## Usage:

- Clone under your project name directory:

```bash
git clone https://github.com/ammarnajjar/template-repo-python.git <Project Name>
```

- Change the template to suite the new project name by running:

```bash
python init.py
```

    result:
     - The year in LICENSE will be set to the current year
     - Readme template will be changed to use the new <Project Name> in the title and the ci badge.
     - The lib directory will be changed to match the new <Project Name>

- This template repo supports [direnv](https://github.com/direnv/direnv), see [installation instruction](https://github.com/direnv/direnv/blob/master/docs/installation.md) and [activation instruction](https://github.com/direnv/direnv/blob/master/docs/hook.md) for more details on how to set it up.

- Change the git origin to match your own:

```bash
git remote set-url origin <Your Origin URL>
```

Alternatively, delete `.git` directory and re-initialize a new git repository using `git init`.

- Install [pre-commit](https://github.com/pre-commit/pre-commit) hooks.

```bash
python -m pip install pre-commit
pre-commit install
```

That's it, happy coding! 😄
