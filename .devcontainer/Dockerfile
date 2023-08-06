FROM python:3.11.4-bullseye

# Install ubuntu packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
  tzdata \
  build-essential \
  git \
  ssh


# Install python packages
COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN adduser sclick