from langchain import LLMChain, PromptTemplate

class BusinessAnalystAgent:
    def __init__(self, language_model):
        self.language_model = language_model

    def extract_requirements(self, user_input):
        # Define prompt for requirement extraction
        prompt = PromptTemplate(
            input_variables=["user_input"],
            template="Extract requirements from the following input: {user_input}"
        )
        chain = LLMChain(llm=self.language_model, prompt=prompt)
        requirements = chain.run(user_input)
        return requirements

    def analyze_requirements(self, requirements):
        # Define prompt for requirement analysis
        prompt = PromptTemplate(
            input_variables=["requirements"],
            template="Analyze the following requirements: {requirements}"
        )
        chain = LLMChain(llm=self.language_model, prompt=prompt)
        analysis = chain.run(requirements)
        return analysis

    def generate_documentation(self, analysis):
        # Define prompt for documentation generation
        prompt = PromptTemplate(
            input_variables=["analysis"],
            template="Generate documentation based on the following analysis: {analysis}"
        )
        chain = LLMChain(llm=self.language_model, prompt=prompt)
        documentation = chain.run(analysis)
        return documentation

    def run(self, user_input):
        requirements = self.extract_requirements(user_input)
        analysis = self.analyze_requirements(requirements)
        documentation = self.generate_documentation(analysis)
        return documentation
