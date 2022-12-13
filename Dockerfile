FROM joyzoursky/python-chromedriver:3.8-alpine-selenium

#install python dependencies
COPY requirements.txt .
RUN pip install -r ./requirements.txt

#set workspace
WORKDIR /app

#copy local files
COPY . .

#create reports dir
RUN mkdir ./reports

#run tests
CMD python -m pytest tests --excelreport=/app/reports/report.xls
