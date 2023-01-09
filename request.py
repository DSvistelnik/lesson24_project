from service import FileService
from typing import Dict
from models import RequestArgs

class Request:

    def __init__(self, service: FileService, mapper: Dict[str, str]) -> None:
        self.service = service
        self.mapper = mapper

    def execute(self, request_args: RequestArgs) -> str:

        task_1, value_1, task_2, value_2 = self._create(request_args)

        getattr(self.service, task_1)(value_1)
        getattr(self.service, task_2)(value_2)

        return self.service.get_result()

    def _create(self, request_args: RequestArgs) -> tuple:

        self.service.add_new_file(request_args.file)

        task_1 = self.mapper[request_args.cmd_1]
        task_2 = self.mapper[request_args.cmd_2]
        value_1 = request_args.value_1
        value_2 = request_args.value_2

        return task_1, value_1, task_2, value_2

