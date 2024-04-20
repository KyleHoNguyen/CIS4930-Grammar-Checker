
from happytransformer import HappyTextToText
from happytransformer import TTTrainArgs
from datasets import load_dataset
import joblib
import os
import io
import csv

# Make models && data direcoty
models_directory = 'models'
if not os.path.exists(models_directory):
    os.makedirs(models_directory)

datasets_directory = 'datasets'
if not os.path.exists(datasets_directory):
    os.makedirs(datasets_directory)

# get dataset
train_dataset = load_dataset("jfleg", split='validation[:]')
eval_dataset = load_dataset("jfleg", split='test[:]')


def generate_csv(csv_path, dataset):
    with open(csv_path, 'w', newline='') as csvfile:
        writter = csv.writer(csvfile)
        writter.writerow(["input", "target"])
        for case in dataset:
     	    # Adding the task's prefix to input 
            input_text = "grammar: " + case["sentence"]
            for correction in case["corrections"]:
                # a few of the cases contain blank strings. 
                if input_text and correction:
                    writter.writerow([input_text, correction])

generate_csv("datasets/train.csv", dataset= train_dataset)
generate_csv("datasets/eval.csv", dataset= eval_dataset)
              

# get model
happy_tt = HappyTextToText("T5", "t5-small")

# train 
args = TTTrainArgs(batch_size=8)
# args.max_input_length = 50  # Set the maximum input length
# args.max_target_length = 50  # Set the maximum target length
# args.do_truncate = True     # Disable truncation if necessary

happy_tt.train("datasets/train.csv", args=args)

# save model
joblib.dump(happy_tt, os.path.join(models_directory, 'happy_tt.pkl'))


# Evaluate model performance
eval_result = happy_tt.eval(eval_dataset)
print(eval_result)