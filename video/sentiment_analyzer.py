from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI

"""
Analyzer the sentiments within a video, potentially classifying as
positive, negative, toxic, concerning etc.

Why isnt this showing up!
"""

from textwrap import dedent


def analyze_attitudes(transcript):
        """
        Analyze the transcript to determine the attitudes expressed.
        You can use sentiment analysis techniques to categorize the attitude.
        """
        # You can use a library like TextBlob or spaCy for sentiment analysis
        from textblob import TextBlob
        
        blob = TextBlob(transcript)
        sentiment = blob.sentiment
        
        if sentiment.polarity > 0:
            attitude = "Positive"
        elif sentiment.polarity < 0:
            attitude = "Negative"
        else:
            attitude = "Neutral"
        
        return attitude

def analyze_themes(summary):
    agent_prompt = dedent("""Analyze the following video transcript and extract any problematic themes from the text. Focus on identifying specific themes that could pose potential risks or concerns for children, particularly those related to the following issues:

                        Sexually explicit material: Any references to or descriptions of sexual acts, nudity, or pornographic content.
                        False or misleading information: Content that contains incorrect information, conspiracy theories, or misleading statements.
                        Violence: Any depictions or discussions of physical harm or violent acts towards people or animals.
                        Extremism or terrorism: Content that promotes or discusses extremist ideologies, terrorism, or radicalization.
                        Hateful or offensive material: Any content that promotes hate speech, discrimination, or offensive language targeting specific groups based on protected characteristics such as race, religion, gender, sexual orientation, or disability.
                        Profanity or vulgar language: Content containing excessive use of offensive language or vulgar expressions.
                        Content encouraging illegal activities: Material that promotes vandalism, crime, or other illegal activities.
                        Harmful behaviors: Content that encourages eating disorders, self-harm, or suicide.
                        Gambling sites and games: References to or promotion of gambling activities.
                        Unmoderated chat rooms: Content that includes interactions without supervision, allowing potentially unsuitable comments.
                        Misrepresentation or discrimination: Content that misrepresents individuals based on gender, promotes sexism, or discriminates against specific groups.

                        Provide a JSON detailed report with identified themes, specifying which parts of the transcript contain the mentioned issues, and whether the themes are problematic.
                        If there are no concerns with a category, don't include it in the final JSON output"""
                          
                     )
     
    llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")

    prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(agent_prompt),
                HumanMessagePromptTemplate.from_template("{transcript}")
            ]
        )
    
    chain = LLMChain(
                llm=llm,
                prompt=prompt,
                verbose=False          
            )
     
    response = chain({"transcript": summary})
    summary = response["text"]
    
    return summary
    