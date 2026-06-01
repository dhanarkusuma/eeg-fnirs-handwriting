# Background

This repository was created for participation in the **Multimodal Brain-Computer Interface (BCI) Grand Challenge** hosted on Codabench. The challenge focuses on imagined handwriting trajectory classification using synchronized EEG and fNIRS signals.

Participants are required to classify each trial into one of four logographic character classes based on:

* EEG signal recordings
* fNIRS signal recordings
* Metadata provided by the organizers

The competition aims to encourage the development of robust machine learning and deep learning approaches for multimodal BCI systems.

Competition link: https://www.codabench.org/competitions/15893/#/pages-tab


# Experiment Results
| Notebook | Model | EEG Range | EEG Sliding Window | fNIRS Range | fNIRS Sliding Window | Accuracy | 
|---|---|---|---|---|---|---|
| linear-svm_pca_001.ipynb | Linear SVM + PCA | 0.0 - 2.0 | 0.5 - 2.0 | 2.0 - 8.0 | 3.0 - 7.0 | 0.4783 |
