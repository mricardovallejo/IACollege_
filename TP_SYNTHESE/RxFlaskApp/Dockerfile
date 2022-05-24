FROM python:3.8

WORKDIR /rxFlaskApp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN dir
CMD ["python", "appRx.py"]
#RUN useradd -ms /bin/bash user
#USER user
#RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
#RUN .venv/bin/pip install --no-cache-dir -r requirements.txt
