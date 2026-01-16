from crewai import Task

from tools import my_tool
from agents import blog_researcher_agent, blog_writer_agent


## Research task
research_task = Task(
    agent=blog_researcher_agent,
    tools=[my_tool],
    description=(
        "Identify the content of - {topic} and extract all the relevant information."
    ),
    async_execution= False,  ## If async_execution will be set to True then it will not be a sequential process, it will be a hiererchial(parallel) process
    expected_output="A 200 word paragraph report about the topic - {topic} from the contents that you will go through"
)

## Writing task
writing_task = Task(
    agent=blog_writer_agent,
    tools=[my_tool],
    description=(
        "Get the info for the topic- {topic}, and create the content of the blog."
    ),

    async_execution= False, ## If async_execution will be set to True then it will not be a sequential process, it will be a hiererchial (parallel) process
    expected_output="Summarize all the info in a well maintain manner for a markdown file format.",
    output_file='new_blog_output.md'
)