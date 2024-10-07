#! /usr/bin/env bash
# ${1}: path to the Taiwan-LLaMa checkpoint folder
# ${2}: path to the adapter_checkpoint downloaded under your folder
# ${3}: path to the input file (.json)
# ${4}: path to the output file (.json)

# python ppl.py --base_model_path $1 --peft_path $2 --test_data_path $3

python predict.py --base_model_path $1 --peft_path $2 --input_file $3 --output_file $4