
build-python-push-docker:
	docker buildx build -f ./Dockerfile -t forzalino/python:dev --push . --platform linux/amd64,linux/arm64 --no-cache

hey:
	hey -c 100 -z 10s -m GET goxo.cc/api/v1
	# -n num requests
	# -c num concurrent requests
	# -z duration of test
	# -m http method
	# -q rate limit per second per worker
	# -t timeout per request