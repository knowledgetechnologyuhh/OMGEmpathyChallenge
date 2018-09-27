# OMGEmpathyChallenge

Website: https://www2.informatik.uni-hamburg.de/wtm/omgchallenges/omg_empathy.html

**Organization**

Pablo Barros, University of Hamburg, Germany </br>
Nikhil Churamani, University of Hamburg, Germany </br>
Angelica Lim, Simon Frases University, Canada </br>
Stefan Wermter, Hamburg University, Germany </br>

**OMG-Empathy Dataset**

The OMG-Empathy corpus is composed of recordings of two individuals talking to each other about a certain topic. One of the individuals is an actor who leads a semi-scripted conversation with a listener. The actors tells stories about what happened to them recently, and we recorded the reactions of the listener to these stories over time, which can contain short interactions.

We created a series of eight topics that the actor talked about, each of them related to one or more emotional state:

- Story 1 - A childhood friend.
- Story 2 - I started a band!
- Story 3 - My relation with my dog.
- Story 4 - I had a bad flight experience.
- Story 5 - I had an adventurous traveling experience.
- Story 6 - I cheated on an exam when I was younger.
- Story 7 - I won a martial arts challenge.
- Story 8 - I ate a very bad food.

The actor was free and encouraged to improvise on each of these topics, so that we recorded a natural conversation scenario, but the actor was instructed to maintain the control over the conversation. This way, we guaranteed that the recorded interaction were not one-sided, and at the same time that the listener did not overtake the direction of the conversation.

We recorded the audio and visual data of both the actor and listener for each interaction. Immediately after each session, we asked the listeners to watch the interactions on a computer screen and use a joystick to annotate how they felt in terms of valence using a continuous scale ranging from positive to negative values. The use of the joystick allowed for continuous and gradual tracking of annotations which are temporally related to the interaction scenario.

We used a total of four different actors, each one of them taking part in the conversation with two different topics. This way we collected different reaction levels from different listeners for the same actor. We had a total of 10 subjects, each one taking part in all the eight topics. This gave us 80 different interaction videos. Each video had an average of 6 minutes, providing us with 480 minutes (8 hours) of recordings.

**Tracks**

We let available for the challenge a pre-defined set of training, validation and testing samples. We separate our samples based on each story: 4 stories for training, 1 for validation and 3 for testing. Each story sample is composed of 10 videos with interactions, one for each listener. Although using the same training, validation and testing data split, we propose two tracks which will measure different aspects of the self-assessed empathy:

The **Personalized Empathy track**, where each team must predict the empathy of a specific person. We will evaluate the ability of proposed models to learn the empathic behavior of each of the subjects over a newly perceived story. We encourage the teams to develop models which take into consideration the individual behavior of each subject in the training data.

The **Generalized Empathy track**, where the teams must predict the general behavior of all the participants over each story. We will measure the performance of the proposed models to learn a general empathic measure for each of the stories individually. We encourage the proposed models to take into consideration the aggregated behavior of all the participants for each story, and to generalize this behavior in a newly perceived story.


**Dataset Structure**

The dataset is separated into 10 folders, one with recordings of each listener. Each folder contains the recordings of 8 different stories, available as a .mp4 file. The order of the stories are described above. Each .mp4 file has an associated .csv file with the valence annotations. The .csv file contains one annotation per frame.And it is structured as follows:



**Scripts**

We provide the following scripts:

- OMG_empathy_extract_faces.py: a script used to extract the faces of the actors and subjects of the dataset.


**How to participate**

Important dates: 
- 25th of September 2018  - Opening of the Challenge - Team registrations begin </li>
- 1st of October 2018 - Training/validation data and annotation available </li>
- 1st of December 2018 - Test data release </li>
- 3rd of December 2018 - Final submission (Results and code) </li>
- 5th of December 2018 - Final submission (Paper) </li>
- 7th of December 2018 - Announcement of the winners </li>

To participate to the challenge, please send us an email to barros @ informatik.uni-hamburg.de with the title "OMG-Empathy Team Registration". This e-mail must contain the following information:
- Team Name
- Team Members
- Affiliation
- Participating tracks

Each team can have a maximum of 5 participants. You will receive from us the access to the dataset and all the important information about how to train and evaluate your models. 
For the final submission, each team will have to send us a .csv file containing the final arousal/valence values for each of the utterances on the test dataset. We also request a link to a GitHub repository where your solution must be stored, and a link to an ArXiv paper with 4-6 pages describing your model and results. The best papers will be invited to submit their detailed research to a journal yet to be specified. Also, the best participating teams will hold an oral presentation about their solution during the WCCI/IJCNN 2018 conference.


**Paper submission**

Each participating team must submit, together with their final results, a short 2-4 pages paper describing their solution. This paper must follow the IEEE specifications ( Latex and Word templates) and will be peer reviewed following the FG 2019 standards. The accepted papers will be included in the FG 2019 workshop proceedings.

**License**

This corpus is distributed under the Creative Commons CC BY-NC-SA 3.0 DE license. If you use this corpus, you have to agree with the following itens:

- To cite our reference in any of your papers that make any use of the database. 
- The references are provided at the end of this page.
- To use the corpus for research purpose only.
- To not provide the corpus to any second parties.


**More information** 

- our website: https://www2.informatik.uni-hamburg.de/wtm/omgchallenges/omg_empathy.html
- You can also find usefull scripts for processing the dataset here: https://github.com/knowledgetechnologyuhh/OMGEmpathyChallenge

For more informations: barros@informatik.uni-hamburg.de
