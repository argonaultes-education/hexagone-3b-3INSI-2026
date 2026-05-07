FROM python:latest

WORKDIR /opt/app

COPY test_summary.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python" , "test_summary.py" ]