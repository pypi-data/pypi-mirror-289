
import gradio as gr
from app import demo as app
import os

_docs = {'gradio_datetime': {'description': 'Component to select a date and (optionally) a time.', 'members': {'__init__': {'value': {'type': 'float | str | datetime.datetime | None', 'default': 'None', 'description': 'default value for datetime.'}, 'include_time': {'type': 'bool', 'default': 'True', 'description': 'If True, the component will include time selection. If False, only date selection will be available.'}, 'type': {'type': '"timestamp" | "datetime" | "string"', 'default': '"timestamp"', 'description': 'The type of the value. Can be "timestamp", "datetime", or "string". If "timestamp", the value will be a number representing the start and end date in seconds since epoch. If "datetime", the value will be a datetime object. If "string", the value will be the date entered by the user.'}, 'timezone': {'type': 'str | None', 'default': 'None', 'description': 'The timezone to use for timestamps, such as "US/Pacific" or "Europe/Paris". If None, the timezone will be the local timezone.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'info': {'type': 'str | None', 'default': 'None', 'description': 'additional component description.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}}, 'postprocess': {'value': {'type': 'float | datetime.datetime | str | None', 'description': 'Expects a tuple pair of datetimes.'}}, 'preprocess': {'return': {'type': 'str | float | datetime.datetime | None', 'description': 'Passes text value as a {str} into the function.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the gradio_datetime changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'submit': {'type': None, 'default': None, 'description': 'This listener is triggered when the user presses the Enter key while the gradio_datetime is focused.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'gradio_datetime': []}}}

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
# `gradio_gradio_datetime`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.2%20-%20orange">  
</div>

datetime for safari
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_gradio_datetime
```

## Usage

```python

import gradio as gr
from gradio_gradio_datetime import gradio_datetime


example = gradio_datetime().example_value()

demo = gr.Interface(
    lambda x:x,
    gradio_datetime(),  # interactive version of your component
    gradio_datetime(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()


```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `gradio_datetime`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["gradio_datetime"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["gradio_datetime"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes text value as a {str} into the function.
- **As output:** Should return, expects a tuple pair of datetimes.

 ```python
def predict(
    value: str | float | datetime.datetime | None
) -> float | datetime.datetime | str | None:
    return value
```
""", elem_classes=["md-custom", "gradio_datetime-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          gradio_datetime: [], };
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
