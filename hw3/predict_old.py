import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from utils import get_prompt, get_bnb_config


model_name = "qlora-out_0.6_1_1_1"
bnb_config = get_bnb_config()
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=bnb_config)

data_path = "data/private_test.json"
predict_output = "predictions.json"

with open(data_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

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
with open(predict_output, 'w', encoding='utf-8') as file:
    json.dump(predictions, file, ensure_ascii=False, indent=4)
