from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, SummarizationPipeline
import javalang


class CodeSummarizer:
    def __init__(self):
        # Initialize the summarization pipeline with the specified model and tokenizer
        self.pipeline = SummarizationPipeline(
            model=AutoModelForSeq2SeqLM.from_pretrained(
                "SEBIS/code_trans_t5_large_code_comment_generation_java_multitask_finetune"),
            tokenizer=AutoTokenizer.from_pretrained(
                "SEBIS/code_trans_t5_large_code_comment_generation_java_multitask_finetune", skip_special_tokens=True,
                legacy=False),
            device=0,# Assumes you have a GPU at device index 0
            max_new_tokens=100
        )

    def tokenize_java_code(self, code):
        # Tokenize the provided Java code using javalang
        tokenList = []
        tokens = list(javalang.tokenizer.tokenize(code))
        for token in tokens:
            tokenList.append(token.value)
        return ' '.join(tokenList)

    def summarize_code(self, code):
        # First tokenize the Java code
        tokenized_code = self.tokenize_java_code(code)
        # Then pass the tokenized code to the summarization pipeline
        return self.pipeline(tokenized_code)[0]

