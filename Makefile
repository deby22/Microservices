start:
	docker-compose up --build

seed:
	docker exec -it articles python seed.py && \
	docker exec -it notification python seed.py
