
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

