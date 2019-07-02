default: run
run: export HOSTNAME=$(shell hostname)
run:	
	docker-compose up -d
build:
	docker-compose build
down:
	docker-compose down
rm:	
	docker image prune -f
clean: down rm
restart: clean run