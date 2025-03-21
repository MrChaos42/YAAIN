import ipywidgets as widgets
from IPython.display import display, clear_output
import random

class Agent:
    def __init__(self, name, temperature=1.0):
        self.name = name
        self.temperature = temperature
        self.memory = []

    def process_message(self, message):
        self.memory.append(f"{self.name}: Received '{message}'")
        response = self.generate_response(message)
        self.memory.append(f"{self.name}: Responded '{response}'")
        return response

    def generate_response(self, message):
        # Simplified response generation with temperature effect
        if random.random() > self.temperature:
            return f"Understood: {message} (from {self.name})"
        else:
            return f"Thinking... {message}... (from {self.name})"

# UI Setup
left_output = widgets.Output()
right_output = widgets.Output()
center_output = widgets.Output()
chat_input = widgets.Text(description="Chat:")
send_button = widgets.Button(description="Send")

# Agent Initialization
left_brain = Agent("Left", temperature=0.8)
right_brain = Agent("Right", temperature=1.2)
center_brain = Agent("Center", temperature=1.0)

# Layout
ui = widgets.VBox([
    widgets.HBox([left_output, right_output]),
    center_output,
    widgets.HBox([chat_input, send_button])
])

display(ui)

def send_message(button):
    message = chat_input.value
    chat_input.value = ""

    with center_output:
        clear_output()
        print(f"User: {message}")

        # Center Brain Logic
        left_response = left_brain.process_message(message)
        right_response = right_brain.process_message(message)
        center_response = center_brain.process_message(f"Left: {left_response}, Right: {right_response}")

        print(f"Center to Left: {left_response}")
        print(f"Center to Right: {right_response}")
        print(f"Center Response: {center_response}")

    # Display Agent Memories
    with left_output:
        clear_output()
        for mem in left_brain.memory:
            print(mem)

    with right_output:
        clear_output()
        for mem in right_brain.memory:
            print(mem)

send_button.on_click(send_message)
