# use the latest image of python
FROM python:3.10
# install dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev python3-dev
# set the working directory to /app
WORKDIR /app
# copy the current directory contents into the container at /app
ADD . /app
# install the requirements
RUN pip install -r requirements.txt
# expose port 5000
EXPOSE 5000
# run flask
CMD ["flask", "run"]