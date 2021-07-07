def importe_total_carrito(request):
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carrito"].items():
            total=total+(float(value["precio"]))
    
    return {"importe_total_carrito":total}