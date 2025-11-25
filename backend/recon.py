import requests

def get_ip_info(ip: str) -> dict:
    """Fetch geolocation and ISP information for a given IP address."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data=response.json()
            return{
                "ip": data.get("ip"),
                "city": data.get("city"),
                "region": data.get("region"),
                "country": data.get("country"),
                "loc": data.get("loc"),
                "org": data.get("org"),
                "postal": data.get("postal"),

            }
        else:
            return {"error": f"Failed to retrieve data from {response.status_code}"}
    except requests.RequestException as e:
        return {"error": str(e)}
    
    with open("recon_log.txt", "a") as log_file:
        log_file.write(f"IP Info requested for: {ip}\n")