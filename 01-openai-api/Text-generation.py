from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model = "gpt-6-astra",
    reasoning = {"effort": "low"},
    #instructions = "Talk like a computer expert",
    #input = "Compare en quelques phrases les format JSON et XML. Quand utiliser l'un ou l'autre?",
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)