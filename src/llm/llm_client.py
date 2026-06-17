from src.prompts.prompt_templates import get_rag_prompt
from src.retrieval.retriever import get_relevant_documents
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

def gemini_agent(user_query: str):
    context, docs = get_relevant_documents(query=user_query)
    prompt_template = get_rag_prompt()

    # Promptni to'liq matn ko'rinishida shakllantiramiz
    final_prompt = prompt_template.format(context=context, question=user_query)


    model = init_chat_model(model="gemini-2.5-flash-lite", model_provider="google_genai")
    agent = create_agent(
        model=model,
    )

    response = agent.invoke({"messages": [final_prompt]})

    docs = [doc.metadata.get('source') for doc in docs]
    return {"answer": response["messages"][-1].content,
            "docs": docs
    }