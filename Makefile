DOCKER_REGISTRY="docker.pkg.github.com/alewkinr/lyra/"

freeze:
	pip freeze > requirements.txt

require:
	pip install -r requirements.txt

generate:
	cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql