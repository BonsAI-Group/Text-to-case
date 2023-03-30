from .IQuestionGenerator import IQuestionGenerator
from .IQuestionAnswerer import IQuestionAnswerer
from .BertLargeSingleModelQuestionAnswerer import BertLargeSingleModelQuestionAnswerer
import pandas as pd


class InterrogativeQuestionGenerator(IQuestionGenerator):
    
    """Retrieves best interrogative question generated."""
    def __init__(self) -> None:
        self.interrogative_pronouns_list = ["What", "Who",  "Where", "When", "Why", "How many", "How much", "How", "Whose", "Which"]
        self.QuestionAnswerer: IQuestionAnswerer = BertLargeSingleModelQuestionAnswerer()
    
    def generateQuestion(self, context, fieldName: str) -> str:
        """Generate the best question given a field name."""
        # Generate questions
        field_questions = self.generateInterrogativeQuestions(fieldName)
        # Answer questions
        question_answer_dataframe = self.answerListQuestion(fieldName, field_questions, context)
        # Get best question based on occurence and score
        best_question = self.getBestQuestion(question_answer_dataframe)
        return best_question

    def generateInterrogativeQuestions(self, fieldName: str) -> str:
        """Generates the interrogative questions given a field name."""
        field_questions = []
        for question_word in self.interrogative_pronouns_list:
            question = question_word + " " + fieldName + "?"
            field_questions.append(question)
        return field_questions
    
    def answerListQuestion (self, label, question_list, context):
        """Gives back a dataframe with the questions, answers, confidence scores."""
        answer_list = []
        score_list = []
        for question in question_list:
            answer, score = self.QuestionAnswerer.answerQuestion(question, context)
            answer_list.append(answer)
            score  = round(score * 100, 2)
            score_list.append(score)
        # creating dataframe
        dictionary = {'label' : label, 'questions': question_list, 'answer': answer_list, 'score': score_list}
        dataframe = pd.DataFrame(data=dictionary)

        return dataframe
    
    def getBestQuestion (self, dataframe):
        """Retrieves the best question based on the highest occurence and confidence score."""
        # retrieving the value with the most occurence
        best_result = dataframe.answer.value_counts().index[0]
        # Getting the index of the best value with the highest confident score
        index_best_result = dataframe.loc[dataframe['answer'] == best_result]['score'].idxmax()
        # Retrieving the question of the best result with the highest occurence and confident score
        best_question = dataframe.iloc[[index_best_result]]['questions'].values[0]
        return best_question