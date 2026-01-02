# AI Hallucination Detector

## Problem Statement
Generative AI models often produce responses that sound confident but may contain incorrect or fabricated information, known as hallucinations.
There is currently no simple way for users to evaluate the reliability of AI-generated content, especially for students and developers who rely on it.

## Solution
AI Hallucination Detector is a Generative AI-based system that evaluates the trustworthiness of AI-generated responses.
It generates multiple responses to the same prompt using different prompt variations and compares them using semantic similarity techniques.
Based on the level of inconsistency, the system assigns a hallucination risk score (Low, Medium, or High).

## How It Works
1. User provides an AI-generated response or prompt.
2. The system creates multiple prompt variations.
3. The Generative AI model produces multiple outputs.
4. Semantic similarity is computed between responses.
5. A hallucination risk score is generated and displayed.

## Tech Stack
- Python
- Generative AI (LLMs)
- Natural Language Processing (NLP)
- Sentence Embeddings
- Streamlit
- OpenAI / Gemini API

## Future Scope
- Integration with fact-checking APIs
- Support for code hallucination detection
- Browser extension for real-time analysis
