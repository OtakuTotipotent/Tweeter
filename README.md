# Tweeter

Talk with other people to your heart's content! Mixing blogging &amp; social interconnections.

## Easy Setup

- Install [Python](https://www.python.org/downloads/) in your system
- Clone [Tweeter Project](https://github.com/OtakuTotipotent/Tweeter) from GitHub on your system

```bash
git clone https://github.com/OtakuTotipotent/Tweeter.git
```

- Create & activate Python Virtual Environment

```bash
# create virtual env
python -m venv .venv
# activate virtual env
.venv/script/activate
```

- Create Database migrations

```bash
python manage.py migrate
```

- Run the project

```bash
python manage.py runserver
```

- Copy/Paste or Ctrl/Click the localhost address into browser window

## Tech Stack

- Django
- HTML
- SQLite
