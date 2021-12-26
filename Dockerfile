# INFO:
# To run shell commands use:
# import os; os.system('cd /opt && ls -l')

# To MANIPULATE outputs from shell into Python, use:
# import os; stream = os.popen('echo Returned output'); output = stream.read(); output

FROM python:latest

ENV TRUE_PERF_APP_DIR=/opt/app/
ENV TRUE_PERF_LOG_DIR=/opt/logs/

WORKDIR /opt/true_performance/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app/main.py" ]

