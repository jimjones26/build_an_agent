# ------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------
from langchain_ollama import ChatOllama
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------
# Define tools
# ------------------------------------------------------------------
search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in Pagosa Springs, CO?")
print(search_results)

tools = [search]

# ------------------------------------------------------------------
# Using language models
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# Create an agent
# ------------------------------------------------------------------
memory = MemorySaver()
model = ChatOllama(
    model="llama3.2:3b-instruct-q8_0",
    base_url="http://a03a-216-147-123-78.ngrok-free.app",
    temperature=0.2,
    num_ctx=16384,
)
