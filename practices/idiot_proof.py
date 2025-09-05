#LV 2nd Idiot Proof

first_name = input("Enter your first name:").strip()
last_name = input("Enter your last name:").strip()
phone = input("Enter your 10-digit phone number:")
gpa_input = input("Enter your GPA:").strip()

full_name = (f"{first_name.title()} {last_name.title()}")

phone_digits = ("".join (filter(str.isdigit,phone)))
formatted_phone = (f"{phone_digits[0:3]} {phone_digits [3:6]} {phone_digits [6:10]}")

gpa = round(float(gpa_input),1)

print("\n---formatted output---")
print(f"Name:{full_name}")
print(f"Phone:{formatted_phone}")
print(f"GPA:{gpa}")
