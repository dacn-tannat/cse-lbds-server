from typing import Iterator, List

from app.database.models.buggy_position import BuggyPosition
from app.database.repositories.buggy_position import BuggyPositionRepository


class BuggyPositionService:
    def __init__(self, db):
        self.__buggy_position_repository = BuggyPositionRepository(db)
    
    def token_error(self, prediction_id, position: List[int]) -> Iterator[BuggyPosition]:
        try:
            buggy_position_list = self.__buggy_position_repository.get_by_prediction_id(prediction_id)

            for pos in buggy_position_list:
                if pos.position in position and not pos.is_token_error:
                    yield self.__buggy_position_repository.update(pos.id, prediction_id, {'is_token_error': True})
                elif pos.position not in position and pos.is_token_error:
                    yield self.__buggy_position_repository.update(pos.id, prediction_id, {'is_token_error': False})
                else:
                    yield pos
        except Exception as e:
            raise e
        
    def suggestion_useful(self, prediction_id, position: List[int]) -> Iterator[BuggyPosition]:
        try:
            buggy_position_list = self.__buggy_position_repository.get_by_prediction_id(prediction_id)

            for pos in buggy_position_list:
                if pos.position in position and not pos.is_suggestion_useful:
                    yield self.__buggy_position_repository.update(pos.id, prediction_id, {'is_suggestion_useful': True})
                elif pos.position not in position and pos.is_suggestion_useful:
                    yield self.__buggy_position_repository.update(pos.id, prediction_id, {'is_suggestion_useful': False})
                else:
                    yield pos
        except Exception as e:
            raise e