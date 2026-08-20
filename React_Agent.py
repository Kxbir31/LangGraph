from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
from numpy.f2py.crackfortran import verbose

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")

search_tool = TavilySearchResults(search_depth = "basic")

tools = [search_tool]

agent = create_agent(tools=tools , llm = llm, agent = "Zero - Shot react description", verbose = True)

