from typing import Any, Callable, Dict, List, Optional, Tuple

from botocore.client import BaseClient
from botocore.docs.bcdoc.restdoc import DocumentStructure
from botocore.docs.utils import DocumentedShape

class ClientDocumenter:
    _CLIENT_METHODS_FILTERS: List[Callable[..., bool]] = ...
    def __init__(
        self,
        client: BaseClient,
        root_docs_path: str,
        shared_examples: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    def document_client(self, section: DocumentStructure) -> None: ...

class ClientExceptionsDocumenter:
    _USER_GUIDE_LINK: str = ...
    _GENERIC_ERROR_SHAPE: DocumentedShape = ...
    def __init__(self, client: BaseClient, root_docs_path: str) -> None: ...
    def document_exceptions(self, section: DocumentStructure) -> None: ...

class ClientContextParamsDocumenter:
    _CONFIG_GUIDE_LINK: str = ...
    OMITTED_CONTEXT_PARAMS: Dict[str, Tuple[str, ...]] = ...
    def __init__(self, service_name: str, context_params: Any) -> None: ...
    def document_context_params(self, section: DocumentStructure) -> None: ...
