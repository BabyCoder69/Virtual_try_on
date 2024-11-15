

***Virtual Try On API***
===

This project helps you virtually try on clothes using a whatsapp interface.


***How to run:***
===
1. Build the docker image with the following command:

    ```docker build -t virtual_tryon .```

2. Run the docker image with the following command:

    ```docker run --rm -it -p 8000:8000 virtual_tryon```


# API Documentation


### 1. POST: /virtual_try_on



***Returns:***
===


***Example:***
===

### *Response:*
```json


```

### 2. GET: /health

Checks the health of the API.

***Returns:***
===
Returns a JSON object containing the status of the API.

### *Response:*
```json
{
  "status_code": "200",
  "health": "healthy"
}
```

---