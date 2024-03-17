
from pymongo.mongo_client import MongoClient
from pprint import pprint
connectURL = 'mongodb+srv://fbmazetti:12345@cluster-db.blzhilc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-DB' #URL de conexão

client = MongoClient(connectURL)

meubanco = client['db_teste']
colecao = meubanco['collection-teste']
document0 = {"type":"trabalho de sistemas de tempo real", "status": "feito"} #documento qualquer
document1 = {"type":"outro trabalho", "status": "em progresso"} #documento qualquer

#insert_document = colecao.insert_one(document1) #comando para inserir um documento
#print(f"Documento inserido com sucesso e seu ID é: {insert_document.inserted_id}")

buscar_primeiro_item = colecao.find_one()
print(buscar_primeiro_item)

buscar_um_item_com_parametro = colecao.find_one({'status': 'em progresso'}) # passando parametros de busca
print(buscar_um_item_com_parametro)

#coleção exemplo do atlas mongoDB
# mydatabase = client['sample_mflix']
# collection = mydatabase['users']

# for doc in collection.find():
#     pprint(doc)
   
client.close()




