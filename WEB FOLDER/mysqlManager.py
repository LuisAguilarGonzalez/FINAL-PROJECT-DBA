class mysqlManager:
	import pymysql as sql
	def tables(self):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="show tables;"
		cursor.execute(query)
		cursor.close()
		connection.close()
		return cursor.fetchall()

	def getProducts(self):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select producto.idProducto, nombreProducto, totalPrecio, nombreCategoria  from producto, productoPrecio,categoriaProducto where producto.idProducto = productoPrecio.idProducto and producto.idCategoria=categoriaProducto.idCategoria;"
		cursor.execute(query)
		cursor.close()
		connection.close()
		return cursor.fetchall()

	def getDetails(self,id):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select nombreConcepto, ROUND((costoConcepto*horasIncluido),2) from concepto, incluido where concepto.idConcepto=incluido.idConcepto and idProducto=%s;"
		cursor.execute(query,id)
		cursor.close()
		connection.close()
		return cursor.fetchall()

	def getDetailsId(self,id):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select concepto.idConcepto, nombreConcepto, ROUND((costoConcepto*horasIncluido),2) from concepto, incluido where concepto.idConcepto=incluido.idConcepto and idProducto=%s;"
		cursor.execute(query,id)
		cursor.close()
		connection.close()
		return cursor.fetchall()

	def getDetailsOne(self,idConcepto,idProducto):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select concepto.idConcepto, ROUND((costoConcepto*horasIncluido),2),nombreConcepto from concepto, incluido where concepto.idConcepto=incluido.idConcepto and concepto.idConcepto=%s and idProducto=%s;"
		args = (idConcepto,idProducto)
		cursor.execute(query,args)
		cursor.close()
		connection.close()
		return cursor.fetchone()

	def getProduct(self,idP):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select producto.idProducto, nombreProducto, totalPrecio, nombreCategoria  from producto, productoPrecio,categoriaProducto where producto.idProducto = productoPrecio.idProducto and producto.idCategoria=categoriaProducto.idCategoria and producto.idProducto=%s;"
		cursor.execute(query,idP)
		cursor.close()
		connection.close()
		return cursor.fetchone()

	def validateUser(self,username,passw):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select * from user where username=%s and password=md5(%s);"
		args = (username,passw)
		cursor.execute(query,args)
		cursor.close()
		connection.close()
		return cursor.fetchone()

	def createUser(self,username,passw):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="call verificarUnico(%s,%s);"
		args = (username,passw)
		cursor.execute(query,args)
		connection.commit()
		cursor.close()
		connection.close()
		return

	def deleteUser(self,idUser):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="delete from user where id=%s;"
		cursor.execute(query,idUser)
		connection.commit()
		cursor.close()
		connection.close()
		return

	def getUsers(self):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="select * from user;"
		cursor.execute(query)
		cursor.close()
		connection.close()
		return cursor.fetchall()

	def changePassw(self,idUser,passw):
		connection = self.sql.connect(user='Luis', passwd='3564',host='localhost',database='facelessrecords')
		cursor = connection.cursor()
		query="update user set password=md5(%s) where id=%s;"
		args=(passw,idUser)
		cursor.execute(query,args)
		connection.commit()
		cursor.close()
		connection.close()
		return
