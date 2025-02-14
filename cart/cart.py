from store.models import Product

class Cart():
    def __init__(self ,request):
        self.session = request.session

        # get the session key if it exists
        cart = self.session.get('session_key')

        # if the user is new , no session key! then create one
        if 'session_key' not in request.session :
            cart = self.session['session_key'] = {}

        # make sure the cart is available on all pages of site
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        self.session.modified = True

    # set the cart button
    def __len__(self):
        return len(self.cart)

    # set the cart page
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()

        # use ids to lookup products in DB model
        products = Product.objects.filter(id__in = product_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities