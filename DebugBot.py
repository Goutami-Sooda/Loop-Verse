# Create the language teaching assistant
from openai import OpenAI
import time

client = OpenAI()

#content = "Can you generate a conversation between a shopkeeper and a customer."

def debugger(content_input):
    assistant = client.beta.assistants.create(
        name="debug_bot",
        instructions="You are a helpful debugger and doubt solver bot. The user may give you code snippets and ask to debug or user may ask you doubt related to programming in c. You should answer to the point, restrict your answer character limit. You need to correct the wrong code given by the user and provide the corrected code.",
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
        instructions="Please address the user as a student. Consider the user as beginner. "
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

#debugger(content)