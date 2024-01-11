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
    history_messages = req.state.session_messages[session_id]
    model = OpenAI()
    answer = model.ask(question, history_messages)
    return answer


