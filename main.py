import click
from functions import add


@click.command()
@click.option("--a", default=0, help="first integer to add")
@click.option("--b", default=0, help="second integer to add")
def arithmetic_add(a, b):
    """Simple program that adds two numbers
    usage python main.py --a 5 --b 6.
    """
    result = add(a, b)
    click.echo(f"result is {result}!")


if __name__ == "__main__":
    arithmetic_add()


# from transformers import pipeline
# import gradio as gr
# import click

# model = pipeline('summarization', model='t5-small', max_length=30)

# def predict(prompt):
#     summary = model(prompt)[0]['summary_text']
#     return summary

# def run_on_gradio():
#     with gr.Blocks() as demo:
#         textbox = gr.Textbox(placeholder="Enter Text block to summarise", lines=4)
#         gr.Interface(fn=predict, inputs=textbox, outputs="text")
#     demo.launch()
