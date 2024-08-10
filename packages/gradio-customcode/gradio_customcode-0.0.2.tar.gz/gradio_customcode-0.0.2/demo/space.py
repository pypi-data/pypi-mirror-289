
import gradio as gr
from app import demo as app
import os

_docs = {'CustomCode': {'description': 'Creates a code editor for viewing code (as an output component), or for entering and editing code (as an input component).', 'members': {'__init__': {'value': {'type': 'str | Callable | tuple[str] | None', 'default': 'None', 'description': 'Default value to show in the code editor. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'language': {'type': 'Literal[\n        "python",\n        "java",\n        "c",\n        "cpp",\n        "markdown",\n        "json",\n        "html",\n        "css",\n        "javascript",\n        "typescript",\n        "yaml",\n        "dockerfile",\n        "shell",\n        "r",\n        "sql",\n        "sql-msSQL",\n        "sql-mySQL",\n        "sql-mariaDB",\n        "sql-sqlite",\n        "sql-cassandra",\n        "sql-plSQL",\n        "sql-hive",\n        "sql-pgSQL",\n        "sql-gql",\n        "sql-gpSQL",\n        "sql-sparkSQL",\n        "sql-esper",\n    ]\n    | None', 'default': 'None', 'description': 'The language to display the code as. Supported languages listed in `gr.Code.languages`.'}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'lines': {'type': 'int', 'default': '5', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'Whether user should be able to enter code or only view it.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'tuple[str] | str | dict | None', 'description': 'Expects a `str` of code or a single-element `tuple`: (filepath,) with the `str` path to a file containing the code.'}}, 'preprocess': {'return': {'type': 'CodeData', 'description': 'Passes the code entered as a `str`.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the CustomCode changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the CustomCode.'}, 'focus': {'type': None, 'default': None, 'description': 'This listener is triggered when the CustomCode is focused.'}, 'blur': {'type': None, 'default': None, 'description': 'This listener is triggered when the CustomCode is unfocused/blurred.'}}}, '__meta__': {'additional_interfaces': {'CodeData': {'source': 'class CodeData(GradioModel):\n    code: str = ""\n    selected_code: SelectedCode = SelectedCode()\n    diff: str = ""', 'refs': ['SelectedCode']}, 'SelectedCode': {'source': 'class SelectedCode(GradioModel):\n    start: int = 0\n    end: int = 0\n    text: str = ""'}}, 'user_fn_refs': {'CustomCode': ['CodeData']}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_customcode`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

Custom Code component that adds features to enhance usage with LLMs
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_customcode
```

## Usage

```python
import json
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

with gr.Blocks() as demo:
    gr.Markdown("## Custom Code Component")
    gr.Markdown("This demo shows how to use the `CustomCode` component to create a code editor with syntax highlighting and line numbering. You can also select a part of the code and click the `Generate Diff` button to see the diff between the selected code and the text input. Java syntax support has also been added")
    with gr.Row():
        with gr.Column():
            txt = gr.Text(container=False, placeholder="New code to add")
            with gr.Row():
                apply_btn = gr.Button("Generate Diff")
                accept_btn = gr.Button("Accept", variant='secondary')
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
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `CustomCode`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["CustomCode"]["members"]["__init__"], linkify=['CodeData', 'SelectedCode'])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["CustomCode"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the code entered as a `str`.
- **As output:** Should return, expects a `str` of code or a single-element `tuple`: (filepath,) with the `str` path to a file containing the code.

 ```python
def predict(
    value: CodeData
) -> tuple[str] | str | dict | None:
    return value
```
""", elem_classes=["md-custom", "CustomCode-user-fn"], header_links=True)




    code_CodeData = gr.Markdown("""
## `CodeData`
```python
class CodeData(GradioModel):
    code: str = ""
    selected_code: SelectedCode = SelectedCode()
    diff: str = ""
```""", elem_classes=["md-custom", "CodeData"], header_links=True)

    code_SelectedCode = gr.Markdown("""
## `SelectedCode`
```python
class SelectedCode(GradioModel):
    start: int = 0
    end: int = 0
    text: str = ""
```""", elem_classes=["md-custom", "SelectedCode"], header_links=True)

    demo.load(None, js=r"""function() {
    const refs = {
            CodeData: ['SelectedCode'], 
            SelectedCode: [], };
    const user_fn_refs = {
          CustomCode: ['CodeData'], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
