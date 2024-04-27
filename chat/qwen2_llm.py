
from langchain.llms.base import LLM
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, LlamaTokenizerFast


class Qwen2_LLM(LLM):
    # 基于本地 Qwen2 自定义LLM类
    tokenizer: AutoTokenizer = None
    model: AutoModelForCausalLM = None


