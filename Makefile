all:
	docker compose up -d && chmod +x execute_dockers.sh && ./execute_dockers.sh && clear && echo "Done!"

clean:
	docker compose stop
	docker compose rm -f
	docker rmi -f tarea3-hadoop