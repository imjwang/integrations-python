from openai import Model, ChatCompletion
from openai.types.chat import ChatCompletion
from pydantic import BaseModel, Optional, List
from ...utils.client import openai_client
from ...utils.cost import Price

class OpenAIChatInput(BaseModel):
    user_content: str
    system_content: Optional[str] = None
    model: Optional[Model] = None
    json_schema: dict = {
        "name": str,
        "description": str
    }
    price: Optional[Price] = None
    api_key: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    n: Optional[int] = None
    stop: Optional[List[str]] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None

class OpenAIChatOutput(BaseModel):
    result: ChatCompletion
    cost: float


async def openai_chat_completion_base(input: OpenAIChatInput) -> OpenAIChatOutput:
    client = openai_client(input.api_key)

    messages = []

    if input.system_content:
        messages.append({"role": "system", "content": input.system_content})

    messages.append({"role": "user", "content": input.user_content})

    chat_params = {
        "model": input.model or "gpt-4o-mini",
        "messages": messages,
    }

    if input.max_tokens is not None:
        chat_params["max_tokens"] = input.max_tokens
    if input.temperature is not None:
        chat_params["temperature"] = input.temperature
    if input.top_p is not None:
        chat_params["top_p"] = input.top_p
    if input.n is not None:
        chat_params["n"] = input.n
    if input.stop is not None:
        chat_params["stop"] = input.stop
    if input.presence_penalty is not None:
        chat_params["presence_penalty"] = input.presence_penalty
    if input.frequency_penalty is not None:
        chat_params["frequency_penalty"] = input.frequency_penalty

    print("Calling OpenAI Chat Completion", meta={"params": chat_params})

    result = await client.chat.completions.create(**chat_params)

    print("OpenAI Chat Completion Result", meta={"result": result})

    cost = 0

    return OpenAIChatOutput(result=result, cost=cost)

if __name__ == "__main__":

    test_inputs = [
        OpenAIChatInput(
            user_content="Hello, how are you?",
            system_content="You are a helpful assistant.",
            model="gpt-4o-mini",
        ),
        OpenAIChatInput(
            user_content="Hello, how are you?",
            system_content="You are a helpful assistant.",
            model="gpt-4o-mini",
        ),
    ]

    for i, input in enumerate(test_inputs, 1):
        print(f"\nTest {i}:")
        print(f"Input: {input}")
        result = openai_chat_completion_base(input)
        print(f"Response: {result}")
        print("-" * 50)


