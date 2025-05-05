from django.shortcuts import render, redirect
from openai import OpenAI
from django.conf import settings
from .models import Message

# Create your views here.
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def chatbot(request):
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        user_message = Message.objects.create(
            user=request.user, role="user", content=user_input
        )

        history = Message.objects.filter(user=request.user).order_by("timestamp")
        messages = [{"role": msg.role, "content": msg.content} for msg in history]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = response.choices[0].message.content
        Message.objects.create(user=request.user, role="system", content=reply)

        return redirect("chatbot:chat")

    history = Message.objects.filter(user=request.user).order_by("timestamp")
    return render(request, "chatbot/chat.html", {"messages": history})
