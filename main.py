from pyscript import document, display # type: ignore

def generate_SKU(e): # initiating a function

    # presents variable by linking the id from the html
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    quantity = document.getElementById("quantity").value

    # uses concatination to generate sku formula
    SKU = category + "-" + product + "-" + quantity

    # displays resulsts to the page
    display(SKU, target="show")

def make_order(e): # initiating a function

   # presents variable by linking the id from the html
   prod1 = document.getElementById("drink1")
   prod2 = document.getElementById("drink2")
   prod3 = document.getElementById("drink3")

   # multiplies the product values for the subtotal
   subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked  # type: ignore

   # subtotal multiplied with the vat formula
   VAT = subtotal * 0.12

   # subtotal added to the vat to get the total
   total = subtotal + VAT

   # displays resulsts to the page
   display(subtotal, VAT, total, target="show")
