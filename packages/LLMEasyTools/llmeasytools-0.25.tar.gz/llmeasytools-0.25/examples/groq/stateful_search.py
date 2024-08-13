from llm_easy_tools import get_tool_defs, process_response
import re
from groq import Groq
client = Groq()

# Define a class for document management
class DocumentManager:
    def __init__(self):
        self.documents = [
            {"title": "Introduction to GPT-4", "content": "GPT-4 is the latest language model by OpenAI. It has several new features."},
            {"title": "Advancements in AI", "content": "Exploring the latest advancements in artificial intelligence. AI is evolving rapidly."},
            {"title": "Natural Language Processing", "content": "Understanding NLP and its applications. NLP is a key part of AI."}
        ]
        self.current_document = None

    def search_document(self, term: str):
        closest_match = None
        min_distance = float('inf')
        for doc in self.documents:
            distance = self._calculate_similarity(term, doc['title'])
            if distance < min_distance:
                min_distance = distance
                closest_match = doc

        if closest_match:
            self.current_document = closest_match
            first_sentence = closest_match['content'].split('.')[0]
            return f"Found document, title: {closest_match['title']}.\n {first_sentence}..."
        else:
            return "No matching document found."

    def lookup_word(self, word: str):
        if not self.current_document:
            return "No document is currently selected."

        sentences = self.current_document['content'].split('.')
        for sentence in sentences:
            if word in sentence:
                return sentence.strip()
        return f"The word '{word}' was not found in the current document."

    def _calculate_similarity(self, term, title):
        # Simple similarity calculation (can be replaced with more sophisticated methods)
        return abs(len(term) - len(title))  # Example simplistic similarity measure

# Create an instance of DocumentManager
doc_manager = DocumentManager()
tools = [doc_manager.search_document, doc_manager.lookup_word]

# Example LLM call to search for a document
response_search = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Find a document about AI"}],
    tools=get_tool_defs(tools),
    tool_choice="auto"
)

# Process the response to search for the document

results_search = process_response(response_search, tools)
print(results_search[0].output)

# Example LLM call to look up a word in the current document
response_lookup = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Look up the word 'evolving'"}],
    tools=get_tool_defs(tools),
    tool_choice="auto",
)
# Process the response to look up the word
results_lookup = process_response(response_lookup, tools)
print(results_lookup[0].output)


## OUTPUT
#
# Found document, title: Advancements in AI.
# Exploring the latest advancements in artificial intelligence...
# AI is evolving rapidly
