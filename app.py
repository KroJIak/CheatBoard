
class LLMInjectorApp:
    def __init__(self, trigger, source, llm, injector):
        self.trigger = trigger
        self.source = source
        self.llm = llm
        self.injector = injector

    def run(self):
        self.trigger.listen(self.handle_trigger)

    def handle_trigger(self):
        question = self.source.get_text()
        if not question.strip():
            return

        response = self.llm.query(question)
        self.injector.inject_text(response.strip())