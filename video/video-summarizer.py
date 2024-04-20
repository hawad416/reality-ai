from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_models import ChatOpenAI
from transcript_extractor import TranscriptAnalyzer

class VideoSummarizer:
    def __init__(self, transcript):
        self.transcript = transcript

        self.llm = ChatOpenAI(temperature=0, model_name="gpt-4-0125-preview")
        # Create a prompt template for summarization
        self.prompt = ChatPromptTemplate(
            messages=[
                SystemMessagePromptTemplate.from_template(
                    """
                    Your task is to summarize the given video transcript.
                    The summary should capture the main points and themes of the video in a concise manner.
                    Please provide the summary below.
                    """
                ),
                HumanMessagePromptTemplate.from_template("{transcript}")
            ]
        )
        # Initialize memory
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        # Create the LLMChain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            verbose=True,
            memory=self.memory
        )
    
    def summarize(self):
        """
        Summarize the video transcript using the LLM chain.
        """
        # Get the summary from the chain
        response = self.chain({"transcript": self.transcript})
        summary = response["text"]
        return summary

if __name__ == "__main__":
    video_id = "m7LvNTbaqSI"
    analyzer = TranscriptAnalyzer(video_id)
    transcript = analyzer.extract_text()
    
    # Create a VideoSummarizer instance
    summarizer = VideoSummarizer(transcript)
    
    # Generate the summary
    summary = summarizer.summarize()
    
    print("Video Summary:\n")
    print(summary)