from crewai_tools import EXASearchTool


##Initialize the tool with a specific youtube channel handel to target your search
my_tool = EXASearchTool(
    website="https://www.wikipedia.org/"
)