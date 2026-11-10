import requests


def understand_order(customer_text):

    url = "http://localhost:11434/api/chat"

    data = {
        "model": "llama3",
        "messages": [
            {
                "role": "system",
                "content": """
                You are a restaurant waiter.
                Understand the customer's food order.
                Reply in Arabic.
                """
            },
            {
                "role": "user",
                "content": customer_text
            }
        ],
        "stream": False
    }

    response = requests.post(url, json=data, timeout=120)

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]