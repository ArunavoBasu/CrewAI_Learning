from crewai import Crew, Process

from agents import blog_researcher_agent, blog_writer_agent
from tasks import research_task, writing_task


##Forming the crew for a sequential process

crew = Crew(
    agents=[blog_researcher_agent, blog_writer_agent],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

##Start the execution with enhanced feedback
result = crew.kickoff(
    inputs={
        'topic': 'AI VS ML VS DL VS Data Science'
    }
)
print(result)