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

## Usage

### With pdm

- `pdm co_technical` To use STDIN
- `pdm co_technical [filename]`

### Without pdm

- `python co_technical`

## Testing

Tests can be run with `pdm test`

## Limitations and considerations

### Invalid commands

Completely invalid commands are undefined behaviour in the specification. However,
consistent with the requirements that establish that other invalid inputs should be
ignored I have ignored invalid inputs.

If additional arguments are provided to MOVE, LEFT, RIGHT or REPORT the commands are
ignored.

While this best aligns with the requested specification, I believe it would
be advantageous to log invalid input - possibly including moves that would send the
robot off the table - to standard error.

### CI and Dockerfiles

I've considered these out of scope for this exercise. I'm happy to discuss the
advantages and my experience of these tools during the interview.
