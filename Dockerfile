FROM python:latest
ADD . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3 bot_telegram.py
