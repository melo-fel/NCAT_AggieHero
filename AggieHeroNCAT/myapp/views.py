from django.shortcuts import render
import openai

# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})

openai.api_key = "<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>"

def chatbot_response(user_input):
    response = openai.Completion.create(engine="gpt-3.5-turbo", prompt=user_input, temperature=0.5, max_tokens=1024,
                                        top_p=1, frequency_penalty=0, presence_penalty=0)
    return response["choices"][0]["texts"]
