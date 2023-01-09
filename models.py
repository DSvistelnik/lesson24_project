from dataclasses import dataclass, field
import marshmallow


@dataclass
class RequestArgs:
    cmd_1: str = field(metadata={'data_key': 'cmd1'})
    cmd_2: str = field(metadata={'data_key': 'cmd2'})
    value_1: str = field(metadata={'data_key': 'value1'})
    value_2: str = field(metadata={'data_key': 'value2'})
    file: str

    class Meta:
        unknown = marshmallow.EXCLUDE
