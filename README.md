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

* Environment: We are running fastText using a VM (ubuntu 18.04 LTS) with t2.micro instance along with a 30 Giga bytes of RAM.

We are working on the below datasets: 

**1) Astronomy Stack Exchange Data:** Astronomy Stack Exchange is a question and answer site for astronomers and astrophysicists. The dataset has been obtained from [Astronomy Stack Exchange](https://astronomy.stackexchange.com/questions?tab=newest&pagesize=50). We have used Python's Library called BeautifulSoup to scrape Questions and their respective Tags from the webpages. This dataset contains 9687 rows and 518 labels and is a multi label dataset. We have also explored hierarchical softmax and bigrams for the dataset.

**2) Ask Ubuntu Stack Exchange Data:** Ask Ubuntu: It is a community-driven question and answer website for the Ubuntu operating system. The dataset source has been derived from [Ask Ubuntu Stack Exchange](https://askubuntu.com/). We have scraped Questions and Tags for this dataset using the python library called BeautifulSoup. It is a multi label dataset with 3,61,702 rows and 3379 labels, however, due to constraints have only scraped dataset from limited webpages not all. We have also explored various techniques of text classification using fastText, such as Bi-grams, Hierarchical softmax etc.

**3) Photography Stack Exchange Data:** Photography Stack Exchange is a question and site for professional, enthusiast and amateur photographers. The source of this dataset can be found here [Photography Stack Exchange](https://photo.stackexchange.com/). We are using BeautifulSoup which is a very popular Python Library to scrape Questions and Tags respectively for this data. This dataset has 20297 rows and 451 labels and is a multi label dataset. After separating labels, we converted those labels in a format which is required to implement fastText.

**4) Stack Overflow Posts :** This is multi label dataset of the Stack Overflow Posts, **retrieved by querying the google cloud platform.** It has 0.5 Million rows with Questions and Tags (along with other columns such as Body, UserID, Answer Count, Created at. We are fetching data directly from the google cloud platform by hitting database throught the colab. [Google Cloud Platform (Big Query)](https://bigquery.cloud.google.com/dataset/bigquery-public-data:stackoverflow)
