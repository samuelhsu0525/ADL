## train:
train the model with qlora.yml
```bash
python -m axolotl.cli.train qlora.yml
```

## Calculate ppl
use ppl.py to caculate Mean perplexity
```bash
python ppl.py --base_model_path Taiwan-LLM-7B-v2.0-chat --peft_path qlora-out_0.6_1_1_1/ --test_data_path data/public_test.json
```

## predict:
use predict.py to predict the private test data
```bash
python predict.py --base_model_path Taiwan-LLM-7B-v2.0-chat --model_path qlora-out_0.6_1_1_1/ --input_file data/private_test.json --output_file predict.json
```