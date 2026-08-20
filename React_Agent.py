from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from numpy.f2py.crackfortran import verbose

load_dotenv()
llm = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")

search_tool = TavilySearch(search_depth = "basic")

tools = [search_tool]

agent = create_agent(
    model=llm,
    tools=tools
    )

result = agent.invoke({
    "messages": [
        ("user", "Give me a funny tweet about what is the weather in Sehore")
    ]
})
print(result.content)