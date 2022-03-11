<div align=center>

# EasyBot.py

![more alt text](./assets/logo.png)

A simple, no fuss Discord bot that can be deployed without any code

<div align=left>

## Installation

### Windows 

1. Install [Python 3.10](https://www.python.org/)
2. Install [Git](https://git-scm.com/)
3. Clone the EasyBot.py Repo 

```sh
git clone https://github.com/Isaac-To/EasyBot.py.git
```

or alternatively, download the latest release of EasyBot.py and unzip it.
4. Install the dependencies by running this cmd: 

```sh
cd installers && pip install -r requirements.txt
```

or use Poetry to install the dependencies:

```sh
cd EasyBot.py && poetry env use 3.10
poetry install
```

5. If using Pip, run the `eb_control.py` file to start the bot. If using Poetry, open up a shell (`poetry shell`) and run `eb_control.py`.

### Linux 

1. Install or compile Python 3.10. If you are compiling from source, and using Debian/Ubuntu, make sure that have these installed:

```sh
sudo apt-get update && sudo apt-get upgrade 
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
       libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
       libncurses5-dev libncursesw5-dev xz-utils tk-dev lzma liblzma-dev libffi-dev python3.10-dev
```

2. Install Git

3. Clone the EasyBot.py Repo 

```sh
git clone https://github.com/Isaac-To/EasyBot.py.git
```

or alternatively, download the latest release of EasyBot.py and unzip it.
4. Install the dependencies by running this cmd: 

```sh
cd installers && pip install -r requirements.txt
```

or use Poetry to install the dependencies:

```sh
cd EasyBot.py && poetry env use 3.10
poetry install
```

5. If using Pip, run the `eb_control.py` file to start the bot. If using Poetry, open up a shell (`poetry shell`) and run `eb_control.py`.