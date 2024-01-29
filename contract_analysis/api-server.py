from fastapi import FastAPI, Request
from smart_contract_crew import SmartContractCrew
from openai import OpenAI


app = FastAPI()

@app.post("/ask")
async def ask(question: str):
    crew = SmartContractCrew()
    result = crew.run(question)
    return result

@app.post("sessions/{session_id}/ask")
async def ask(req: Request, question: str, session_id: str):
    # MOCK for now
    session = req.state.sessions[session_id]
    model = OpenAI()
    # TODO: for a very long chat, shorten the messages with MemGpt
    answer = model.ask(question, session.messages)
    return answer


