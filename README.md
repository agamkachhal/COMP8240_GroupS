Applications of Data Science (COMP8240)
===

## Group S 

*Group Members:* <br>

**Agam Kachhal  (45762643)** <br>
**Rohit Manral  (45710864)** <br>
**Shubham Rana  (45812713)** <br>
**Kripali Gandhi(45712158)** <br>

## Project Title: Fasttext Implementation ##

This repository belongs to *Group S* for the Application of Data Science (COMP8240) Major Project. We are going to implement the fasttext, which is an open-source, lightweight, free library that allows users to learn text classifiers and text representations. It works on standard, generic hardware. Model size  can later be reduced to fit on mobile devices.

* Environment: We are running fastText using a VM (ubuntu 18.04 LTS) with t2.micro instance along with a 30 Giga bytes of RAM.

We are working on the below datasets: 

**1) Amazon product data:** We extracted amazon product data(i.e., health care, etc.) which contains 0.34 Million user reviews. This dataset includes reviews (ratings, text, helpfulness votes), product metadata (descriptions, category information, price, brand, and image features), and links (also viewed/also bought graphs) and presented in JSON format. [Amazon Product Data Source](https://jmcauley.ucsd.edu/data/amazon/)

**2) Social recommendation data (LibraryThing reviews):** This dataset includes ratings as well as social (or trust) relationships between users. Data are from LibraryThing (a book review website). Moreover, this is a multi label classification data and is currently been presented in JSON format with 1.7 Million reviews.[Social Recommendation Data](https://cseweb.ucsd.edu/~jmcauley/datasets.html#google_local)

**3) Good Read Reviews Spoiler:** We extracted this concentrated English review subset dataset for spoiler detection, where each book/user has at least one associated spoiler review. This dataset contains more than 1.3 Million book reviews presented in JSON format.[Good Read Reviews Spoiler Data](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/reviews)

**4) Stack Exchange posts :** This is multi label dataset of the stack exchange posts, **retrieved by querying the google cloud platform.** It has 0.5 Million rows with text and tags, and it requires pre-processing as well because this is in semi-structured (JSON) format. We are fetching data directly from the google cloud platform by hitting database throught the colab. [Stack Exchange Posts Data](https://bigquery.cloud.google.com/dataset/bigquery-public-data:stackoverflow)

## Challenges:

1. Google colab not supports to read 1.3 Million data from the source, so we used the shell commands to reduce the file size to 0.5 Million rows and process them.

2. Social Recommendtion data has wrong JSON format(badJson ~ it has data enclosed in single quotes whereas python parses only JSON data enclosed in double quotes), so we pre-process this file before reading in the Colab.
