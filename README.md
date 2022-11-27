# Hadoop-searchEng

Para importar el archivo JSON a la database de MongoDB, se debe ejecutar el siguiente comando:
```bash
mongoimport -u root -p rootpassword --db data --collection words --file db.json --authenticationDatabase admin --port 27017
```