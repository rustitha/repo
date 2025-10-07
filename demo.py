# --- PII Data Variables for Scanning ---

# PII: Personal Identification
user_full_name = "Jane Doe"
user_first_name = "Jane"
user_last_name = "Doe"

# PII: Contact Information
user_email = "jane.doe@example.com"
user_phone_number = "+1 (555) 123-4567"
user_home_address = "123 Main St, Anytown, CA 90210"

# PII: Financial and Sensitive Identifiers
credit_card_number = "1234-5678-9012-3456"
social_security_number = "987-65-4321"
driver_license_number = "A1234567"

# PII: Online and Technical Data
ip_address = "192.168.1.1"
device_id = "device_xyz_12345"
session_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ"

# PII: Health and Medical Information
medical_record_number = "MRN-987654"
patient_name = "John Smith"
health_insurance_id = "HI-1234567890"

# PII: Other Potentially Sensitive Information
date_of_birth = "1990-05-15"
passport_number = "P1234567"
bank_account_number = "9876543210"

# --- Functions that use these PII variables ---

def send_welcome_email(email_address, name):
    """Sends a welcome email to the user."""
    print(f"Sending welcome email to: {email_address} for {name}")

def log_user_activity(user_id, ip):
    """Logs user activity with their IP address."""
    print(f"User {user_id} logged in from IP: {ip}")

def process_payment(credit_card, amount):
    """Simulates processing a payment with a credit card number."""
    print(f"Processing a payment of ${amount} with card: {credit_card}")

# --- Example function calls using the PII variables ---
# These function calls are where your scanner should flag the use of PII.

send_welcome_email(user_email, user_first_name)
log_user_activity(user_full_name, ip_address)
process_payment(credit_card_number, 50.00)
