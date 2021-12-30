# DB Services

<!-- Connect to Db -->

docker-compose -f local.yml exec postgres bash
psql -U debug hackernews

## Django Services

<!-- Django Shell -->

docker-compose -f local.yml exec django python3 manage.py shell

## Docker Services
<!-- Remove All Containers -->
docker rm -f $(docker ps -a -q)

<!-- Remove all Volume -->
docker volume rm $(docker volume ls -q)

## Docker Compose Services
<!-- Redis CLI -->
docker-compose -f local.yml exec redis redis-cli
