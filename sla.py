import json

import requests

url = "http://127.0.0.1:5001/articles"
headers = {
    "Content-Type": "application/json",
}

error_counter = 0
for num in range(100):
    print(num)
    response = requests.post(
        url,
        data=json.dumps(
            {"title": f"Article no {num}", "content": "Article content", "author": 1}
        ),
        headers=headers,
    )
    if response.status_code == 500:
        error_counter += 1

print(f"Errors: {error_counter}")
