from flask import Flask, render_template, request,redirect
import listManager
app = Flask(__name__)
global x
x=None
@app.route('/')
def index():
  if(x==None):
    return render_template("login.html")
  return redirect("/cotizaciones",code=302)

@app.route('/loginSuccesful',methods = ["POST"])
def loginSuccesful():
  lstMan = listManager.listManager()
  global x
  x = lstMan.validateUser(request.form["username"],request.form["password"])
  return redirect("/cotizaciones",code=302)


@app.route('/productList')
def productList():
  if x==None:
    return redirect("/",code=302)
  lstMan = listManager.listManager()
  products = lstMan.getProducts()
  return render_template('productList.html',len=len(products),products=products)

@app.route('/productDetails',methods = ['GET'])
def productDetails():
  if x==None:
    return redirect("/",code=302)
  productId=request.args.get("productId")
  lstMan = listManager.listManager()
  product = lstMan.getProductId(productId)
  detailsList = lstMan.getDetailsId(request.args.get("productId"))
  return render_template('productDetails.html', len=len(detailsList), products=detailsList, productName=product.nameProduct)

@app.route('/cotizaciones')
def cotizaciones():
  if x==None:
    return redirect("/",code=302)
  lstMan = listManager.listManager()
  cots = lstMan.getCotiz()
  return render_template('cotizaciones.html',len=len(cots),cots=cots)

@app.route('/clientList')
def clientList():
  if x==None:
    return redirect("/",code=302)
  lstMan = listManager.listManager()
  clients = lstMan.getClients()
  return render_template('clientList.html', len = len(clients), clients=clients)

@app.route('/createClientSuccesful', methods = ['POST'])
def createClientSuccesful():
  lstMan=listManager.listManager()
  lstMan.createClient(request.form["nombre"],request.form["rfc"],request.form["tipoCliente"])
  return redirect('/clientList',code=302)

@app.route('/createClient')
def createClient():
  if x==None:
    return redirect("/",code=302)
  return render_template('createClient.html')

@app.route('/createCotizacion', methods = ['POST'])
def createCotizacion():
  lstMan = listManager.listManager()
  products = lstMan.getProducts()
  return render_template('createCotizacion.html', idCliente=request.form["clientId"], products = products, len =len(products))

@app.route('/createCotSuccesful', methods=['POST'])
def createCotizacionSuccesful():
  lstMan=listManager.listManager()
  lstMan.createCotizacion(request.form["idCliente"],request.form["idProducto"],request.form["hrs"], request.form["comentarios"], request.form["pago"])
  return redirect('/cotizaciones',code =302)

@app.route('/confirmDeleteClient', methods=['POST'])
def confirmDeleteClient():
  lstMan=listManager.listManager()
  lstMan.deleteClient(request.form["clientId"])
  return redirect('/clientList',code=302)

@app.route('/editarCotizaciones',methods=["POST"])
def editarCotizaciones():
  lstMan = listManager.listManager()
  idCot = request.form["idCotizacion"]
  idProduct = request.form["idProduct"]
  product = lstMan.getProductId(idProduct)
  detailsList = lstMan.getDetailsId(product.idProduct)

  return render_template('/editarCotizaciones.html',details = detailsList, idCot = idCot, idProduct = product.idProduct)


@app.route('/alterCot', methods=['POST'])
def alterCot():
  lstMan=listManager.listManager()
  listId = request.form.getlist("includeId")
  idCot = request.form["idCot"]
  idProduct = request.form["idProduct"]
  for idConcept in listId:
    if(request.form["id"+idConcept]=="false"):
      lstMan.alterCot(idCot,idConcept,idProduct)
  return redirect('/cotizaciones',code=302)

@app.route('/editClient', methods=['GET'])
def editClient():
  if x==None:
    return redirect("/",code=302)
  lstMan=listManager.listManager()
  client=lstMan.getClient(request.args.get("clientId"))
  return render_template('/editarCliente.html',client = client)

@app.route('/editClientSuccesful', methods=['POST'])
def editClientSuccesful():
  lstMan=listManager.listManager()
  lstMan.editClient(request.form["idClient"],request.form["rfc"],request.form["tipoCliente"],request.form["nombre"])
  return redirect('/clientList',code=302)

@app.route('/deleteCotizacion', methods=['POST'])
def deleteCotizacion():
  lstMan=listManager.listManager()
  lstMan.deleteCotizacion(request.form["idCotizacion"])
  return redirect('/cotizaciones',code=302)

@app.route('/userList')
def userList():
  if x==None:
    return redirect("/",code=302)
  lstMan=listManager.listManager()
  userList = lstMan.getUsers()
  return render_template('userList.html', userList=userList, len=len(userList))

@app.route('/confirmDeleteUser',methods=["POST"])
def confirmDeleteUser():
  lstMan=listManager.listManager()
  userList = lstMan.deleteUser(request.form["userId"])
  return redirect('/userList',code=302)

@app.route('/createUser')
def createUser():
  if x==None:
    return redirect("/",code=302)
  return render_template('createUser.html')

@app.route('/createUserSuccesful', methods=["POST"])
def createUserSuccesful():
  lstMan = listManager.listManager()
  lstMan.createUser(request.form["username"],request.form["passw"])
  return redirect('/userList',code=302)

@app.route('/editUser', methods=["GET"])
def editUser():
  if x==None:
    return redirect("/",code=302)
  idUser = request.args.get("userId")
  return render_template('editUser.html',userId = idUser)

@app.route('/changePassw', methods =["POST"])
def changePassw():
  lstMan = listManager.listManager()
  lstMan.changePassw(request.form["idUser"],request.form["passw"])
  return redirect('/userList',code=302)

@app.route('/cambioCotizacion')
def cambioCotizacion():
  if x==None:
    return redirect("/",code=302)
  lstMan = listManager.listManager()
  cambioList = lstMan.cambioCotizacion()
  return render_template('cambioCotizacion.html',cambioList=cambioList)