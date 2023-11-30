from cli import academic_gpt
from gpt_client import gpt_client
from docx_manager import docx_manager
import util

if __name__ == "__main__":
    gpt_cli = academic_gpt()
    gpt_client = gpt_client()
    docx_manager = docx_manager(gpt_cli.get_source_path(), gpt_cli.get_destination_path())
    docx_manager.fine_tune(gpt_client, gpt_cli.get_prompt_path())
