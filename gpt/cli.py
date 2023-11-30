import argparse
import util

class academic_gpt:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "academic_gpt_cli")
        parser.add_argument("-p", "--prompt", default = f"/Users/{util.get_user()}/Downloads/prompt.txt")
        parser.add_argument("-s", "--source", default = f"/Users/{util.get_user()}/Downloads/sample.docx")
        parser.add_argument("-d", "--destination", default = f"/Users/{util.get_user()}/Downloads/output.docx")
        self.args = parser.parse_args()

    def get_prompt_path(self):
        return self.args.prompt

    def get_source_path(self):
        return self.args.source

    def get_destination_path(self):
        return self.args.destination


