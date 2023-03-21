# Text-to-case

## Introduction
The goal of this project is to get spoken text from a `speech to text` model, and extract the right information from it to fill in a form.<br>
After researching, we split the project into 2 different parts:<br>
1. Question answering
2. Question generating

### Question answering
Because the spoken **text could be about anything**, we need a **large model** that understands a lot of **different types of contexts**. Because it would take a lot of time to do that ourselfs, we are going to use **existing models** for this. The model type that could be the best for this problem is the `question answering model`. There are enough models that we can try and/ or tweak.
### Question generating
If you choose to use an existing question answering model, we need questions to ask the model. Most of the **fields from a form are not question based**, but they are **using keywords**, such as `FirstName`, `Email`, `Priority`, etc.<br> 
The research for this can be found in the structure below.


## Structure
- Question Generating
    - Interrogative pronounce
    - ChatGPT
- Question Answering