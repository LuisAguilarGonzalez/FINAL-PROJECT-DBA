class psqlManager:
   import psycopg2 as psql
   # def __init__(self):
   #    self.cursor = self.conn.cursor()
   # def close(self):
   #    self.cursor.close()
   #    self.conn.close()

   def getCots(self):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "SELECT * from cotizacion order by idCotizacion ;"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      conn.close()
      return result

   def getClientes(self):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "SELECT * from clientes where activo=TRUE order by idClientes;"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      conn.close()
      return result

   def getClienteId(self,idCliente):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "SELECT * from clientes where idClientes=%s ;"
      cursor.execute(query,(idCliente,))
      result = cursor.fetchone()
      cursor.close()
      conn.close()
      return result

   def createClient(self,name,rfc,type):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "insert into clientes values(default, %s,%s,%s, TRUE);"
      cursor.execute(query,(name,rfc,type))
      conn.commit()
      cursor.close()
      conn.close()

   def createCotizacion(self,idCliente,idProducto,hrs,subtotal,comentarios,pago):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "insert into cotizacion values(default, %s,%s,%s,0,%s,%s,TO_DATE(%s,'YYYY-MM-DD'),FALSE);"
      cursor.execute(query,(idCliente,idProducto,hrs,subtotal,comentarios,pago))
      conn.commit()
      cursor.close()
      conn.close()

   def deleteClient(self,idCliente):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "UPDATE clientes set activo = FALSE where idClientes=%s;"
      cursor.execute(query,(idCliente,))
      conn.commit()
      cursor.close()
      conn.close()

   def alterCot(self,idCotizacion,descuentoConcepto,nombreConcepto):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "select aplicacionDescuento(%s,%s,%s);"
      data = (idCotizacion,descuentoConcepto,nombreConcepto,)
      cursor.execute(query,data)
      conn.commit()
      cursor.close()
      conn.close()

   def editClient(self, idCliente,rfc,tipoCliente,nombreCliente):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "UPDATE clientes set nombre = %s, rfc = %s, tipoPersona=%s where idClientes=%s;"
      data=(nombreCliente,rfc,tipoCliente,idCliente,)
      cursor.execute(query,data)
      conn.commit()
      cursor.close()
      conn.close()

   def deleteCotizacion(self, idCotizacion):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "delete from cotizacion where idCotizacion= %s;"
      cursor.execute(query,(idCotizacion,))
      conn.commit()
      cursor.close()
      conn.close()

   def getCambios(self):
      conn = self.psql.connect(database="facelessrecords", user='luis', password='1234', host='localhost')
      cursor = conn.cursor()
      query = "select * from cambioCotizacion;"
      cursor.execute(query)
      result = cursor.fetchall()
      cursor.close()
      conn.close()
      return result
