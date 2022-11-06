# Run app into your local.

This repository contains my learning about scraping with python

### Installation.

Clone this repository into your local machine.

```
git clone https://github.com/fwwz-id/scrape-with-python.git
```

Create python virtual environment by typing this into your terminal.

```
python -m venv .venv
```

Then run your python virtual environment. The detailed explanation is [here](https://docs.python.org/3/library/venv.html "documentation of venv").

```
source .venv/bin/activate
```

Install required libraries using pip

```
pip install -r requirements.txt
```

### Usage

To type check your _program.py_ use **mypy.**

```
mypy src/scraper.py
```

To run this project, use this command

```
python src/scraper.py
```
