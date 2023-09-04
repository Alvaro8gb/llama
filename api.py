
import fire
from flask import Flask, jsonify, request, render_template
from llama import Llama
from typing import List, Optional

CKPT_DIR = "llama-2-7b-chat"
TOKENIZER_PATH = "tokenizer.model"
PORT = 8001

def main(
    ckpt_dir: str = CKPT_DIR,
    tokenizer_path: str = TOKENIZER_PATH,
    temperature: float = 0.6,
    top_p: float = 0.9,
    max_seq_len: int = 512,
    max_batch_size: int = 8,
    max_gen_len: Optional[int] = None,
):

    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )

    app = Flask("Api LLama LLM " + ckpt_dir)

    @app.route('/chat',  methods=['POST'])
    def chat_completion():
        data = request.get_json()
        dialogs = data.get('dialogs')

        print(dialogs)

        results = generator.chat_completion(
            dialogs,
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )

        return results

    app.run(host='0.0.0.0', port=PORT)

if __name__ == "__main__":
    fire.Fire(main)
