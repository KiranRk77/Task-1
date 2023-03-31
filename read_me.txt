Welcome to the Address API!

This API allows you to create, update, delete, and retrieve addresses. 
Each address contains the coordinates of the address, and is saved to an SQLite database. 
Addresses are validated to ensure that the coordinates are valid.

Create Virtual Enviornament using 'python -m venv venv' 
Activate the Enviornament.

Getting Started:

1. Install the required dependencies by running `pip install -r requirements.txt`

2. Start the server by running `uvicorn app:app --reload`

3. Navigate to `http://localhost:8000/docs` to view the API documentation and test the API using the interactive Swagger UI.

4. To create a new address, send a POST request to `/addresses/` with the following JSON payload:

{
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip_code": "12345",
    "latitude": 37.7749,
    "longitude": -122.4194
}

5. To retrieve all addresses, send a GET request to `/addresses/`.

6. To retrieve addresses within a given distance and location coordinates, 
   send a GET request to `/addresses/nearby?latitude={latitude}&longitude={longitude}&distance={distance}`, where `{latitude}` and `{longitude}` 
   are the coordinates of the location you want to search from, and `{distance}` is the maximum distance (in miles) from the location.

7. To update an existing address, send a PUT request to `/addresses/{address_id}` with the JSON payload of the updated address.

8. To delete an existing address, send a DELETE request to `/addresses/{address_id}`.

Enjoy using the Address Book API!
