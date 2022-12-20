up:
	docker-compose up --build -d

prod-up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d

stop:
	docker-compose stop

down:
	docker-compose down

delete:
	docker-compose down -v

db:
	docker exec -it postgres-database psql -d bubble -U example