import os
import requests
import json
from azure.identity import DefaultAzureCredential

# Define the scope needed for Microsoft Graph API access
# Note: You might need User.Read.All permission granted to your app/identity
# if fetching profiles other than your own.
GRAPH_SCOPE = ["https://graph.microsoft.com/.default"]

def get_graph_token():
    """Authenticates and retrieves an access token for Microsoft Graph."""
    try:
        # Ensure you are logged in via Azure CLI (`az login`) or have other credentials configured
        credential = DefaultAzureCredential()
        access_token = credential.get_token(*GRAPH_SCOPE)
        return access_token.token
    except Exception as e:
        print(f"Error obtaining Graph token: {e}")
        return None

def print_profile_summary(parsed_json):
    """Prints a summary of the profile: top-level areas and userPrincipalName(s)."""
    print("\nTop-level areas in profile:")
    for key in parsed_json.keys():
        if not key.startswith("@odata"):  # skip odata.context keys
            print(f"  - {key}")

    # Print userPrincipalName(s) from account section
    accounts = parsed_json.get("account", [])
    if accounts:
        print("\nuserPrincipalName(s) in account:")
        for acc in accounts:
            upn = acc.get("userPrincipalName", None)
            print(f"  - {upn if upn else '[empty]'}")
    else:
        print("No 'account' section found in profile.")

def print_profile_details(parsed_json):
    """Prints the full profile JSON, pretty-printed."""
    print(json.dumps(parsed_json, indent=2))

def get_my_profile():
    """Fetches the current user's profile from Microsoft Graph."""
    token = get_graph_token()
    if not token:
        print("Could not authenticate with Microsoft Graph.")
        return

    graph_url = "https://graph.microsoft.com/beta/me/profile"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    print(f"Making GET request to: {graph_url}")

    try:
        response = requests.get(graph_url, headers=headers)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        print("\nResponse Status Code:", response.status_code)
        #print("Profile Data:")
        try:
            parsed_json = response.json()
            print_profile_details(parsed_json)
            print_profile_summary(parsed_json)
        except json.JSONDecodeError:
            print(response.text)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_user_profile(user_id):
    """Fetches a specific user's profile from Microsoft Graph."""
    token = get_graph_token()
    if not token:
        print("Could not authenticate with Microsoft Graph.")
        return

    # Use the user_id (can be UPN like 'user@example.com' or Azure AD object ID)
    graph_url = f"https://graph.microsoft.com/beta/users/{user_id}/profile"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    print(f"Making GET request to: {graph_url}")

    try:
        response = requests.get(graph_url, headers=headers)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        print("\nResponse Status Code:", response.status_code)
        #print("Profile Data:")
        try:
            parsed_json = response.json()
            print_profile_details(parsed_json)
            print_profile_summary(parsed_json)
        except json.JSONDecodeError:
            print(response.text)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
        if response.status_code == 403:
            print("Received a 403 Forbidden error. Check if the authenticated identity has User.Read.All permissions.")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    #target_user = "271342b4-6857-41f6-9989-256df195c8d0" # rjmcvey2013_gmail.com#EXT#@rjmcvey2013gmail.onmicrosoft.com
    target_user = "2f2714b7-eceb-4611-a918-bcbeebcf6519" # ryan@rjmcvey2013gmail.onmicrosoft.com
    print(f"Attempting to fetch profile for: {target_user}")
    get_user_profile(target_user)
    # Uncomment the line above to fetch a specific user's profile  


    
    # To get your own profile as before:
    # print("\nAttempting to fetch own profile:")
    # get_my_profile() # Fetching own profile for testing