class CodeTranslator:
    def __init__(self, apikey, model):
        self.api_key = apikey
        self.model = model

    def translate_code(self, code, source_language, target_language):
        import openai
        
        openai.api_key = self.api_key

        prompt = f'''You are an expert programmer in all programming languages. Translate the "{source_language}" code to "{target_language}" code. Do not include \\\\\\.

        Example translating from JavaScript to Python:

        JavaScript code:
        for (let i = 0; i < 10; i++) {{
            console.log(i);
        }}

        Python code:
        for i in range(10):
            print(i)
        
        {source_language} code:
        {code}

        {target_language} code (no \\\\\\):
        '''

        completions = openai.ChatCompletion.create(
            model=self.model,
            messages=[{'role': 'system', 'content': f'{prompt}'}],
            temperature=0,
        )

        message = completions.choices[0].message.content
        return message.strip()
