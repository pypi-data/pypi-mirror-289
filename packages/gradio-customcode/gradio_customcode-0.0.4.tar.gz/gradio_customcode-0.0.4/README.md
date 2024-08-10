---
tags: [gradio-custom-component, Code, code, codebox, llm, coding]
title: gradio_customcode
short_description: Custom Code component that adds features to enhance usage with LLMs
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_customcode`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  

Custom Code component that adds features to enhance usage with LLMs

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

## `CustomCode`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | tuple[str] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Default value to show in the code editor. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>language</code></td>
<td align="left" style="width: 25%;">

```python
Literal[
        "python",
        "java",
        "c",
        "cpp",
        "markdown",
        "json",
        "html",
        "css",
        "javascript",
        "typescript",
        "yaml",
        "dockerfile",
        "shell",
        "r",
        "sql",
        "sql-msSQL",
        "sql-mySQL",
        "sql-mariaDB",
        "sql-sqlite",
        "sql-cassandra",
        "sql-plSQL",
        "sql-hive",
        "sql-pgSQL",
        "sql-gql",
        "sql-gpSQL",
        "sql-sparkSQL",
        "sql-esper",
    ]
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The language to display the code as. Supported languages listed in `gr.Code.languages`.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.</td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
Component | Sequence[Component] | set[Component] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.</td>
</tr>

<tr>
<td align="left"><code>lines</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>5</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Whether user should be able to enter code or only view it.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the CustomCode changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the CustomCode. |
| `focus` | This listener is triggered when the CustomCode is focused. |
| `blur` | This listener is triggered when the CustomCode is unfocused/blurred. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes the code entered as a `str`.
- **As input:** Should return, expects a `str` of code or a single-element `tuple`: (filepath,) with the `str` path to a file containing the code.

 ```python
 def predict(
     value: CodeData
 ) -> tuple[str] | str | dict | None:
     return value
 ```
 

## `CodeData`
```python
class CodeData(GradioModel):
    code: str = ""
    selected_code: SelectedCode = SelectedCode()
    diff: str = ""
```

## `SelectedCode`
```python
class SelectedCode(GradioModel):
    start: int = 0
    end: int = 0
    text: str = ""
```
