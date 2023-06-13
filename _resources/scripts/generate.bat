@echo off
docker build -t protos .
docker run --name="protos_run" protos
docker cp protos_run:proto/proto-device-utils/device_utils.py ./deviceutils/device_utils.py
docker rm protos_run
docker rmi protos
echo "BAT done"