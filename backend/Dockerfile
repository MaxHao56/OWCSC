FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


WORKDIR /OWCSC
COPY . .

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN chmod +x /OWCSC/entrypoint.sh

EXPOSE 8000

CMD ["sh", "/OWCSC/entrypoint.sh"]