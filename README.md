## **Predict Research Significance Based on Its Abstract**

#### A. Data Collection  
Raw data were fetched from [Pubmed](https://www.ncbi.nlm.nih.gov/pubmed/) in Medline format with different start date, and were divided into three groups:  
  * **Group 0** includes publications from **6** journals:  
  Nature (from: 2016-01-01),<br>Science (from: 2016-01-01),<br>Cell (from: 2016-01-01),<br>New England Journal of Medicine (nejm) (from: 2016-01-01),<br>Nature Biotechnology (nat_biotechnol) (from: 2016-01-01),<br>Lancet (from: 2016-01-01).<br>

* **Group 1** includes publications from **4** journals: <br>
The Journal of Clinical Investigation (jci) (from: 2016-01-01),<br>Genes & Development (gens_dev) (from: 2016-01-01),<br>Proceedings of the National Academy of Sciences of the United States of America (pnas) (from: 2016-01-01),<br>Nature Communications (nat_comm) (from: 2016-01-01).<br>

* **Group 2** includes publications from **3** journals: <br>
Journal of Biological Chemistry (jbc) (from: 2016-01-01),<br>Scientific Reports (sci_rep) (from: 2017-06-01),<br>Plos One (from: 2017-06-01).<br>


#### B. Data Munging
* Downloaded medline formatted data from each journal were converted to pandas dataframe type with columns: **'PMID', 'Title', 'Abstract'** and **'Journal'**. Detailed code could be found in ***format_convert.py***.<br>

* All converted data in the same group were combined into one single dataframe. Records with incorrect data in **'Abstract'** column were removed. Detailed code could be found in ***data_combine.py***<br>

* Summary of the cleaned data were shown below:<br>
    * Total data in all groups:<br>
    ![](total_count.jpg)<br>
    * Counts in individual groups:<br>
    ![](0_counts.jpg)
    ![](1_counts.jpg)
    ![](2_counts.jpg)<br>

#### C. Feature Engineering
* Data split:<br>
 1. Data in each group were randomly shuffled by rows;
 2. 20% of data were used as test data, and 80% of data were used as training data.<br>

* Nature language processing:<br>
 1. Each word in abstract was lemmatized and lower cased;
 2. None English words and stop words were removed;
 3. Customized stop words were removed. <br>  

* Data combination:<br>
    Cleaned abstracts in all groups were combined into single csv file (**x_train.csv** & **x_test.csv**). And their corresponding labels were also combined into single csv file with same order (**y_train.csv** & **y_test.csv**).   <br>

* Detailed code could be found in ***data_clean.py***

#### D. Model Training
* Word to vector:<br>
Abstracts were converted to sparse matrix by using TF-IDF method.

* Scaling:<br>
MaxAbsScaler was used to scale the features.

* Model Training:<br>
Due to the limited computation power, logistic regression model was used for this project. Various parameters were tested and recorded in ***logistic_regression_params.csv***. The confusion matrix of the best model could be found in ***logreg_cm.csv***. Detailed code could be found in ***logreg_params_search.py*** and ***model_training.py***.

* A sample model was demonstrated here:<br>
[https://if-pred.herokuapp.com](https://if-pred.herokuapp.com)
