default: run
run:
	export HOSTNAME=$(shell hostname)
	docker-compose up -d
build:
	docker-compose -f docker-compose-build.yml build
down:
	docker-compose down
delete:
	docker rmi fadhlanhazmi/filebeat:1.0.0
clean: down delete
restart: clean run