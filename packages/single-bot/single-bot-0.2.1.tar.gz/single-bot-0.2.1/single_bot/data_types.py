from typing import TypedDict, Optional


class Metadata(TypedDict):
    messenger_name: str
    messenger_user_id: str
    messenger_chat_id: Optional[str]
    reply_to_message_id: Optional[str]
    authorized: Optional[bool]

class Message(TypedDict):
    metadata: Metadata
    text: str
    files: Optional[dict]


class MessengerRequest(TypedDict):
    metadata: Metadata
    message: Message


class InputField(TypedDict):
    node: callable
    validator: Optional[callable]
    description: Optional[str]


class InputTemplate(TypedDict):
    input_field: Optional[InputField]
    buttons: dict


class UserStateDict(TypedDict):
    input_template: InputTemplate
    values: Optional[dict]


class RequestedData(TypedDict): ...


class History(TypedDict):
    node: str
    position_in_node: int
    requested_values: dict
    question: str
    answer: str
