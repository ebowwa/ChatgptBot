import openai

class ChatGPT:
    def __init__(self):
        # Initialize the ChatGPT instance
        self.chatbot = openai.Completion.create(
            engine="text-davinci-002",
            prompt="",
            temperature=0.5,
            max_tokens=1024,
            n=1,
            stop=None,
        )

    def generate_response(self, input: str) -> str:
        # Generate a response to the given input
        response = self.chatbot.complete(input=input)
        return response.choices[0].text
