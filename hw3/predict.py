import json
import torch
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
from utils import get_prompt, get_bnb_config

def main(base_model_path, model_path, input_file, output_file):
    bnb_config = get_bnb_config()
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, quantization_config=bnb_config)

    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    predictions = [
        {
            "id": item["id"],
            "output": (
                LLM_response := tokenizer.decode(
                    model.generate(**tokenizer(get_prompt(item["instruction"]), return_tensors="pt"))[0],
                    skip_special_tokens=True
                ).split("ASSISTANT:", 1)[-1].strip()
            )
        }
        for item in data
    ]

    # Save predictions to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(predictions, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute Language Model Predictions")
    parser.add_argument("--base_model_path", required=True, help="Path to the base model")
    parser.add_argument("--model_path", required=True, help="Path to the fine-tuned model")
    parser.add_argument("--input_file", required=True, help="Path to the input JSON file")
    parser.add_argument("--output_file", required=True, help="Path to the output JSON file")

    args = parser.parse_args()

    main(args.base_model_path, args.model_path, args.input_file, args.output_file)
