# tools.py
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
from langchain.tools import tool  # <-- new way to define a tool
from datetime import datetime

# DuckDuckGo search tool
duck_search = DuckDuckGoSearchRun()

@tool
def search(query: str) -> str:
    """
    Search the web for information using DuckDuckGo.
    """
    return duck_search.run(query)

# Wikipedia tool
wiki = WikipediaAPIWrapper()

@tool
def wikipedia(query: str) -> str:
    """
    Search Wikipedia for information.
    """
    return wiki.run(query)

# # Save to file tool
# def save_to_file(content: str, filename: str = None) -> str:
#     """
#     Saves the given content to a text file.
#     Returns the file name as confirmation.
#     """
#     if filename is None:
#         # Generate filename based on timestamp
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"research_{timestamp}.txt"

#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(content)
    
#     return f"Saved to {filename}"

# save_tool = {
#     "name": "save_to_file",
#     "func": save_to_file,
#     "description": "Saves the output text to a local file"
# }

# List of all tools for the agent
all_tools = [search, wikipedia]


# Function to save research organized
def save_research_to_file(data: dict, question: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "research_output.txt"

    lines = [
        f"Time: {now}",
        f"Question: {question}",
        "",
        f"Topic: {data.get('topic', '')}",
        "",
        "Summary:",
        data.get('summary', ''),
        "",
        "Sources:"
    ]

    for src in data.get("sources", []):
        lines.append(f"- {src}")

    lines.append("")
    lines.append("Tools used:")
    for tool in data.get("tools_used", []):
        lines.append(f"- {tool}")

    lines.append("\n" + "-"*50 + "\n")

    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Research saved successfully to {filename}")