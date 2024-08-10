
import gradio as gr
from app import demo as app
import os

_docs = {'AutocompleteTextbox': {'description': 'Creates a very simple textbox for user to enter string input or display string output.', 'members': {'__init__': {'value': {'type': 'CommandData | Callable | None', 'default': 'None', 'description': 'default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'commands': {'type': 'list[str] | None', 'default': 'None', 'description': None}, 'placeholder': {'type': 'str | None', 'default': 'None', 'description': 'placeholder hint to provide behind textbox.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'component name in interface.'}, 'container': {'type': 'bool', 'default': 'True', 'description': None}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'rtl': {'type': 'bool', 'default': 'False', 'description': 'If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'str | CommandData | dict | None', 'description': 'Expects a {str} returned from function and sets textarea value to it.'}}, 'preprocess': {'return': {'type': 'dict', 'description': 'Passes text value as a {str} into the function.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the AutocompleteTextbox changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the AutocompleteTextbox.'}, 'submit': {'type': None, 'default': None, 'description': 'This listener is triggered when the user presses the Enter key while the AutocompleteTextbox is focused.'}}}, '__meta__': {'additional_interfaces': {'CommandData': {'source': 'class CommandData(GradioModel):\n    command: str | None = None\n    text: str = ""'}}, 'user_fn_refs': {'AutocompleteTextbox': ['CommandData']}}}

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
# `gradio_autocompletetextbox`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

A textbox that supports autocomplete suggestions defined during initialization
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_autocompletetextbox
```

## Usage

```python

import gradio as gr
from matplotlib import container
from gradio_autocompletetextbox import AutocompleteTextbox
from numpy import place


with gr.Blocks() as demo:
    gr.Markdown("## AutocompleteTextbox")

    with gr.Row():
        with gr.Column():
            code = gr.Code()
        with gr.Column(elem_classes=["col_container"]):
            chatbot = gr.Chatbot(bubble_full_width=False, container=False)
            
            input_text = AutocompleteTextbox(
                show_label=False,
                commands=["/start", "/stop", "/help", "/info"],
                placeholder="Type a command...", 
                interactive=True, 
                container=False,
            )
            
            clear = gr.Button("Clear")
            
    ref = gr.Text(container=False, placeholder="Type a command...")

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `AutocompleteTextbox`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["AutocompleteTextbox"]["members"]["__init__"], linkify=['CommandData'])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["AutocompleteTextbox"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes text value as a {str} into the function.
- **As output:** Should return, expects a {str} returned from function and sets textarea value to it.

 ```python
def predict(
    value: dict
) -> str | CommandData | dict | None:
    return value
```
""", elem_classes=["md-custom", "AutocompleteTextbox-user-fn"], header_links=True)




    code_CommandData = gr.Markdown("""
## `CommandData`
```python
class CommandData(GradioModel):
    command: str | None = None
    text: str = ""
```""", elem_classes=["md-custom", "CommandData"], header_links=True)

    demo.load(None, js=r"""function() {
    const refs = {
            CommandData: [], };
    const user_fn_refs = {
          AutocompleteTextbox: ['CommandData'], };
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
