from openai import OpenAI


def get_response(message):
    client = OpenAI(api_key='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'
                    )

    chat = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        model="gpt-3.5-turbo",
        stream=True,
    )
    response = ''
    for chunk in chat:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content+" "
    return response

# print(get_response("Hello how r u"))