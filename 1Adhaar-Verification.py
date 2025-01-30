import json

def adhaar_verification(adhaar_number, otp): 
    if len(adhaar_number) == 12 and adhaar_number.isdigit():
        
        if otp == "000000":  
            return {
                "status": "success",
                "message": "Adhaar authentication successful.",
                "adhaar_number": adhaar_number
            }
        else:
            return {
                "status": "failure",
                "message": "Invalid OTP provided.",
                "adhaar_number": adhaar_number
            }
    else:
        return {
            "status": "failure",
            "message": "Invalid Adhaar number. It must be 12 digits.",
            "adhaar_number": adhaar_number
        }

adhaar_number = input("Enter Adhaar Number (12 digits): ")
otp = input("Enter OTP: ")
response = adhaar_verification(adhaar_number, otp)
print(response["status"])
print(response["message"])
print(response["adhaar_number"])
