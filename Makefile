default: run
run:
	export HOSTNAME=$(shell hostname)
	docker-compose up -d
build:
	docker-compose -f docker-compose-build.yml build
down:
	docker-compose down
rm:
	docker rmi fadhlanhazmi/filebeat:1.0.0
clean: down rm
restart: clean run