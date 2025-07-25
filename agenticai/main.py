from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

search_tool = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search_tool.run,
        description="Search current events and general knowledge"
    )
]

# Load API key from environment
openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_key)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

@app.post("/ask")
async def ask_agent(request: QueryRequest):
    try:
        response = agent.run(request.query)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
