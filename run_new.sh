docker-compose down -v
docker stop status-api handshake-api counter-api hardwareinfo-api database
docker rm status-api handshake-api counter-api hardwareinfo-api database
docker-compose up --build
