FROM python:3.6
MAINTAINER Nar Kumar Chhantyal "nkchhantyal@gmail.com"
COPY . /app
WORKDIR /app
RUN apt update && apt install python-dev -y
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
CMD ["app:app"]
