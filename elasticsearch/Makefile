default: run
run: export HOSTNAME=$(shell hostname)
run:	
	docker-compose up -d
build:
	docker-compose build
down:
	docker-compose down
rm:	
	docker images | grep docker-logs | awk '{print $1 ":" $2}' | xargs docker rmi
clean: down rm
restart: clean run