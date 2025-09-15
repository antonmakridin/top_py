import os
import sys

import const

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import openai
from langchain.chat_models import openai

os.environ["OPENAI_API_KEY"] = const.APIKEY

query = sys.argv[1]
loader = TextLoader('work\\data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))
