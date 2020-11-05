Applications of Data Science (COMP8240)
===

## Group S 

*Group Members:* <br>

**Agam Kachhal  (45762643)** <br>
**Rohit Manral  (45710864)** <br>
**Shubham Rana  (45812713)** <br>
**Kripali Gandhi(45712158)** <br>

<center> <h1>fastText Implementation </h1> </center>

<p align="center">
  <img width="260" height="150" src="https://fasttext.cc/img/ogimage.png">
</p>

This repository contains the work of *Group S* for the Application of Data Science (COMP8240) Major Project. We have implemented fastText on four different datasets, which is an open-source, lightweight, free library that allows users to learn text classifiers and text representations. It works on standard, generic hardware. Model size  can later be reduced to fit on mobile devices.

* Environment : AWS Virtual Machine and server - Ubuntu 18.04 LTS , Google Colaboratory
* Code Management (Version Control, Code History): GitHub
* For Reporting:  Latex + Overleaf

We are working on the below datasets: 

**1) Astronomy Stack Exchange Data:** Astronomy Stack Exchange is a question and answer site for astronomers and astrophysicists. The dataset has been obtained from [Astronomy Stack Exchange](https://astronomy.stackexchange.com/questions?tab=newest&pagesize=50). We have used Python's Library called BeautifulSoup to scrape Questions and their respective Tags from the webpages. This dataset contains 9687 rows and 518 labels and is a multi label dataset. We have also explored hierarchical softmax and bigrams for the dataset.

**2) Ask Ubuntu Stack Exchange Data:** Ask Ubuntu: It is a community-driven question and answer website for the Ubuntu operating system. The dataset source has been derived from [Ask Ubuntu Stack Exchange](https://askubuntu.com/). We have scraped Questions and Tags for this dataset using the python library called BeautifulSoup. It is a multi label dataset with 3,61,702 rows and 3379 labels, however, due to constraints have only scraped dataset from limited webpages not all. We have also explored various techniques of text classification using fastText, such as Bi-grams, Hierarchical softmax etc.

**3) Photography Stack Exchange Data:** Photography Stack Exchange is a question and site for professional, enthusiast and amateur photographers. The source of this dataset can be found here [Photography Stack Exchange](https://photo.stackexchange.com/). We are using BeautifulSoup which is a very popular Python Library to scrape Questions and Tags respectively for this data. This dataset has 20297 rows and 451 labels and is a multi label dataset. After separating labels, we converted those labels in a format which is required to implement fastText.

**4) Stack Overflow Posts :** This is multi label dataset of the Stack Overflow Posts, **retrieved by querying the google cloud platform.** It has 0.5 Million rows with Questions and Tags (along with other columns such as body, user_id, answer_count, created_at, many more. We are fetching data directly from Big Query (Google Cloud Console) by hitting database throught the Google Colab.After separating labels, we converted those labels in a format which is required to implement fastText. [StackOverflow Posts ~ Big Query](https://console.cloud.google.com/marketplace/product/stack-exchange/stack-overflow).

**Results** : We had trained our four new datasets on different models with different hyper parameters. Thus, after applying some optimal hyperparameters(epochs, learning_rate, 
hierarchical softmax loss, wordNgrams and other scalling parameters) in every successive model of our datasets we noticed that both Precision and Recall increased simultaneously.
