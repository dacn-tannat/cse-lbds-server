from fastapi import HTTPException
from app.database.repositories.source_code import SourceCodeRepository
import httpx
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv('.env.development')

# Access the variables
piston_api_url = os.getenv("PISTON_API_URL")

class SourceCodeService:
    def __init__(self, db):
        self.__source_code_repository = SourceCodeRepository(db)

    def get_by_id(self, id):
        source_code = self.__source_code_repository.get_by_id(id)
        if source_code is None:
            raise HTTPException(status_code=404, detail='Code not found')
        return source_code
    
    def get_all(self):
        return self.__source_code_repository.get_all()

    async def submit(self, source_code, testcase):
        payload = {
            "language": "c++",
            "version": "10.2.0",
            "files": [
                {
                    "name": "main.cpp",
                    "content": source_code
                }
            ],
            "stdin": "",
            "args": testcase[0]['input'],
            "compile_timeout": 10000,
            "run_timeout": 3000,
            "compile_memory_limit": -1,
            "run_memory_limit": -1
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(piston_api_url, json=payload)
    
        # Kiểm tra xem yêu cầu có thành công không
        if response.status_code == 200:
            response_data = response.json()
            if response_data["run"]["exit_code"] == 0:
                return response_data
        else:
            return {"error": "Failed to fetch data from external API"}
        