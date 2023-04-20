from .IQuestionGenerator import IQuestionGenerator
from .IQuestionAnswerer import IQuestionAnswerer
from .BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
import pandas as pd


class InterrogativeQuestionGenerator(IQuestionGenerator):
    
    """Retrieves best interrogative question generated."""
    def __init__(self) -> None:
        self.interrogativePronounsList = ["What", "Who",  "Where", "When", "Why", "How many", "How much", "How", "Whose", "Which"]
        self.QuestionAnswerer: IQuestionAnswerer = BertLargeSingleModelQuestionAnswerer()
    
    def generateQuestion(self, context, fieldName: str) -> str:
        """Generate the best question given a field name."""
        # Generate questions
        fieldQuestions = self.generateInterrogativeQuestions(fieldName)
        # Answer questions
        questionAnswerDataframe = self.answerListQuestion(fieldName, fieldQuestions, context)
        # Get best question based on occurence and score
        bestQuestion = self.getBestQuestion(questionAnswerDataframe)
        return bestQuestion

    def generateInterrogativeQuestions(self, fieldName: str) -> str:
        """Generates the interrogative questions given a field name."""
        fieldQuestions = []
        for questionWord in self.interrogativePronounsList:
            question = questionWord + " " + fieldName + "?"
            fieldQuestions.append(question)
        return fieldQuestions
    
    def answerListQuestion (self, label, questionList, context):
        """Gives back a dataframe with the questions, answers, confidence scores."""
        answerList = []
        scoreList = []
        for question in questionList:
            answerObj = self.QuestionAnswerer.answerQuestion(question, context)
            answerList.append(answerObj.answer)
            score  = round(answerObj.confidence * 100, 2)
            scoreList.append(score)
        # creating dataframe
        dictionary = {'label' : label, 'questions': questionList, 'answer': answerList, 'score': scoreList}
        dataframe = pd.DataFrame(data=dictionary)

        return dataframe
    
    def getBestQuestion (self, dataframe):
        """Retrieves the best question based on the highest occurence and confidence score."""
        # retrieving the value with the most occurence
        bestResult = dataframe.answer.value_counts().index[0]
        # Getting the index of the best value with the highest confident score
        indexBestResult = dataframe.loc[dataframe['answer'] == bestResult]['score'].idxmax()
        # Retrieving the question of the best result with the highest occurence and confident score
        bestQuestion = dataframe.iloc[[indexBestResult]]['questions'].values[0]
        return bestQuestion