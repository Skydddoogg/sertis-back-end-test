# Sertis Back-End Test
## Let's try
run ```docker-compose up``` in terminal.
## Endpoints
### create 
URL: ```http://127.0.0.1:8000/api/cards/```

Example Request Body:
```json
{
    "name":"Java Fundamental",
    "content": "This is the best Java course ever!",
    "category": "technology",
    "status": false,
    "author": "Thanawat Lodkaew"
}
```
### get all
URL: ```http://127.0.0.1:8000/api/cards/```

### get
URL: ```http://127.0.0.1:8000/api/cards/<id>/```

Example Complete URL: ```http://127.0.0.1:8000/api/cards/5f6ac3711c239d1cbe1c8c81/```
### update
URL: ```http://127.0.0.1:8000/api/cards/<id>/```

Example Complete URL: ```http://127.0.0.1:8000/api/cards/5f6ac3711c239d1cbe1c8c81/```

Example Request Body:
```json
{
    "name":"Python Fundamental",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "category": "technology",
    "status": false,
    "author": "Thanawat Lodkaew"
}
```
### delete
URL: ```http://127.0.0.1:8000/api/cards/<id>/```

Example Complete URL: ```http://127.0.0.1:8000/api/cards/5f6ac3711c239d1cbe1c8c81/```

Example Request Body:
```json
{
    "author": "Thanawat Lodkaew"
}
```
