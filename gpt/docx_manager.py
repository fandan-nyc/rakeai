import docx
import config

class docx_manager:
    def __init__(self, input_file_path, output_file_path):
        self.output_file_path = output_file_path
        self.input_doc = docx.Document(input_file_path)

    def fine_tune(self, gpt_client, prompt_path):
        count = 0
        chunk_to_tune = None
        for para in self.input_doc.paragraphs:
            if count >= 1: # does not modify the title
                chunk = para.text
                para_word_count = self.word_count(chunk)
                print(para_word_count)
                if(para_word_count < config.skip_small_para_size):
                    print(chunk)
                    # does not change the sub titles etc
                    continue
                if( para_word_count > 1900):
                    print("warning: this is too long")
                new_chunk = gpt_client.fix_grammer(chunk, prompt_path)
                para.text = new_chunk
            count += 1
        self.input_doc.save(self.output_file_path)

    def word_count(self, data):
        return len(data.split(" "))
