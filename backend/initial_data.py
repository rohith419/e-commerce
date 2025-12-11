# Optional: helper to create sample data when run within Django shell.
def create_sample_products():
    from products.models import Product
    Product.objects.create(title='Sample Product 1', description='A demo product', price=99.99)
    Product.objects.create(title='Sample Product 2', description='Another demo product', price=149.50)
