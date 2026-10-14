from crewai import Agent,Task,Crew,LLM


# Local Qwen model through Ollama

llm = LLM(
    model="ollama/qwen2.5:1.5b",
    base_url="http://localhost:11434"
)

researcher=Agent(
    role="AI Researcher",
    goal="Explain AGENTIC AI in artificial intelligence IN simple terms",
    backstory="you are Agentic AI resarcher,you are working since AI comes in the globe"
    
),
llm=llm,
verbose=True

task=Task(
    description=(
        "What is model context protocol used for agentic AI",
        'how it use in agentic AI',
    ),
    Expected_output=("a beginner friendly explanationof MCP",
                     "With simple examples"
                     
),
    agent=researcher
    

)

crew=Crew(agents=[researcher],tasks=[task],
          verbose=True)

verbose=True
result=crew.kickoff()
print(print("\n=============================="))
print("FINAL ANSWER:\n")
print(result)

