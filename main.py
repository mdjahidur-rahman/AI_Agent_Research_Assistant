from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.output_parsers import PydanticOutputParser

from tools import all_tools
from tools import save_research_to_file

# Load your API key from .env
load_dotenv()


#  Define structured output

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


# Initialize the LLM

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Define the system prompt

system_prompt = """
You are a research assistant.

Answer the user's question with a **detailed, well-explained summary** (3-5 sentences).

You have access to the following tools:
- DuckDuckGo Search: Use for general web searches.
- Wikipedia: Use for Wikipedia articles (return name and URL).

**Instructions**:
1. Always include tools you used in the "tools_used" field.
2. Fetch accurate sources and return them in the "sources" field in this format: "Name - URL".
3. Output must be valid JSON **exactly like this**:

{
    "topic": "...",
    "summary": "...",
    "sources": ["Name - URL", "Name - URL"],
    "tools_used": ["DuckDuckGo Search", "Wikipedia"]
}

Do not include any text outside the JSON.
"""


# Create the agent

agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt=system_prompt
)


# Run the agent

user_question = input("Enter your research query: ")

response = agent.invoke(
    {"messages": [
        {
            "role": "user", 
            "content": user_question
        }
     ]
    }
)


# Parse the output into Python object

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

parsed_response = parser.parse(response["messages"][-1].content)


# Show results

print("Raw response from LLM:")
print(response["messages"][-1].content)
print("\nParsed response:")
print(parsed_response)


# user intention to save or not
user_question_lower = user_question.lower()

positive_keywords = ["save", "store", "write to file", "export"]
negative_keywords = ["don't save", "do not save", "no save", "skip saving"]

should_save = any(kw in user_question_lower for kw in positive_keywords) \
              and not any(kw in user_question_lower for kw in negative_keywords)

if should_save:
    save_research_to_file(parsed_response.dict(), user_question)
else:
    print("Research not saved as per user instruction.")
