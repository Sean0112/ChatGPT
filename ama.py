import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:

    prompt = input("Ask OpenAI Anything: ")
    if(prompt == "exit" or prompt == "q" or prompt == "x" or prompt == "z" or prompt == "c"):
        break
    completions = openai.Completion.create(prompt=prompt,
                                           engine="text-davinci-002",
                                           max_tokens=100)
    completion = completions.choices[0].text
    print(completion)
