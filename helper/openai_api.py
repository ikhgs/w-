import os
import openai

# Définissez directement votre clé API ici
OPENAI_API_KEY ='sk-proj-dku33dCFA4CRNwVUkjRsT3BlbkFJfZWrgeJenYTzNSiNo2Xn'
openai.api_key = OPENAI_API_KEY

def text_completion(prompt: str) -> dict:
    '''
    Call OpenAI API for text completion

    Parameters:
        - prompt: user query (str)

    Returns:
        - dict
    '''
    try:
        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=f'Human: {prompt}\nAI: ',
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }

# Exemple d'utilisation
result = text_completion('Quel temps fait-il aujourd\'hui ?')
print(result)



        
