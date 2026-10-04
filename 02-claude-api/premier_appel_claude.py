import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "Explique en trois phrases ce qu'est un LLM."
        }
    ]
)

for block in message.content:
    if block.type == "text":
        print(block.text)