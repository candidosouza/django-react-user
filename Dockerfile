FROM python:3.11

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1

RUN apt update && apt install -y --no-install-recommends curl wget libgtk-3-0 gettext
RUN  python -m pip install --upgrade pip

RUN useradd -ms /bin/bash python

RUN pip install poetry

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app
ENV PATH="$PATH:$PYTHONPATH/.venv/bin"


CMD ["tail", "-f", "/dev/null"]