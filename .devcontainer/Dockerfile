FROM python:3.13.2-bookworm

# Install ubuntu packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
  git \
  ssh \
  curl \
  sudo


# Install python packages
# COPY .devcontainer/requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt

# Install Poetry
ENV POETRY_VERSION=1.8.3
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3.13 -
ENV PATH="/opt/poetry/bin:${PATH}"

RUN adduser sclick