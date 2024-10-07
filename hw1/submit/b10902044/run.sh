#! /usr/bin/env bash
#python3 transfer_train.py
cp $1 $2 .

python transform.py test.json

python run_swag_no_trainer.py --train_file train_p1.json --validation_file transformed_test.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1 --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path model_p1_shi_221_s64

python convert.py test.json

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_22/ --max_seq_length 512

mv output.csv output_22.csv

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_23/ --max_seq_length 512

mv output.csv output_23.csv

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_25/ --max_seq_length 512

mv output.csv output_25.csv

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_28/ --max_seq_length 512

mv output.csv output_28.csv

python run_swag_no_trainer.py --train_file train_p1.json --validation_file transformed_test.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1 --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path model_p1_shi_221

python convert.py test.json

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_27/ --max_seq_length 512

mv output.csv output_27.csv

python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_29/ --max_seq_length 512

mv output.csv output_29.csv

python blend.py

python final.py $3
