## prepare the file
first copy the context.json and test.json file from the path $1 and $2
```bash
cp $1 $2 .
```
use transform.py to let test.json convert to fit the phase1 model
```bash
python transform.py test.json
```

## phase1:
use model_p1_shi_221_s64 to predict the selected paragraph for test file and output it as a list saved in the test_output.txt file
```bash
python run_swag_no_trainer.py --train_file train_p1.json --validation_file transformed_test.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1 --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path model_p1_shi_221_s64
```
use convert.py to make test file have our predicted paragraph and convert to fit phase2 model
```bash
python convert.py test.json
```

## phase2:
use model_22 to predict the answer and save in the output_22.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_22/ --max_seq_length 512
mv output.csv output_22.csv
```
use model_23 to predict the answer and save in the output_23.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_23/ --max_seq_length 512

mv output.csv output_23.csv
```
use model_25 to predict the answer and save in the output_25.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_25/ --max_seq_length 512

mv output.csv output_25.csv
```
use model_28 to predict the answer and save in the output_28.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_28/ --max_seq_length 512

mv output.csv output_28.csv
```

## using another phase1 model

## phase1:
use model_p1_shi_221 to predict the selected paragraph for test file and output it as a list saved in the test_output.txt file
```bash
python run_swag_no_trainer.py --train_file train_p1.json --validation_file transformed_test.json --per_device_train_batch_size 2 --per_device_eval_batch_size 1 --learning_rate 2e-5 --num_train_epochs 0 --max_seq_length 512 --model_name_or_path model_p1_shi_221
```
use convert.py to make test file have our predicted paragraph and convert to fit phase2 model
```bash
python convert.py test.json
```

## phase2:
use model_27 to predict the answer and save in the output_27.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_27/ --max_seq_length 512
mv output.csv output_27.csv
```
use model_29 to predict the answer and save in the output_29.csv file
```bash
python run_qa_no_trainer.py --train_file train_p2.json --validation_file train_p2.json --test_file converted_test.json --per_device_train_batch_size 4 --per_device_eval_batch_size 4 --do_predict --learning_rate 1e-5 --gradient_accumulation_steps 1 --num_train_epochs 0 --model_name_or_path model_29/ --max_seq_length 512
mv output.csv output_29.csv
```

## blending:
with 6 different version answers, we can use them to blend the answers for better performance and output as predict.csv
the rule is selecting the most common answer or the shortest one in case of a tie
```bash
python blend.py
```

## output the prediction.csv to the path $3
```bash
python final.py $3
```