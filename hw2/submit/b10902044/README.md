## prepare the file
use transform.py to let train/test file convert to fit the predict model

```bash
python transform.py $1
```

## train:
train the model
```bash
python run_summarization.py \
  --model_name_or_path google/mt5-small \
  --train_file data/train.json \
  --test_file data/public.json \
  --output_dir model_1/ \
  --per_device_train_batch_size 4 \
  --text_column maintext\
  --summary_column title\
  --num_train_epochs 5 \
  --learning_rate 1e-4 \
  --save_steps 1000 \
  --logging_steps 100 \
  --overwrite_output_dir \
  --predict_with_generate \
  --max_source_length 1024 \
  --max_target_length 128 \
  --do_train
```

## predict:
use predict.py to predict the test data
```bash
python predict.py \
  --model_name_or_path model_1 \
  --train_file train.json \
  --validation_file $1 \
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
```


## output the submission.jsonl to the path $2
```bash
mv submission.jsonl $2
```