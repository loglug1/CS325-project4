# Summarizer Module

import google.generativeai as genai
from abc import ABC, abstractmethod

#Summarizer Interface
class Summarizer(ABC):
    @abstractmethod
    def summarize(self, article_text):
        pass

#Google Gemini implementation of Summarizer, requires API key from https://aistudio.google.com/app/apikey
class GeminiSummarizer(Summarizer):
    def __init__(self,api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def summarize(self, article_text):
        response = self.model.generate_content(f'Summarize the following news article in 50 words or less: {article_text}')
        try:
            summary = response.text
        except:
            summary = "Error when creating summary, more details below:\n" + str(response.prompt_feedback)

        return summary