# CIS4930-Grammar-Checker

PROJECT PROPOSAL

Grammar Verification

Team Members:

Rafael Sevilla
Alex Fleis
Kyle Ho-Nguyen
Christopher Bursch

Motivation:

Grammatical errors and typos are very common in written text. When they occur they lead to misunderstanding, reduce clarity and flow interruption of essays, memos, etc. By leveraging machine learning techniques, we aim to develop an approach for typo correction grammar verification that can identify and rectify errors in written text, thereby improving the quality and flow of communication. 

Objective:

Generate a grammar checker that firstly can rectify grammatical errors (grammar/spell checker), and with more improvements can lead to context-specific corrections on written text.

Previous Work: 

One tool used to detect and aid in correcting grammar mistakes is natural language processing (NLP). NLP is something that has been used for understanding the semantics of a sentence to make detection and correction possible. The effectiveness of NLP has been evaluated and different forms of testing have been used to account for ambiguity of the English language. 

Expected Outcome

Previous models have shown good to great progress on being able to guess what word a typo was intended to be. Many models can take into account context, so there is precedent. Likely the model will be able to guess correctly most of the time but will obviously not be perfect. 

Implementation Plan:

1. Study the structure of primarily T5 and GEC models 
2. Using the listed datasets, start training just intending to identify misspelled words
3. After decent results on step 2, see if the model can be adapted to incorporate previous and next words to influence suggested spelling.
4. Extend the range of the context it considers - perhaps it starts with just the adjacent words, but then includes words further away as well

Work Distribution:

Although we are assigning specific sections of the project to each group member, it is expected that all four of us will provide assistance whenever it is needed.
Data Collection and Preprocessing: Kyle and Christopher will be in charge of cleaning the data and preparing the data for the training models.
Model implementation: Rafael and Alex will be in charge of developing the learning models. This means tuning the hyperparameters, tweaking the models when needed, etc.
Testing and Evaluation: All four of us will be participating in testing and evaluating the models.
Documentation and Reporting: We will split up the technical paper into equal parts and record the mid term video and final video together. We will also consistently document our progress on Github to show collaboration.

Course Topics:

Topics discussed in class that will be relevant to the project.
Evaluation Metrics
Overfitting/ Underfitting
Feature Scaling
Data Preprocessing
Cross Validation

Architectures:

-Transformer Model: T5
-Grammatical Error Correction (GEC)




Datasets:

-C4_200M dataset
- JFLEG
- Typo Dataset (Parallel Format)

APIs and Frameworks:

https://www.nltk.org/ 
Helpful platform for using Python to work with language 
https://pypi.org/project/llm/ 
Useful for interacting with a language model

Timeline:

Assuming the due dates won’t change for the mid-term video submission and the final project submission:
February 10th - February 17th: Study the structure of the T5 and GEC models and wait for proposal feedback.
February 18th - February 25th: Train model using the listed datasets.
February 26th - March 9th: Upgrade model to be able to adapt by making suggestions based on adjacent words.
March 10th - March 21st: Update model to extend the range of the context from adjacent words to 2+ words surrounding the misspelled word.
March 21st - March 23rd: Record 5 minute code walkthrough video.
March 23rd - April 6th: Add finishing touch to the project.
April 7th - April 15th: Write the technical paper as a group.
April 16th - April 19th: Record the 10 minute video of our model using the technical paper as a rough outline of topics to discuss during the video.

Sources & resources: 

https://www.vennify.ai/fine-tune-grammar-correction/

https://towardsdatascience.com/nlp-building-a-grammatical-error-correction-model-deep-learning-analytics-c914c3a8331b

https://www.kaggle.com/datasets/bittlingmayer/spelling


https://typo.kshitijshah.net/dataset/

https://towardsdatascience.com/deep-learning-autocorrect-product-and-technical-overview-1c219cee0698

https://medium.com/analytics-vidhya/a-comprehensive-guide-to-build-your-own-language-model-in-python-5141b3917d6d 

https://dl.acm.org/doi/abs/10.5555/1074100.1074630

https://academic.oup.com/jamia/article/18/5/544/829676
