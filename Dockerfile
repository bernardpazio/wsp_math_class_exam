FROM python:3
ENV PYTHONUNBUFFERED=1

ADD requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt
WORKDIR /app

CMD /bin/bash while true do; python3 manage.py runserver 0.0.0.0:8000; done