class cotizacion:
	def __init__(self,idCotizacion,objCliente,objProducto,horas,descuentos,total,comentarios,limitePago,editado):
		self.idCotizacion = idCotizacion
		self.objCliente = objCliente
		self.objProducto = objProducto
		self.horas = horas
		self.total = total
		self.descuentos = descuentos
		self.iva = float(total)*.16
		self.comentarios = comentarios
		self.limitePago = limitePago
		self.editado = editado