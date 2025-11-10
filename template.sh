# create directory
mkdir -p research
mkdir -p chatbot
mkdir -p chatbot/config
mkdir -p chatbot/logger
mkdir -p chatbot/exception
mkdir -p chatbot/prompts
mkdir -p chatbot/utils
mkdir -p chatbot/src
mkdir -p chatbot/model
mkdir -p tests/



# create files
touch setup.py
touch requirements.txt
touch research/trials.ipynb

touch chatbot/__init__.py

touch chatbot/config/config.yaml

touch chatbot/logger/__init__.py
touch chatbot/exception/__init__.py

touch chatbot/prompts/__init__.py
touch chatbot/prompts/prompt.py

touch chatbot/utils/__init__.py
touch chatbot/utils/config_loader.py
touch chatbot/utils/api_key_loader.py
touch chatbot/utils/model_loader.py
touch chatbot/utils/docs_ops.py
touch chatbot/utils/file_io.py

touch chatbot/src/__init__.py
touch chatbot/src/chat_ingestor.py
touch chatbot/src/retriever.py
touch chatbot/src/generate.py


echo "Directories and files created successfully!"
