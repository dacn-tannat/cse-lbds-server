from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.database.repositories.source_code import SourceCodeRepository
import httpx
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv('.env.development')

# Access the variables
jobe_url = os.getenv("JOBE_URL") + 'runs'

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
    
    def create(self, source_code, db: Session):
        db.add(source_code)
        db.commit()
        db.refresh(source_code)
        return source_code

    async def submit(self, source_code, testcase):
        status = 4
        verdict = []
        score = 0
        message = 'Accepted'
        for test in testcase:
            payload = {
                "run_spec": {
                    "language_id": "cpp",
                    "sourcefilename": "main.cpp",
                    "sourcecode": source_code,
                    "input": test['input'],
                }
            }

            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(jobe_url, json=payload)
            except Exception as e:
                print(e)
                raise HTTPException(status_code=500, detail='Error when sending request to Jobe API')
    
            if response.status_code == 200:
                response_data = response.json()
                if response_data['outcome'] == 15:
                    if response_data['stdout'] == test['output']:
                        verdict.append({
                            "testcase_id": test['id'],
                            "status": True
                        })
                        score += 1
                    else:
                        status = 1
                        verdict.append({
                            "testcase_id": test['id'],
                            "status": False
                        })
                    continue
                elif response_data['outcome'] == 11:
                    status = 0
                    message = response_data['cmpinfo']
                    break
                elif response_data['outcome'] == 12:
                    status = 7
                    message = response_data['stderr']
                    break
                elif response_data['outcome'] == 13:
                    status = 2
                    message = response_data['stderr']
                    break
                elif response_data['outcome'] == 17:
                    status = 6
                    message = response_data['cmpinfo']
                    break
                elif response_data['outcome'] == 19:
                    status = 3
                    message = response_data['stderr']
                    break
            print('Error when sending request to Jobe API')
            print(response.text)
            return HTTPException(status_code=500, detail='Error when sending request to Jobe API')

        return {
            "status": status,
            "verdict": verdict,
            "score": score,
            "message": message
        }
        
        