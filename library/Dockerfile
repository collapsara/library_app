FROM python:3.9.1

WORKDIR /home/library_app/

RUN pip install --upgrade pip
COPY library_app/requirements.txt /home/library_app/requirements.txt
RUN pip install -r requirements.txt

COPY library_app/ /home/library_app/