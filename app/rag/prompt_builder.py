def build_prompt(
        question : str,
        contexts : list[str],

)->str:
    prompt = """
    You are an AI assistant that answers questions using uploaded engineering documents.
    
    Instructions:
    
    - Use ONLY the provided context.
    - If the answer cannot be found in the context, say: "I couldn't find the answer in the uploaded documents."
    - Do not make up information.
    - Answer clearly and concisely.
    
    Context:
    -----------------------------------------------------------------------------------------
    """



    for index,context in enumerate(contexts,start=1):
        prompt+=f"\ncontext {index}:\n"
        prompt+=context+"\n"


    prompt+= f"Question: \n {question}\n\nAnswer:"

    return prompt
