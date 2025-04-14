import requests
import json
import ipaddress


def ip_check(ip_address):
    # Defining the api-endpoint
    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '360'
    }

    headers = {
        'Accept': 'application/json',
        'Key': 'Your_AbuseIPDB_API_Key' # Ensure to paste your AbuseIPDB API key here otherwise the script won't work
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)

    # Formatted output
    decodedResponse = json.loads(response.text)
    data = decodedResponse["data"]

    # Defining all variables for the results
    full_datetime = data["lastReportedAt"]

    if full_datetime: # AbuseIPDB returns the date and time, we just want the date so we split it.
        date_only = full_datetime.split("T")[0]
    else:
        date_only = "N/A"

    country = data["countryCode"]
    isp = data["isp"]
    domain = data.get("domain") or "N/A"
    total_reports = data["totalReports"]
    confidence_score = data["abuseConfidenceScore"]

    if int(confidence_score) >= 85:
        verdict = "Malicious"
    elif int(confidence_score) >= 50:
        verdict = "Suspicious"
    elif int(confidence_score) >= 10:
        verdict = "Low risk - Possibly abused"
    else:
        verdict = "Clean"

    # Format the result
    result = f"""
----------------------------------------------------------------------------
| IP Address:        {ip_address:<54}|
| Country:           {country:<54}|
| ISP:               {isp:<54}|
| Domain:            {domain:<54}|
| Total Reports:     {total_reports:<54}|
| Last Reported:     {date_only:<54}|
| Confidence Score:  {confidence_score:<54}|
| Verdict:           {verdict:<54}|
----------------------------------------------------------------------------
    """
    # Return the result
    return result



# Function to save the results to file
def save_to_file(content):
    with open("IPCheck_lookups.txt", "a") as file:
        file.write(content)



def user_interface():

    while True:
        print("""
|---------------------------------|
| IPCheck - Powered by AbuseIPDB  |
|---------------------------------|  
        """)

        user_input = str(input("[-] Enter IP: "))
        try:
            # Verifies that the IP is public
            if ipaddress.ip_address(user_input).is_global:
                print("[+] Checking IP... Valid IP")
            else:
                print("[!] This is a private IP. IP must be public!")
                continue
        except ValueError:
            print("[!] Oops, that's not valid input.")
            continue

        result = ip_check(user_input) # Saving the result of the lookup in a variable
        print(result)

        while True:
            save_file = input("[+] Would you like to save the file? (Y/N): ")
            if save_file.upper() == "Y":
                save_to_file(result)
                print("[+] Successfully saved.")
                break
            elif save_file.upper() == "N":
                print("[+] Okay...")
                exit(0)
            else:
                print("[!] Invalid Input.")
                continue

        exit(0)


if __name__ == '__main__':
    user_interface()