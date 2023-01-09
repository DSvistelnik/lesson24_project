from DAO import FileDao
from service import FileService
from request import Request
from constans import QUERY


dao = FileDao()
service = FileService(dao)
user_request = Request(service, QUERY)