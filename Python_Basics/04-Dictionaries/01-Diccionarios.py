# Create a dictionary to store hotel information
hotel_data = {
	"name": "Hotel El Sitio",
	"star_rating": 5,
    # The value of 'rooms' is a list of dictionaries, where each dictionary represents a room
	"rooms": [
        {
			"room_number": 1,
			"floor_number" : 1,
			"nightly_rate" : 100
        },
        {
            "room_number": 2,
            "floor_number" : 1,
            "nightly_rate" : 100
        },
        {
            "room_number": 3,
            "floor_number" : 2,
            "nightly_rate" : 200
        },
        {
            "room_number": 4,
            "floor_number" : 2,
            "nightly_rate" : 250
        }               
		]
	}

#show the room assigned to the guest	
print(f"Estimado huesped, el hotel: {hotel_data['name']} le asigna la habitación # : {hotel_data['rooms'][3]['room_number']} la cual tiene un precio de: {hotel_data['rooms'][3]['nightly_rate']}")

