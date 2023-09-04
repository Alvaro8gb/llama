
build:
	sudo docker build -t llama .
run:
	sudo docker run --name llama_api -p 8008:8000 llama
rm-cache:
	find . -name "*.pyc" -delete