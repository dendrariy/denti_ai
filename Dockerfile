FROM joyzoursky/python-chromedriver:3.8-alpine-selenium

#install python dependencies
COPY requirements.txt .
RUN pip install -r ./requirements.txt

#set workspace
WORKDIR /app

#copy local files
COPY . .

CMD python -m pytest tests