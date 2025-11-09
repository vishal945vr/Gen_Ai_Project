from crewai import Agent, Task, Crew, Process
from crewai import LLM
from dotenv import load_dotenv
import os
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="ollama/llama3")


# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("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")



# Researcher Agent
resecherAgent = Agent(
    role="Research Analyst",
    goal="Conduct thorough research on given topics and gather accurate information",
    backstory="""You are an experienced research analyst with a keen eye for detail.
    You excel at finding relevant information, verifying facts, and synthesizing
    complex data into clear insights.""",
    llm=llm,  # directly use LLM here
    verbose=True,
    allow_delegation=False
)

# Writer Agent
write = Agent(
    role="Content Editor",
    goal="Review and refine content to ensure quality, accuracy, and consistency",
    backstory="""You are a meticulous editor with an eye for perfection.
    You ensure all content is polished, error-free, and maintains a consistent
    voice and style throughout.""",
    llm=llm,  # directly use LLM
    verbose=True,
    allow_delegation=False
)

# Reviewer Agent
reviewAgent = Agent(
    role="Reviewer",
    goal="Ensure final content quality and factual accuracy",
    backstory="""You are an expert reviewer who polishes and perfects written content.""",
    llm=llm,  # directly use LLM
    verbose=True,
    allow_delegation=False
)

# Tasks
taskresecher = Task(
    description="""Research the topic: {topic}
    1. Gather comprehensive information
    2. Identify key points and insights
    3. Find relevant statistics and examples
    4. Verify accuracy
    Provide a detailed research report.""",
    expected_output="A comprehensive research report with key findings and insights",
    agent=resecherAgent
)

taskwrite = Task(
    description="""Using the research findings, write a blog post about: {topic}
    - Engaging introduction
    - Structured main sections
    - Examples and data
    - Compelling conclusion
    Target length: 800-1000 words""",
    expected_output="A well-written blog post of 800-1000 words",
    agent=write
)

taskreview = Task(
    description="""Review and edit the blog post about: {topic}
    - Fix grammar/spelling
    - Improve flow
    - Ensure factual accuracy
    Provide final, publication-ready version.""",
    expected_output="A polished, publication-ready blog post",
    agent=reviewAgent
)

# Crew
crewouput = Crew(
    agents=[resecherAgent, write, reviewAgent],
    tasks=[taskresecher, taskwrite, taskreview],
    process=Process.sequential
)

# Run Crew
def run_crew(topic: str):
    result = crewouput.kickoff(inputs={"topic": topic})
    return result

if __name__ == "__main__":
    topic = "The Impact of Artificial Intelligence on Modern Healthcare"
    print(f"🚀 Starting content creation for topic: {topic}\n")
    final_output = run_crew(topic)
    print("✅ Final Output:\n", final_output)
