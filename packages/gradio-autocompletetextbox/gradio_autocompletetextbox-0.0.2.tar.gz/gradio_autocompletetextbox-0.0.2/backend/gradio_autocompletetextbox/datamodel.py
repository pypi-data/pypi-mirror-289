from gradio.data_classes import GradioModel

class CommandData(GradioModel):
    command: str | None = None
    text: str = ""
