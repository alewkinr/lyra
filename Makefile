SERVICE_NAME?=service

start:
	docker-compose --env-file ./.env up -d
dev:
	docker-compose --env-file ./.env up --build
generate:
	grep -r -l '{{SERVICE_NAME}}' . | grep -v "Makefile" | xargs sed -i -e 's/{{SERVICE_NAME}}/$(SERVICE_NAME)/g'
	find . -name '*.*-e' -exec rm {} +
freeze:
	pip freeze > requirements.txt
require:
	pip install -r requirements.txt