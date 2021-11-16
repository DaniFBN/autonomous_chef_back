from types import TracebackType
from typing import Any, Dict, List, Optional, Union
from graphql import GraphQLError


class NotFoundGqlException(GraphQLError):
    __message = "Object doesn't exist"


    def __init__(self, message: str = None, nodes: Any = None, stack: Optional[TracebackType] = None, source: Optional[Any] = None, positions: Optional[Any] = None, locations: Optional[Any] = None, path: Union[List[Union[int, str]], List[str], None] = None, extensions: Optional[Dict[str, Any]] = None) -> None:

        message = NotFoundGqlException.__message

        super().__init__(message, nodes=nodes, stack=stack, source=source,
                         positions=positions, locations=locations, path=path, extensions=extensions)
