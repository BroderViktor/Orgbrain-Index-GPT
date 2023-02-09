import os

from IPython.display import Markdown, display

from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

os.environ['OPENAI_API_KEY'] = "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"
if (input("Skriv 1 hvis data allerede er loaded") != "1"):
    print("Loaded data")
    documents = SimpleDirectoryReader('C:\GitRepos\gpt_index\examples\paul_graham_essay\data').load_data()
    index = GPTSimpleVectorIndex(documents)

    index.save_to_disk('index.json')
else:
    print("Fetched data")
    index = GPTSimpleVectorIndex.load_from_disk('index.json')

question = input("Write a question about the text")
response = index.query(question, response_mode="default")
print(response)