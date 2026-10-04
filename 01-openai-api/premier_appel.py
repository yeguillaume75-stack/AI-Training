from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input="Explique en trois phrases ce qu'est un LLM."
)

print(response.output_text)