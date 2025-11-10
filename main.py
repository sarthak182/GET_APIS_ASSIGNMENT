import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()  #raising exception for HTTP errors
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit()

users = response.json()

if not users: #check for empty list
    print("No users found in the API response.")
    exit()

print("Users whose city name start with 'S':")
print("-" * 24)
count=0

for i, user in enumerate(users, start=1):
    name = user.get('name', 'N/A')
    username = user.get('username', 'N/A')
    email = user.get('email', 'N/A')
    city = user.get('address', {}).get('city', 'N/A') #handling missing data

    if city.startswith('S'):
        count+=1
        print(f"User {i}:")
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print("-" * 24)

print("Summary:")
print(f"Total users retrieved:    {len(users)}")
print(f"Matching users:           {count}")
print(f"Remaining users:          {len(users)-count}")