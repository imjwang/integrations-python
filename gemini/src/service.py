from restack_ai import Restack
from pydantic import BaseModel


class GeminiServiceOptions(BaseModel):
    rate_limit: int

class RestackWrapper(BaseModel):
    client: Restack
    
    class Config:
        arbitrary_types_allowed = True


class GeminiServiceInput(BaseModel):
    client: RestackWrapper
    options: GeminiServiceOptions


async def gemini_service(input: GeminiServiceInput):
    return await input.client.start_service(
        functions=[],
        options=input.options
    )

if __name__ == "__main__":
    gemini_service(
        client=Restack(),
        options=GeminiServiceOptions(rate_limit=100000)
    )
