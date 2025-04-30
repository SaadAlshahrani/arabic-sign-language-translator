FROM python:3.10.6-buster

WORKDIR /prod

COPY requirements_prod.txt requirements_prod.txt

RUN pip install --no-cache-dir -r requirements_prod.txt
RUN apt install ffmpeg

COPY arabic_sign_language_translator arabic_sign_language_translator

CMD streamlit run arabic_sign_language_translator/Home.py --server.port $PORT
