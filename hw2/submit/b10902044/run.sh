#! /usr/bin/env bash

cp $1 .
python transform.py $1

python predict.py \
  --model_name_or_path model_1 \
  --train_file train.json \
  --validation_file test.json \
  --output_dir model_predict/ \
  --per_device_train_batch_size 4 \
  --text_column maintext \
  --summary_column title \
  --num_train_epochs 1 \
  --learning_rate 1e-4 \
  --per_device_eval_batch_size 8 \
  --max_source_length 1024 \
  --max_target_length 128 \
  --num_beams 5 \
  --seed 64

mv submission.jsonl $2
