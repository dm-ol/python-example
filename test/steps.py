# Import the base64 module
import base64

# Define an array of strings representing the steps in a software development lifecycle
steps = ["plan", "code", "test", "delivery", "deploy", "monitor"]

# Loop through each step in the array and perform an operation
for step in steps:
    # Encode the current step in base64 format and print it
    step_b64 = base64.b64encode(step.encode()).decode()
    print("b'" + step_b64 + "'")
