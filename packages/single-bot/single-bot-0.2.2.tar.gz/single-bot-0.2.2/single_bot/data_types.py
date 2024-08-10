from typing import TypedDict, Optional


class Metadata(TypedDict):
    message_id: Optional[str]
    messenger_name: str
    messenger_user_id: str
    username: Optional[str]
    messenger_chat_id: Optional[str]
    reply_to_message_id: Optional[str]
    authorized: Optional[bool]

class Message(TypedDict):
    metadata: Metadata
    text: str
    content: Optional[list]


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
