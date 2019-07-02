default: run
run:
	export HOSTNAME=${HOSTNAME}
	docker-compose up -d
build:
	docker-compose -f docker-compose-build.yml build
stop:
	docker-compose down
delete:
	docker rmi $(docker images | grep docker-elk | tr -s ' ' | cut -d ' ' -f 3)
clean: stop delete
restart: clean run