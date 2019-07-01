docker-compose down
docker rmi $(docker images | grep docker-logs | tr -s ' ' | cut -d ' ' -f 3)
docker-compose up -d
docker logs dockerlogselk_filebeat_1 --follow