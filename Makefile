start:
	docker-compose up --build

seed:
	docker exec -it notification python seed.py && \
	docker exec -it articles python seed.py

listen:
	docker exec -it notification python consumer.py