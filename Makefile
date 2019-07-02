default: run
run:
	export HOSTNAME=$(shell hostname)
	docker-compose up -d
build:
	docker-compose -f docker-compose-build.yml build
down:
	docker-compose down
delete:
	docker rmi $(docker images | grep docker-logs | tr -s ' ' | cut -d ' ' -f 3)
clean: down delete
restart: clean run