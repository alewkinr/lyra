REGISTRY=docker.pkg.github.com/alewkinr/lyra

build:
	docker build . -t ${REGISTRY}/auth
	docker tag ${REGISTRY}/auth ${REGISTRY}/auth && docker push ${REGISTRY}/auth