from langchain.chat_models import init_chat_model


def get_model(model_type):
    return LLMService(model_type)

class LLMService:

    def __init__(self, model_type, *args, **kwargs):
        self.model_type = model_type or "gpt-3.5-turbo"
        ...
