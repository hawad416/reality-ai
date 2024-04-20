from history.fake_video_ids import get_fake_eating_disorder_vids, get_fake_suicide_vids, get_fake_terrorism_vids
from video.transcript_extractor import TranscriptAnalyzer
from video.sentiment_analyzer import analyze_attitudes, analyze_themes
from typing import List, Dict, Any

class ConsumptionOutput:
    def __init__(self):
        # dictionary to store the analysis results
        self.analysis_results: Dict[str, Dict[str, Any]] = {}

    def get_history(self) -> List[str]:
        """
        Retrieve the history of video IDs for the user.
        """
        # combine different categories of video IDs (e.g., eating disorder, suicide, terrorism).
        # for now these are fake as it takes long to get the watch history 

        video_ids = get_fake_eating_disorder_vids() + get_fake_suicide_vids() + get_fake_terrorism_vids()
        return video_ids

    def analyze_videos(self, video_ids: List[str]):
        """
        Analyze videos using video IDs to obtain summaries and sentiments.
        """
        for video_id in video_ids:
            # create an instance of TranscriptAnalyzer for each video ID
            analyzer = TranscriptAnalyzer(video_id)
            summary = analyzer.extract_text()
            attitude = analyze_attitudes(summary)
            key_themes = analyze_themes(summary)
            
            # store the analysis results in a dictionary with video_id as the key
            self.analysis_results[video_id] = {
                "summary": summary,
                "attitude": attitude,
                "key_themes": key_themes
            }

    def generate_recommendations(self):
        """
        Generate recommendations based on analysis results.
        """
        recommendations = []
        
        # For demonstration purposes, the recommendations could be based on specific key themes or attitudes
        for video_id, analysis in self.analysis_results.items():
            key_themes = analysis["key_themes"]
            attitude = analysis["attitude"]

            recommendations.append((video_id, "Consider watching less of this content for your well-being."))

            
            # this is just a placeholder for now until i can use the analysis to generate recs.
            # # Generate recommendations based on the analysis results
            # if "suicide" in key_themes or attitude == "Negative":
            #     recommendations.append((video_id, "Consider watching less of this content for your well-being."))
            
            # Add more recommendation rules here as needed
        
        return recommendations

    def get_analysis_results(self):
        """
        Retrieve the stored analysis results.
        """
        return self.analysis_results

    def run_analysis(self):
        """
        Run the overall analysis workflow.
        """
        # Retrieve history (fake video ids for now on problematic vids
        video_ids = self.get_history()
        
        # Analyze videos
        self.analyze_videos(video_ids)
        
        # Generate recommendations
        recommendations = self.generate_recommendations()
        
        # Return the analysis results and recommendations
        return self.analysis_results, recommendations

# testing it out
if __name__ == "__main__":
    consumption_output = ConsumptionOutput()
    results, recommendations = consumption_output.run_analysis()
    
    print("Analysis Results:")
    print(results)
    
    # recommendations are going to be displayed to the parent. 
    print("\nRecommendations:")
    for video_id, recommendation in recommendations:
        print(f"Video ID: {video_id}, Recommendation: {recommendation}")
