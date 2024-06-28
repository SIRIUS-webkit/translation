# Translation Web

Tailwind Css was also used.

## Installation

```bash
pip install -r requirements.txt
```

To run tailwind, need to download [node.js](https://nodejs.org/en) first, after that changed the npm dir under setting.py file. To check npm path run

```python
where npm
```

and copy the value and changed under setting.py

```python
NPM_BIN_PATH = "...."
```

## Usage

To run,

```python
py manage.py runserver
```

To run tailwind,

```python
py manage.py tailwind start
```
