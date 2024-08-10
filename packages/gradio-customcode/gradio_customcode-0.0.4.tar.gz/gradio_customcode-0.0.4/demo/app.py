import json
import time
import gradio as gr
from gradio_customcode import CustomCode
from sympy import cancel

def process_code(code_input):
    print(f"PROCESS CODE FN: {code_input}")
    return code_input.__dict__

def show_diff(text_input, code_data):
    code = code_data.code
    start, end = code_data.selected_code.start, code_data.selected_code.end
    modified_code = code[:start] + text_input + code[end:]
    return_dict = {"code": code, "diff": modified_code}
    print(return_dict)
    return return_dict

def show_diff_stream(text_input, code_data):
    code = code_data.code
    start, end = code_data.selected_code.start, code_data.selected_code.end
    partial = ""
    for char in text_input:
        partial += char if char else ""
        modified_code = code[:start] + partial + code[end:]
        yield {"code": code, "diff": modified_code}
        # Sleep for a short duration to simulate streaming
        time.sleep(0.05)

with gr.Blocks() as demo:
    gr.Markdown("## Custom Code Component")
    gr.Markdown("This demo shows how to use the `CustomCode` component to create a code editor with syntax highlighting and line numbering. You can also select a part of the code and click the `Generate Diff` button to see the diff between the selected code and the text input. Java syntax support has also been added")
    with gr.Row():
        with gr.Column():
            txt = gr.Text(container=False, placeholder="New code to add")
            with gr.Row():
                apply_btn = gr.Button("Generate Diff")
                stream_diff_btn = gr.Button("Stream Diff")
                accept_btn = gr.Button("Accept", variant='primary')
                cancel_btn = gr.Button("Cancel", variant='stop')

        with gr.Column():
            code = CustomCode(language='python', interactive=True)
            lang = gr.Dropdown(choices=CustomCode.languages, value='python', label='Language')

    gr.Markdown("The way we generate diffs is by modifying the value of the component. "
                "Unlike the standalone `Code` component, the `CustomCode` component's value is a data model defined like so: \n"
                "```python\nclass SelectedCode(GradioModel):\n\tstart: int = 0\n\tend: int = 0\n\ttext: str = \"\"\n\n"
                "class CodeData(GradioModel):\n\tcode: str = \"\"\n\tselected_code: SelectedCode = SelectedCode()\n\tdiff: str = \"\"\n```\n"
                "When using this component as an input to some function, be sure to properly access the fields of `CodeData`.\n"
                "When using it as an output component, you can be a bit more flexible. If you just pass a string, it will behave like the standard `gr.Code` component. "
                "However, to generate the diff view, you must pass a dictionary with keys 'code' (for the original code) and 'diff' (for the new code)."
                "The diff view will be automatically generated, and will no longer be interactive regardless of the initial setting."
                "The diff view can be exited by either passing a string as input to the component, or a dictionary where the value of 'diff' is an empty string or None"
    )

    # TEST STREAMING DIFF
    stream_diff_btn.click(
        fn=show_diff_stream,
        inputs=[txt, code],
        outputs=[code]
    )

    codeout = gr.JSON(label="Processed Code Output")

    # Update JSON and text output when button is clicked
    code.change(
        fn=lambda code: code.__dict__,
        inputs=[code],
        outputs=[codeout]
    )

    lang.change(
        lambda lang: CustomCode(language=lang),
        inputs=[lang],
        outputs=[code]
    )
    
    apply_btn.click(
        fn=show_diff,
        inputs=[txt, code],
        outputs=[code]
    )
    accept_btn.click(
        fn=lambda code: code.diff,
        inputs=[code],
        outputs=[code]
    )

    cancel_btn.click(
        fn=lambda code: code.code,
        inputs=[code],
        outputs=[code]
    )

if __name__ == "__main__":
    demo.launch()