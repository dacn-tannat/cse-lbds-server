import base64
from fastapi import HTTPException
from app.database.models.problem import Problem
from app.database.models.source_code import SourceCode
from app.database.repositories.source_code import SourceCodeRepository
import httpx
from dotenv import load_dotenv
import os
from jinja2 import Template

from app.database.schemas.source_code import SourceCodeRequestSchema, SourceCodeSubmitResponseSchema

# Load the .env file
load_dotenv('.env')

# Access the variables
jobe_url = os.getenv("JOBE_URL")

class SourceCodeService:
    def __init__(self, db):
        self.__source_code_repository = SourceCodeRepository(db)

    def get_by_id(self, id) -> SourceCode:
        source_code = self.__source_code_repository.get_by_id(id)
        if source_code is None:
            raise HTTPException(status_code=404, detail='Code not found')
        return source_code
    
    def get_all(self):
        return self.__source_code_repository.get_all()
    
    def create(self, source_code):
        self.__source_code_repository.create(source_code)

    async def submit(self, user_source_code: str, problem: Problem) -> SourceCodeSubmitResponseSchema:
        if problem.is_submited_once:
            return await self.submit_once(user_source_code, problem.testcase, problem.template)
        else:
            return await self.submit_multiple(user_source_code, problem.testcase, problem.template)
        
    async def submit_multiple(self, user_source_code: str, testcase: list[dict], template: str) -> SourceCodeSubmitResponseSchema:
        status = 4
        verdict = []
        score = 0
        message = 'Accepted'
        template = Template(template)
        async with httpx.AsyncClient(timeout=20) as client:
            for test in testcase:
                rendered_code = template.render(STUDENT_ANSWER=user_source_code, TEST=test)
                payload = {
                    "run_spec": {
                        "language_id": "cpp",
                        "sourcefilename": "main.cpp",
                        "sourcecode": rendered_code,
                        "input": test.get('input', None),
                        "file_list": [(item["file_id"], item["file_name"]) for item in test.get("file_list", [])],
                        "parameters": {
                            "compileargs": ["-Wno-unused-variable", "-Wno-error=unused-variable"]
                        }
                    }
                }
                try:
                    response = await client.post(f"{jobe_url}/runs", json=payload)
                except Exception as e:
                    print(e)
                    raise HTTPException(status_code=500, detail='Error when sending request to Jobe server')

                if test.get('file_list') and response.status_code == 404:
                # Gọi API put_file để cập nhật dữ liệu trước khi retry
                    for file in test['file_list']:
                        content = base64.b64encode(file['file_content'].encode('utf8')).decode(encoding='UTF-8')
                        put_file_response = await client.put(
                            f"{jobe_url}/files/{file['file_id']}", 
                            json={"file_contents": content }
                        )

                        if put_file_response.status_code != 204:
                            raise HTTPException(status_code=500, detail="Jobe server cannot find input files")

                    response = await client.post(f"{jobe_url}/runs", json=payload)

                    if response.status_code == 404:
                        raise HTTPException(status_code=404, detail="Jobe server cannot upload input files")

                if response.status_code == 200:
                    response_data = response.json()
                    if response_data['outcome'] == 15:
                        if response_data['stdout'] == test['output']:
                            verdict.append({
                                'testcase_id': test['id'],
                                'output': response_data['stdout'],
                                'status': True
                            })
                            score += 1
                        else:
                            status = 1
                            verdict.append({
                                'testcase_id': test['id'],
                                'output': response_data['stdout'],
                                'status': False
                            })
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
                        message = response_data['stdout']
                        break
                    elif response_data['outcome'] == 17:
                        status = 6
                        message = response_data['cmpinfo']
                        break
                    elif response_data['outcome'] == 19:
                        status = 3
                        message = response_data['stderr']
                        break
                else:
                    raise HTTPException(status_code=500, detail='Error when sending request to Jobe server')
        return SourceCodeSubmitResponseSchema(
            status=status,
            verdict=verdict,
            score=score/len(testcase),
            message=message
        )

    async def submit_once(self, user_source_code: str, testcase: list[dict], template: str) -> SourceCodeSubmitResponseSchema:
        status = 4
        verdict = []
        score = 0
        message = 'Accepted'

        template = Template(template)
        rendered_code = template.render(STUDENT_ANSWER=user_source_code, TESTCASES=testcase)

        file_list = [(item["file_id"], item["file_name"]) for test in testcase for item in test.get("file_list", [])]
        input = "\n".join(test.get("input", "") for test in testcase)
        
        payload = {
            "run_spec": {
                "language_id": "cpp",
                "sourcefilename": "main.cpp",
                "sourcecode": rendered_code,
                "file_list": file_list,
                "input": input,
                "parameters": {
                    "compileargs": ["-Wno-unused-variable", "-Wno-error=unused-variable"]
                }
            }
        }

        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response = await client.post(f"{jobe_url}/runs", json=payload)

                if file_list and len(file_list) > 0 and response.status_code == 404:
                    # Gọi API put_file để cập nhật dữ liệu trước khi retry
                    for file in file_list:
                        content = base64.b64encode(file['file_content'].encode('utf8')).decode(encoding='UTF-8')
                        put_file_response = await client.put(
                            f"{jobe_url}/files/{file['file_id']}", 
                            json={"file_contents": content }
                        )

                        if put_file_response.status_code != 204:
                            raise HTTPException(status_code=500, detail="Jobe server cannot find input files")

                    response = await client.post(f"{jobe_url}/runs", json=payload)

                    if response.status_code == 404:
                        raise HTTPException(status_code=404, detail="Jobe server cannot upload input files")
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail='Error when sending request to Jobe server')

        if response.status_code == 200:
            response_data = response.json()
            if response_data['outcome'] == 15:
                # Tách chuỗi bằng dấu phân cách
                outputs = response_data['stdout'].split("#<ab@17943918#@>#\n")

                # So sánh output đã tách với expected_outputs
                for i, (actual, test) in enumerate(zip(outputs, testcase), 1):
                    if actual == test['output']:
                        verdict.append({
                            'testcase_id': test['id'],
                            'output': actual,
                            'status': True
                        })
                        score += 1
                    else:
                        status = 1
                        verdict.append({
                            'testcase_id': test['id'],
                            'output': actual,
                            'status': False
                        })
               
            elif response_data['outcome'] == 11:
                status = 0
                message = response_data['cmpinfo']
            elif response_data['outcome'] == 12:
                status = 7
                message = response_data['stderr']
            elif response_data['outcome'] == 13:
                status = 2
                message = response_data['stderr']
            elif response_data['outcome'] == 17:
                status = 6
                message = response_data['cmpinfo']
            elif response_data['outcome'] == 19:
                status = 3
                message = response_data['stderr']

        return SourceCodeSubmitResponseSchema(
            status=status,
            verdict=verdict,
            score=score/len(testcase),
            message=message
        )
        
    async def create_submission(self, source_code_request: SourceCodeRequestSchema, problem: Problem, user_id: str):
        try:
            output = await self.submit(source_code_request.source_code, problem)
            source_code = SourceCode(
                problem_id=source_code_request.problem_id,
                source_code=source_code_request.source_code,
                status=output.status,
                score=output.score,
                verdict=output.verdict,
                user_id=user_id
            )
            return self.__source_code_repository.create(source_code), output
        except Exception as e:
            raise e