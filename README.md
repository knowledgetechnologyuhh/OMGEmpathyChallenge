# OMGEmotionChallenge

Website: https://www2.informatik.uni-hamburg.de/wtm/omgchallenges/omg_empathy.html

**Organization**

Pablo Barros, University of Hamburg, Germany </br>
Nikhil Churamani, University of Hamburg, Germany </br>
Angelica Lim, Simon Frases University, Canada </br>
Stefan Wermter, Hamburg University, Germany </br>

**OMG-Empathy Dataset**

The OMG-Empathy corpus is composed of recordings of two individuals talking to each other about a certain topic. One of the individuals is an actor who leads a semi-scripted conversation with a listener. The actors tells stories about what happened to them recently, and we recorded the reactions of the listener to these stories over time, which can contain short interactions.

We created a series of eight topics that the actor talked about, each of them related to one or more emotional state:

- A childhood friend.
- I started a band!
- My relation with my dog.
- I had a bad flight experience.
- I ate a very bad food.
- I won a martial arts challenge.
- I had an adventurous traveling experience.
- I cheated on an exam when I was younger.
The actor was free and encouraged to improvise on each of these topics, so that we recorded a natural conversation scenario, but the actor was instructed to maintain the control over the conversation. This way, we guaranteed that the recorded interaction were not one-sided, and at the same time that the listener did not overtake the direction of the conversation.

We recorded the audio and visual data of both the actor and listener for each interaction. Immediately after each session, we asked the listeners to watch the interactions on a computer screen and use a joystick to annotate how they felt in terms of valence using a continuous scale ranging from positive to negative values. The use of the joystick allowed for continuous and gradual tracking of annotations which are temporally related to the interaction scenario.

We used a total of four different actors, each one of them taking part in the conversation with two different topics. This way we collected different reaction levels from different listeners for the same actor. We had a total of 10 subjects, each one taking part in all the eight topics. This gave us 80 different interaction videos. Each video had an average of 6 minutes, providing us with 480 minutes (8 hours) of recordings.

**Tracks**

We let available for the challenge a pre-defined set of training, validation and testing samples. We separate our samples based on each story: 4 stories for training, 1 for validation and 3 for testing. Each story sample is composed of 10 videos with interactions, one for each listener. Although using the same training, validation and testing data split, we propose two tracks which will measure different aspects of the self-assessed empathy:

The **Personalized Empathy track**, where each team must predict the empathy of a specific person. We will evaluate the ability of proposed models to learn the empathic behavior of each of the subjects over a newly perceived story. We encourage the teams to develop models which take into consideration the individual behavior of each subject in the training data.

The **Generalized Empathy track**, where the teams must predict the general behavior of all the participants over each story. We will measure the performance of the proposed models to learn a general empathic measure for each of the stories individually. We encourage the proposed models to take into consideration the aggregated behavior of all the participants for each story, and to generalize this behavior in a newly perceived story.


**Dataset Structure**

The dataset is separated into the following files:

- omg_TrainVideos.csv
- omg_ValidationVideos.csv
- DetailedAnnotations (You will receive this data when registering for the challenge)
- Transcripts (You will receive this data when registering for the challenge)

Each of the CSV files contain the following information:


link: The link to access the youtube video
start:  the timestamp where the video starts
end: the timestamp where the video ends
video: the video-id, used to associate the video with the annotations
utterance: the utterance name, used to associate the video with the annotations
arousal: the calculated goldstandard of the arousal
valence: the calculated goldstandard of the valence
emotionMaxVote: the resulting categorical emotion from voting over all annotations

For the OMG-Emotion challenge, we will compute the arousal/valence value of a model with the goldstandard of the test set. The categorical emotion will not be used for evaluating the model, but could be usefull when designing or training your model.

The DetailedAnnotations folder contains all the annotations for each utterance. Each annotation was made when taking into consideration the video as part of a sequence, so it could be useful to use this additional information when designing your 
models.

The Transcripts folder contains all the transcripts for each of the utterance in the dataset.

**Scripts** 

We provide the following scripts:

- prepare_data.py: a script used to read, download, cut and organize the dataset.
- calculateEvaluationCCC.py: a script used to calculate the CCC of the output of a model and the validation set. The file with the model's output must be a CSV file containng the following information: 

```
video, utterance, arousal, valence
74de88564,utterance_1.mp4,0.05738688939330001,0.115515408794,
74de88564,utterance_2.mp4,0.05738688939330001,0.119515408794,
74de88564,utterance_3.mp4,0.05738688939330001,0.2122515408794,
74de88564,utterance_4.mp4,0.05738688939330001,0.314515408794,
74de88564,utterance_5.mp4,0.05738688939330001,0.10294515408794,
74de88564,utterance_6.mp4,0.05738688939330001,0.1224515408794,
74de88564,utterance_7.mp4,0.05738688939330001,0.654515408794,
...

```

It is important to note that the order of the videos and utterances present in this file **must** be the same as the order of the videos and utterances on the  omg_ValidationVideos.csv.

**How to participate**

Important dates: 
- Publishing of training and validation data with annotations: March 14, 2018. 
- Publishing of the test data, and opening of the online submission: April 11, 2018.
- Closing of the submission portal: April 13, 2018. 
- Announcement of the winner through the submission portal: April 18, 2018.


To participate, please send us an email to barros@informatik.uni-hamburg.de with the title "OMG-Emotion Recognition Team Registration". This e-mail must contain the following information: 
- Team Name
- Team Members
- Affiliation

Each team can have a maximum of 5 participants. You will receive from us the access to the dataset and all the important information about how to train and evaluate your models. 
For the final submission, each team will have to send us a .csv file containing the final arousal/valence values for each of the utterances on the test dataset. We also request a link to a GitHub repository where your solution must be stored, and a link to an ArXiv paper with 4-6 pages describing your model and results. The best papers will be invited to submit their detailed research to a journal yet to be specified. Also, the best participating teams will hold an oral presentation about their solution during the WCCI/IJCNN 2018 conference.

**License**

This corpus is distributed under the Creative Commons CC BY-NC-SA 3.0 DE license. If you use this corpus, you have to agree with the following itens:

- To cite our reference in any of your papers that make any use of the database. 
- The references are provided at the end of this page.
- To use the corpus for research purpose only.
- To not provide the corpus to any second parties.


**More information** 

- You can access a detailed information about an early version of the dataset here: https://arxiv.org/abs/1803.05434
- You can also find usefull scripts for processing the dataset here: https://github.com/knowledgetechnologyuhh/OMGEmotionChallenge

For more informations: barros@informatik.uni-hamburg.de
