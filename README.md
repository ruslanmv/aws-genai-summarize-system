# AWS GenAI Summarization System - Team Seven

**Introduction**

This repository outlines the development of a serverless system using AWS Lambda functions to automatically summarize meeting recordings for ACME, a software consultancy. This system aims to improve the efficiency of ACME's architects by automating note-taking, summarization, and action item creation.

**User Case**

ACME's architects frequently hold video conferences, leading to a significant time commitment in transcribing meetings and summarizing key points. This project explores leveraging Generative AI (GenAI) to automate these tasks, enhancing the architects' productivity.

**System Overview**

The proposed system comprises the following components:

1. **S3 Bucket:** Stores uploaded meeting recordings as audio files.
2. **Lambda Function:**
   - Triggers upon a new meeting recording upload to the S3 bucket.
   - Transcribes the audio using Amazon Transcribe.
   - Employs a Generative AI model to summarize the transcribed text.
   - (Optional) Integrates with ACME's JIRA instance using the JIRA API to create tasks or stories based on identified action items.
3. **Amazon CloudWatch:** Monitors Lambda execution and system logs for troubleshooting and insights.

**Key Stakeholders**

- **Head of PlatformOps Engineering:** Requires a "plug and play" solution due to limited development resources.
- **Head of Data Science:** Offers expertise in model fine-tuning, if necessary.
- **Chief Financial Officer:** Emphasizes cost-effectiveness and usage metrics.

**Benefits**

- **Increased Architect Productivity:** Saves time from manually taking meeting notes, allowing architects to focus on core tasks.
- **Improved Meeting Recall:** Provides concise summaries for efficient review and action item tracking.
- **Enhanced Collaboration:** Facilitates task creation and assignment within ACME's JIRA system (optional).
- **Cost-Effective:** Leverages serverless architecture with pay-per-use billing for AWS services.


Complete details [here](case.md)

**Building the System**

**Prerequisites**

- An AWS account with appropriate permissions.
- Experience with Python programming and AWS services.
- Familiarity with Generative AI models (optional).

**Steps**

1. **Create an S3 Bucket:** Store uploaded meeting recordings.
2. **Develop the Lambda Function:** Implement the logic described in the System Overview section. more details [here](setup.md)
3. **Configure CloudWatch Logging:** Monitor Lambda function execution and logs.
4. **Deploy:** Upload the Lambda function code to AWS.
5. **(Optional) JIRA Integration:** Set up authentication and configure task creation using the JIRA API.

**Deployment Diagram**


**Code Structure**

The codebase will be organized to include:

- `lambda_function.py`: Contains the main Lambda function logic.
- `requirements.txt`: Lists necessary Python dependencies for deployment.
- Additional files (optional): Might include scripts for transcribing audio files or interacting with the JIRA API.

**Extending the System**

- Integrate with different Generative AI models for improved summarization quality.
- Explore speech-to-text alternatives for broader audio format support.
- Implement user authentication for secure access to meeting summaries.

**Contributing**

We welcome contributions to this project! Please refer to the CONTRIBUTION.md file (to be added) for guidelines on submitting pull requests.

**License**

This project is licensed under the MIT License (see LICENSE.md file).

**Disclaimer**

This project serves as a reference only and does not constitute production-ready code. Modifications are required to align with specific deployment environments and security considerations.













