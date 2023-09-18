# test_ai_coach.py

import unittest
from ai_coach import AICoach

class TestAICoach(unittest.TestCase):

    def setUp(self): 
        self.coach = AICoach()

    def test_analyze_text(self):
        input_text = "This is a test."
        result = self.coach.analyze_text(input_text)
        self.assertIsNotNone(result)

    def test_provide_feedback(self):
        
        analysis_results = {"sentiment": "positive", "grammar_errors": 0}
        feedback = self.coach.provide_feedback(analysis_results)
        self.assertIsInstance(feedback, str)


if __name__ == '__main__':
    unittest.main()
