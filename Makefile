
build:
	sudo docker build -t llama .
run:
	sudo docker run --gpus all --name llama_api -p 8001:8001 llama --max_seq_len 1000 --max_gen_len 1000 --temperature 0.5
rm-cache:
	find . -name "*.pyc" -delete