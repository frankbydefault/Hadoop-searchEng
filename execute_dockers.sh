#!/bin/bash
echo "Executing entrypoint script"
sleep 10
docker exec -it hadoop hdfs dfs -mkdir /user
docker exec -it hadoop hdfs dfs -mkdir /user/hduser
docker exec -it hadoop hdfs dfs -mkdir input
docker exec -it hadoop bash -c "hdfs dfs -put /home/hduser/wiki/carpeta1/* input/"
docker exec -it hadoop bash -c "hdfs dfs -put /home/hduser/wiki/carpeta2/* input/"
docker exec -it hadoop bash -c "sudo chmod 777 wiki"
docker exec -it hadoop bash -c "sudo chmod 777 wiki/*"
docker exec -it hadoop mapred streaming -files wiki/mapper.py,wiki/reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./wiki/mapper.py -reducer ./wiki/reducer.py
docker exec -it hadoop hdfs dfs -copyToLocal /user/hduser/output/part-00000 ./output.txt
docker exec -it hadoop mv wiki/txtToJson.py .
docker exec -it hadoop python txtToJson.py
docker cp hadoop:/home/hduser/db.json ./
docker cp ./db.json mongo:/
docker exec -it mongo mongoimport -u root -p rootpassword --db data --collection words --file db.json --authenticationDatabase admin --port 27017
