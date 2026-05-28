import sys
import requests


def main():
    
    
    if len(sys.argv) == 2:
        try:
            user_input = float(sys.argv[1])
                
            
        
        except ValueError:
            sys.exit("invalid input")

        try:
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=cad5e66453fcca7d4f6710b6e7c8bf9842be402e6da154c71862aa0c3b5b3764")
            data = response.json()
            price = user_input * float(data['data']['priceUsd'])
            print(f"${price:,.4f}")
        except requests.RequestException:
            sys.exit()

    else:
        sys.exit("Invalid input")

main()