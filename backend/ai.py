from openai import OpenAI

client = OpenAI(api_key="sk-HxelGCkNiiv9rndKVVIZgeqbgRy_")


def get_ai_response(question, db_context=None):
    prompt = f"""
    You are an agricultural assistant for African farmers.

    Context from database:
    {db_context}

    Question:
    {question}

    Provide a helpful, practical farming answer.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful agricultural expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content