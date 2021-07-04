from JAGUARETEAPP.models import Producto

class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")

        if not carro:
            carro=self.session["carro"]={}
        self.carro=carro

    def agregar(self, Producto):
        if str(Producto.id) not in self.carro.keys():
            self.carro[Producto.id] = {
                "producto_id": Producto.id,
                "marca": Producto.marca,
                "color": Producto.color,
                "precio": str(Producto.precio),
                "imagen": Producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(Producto.id):
                    value["quantity"]+=1
                    break
        self.save()

    def save(self):
        self.session["carro"]= self.carro
        self.session.modified=True

    def eliminar(self, Producto):
        producto_id=str(Producto.id)
        if producto_id in self.carro:
            del self.carro[Producto.id]
            self.save()

    def quitar(self, Producto):
        for key, value in self.carro.items():
                if key == str(Producto.id):
                    value["quantity"]-=1
                    if value["quantity"]<1:
                        self.eliminar(Producto)
                    else:
                        self.save()
                    break
                else:
                    "El producto no existe en el carrito"

    def elimina_carrito(self):
        self.session["carro"]= {}
        self.session.modified=True






        