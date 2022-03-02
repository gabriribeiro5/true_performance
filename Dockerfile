# INFO:
# To run shell commands use:
# import os; os.system('cd /opt/app && ls -l')

# To MANIPULATE outputs from shell into Python, use:
# import os; stream = os.popen('echo Returned output'); output = stream.read(); output

# First run:
#     sudo docker build .
#     sudo docker run <image id>

# Access container interactive mode
#     sudo docker container start -i <container id>

FROM python:latest

ENV TRUE_PERF_APP_DIR=/opt/true_performance/app
ENV TRUE_PERF_LOG_DIR=/opt/logs/

WORKDIR /opt/logs/
WORKDIR /opt/true_performance/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN [ "/bin/bash" ]

CMD [ "python", "app/main.py" ]

