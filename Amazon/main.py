import time
from amazon.address import Address
from amazon.creditCard import CreditCard
from amazon.customer import Customer
from amazon.electricBankTransfer import ElectronicBankTransfer
from amazon.orderShipment import OrderShipment
from amazon.payment import Payment
from amazon.product import Product
from amazon.productCategory import ProductCategory
from amazon.productReview import ProductReview
from amazon.seller import Seller
from amazon.shipmentStatus import ShipmentStatus, ShipmentStatusUpdate

# Create a customer
customer_address1 = Address(streetAddress="123 Main St", city="Anytown", state="CA", zipCode="12345", country="USA")
customer1 = Customer(id=1, name="John Doe", email="john.doe@example.com", phone="555-1234")
customer1.addShippingAddress(customer_address1)

# Add credit card to customer
credit_card1 = CreditCard(cardHoldersName="John Doe", cardNumber="1234-5678-9876-5432",
                         expirationYear=2024, expirationMonth=12, cvv="123", authority="Visa")
customer1.addCreditCard(credit_card1)

# Add electronic bank transfer to customer
bank_transfer = ElectronicBankTransfer(accountHoldersName="John Doe", bankName="Example Bank",
                                       bankLocation="Anytown, USA", routingNumber="123456789",
                                       accountNumber="9876543210")
customer1.setBankAccount(bank_transfer)

# Create a seller
seller_address1 = Address(streetAddress="456 Oak St", city="Another Town", state="CA", zipCode="54321", country="USA")
seller1 = Seller(id=2, name="Jane Seller", email="jane.seller@example.com", phone="555-4321", location=seller_address1)

# Create a product
product_category1 = ProductCategory(categoryId=1, name="Electronics", description="Electronic Devices")
product1 = Product(productID=1, name="Smartphone", description="Latest smartphone model",
                  price=799.99, category=product_category1, availableItemCount=10, seller=seller1)

# Create a product review
review = ProductReview(reviewId=1, rating=5, review="Great product!", product=product1, reviewer=customer1)

# Add product to customer's cart
customer_cart = customer1.getShoppingCart()
customer_cart.addItem(product1, quantity=2)

# Checkout and create an order
order = customer_cart.checkout()
order_status_update = ShipmentStatusUpdate(shipmentNumber=1, status=ShipmentStatus.PENDING)
order_shipment = OrderShipment(shipmentNumber=1, shipmentDate=round(time.time() * 1000),
                               estimatedArrival=round(time.time() * 1000) + 86400000, carrier="Amazon Shipping")
order_shipment.addShipmentHistory(order_status_update)
payment = Payment(customer=customer1, amount=order.calculateTotal(), electronicBankTransfer=bank_transfer)
customer1.placeOrder(order, order_shipment, payment)

#deliver order
order.deliver()

#add review
customer1.addProductReview(review)

#fetch review
product1.getReview()

#Return & Refund
order.returnOrder()