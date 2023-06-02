from pydantic import BaseModel


class Header(BaseModel):
    need_rewrite: str
    sending_process_status: str
    message_type: str
    processing_type: str
    receiver_system: str
    message_id: str
    sender_system: str

class MessageData(BaseModel):
    data: str

class Message(BaseModel):
    header: Header
    message: MessageData

