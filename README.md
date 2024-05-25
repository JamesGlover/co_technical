# co_technical

## Prerequisites

- Python 3.12
- [PDM](https://pdm-project.org/en/stable/) (Optional)

  Windows Powershell:

  ```powershell
  (Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | py -
  ```

  Linux/Mac/WSL:

  ```sh
  curl -sSL https://pdm-project.org/install-pdm.py | python3 -
  ```

## Installation

- Clone the git repo
  
  ```sh
  git clone git@github.com:JamesGlover/co_technical.git
  ```

### Installing dependencies

This application has no additional runtime dependencies. However, there are development
dependencies for testing and linting.

### With PDM

- `pdm install`

### Without PDM (Using Pip)

- `python -m venv .venv`
- `.venv/bin/activate` or `PS .venv\Scripts\Activate.ps1`
- `pip install -r requirements.txt`
