REGISTRY=docker.pkg.github.com/alewkinr/lyra

build:
	docker build . -t ${REGISTRY}/runner
	docker tag ${REGISTRY}/runner ${REGISTRY}/runner && docker push ${REGISTRY}/runner