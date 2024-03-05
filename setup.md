## Setup enviroment
Jupyter Notebook script that combines the previous code snippets to create the `lambda_function.zip` file. You can copy and paste this into a Jupyter Notebook cell:

```python
%%bash
# Create directories and activate virtual environment
mkdir my_lambda_function
cd my_lambda_function
python -m venv venv
source venv/bin/activate

# Install required packages
pip install --no-build-isolation --force-reinstall "boto3>=1.28.57" "awscli>=1.29.57" "botocore>=1.31.57"
pip install "langchain>=0.0.350" "transformers>=4.24,<5" sqlalchemy -U "faiss-cpu>=1.7,<2" "pypdf>=3.8,<4" pinecone-client==2.2.4 apache-beam==2.52. tiktoken==0.5.2 "ipywidgets>=7,<8" matplotlib==3.8.2 anthropic==0.9.0
pip install datasets==2.15.0
pip install numexpr==2.8.8
pip install --quiet xmltodict==0.13.0 duckduckgo-search yfinance pandas_datareader langchain_experimental pysqlite3 google-search-results
pip install --quiet beautifulsoup4==4.12.2
pip install --quiet "pillow>=9.5,<10"
pip install -qU --no-cache-dir nemoguardrails==0.5.0
pip install -qU "faiss-cpu>=1.7,<2" "langchain>=0.0.350" "pypdf>=3.8,<4" "ipywidgets>=7,<8"

# Package the Lambda function and its dependencies
deactivate
cd venv/lib/python*/site-packages
zip -r9 ${OLDPWD}/lambda_function.zip .
cd $OLDPWD

# Add your Lambda function code to the zip file (replace "lambda.py" with your actual Lambda function script)
zip -g lambda_function.zip lambda.py
```

Please note that this script assumes you're running it in a Unix-like environment (Linux or macOS). If you're using Windows, you'll need to adjust the script accordingly.

Keep in mind that Jupyter Notebook runs in a separate environment, so you may need to install some system-level dependencies (e.g., g++) manually outside of the notebook if they are required by your packages.