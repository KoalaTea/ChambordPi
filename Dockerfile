FROM python:3.7
RUN mkdir /app
COPY run.py /app
COPY requirements.txt /app
RUN pip install /app/requirements.txt
COPY chambordpi/ /app
WORKDIR /app
ENTRYPOINT [ "python", "-u", "run.py" ]