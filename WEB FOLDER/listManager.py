import mysqlManager
import psqlManager
import product
import cotizacion
import cliente
import user
class listManager:
	def getProducts(self):
		dbMysql = mysqlManager.mysqlManager()
		productList = dbMysql.getProducts()
		objList = list()
		for x in productList:
			objList.append(product.product(x[0],x[1],x[2],x[3]))
		del dbMysql
		return objList

	def getDetails(self,id):
		dbMysql = mysqlManager.mysqlManager()
		details = dbMysql.getDetails(id)
		dic = dict()
		for x in details:
			dic[x[0]]=x[1]
		return dic

	def getDetailsId(self,id):
		dbMysql = mysqlManager.mysqlManager()
		details = dbMysql.getDetailsId(id)
		detailsList = list()
		for x in details:
			nestList = list()
			nestList.append(x[0])
			nestList.append(x[1])
			nestList.append(x[2])
			detailsList.append(nestList)
		return detailsList

	def getProductId(self,id):
		dbMysql = mysqlManager.mysqlManager()
		result = dbMysql.getProduct(id)
		productObj = product.product(result[0],result[1],result[2],result[3])
		return productObj

	def getCotiz(self):
		dbPsql= psqlManager.psqlManager()
		dbMysql = mysqlManager.mysqlManager()
		cotizList = dbPsql.getCots()
		objList = list()
		for x in cotizList:
			prod = dbMysql.getProduct(x[2])
			productObj = product.product(prod[0],prod[1],prod[2],prod[3])
			client = dbPsql.getClienteId(x[1])
			clienteObj = cliente.cliente(client[0],client[1],client[2],client[3],client[4])
			objList.append(cotizacion.cotizacion(x[0],clienteObj,productObj,x[3],x[4],x[5],x[6],x[7],x[8]))
		return objList

	def getClients(self):
		dbPsql = psqlManager.psqlManager()
		clientList=dbPsql.getClientes()
		objList = list()
		for x in clientList:
			objList.append(cliente.cliente(x[0],x[1],x[2],x[3],x[4]))
		return objList

	def createClient(self,name,rfc,type):
		dbPsql = psqlManager.psqlManager()
		dbPsql.createClient(name,rfc,type)
		return

	def createCotizacion(self,idCliente,idProducto,hrs,comentarios,pago):
		dbPsql = psqlManager.psqlManager()
		dbMysql = mysqlManager.mysqlManager()
		price = dbMysql.getProduct(idProducto)
		dbPsql.createCotizacion(idCliente,idProducto,hrs,price[2],comentarios,pago)
		return

	def deleteClient(self, idCliente):
		dbPsql = psqlManager.psqlManager()
		dbPsql.deleteClient(idCliente)
		return

	def alterCot(self,idCot,idConcepto,idProducto):
		dbPsql= psqlManager.psqlManager()
		dbMysql = mysqlManager.mysqlManager()
		concepto = dbMysql.getDetailsOne(idConcepto,idProducto)
		dbPsql.alterCot(idCot, concepto[1],concepto[2] )

	def getClient(self,idCliente):
		dbPsql= psqlManager.psqlManager()
		client = dbPsql.getClienteId(idCliente)
		clienteObj = cliente.cliente(client[0],client[1],client[2],client[3],client[4])
		return clienteObj

	def editClient(self, idCliente,rfc,tipoCliente,nombreCliente):
		dbPsql= psqlManager.psqlManager()
		dbPsql.editClient(idCliente,rfc,tipoCliente,nombreCliente)
		return

	def deleteCotizacion(self,idCot):
		dbPsql = psqlManager.psqlManager()
		dbPsql.deleteCotizacion(idCot)
		return

	def validateUser(self,username,passw):
		dbMysql = mysqlManager.mysqlManager()
		validate = dbMysql.validateUser(username,passw)
		return (user.user(validate[0],validate[1]) if validate else None)

	def createUser(self,username,passw):
		dbMysql = mysqlManager.mysqlManager()
		dbMysql.createUser(username,passw)
		return

	def deleteUser(self,idUser):
		dbMysql = mysqlManager.mysqlManager()
		dbMysql.deleteUser(idUser)
		return

	def getUsers(self):
		dbMysql = mysqlManager.mysqlManager()
		userList = dbMysql.getUsers()
		objList = list()
		for x in userList:
			objList.append(user.user(x[0],x[1]))
		return objList

	def changePassw(self,idUser,passw):
		dbMysql = mysqlManager.mysqlManager()
		dbMysql.changePassw(idUser,passw)
		return

	def cambioCotizacion(self):
		dbPsql = psqlManager.psqlManager()
		return dbPsql.getCambios()

	# get detailsById
	# call function and send conceptoId, conceptoNombre, cotId