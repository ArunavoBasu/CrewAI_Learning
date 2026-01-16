from crewai import Agent, LLM
from tools import my_tool

import os
from dotenv import load_dotenv

## Loading the env file
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
my_model = os.getenv("MODEL")
exa_api_key = os.getenv("EXA_API_KEY")


## Initializing the LLM
llm = LLM(
    model=my_model,
    temperature=0.2,
    max_tokens=2000
)

## Creat a researcher agent
blog_researcher_agent = Agent(
    llm = llm,
    role= 'Blog researcher',
    goal = 'Get the relevant content for the topic - {topic}.',
    backstory = 'Expert in understanding AI, Machine Learning and Data Science topic',
    memory = True,
    verbose = True,
    tools=[my_tool],
    respect_context_window=True,  # Enables automatic context management
)

## Creat a writer agent
blog_writer_agent = Agent(
    llm=llm,
    role= 'Blog writer',
    goal = 'Narrate a tech story about- {topic}',
    backstory = 'With a flair for simplufying complex topics, you craft engaging stories bringing new discoveries into the light as well.',
    memory = True,
    verbose = True,
    tools = [my_tool]
)

