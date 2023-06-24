FROM python:3.11.3-slim-bullseye
COPY . /pujl-bot
WORKDIR /pujl-bot
RUN pip install -r requirements.txt
ENTRYPOINT [ "python","/pujl-bot/bot.py" ]
