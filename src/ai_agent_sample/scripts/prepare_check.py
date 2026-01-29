from ai_agent_sample.llm.bedrock import call_claude
from ai_agent_sample.agent.core import Message

def main():

    result = call_claude("こんにちは")
    print("LLM response:")
    print(result)

if __name__ == "__main__":
    main()
