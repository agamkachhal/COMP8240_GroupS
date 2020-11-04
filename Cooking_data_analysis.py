#loading required libraries
import os
import subprocess


print("Getting Cooking data ...")
print(os.popen("wget https://dl.fbaipublicfiles.com/fasttext/data/cooking.stackexchange.tar.gz && tar xvzf cooking.stackexchange.tar.gz").read())

print("printing head of the dataset")
print(os.popen("head cooking.stackexchange.txt").read())

print("printing the word count")
print(os.popen("wc cooking.stackexchange.txt").read())

print("splitting data in training & validation.")
print(os.popen("head -n 12404 cooking.stackexchange.txt > cooking.train").read())
print(os.popen("tail -n 3000 cooking.stackexchange.txt > cooking.valid").read())

print("The Word counts of the train & valid")
print(os.popen("wc cooking.train").read())
print(os.popen("wc cooking.valid").read())

print("Modelling starts ....")

print("Our First classifier")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Making model better : Crude Normalization")

print(os.popen('cat cooking.stackexchange.txt | sed -e "s/\([.\!?,/()]\)/ \1 /g" | tr "[:upper:]" "[:lower:]" > cooking.preprocessed.txt').read())

print("Pre-processing done")
print("splitting data in training & validation.")
print(os.popen("head -n 12404 cooking.preprocessed.txt > cooking.train").read())
print(os.popen("tail -n 3000 cooking.preprocessed.txt > cooking.valid").read())

print("The Word counts of the train & valid")
print(os.popen("wc cooking.train").read())
print(os.popen("wc cooking.valid").read())

print("Second classifier")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Adding epochs (25)")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking -epoch 25").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Adding learning rate 1.0")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking -lr 1.0").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Adding epochs (25) & learning rate 1.0")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking -lr 1.0 -epoch 25").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Scaling Up model: lr 1.0 , epochs 25, wrodNgrams 2 & other scaling parameters")
print(os.popen("./fasttext supervised -input cooking.train -output model_cooking -lr 1.0 -epoch 25 -wordNgrams 2 -bucket 200000 -dim 50 -loss hs").read())
print(os.popen("./fasttext test model_cooking.bin cooking.valid").read())

print("Checking Score on Prob 0.5 for Model")
print(os.popen("./fasttext test model_cooking.bin cooking.valid -1 0.5").read())

print("Modelling done .....")
