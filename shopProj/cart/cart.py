from product.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('cart')

        # If the user is new, No session key! Create one
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        # Tell django session was modified saves it
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    # Debugging
    def get_cart_contents(self):
        return self.cart

    def get_products(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        # Return the products
        return products

    def get_qty(self):
        quantities = self.cart
        return quantities

    def update(self, product_id, quantity):
        product_id = str(product_id)
        product_qty = int(quantity)

        # Get the cart
        ourcart = self.cart

        #Update the cart dict
        ourcart[product_id] = product_qty

        # Tell django session was modified saves it
        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product_id):
        product_id = str(product_id)

        # Get the cart
        ourcart = self.cart

        #delete the item from the cart dict
        if product_id in ourcart:
            ourcart.pop(product_id, None)

        # Tell django session was modified saves it
        self.session.modified = True

        thing = self.cart
        return thing

