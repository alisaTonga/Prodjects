import os
import qrcode
from PIL import Image
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate a random quote
quote = fake.catch_phrase()

# Create a QR code for the quote
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(quote)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save(os.path.join(os.getcwd(), "random_quote_qr.png"))

# Print the generated quote
print("Generated quote:")
print(quote)