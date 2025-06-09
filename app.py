import mesop as me
import boto3
import os

# Configure AWS credentials (use environment variables or IAM role)
bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name='us-east-2')

# Replace with your actual KB and model info
KNOWLEDGE_BASE_ID = os.getenv("BEDROCK_KNOWLEDGE_BASE_ID", "MAKZOATKHX")
MODEL_ARN = os.getenv("BEDROCK_MODEL_ARN", "arn:aws:bedrock:us-east-2::foundation-model/anthropic.claude-3-haiku-20240307-v1:0")

@me.page()
def home():
    me.text("Ask your question:")
    query = me.input("Question")
    if query:
        me.text("Querying...")
        answer = retrieve_from_kb(query)
        me.text_area("Answer", answer, readonly=True, height=200)


def retrieve_from_kb(query: str) -> str:
    try:
        response = bedrock_client.retrieve_and_generate(
            input={"text": query},
            retrieveAndGenerateConfiguration={
                "knowledgeBaseConfiguration": {"knowledgeBaseId": KNOWLEDGE_BASE_ID},
                "modelArn": MODEL_ARN
            }
        )
        return response['output']['text']
    except Exception as e:
        return f"Error: {str(e)}"


