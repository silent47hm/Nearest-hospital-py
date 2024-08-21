import requests

url = "https://google-autocomplete-near-by-places-and-services.p.rapidapi.com/v1/google/get-service-by-id"

querystring = {"placeId":"ChIJZWZ6QRMsDogRzHlilwcznbg","language":"en"}

headers = {
	"x-rapidapi-key": "9dc28790d2mshdb96c2569b20f20p1e3121jsn2806faa392ac",
	"x-rapidapi-host": "google-autocomplete-near-by-places-and-services.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())