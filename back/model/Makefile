REGISTRY=docker.pkg.github.com/alewkinr/lyra

build:
	docker build . -t ${REGISTRY}/model
	docker tag ${REGISTRY}/model ${REGISTRY}/model && docker push ${REGISTRY}/model