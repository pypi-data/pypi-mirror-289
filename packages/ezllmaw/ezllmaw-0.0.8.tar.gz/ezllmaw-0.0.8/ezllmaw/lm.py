from pydantic import Field, BaseModel
import requests

headers={
    "Content-Type": "application/json",
    }

class OllamaLLM(BaseModel):
    """
    Ref1: https://dev.to/jayantaadhikary/using-the-ollama-api-to-run-llms-and-generate-responses-locally-18b7
    
    Ref2: https://medium.com/@shmilysyg/setup-rest-api-service-of-ai-by-using-local-llms-with-ollama-eb4b62c13b71

    Ref3: https://github.com/ollama/ollama/blob/main/docs/api.md

    Ref4: http://localhost:11434/api/generate
    
    Ref5: http://localhost:11434/api/embed
    """
    base_url:str = Field(default="http://localhost:11434", description="end point")
    model:str = Field(default="llama3.1", description="model name")
    stream:bool = Field(default=False)
    temperature:float = Field(default=0)
    type:str = Field(default="gen", description="gen, chat, embeddings")

    def __call__(self, request):
        return self.forward(request)
    
    def forward(self, request):
        payload = {
            "model": self.model,
            "stream": self.stream,
            "options": {
                "temperature": self.temperature
            },
        }
        if self.type=="gen":
            payload.update({"prompt": request})
        if self.type=="embeddings":
            # request can be a string or list of string.
            payload.update({"input": request})
        
        if self.type=="gen":
            url = f"{self.base_url}/api/generate"
        elif self.type=="embeddings":
            url = f"{self.base_url}/api/embed"
        else:
            raise ValueError("Other type of models are not implmented yet.")
        
        response = requests.post(url=url, headers=headers, json=payload)
        response = response.json()
        
        if self.type=="gen":
            return response["response"] 
        elif self.type=="embeddings":
            return response["embeddings"]
        else:
            raise ValueError("Other type of models are not implmented yet.")