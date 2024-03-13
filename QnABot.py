# Create the language teaching assistant
from openai import OpenAI
import time

client = OpenAI()

#content = "Generate a looping statement related question in C language of easy level."

def generate_qna(content_input):
    assistant = client.beta.assistants.create(
        name="QnA_bot",
        instructions="You are a helpful question generator bot, who asks the user questions related to only looping concepts in C programming language. The user sets easy, medium or hard based on that you have to generate questions. Then the user provides answer to your question you need to check if the answer is right. If it is right then you should print (Amazing! you did it) and then generate another question . If the user gives wrong answer you should print (Sorry it's wrong, try again).  You should not correct the user or solve the question for the user if the user's answer is wrong. They have to try again. You are not supposed to print the correct answer.",
        #tools=[{"type": "retrieval"}],
        model="gpt-3.5-turbo-0125"  # or any other language-focused model
    )

    #print(assistant)
    #Assistant(id='asst_U4KyfS9qOgI6vGKr2PKTAFgp', created_at=1709974491, description=None, file_ids=[], instructions='You are a helpful assistant who interacts with the user to teach them languages. You have to clear their doubts and answer to the point. Assume the role given by the user and continue to chat with them.', metadata={}, model='gpt-3.5-turbo-0125', name='Lang_bot', object='assistant', tools=[])

    # Create a new thread
    thread = client.beta.threads.create()

    # Add a message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content_input
    )

    #print(thread)
    #print(message)

    # Run the assistant on the thread
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        #messages=messages_data,
        instructions="Please address the user as Student. Consider the user as a undergraduate student."
    )

    #print(run)

    while run.status != 'completed':
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(thread_id = thread.id, run_id = run.id)
        print(run.status)

    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
    )

    #print(messages)
    print(messages.data[0].content[0].text.value)

    return messages.data[0].content[0].text.value

#generate_qna(content)