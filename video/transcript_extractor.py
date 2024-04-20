from youtube_transcript_api import YouTubeTranscriptApi
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory


"""
Extracts & cleans up transcipt from a youtube video.?
"""

class TranscriptAnalyzer:
    def __init__(self, video_id):
        self.video_id = video_id
        self.transcript = self.get_transcript()

    def get_transcript(self):
        """
        Retrieve the transcript for the given YouTube video ID.
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
            return transcript
        except Exception as e:
            print(f"An error occurred while retrieving the transcript: {e}")
            return None

    def extract_text(self):
        """
        Extracts text from the transcript.
        """
        if self.transcript:
            return ' '.join([entry['text'] for entry in self.transcript])
        else:
            return ""
        
        
    def decorate_text(self):
        llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        if self.transcript != "":    
            transcript_text = self.extract_text()
  
            prompt = ChatPromptTemplate(
                messages=[
                    SystemMessagePromptTemplate.from_template(
                        """
                        Clean up this video transcript text by adding punctuation in the correct places and returning the complete text back with the punctuation added.
                        """     
                    ),
                    HumanMessagePromptTemplate.from_template("{question}")
                ]
            )
   
        memory = ConversationBufferMemory()
        
        conversation = LLMChain(
                llm=llm,
                prompt=prompt,
                verbose=True,
                memory=memory
            )

        answer = conversation({"question": transcript_text})['text']

        return answer


