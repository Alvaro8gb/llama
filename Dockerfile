FROM python:3.10

WORKDIR /llama
ADD . /llama

RUN pip install -r /llama/requirements.txt 

EXPOSE 8001
ENTRYPOINT ["torchrun", "--nproc_per_node", "1", "api.py"]