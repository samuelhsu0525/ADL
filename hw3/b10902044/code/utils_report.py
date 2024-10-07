from transformers import BitsAndBytesConfig
import torch


def get_prompt(instruction: str) -> str:
    '''Format the instruction as a prompt for LLM.'''
    # return f"你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。USER: {instruction} ASSISTANT:"
    return f"你是人工智慧助理，以下是用戶和人工智能助理之間的對話。你要對用戶的問題提供有用、安全、詳細和禮貌的回答。範例一: 翻譯成現代文：\n唐子謂尊師曰： 本入山為求長生，今反為虎狼之餐。\n回答: 唐臣對薛尊師說： 本來入山是為瞭尋求長生不死的，現在反倒成為虎狼之食瞭\n 範例二:父母很害怕，請薛二娘來治療。\n把這句話翻譯成文言文：\n回答:父母患之，迎薛巫以辨之。USER: {instruction} ASSISTANT:"


def get_bnb_config() -> BitsAndBytesConfig:
    '''Get the BitsAndBytesConfig.'''
    bnb_configuration = BitsAndBytesConfig(
        load_in_4bit = True,
        bnb_4bit_compute_dtype = torch.bfloat16,
        bnb_4bit_use_double_quant = True,
        bnb_4bit_quant_type = 'nf4'
    )
    return bnb_configuration
    pass
