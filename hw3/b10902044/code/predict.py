import json
import torch
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
from utils import get_prompt, get_bnb_config
from peft import PeftModel

def main(base_model_path, peft_path, input_file, output_file):
    bnb_config = get_bnb_config()
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    model = AutoModelForCausalLM.from_pretrained(
        base_model_path,
        torch_dtype=torch.bfloat16,
        quantization_config=bnb_config
    )
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)

    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    peft_path = args.peft_path
    model = PeftModel.from_pretrained(model, peft_path)

    # predictions = [
    #     {
    #         "id": item["id"],
    #         "output": (
    #             LLM_response := tokenizer.decode(
    #                 model.generate(**tokenizer(get_prompt(item["instruction"]), return_tensors="pt"))[0],
    #                 skip_special_tokens=True
    #             ).split("ASSISTANT:", 1)[-1].strip()
    #         )
    #     }
    #     for item in data
    # ]


    predictions = []
    for item in data:
        id = item["id"]
        text = item["instruction"]
        # print("input: ", text)

        # Tokenize and generate predictions
        prompt_input = get_prompt(text)
        input_data = tokenizer(prompt_input, return_tensors="pt")
        with torch.no_grad():
            predict_results = model.generate(**input_data)

        # Decode predictions and extract LLM response
        predictions_text = tokenizer.decode(predict_results[0], skip_special_tokens=True)
        LLM_response = predictions_text.split("ASSISTANT:", 1)[-1].strip()

        print("response: ", LLM_response)

        predictions.append({
            "id": id,
            "output": LLM_response
        })

    # Save predictions to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(predictions, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Execute Language Model Predictions")
    parser.add_argument("--base_model_path", required=True, help="Path to the base model")
    parser.add_argument("--peft_path", required=True, help="Path to the fine-tuned model")
    parser.add_argument("--input_file", required=True, help="Path to the input JSON file")
    parser.add_argument("--output_file", required=True, help="Path to the output JSON file")

    args = parser.parse_args()

    main(args.base_model_path, args.peft_path, args.input_file, args.output_file)
