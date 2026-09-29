from openai import OpenAI

client = OpenAI(
    api_key="",
    base_url=""
)

with open("knowledge.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

while True:

    question = input("Ask AI: ")

    response = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "system",
                "content": f"Answer only from this document:\n\n{knowledge}"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAI:", response.choices[0].message.content)