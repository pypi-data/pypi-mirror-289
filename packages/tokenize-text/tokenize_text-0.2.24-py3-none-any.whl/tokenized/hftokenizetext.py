import subprocess
import json


class TokenizerHandler:
    def __init__(self, input_file='tokenized/dist/inputdata', output_file='tokenized/dist/outputdata', script_name='tokenized/dist/protected_function.py'):
        self.input_file = input_file
        self.output_file = output_file
        self.script_name = script_name

    def write_to_input_file(self, text):
        with open(self.input_file, 'w', encoding='utf-8') as infile:
            infile.write(text)

    def execute_script(self):
        try:
            subprocess.run(['python', self.script_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing script: {e}")

    def read_output_file(self):
        try:
            with open(self.output_file, 'r', encoding='utf-8') as outfile:
                data = outfile.read()
                # Convert the string back to a list
                inputs_list = json.loads(data)
                return inputs_list
        except FileNotFoundError:
            print("Output file not found.")
            return None
        except json.JSONDecodeError:
            print("Error decoding JSON from the output file.")
            return None

    def get_tokenized_inputs(self, text):
        try:
            # Step 1: Write the text to the input file
            self.write_to_input_file(text)

            # Step 2: Execute the protected_function.py script
            self.execute_script()

            # Step 3: Read the output from the output file
            tokenized_output = self.read_output_file()

            return tokenized_output

        except Exception as e:
            print("Error:", e)
            return None


