from pydantic import BaseModel

class Header(BaseModel):
    processing_type: str
    sending_process_status: bool
    sender_system: str
    message_type: str
    message_id: str
    content_type: str
    properties: str

class Message(BaseModel):
    header: Header
    message: str
