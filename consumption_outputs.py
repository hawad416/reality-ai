from history.fake_video_ids import get_fake_eating_disorder_vids, get_fake_suicide_vids, get_fake_terrorism_vids
from video.transcript_extractor import TranscriptAnalyzer
from video.sentiment_analyzer import analyze_attitudes, analyze_themes, justify_problems
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

   
    def generate_parental_recommendations(self) -> List[str]:
        """
        Generate parental recommendations based on analysis results.
        
        Parameters:
        analysis_results (dict): A dictionary where keys are video IDs and values are dictionaries with
                                'summary', 'attitude', and 'key_themes' as keys.
        
        Returns:
        list: A list of recommendations for the parent, indicating which videos require attention and why.
        """
        recommendations = []
        
        # Define a list of key themes that could be concerning
        concerning_themes = [
            "sexually explicit material",
            "false or misleading information",
            "violence",
            "extremism or terrorism",
            "hateful or offensive material",
            "profanity or vulgar language",
            "illegal activities",
            "harmful behaviors",
            "gambling",
            "unmoderated chat rooms",
            "misrepresentation or discrimination"
        ]
        
        # Iterate through analysis results
        for video_id, analysis in self.get_analysis_results().items():
            # Check if any concerning themes are present in the analysis results
            key_themes = analysis.get("key_themes", [])
        
            # Check which concerning themes are present in the key themes
            themes_found = [theme for theme in concerning_themes if theme in key_themes]
            
            # If any concerning themes are found, generate a recommendation for the parent
            if themes_found:
                # Convert the list of found themes into a string
                themes_str = ', '.join(themes_found)
                
                # Retrieve other information such as attitude and summary
                attitude = analysis.get("attitude", "")
                summary = analysis.get("summary", "")
                
                # Create a detailed recommendation including video ID, concerning themes, attitude, and summary
                recommendation = (
                    f"Video ID: {video_id}\n"
                    f"Concerning Themes: {themes_str}\n"
                    f"Attitude: {attitude}\n"
                    f"Flagged: {justify_problems(key_themes)}\n"
                )
                
                recommendations.append(recommendation)
        
        print(recommendations)
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
        recommendations = self.generate_parental_recommendations()
        
        # Return the analysis results and recommendations
        return self.analysis_results, recommendations

# testing it out
if __name__ == "__main__":
    consumption_output = ConsumptionOutput()
    results, recommendations = consumption_output.run_analysis()

    print(recommendations)
    
    print("Analysis Results:")
    #print(results)
    
    # recommendations are going to be displayed to the parent. 
    print("\nRecommendations:")
    for recommendation in recommendations:
        print(recommendation)

    
