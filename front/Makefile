REGISTRY=docker.pkg.github.com/alewkinr/lyra

build:
	docker build . -t ${REGISTRY}/ui
	docker tag ${REGISTRY}/ui ${REGISTRY}/ui && docker push ${REGISTRY}/ui