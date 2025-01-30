import requests
import json

def aadhaar_verification(aadhaar_number, otp):
    
    url = ""
    
    api_key = ""
    
    data = {
        "aadhaar_number": aadhaar_number,
        "otp": otp,
        "apikey": api_key  
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "token"  
    }

    try:
        response = requests.post(url, json=data, headers=headers)

        
        if response.status_code == 200:
            result = response.json()  
            
            
            if result.get("status") == "success":
                return {
                    "status": "success",
                    "message": "Aadhaar authentication successful.",
                    "aadhaar_number": aadhaar_number
                }
            else:
                return {
                    "status": "failure",
                    "message": "Aadhaar authentication failed.",
                    "aadhaar_number": aadhaar_number
                }
        else:
            
            return {
                "status": "failure",
                "message": "Error in API request.",
                "aadhaar_number": aadhaar_number
            }
    
    except Exception as e:
                return {
            "status": "failure",
            "message": f"An error occurred: {e}",
            "aadhaar_number": aadhaar_number
        }


aadhaar_number = input("Enter Aadhaar Number (12 digits): ")
otp = input("Enter OTP: ")


response = aadhaar_verification(aadhaar_number, otp)


print(response["status"])
print(response["message"])
print(response["aadhaar_number"])
