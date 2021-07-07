from JAGUARETEAPP.models import Producto

class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carrito")

        if not carro:
            carro=self.session["carrito"]={}
        self.carro=carro

    def agregar(self, Producto):
        if str(Producto.id) not in self.carro.keys():
            self.carro[Producto.id] = {
                "producto_id": Producto.id,
                "nombre": Producto.nombre,
                "precio": str(Producto.precio),
                "cantidad": 1,
                
            }
        else:
            for key, value in self.carro.items():
                if key == str(Producto.id):
                    value["cantidad"]+=1
                    value["precio"]=float(value["precio"])+float(Producto.precio)
                    break
        self.save()

    def save(self):
        self.session["carrito"]= self.carro
        self.session.modified=True

    def eliminar(self, Producto):
        Producto.id=str(Producto.id)
        if Producto.id in self.carro:
            del self.carro[Producto.id]
            self.save()

    def quitar(self, Producto):
        for key, value in self.carro.items():
                if key == str(Producto.id):
                    value["cantidad"]-=1
                    value["precio"]=float(value["precio"])-float(Producto.precio)
                    if value["cantidad"]<1:
                        self.eliminar(Producto)
                    else:
                        self.save()
                    break
                else:
                    "El producto no existe en el carrito"

    def elimina_carrito(self):
        self.session["carrito"]= {}
        self.session.modified=True






        