FROM python:3.10.4-buster AS builder
RUN apt-get update && apt-get install -y --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

FROM builder AS builder-venv

COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install -r /requirements.txt

FROM builder-venv AS tester

COPY . /app
WORKDIR /app
RUN /venv/bin/pytest

FROM python:3.10.4-buster AS runner
COPY --from=tester /venv /venv
COPY --from=tester /app /app

WORKDIR /app

ENTRYPOINT ["/venv/bin/python3", "-m", "woolyherdz"]
USER 1001

LABEL name={NAME}
LABEL version={VERSION}
