FROM python:3.10-slim-bookworm

RUN apt update && apt upgrade -y
RUN apt install -y git curl python3-pip ffmpeg wget bash neofetch software-properties-common

COPY requirements.txt .
RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

WORKDIR /app
COPY . .

CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
# Or use this if using gunicorn:
# CMD gunicorn app:app & python3 -m devgagan
