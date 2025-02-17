from typing import Iterator, List

from app.database.models.buggy_position import BuggyPosition
from app.database.repositories.buggy_position import BuggyPositionRepository


class BuggyPositionService:
    def __init__(self, db):
        self.__buggy_position_repository = BuggyPositionRepository(db)
    
    def bug_check(self, prediction_id, position: List[int]) -> Iterator[BuggyPosition]:
        try:
            buggy_position_list = self.__buggy_position_repository.get_by_prediction_id(prediction_id)

            for pos in buggy_position_list:
                if pos.id in position and not pos.is_used:
                    yield self.__buggy_position_repository.update(pos.id, {'is_used': True})
                elif pos.id not in position and pos.is_used:
                    yield self.__buggy_position_repository.update(pos.id, {'is_used': False})
                else:
                    yield pos
        except Exception as e:
            raise e