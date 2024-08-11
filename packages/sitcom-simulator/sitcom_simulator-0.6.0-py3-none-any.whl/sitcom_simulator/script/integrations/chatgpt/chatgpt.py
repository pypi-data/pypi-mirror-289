def chat(
        prompt: str,
        max_tokens:int=2048,
        temperature:float=1,
        model: str="gpt-4o-mini",
    ):
    """
    Given a prompt, returns a response from ChatGPT.

    :param prompt: The prompt for the chat
    :param max_tokens: The maximum number of tokens to generate
    :param temperature: The temperature to use when generating the response, which controls randomness. Higher values make the response more random, while lower values make the response more deterministic.
    :param model: The model to use for the chat
    """
    import openai
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": "You are a helpful script-writing assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message["content"].strip()