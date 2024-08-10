from gradio.data_classes import GradioModel

class SelectedCode(GradioModel):
    start: int = 0
    end: int = 0
    text: str = ""

class CodeData(GradioModel):
    code: str = ""
    selected_code: SelectedCode = SelectedCode()
    diff: str = ""
