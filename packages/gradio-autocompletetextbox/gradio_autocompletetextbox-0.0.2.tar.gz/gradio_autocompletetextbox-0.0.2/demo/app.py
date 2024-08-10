
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
