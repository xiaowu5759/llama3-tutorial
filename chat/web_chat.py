from dataclasses import asdict, dataclass

import streamlit as st
from langchain_community.llms.ollama import Ollama


@dataclass
class GenerationConfig:
    # 定义数据，配置生成数据
    max_length: int = 32768
    top_p: float = 0.8
    temperature: float = 0.8
    do_sample: bool = True
    repetition_penalty: float = 1.005


def prepare_generation_config() -> GenerationConfig:
    with st.sidebar:
        max_length = st.slider('Max Length',
                               min_value=8,
                               max_value=8192,
                               value=8192)
        top_p = st.slider('Top P', 0.0, 1.0, 0.8, step=0.01)
        temperature = st.slider('Temperature', 0.0, 1.0, 0.7, step=0.01)
        st.button('Clear Chat History')

    generation_config = GenerationConfig(max_length=max_length,
                                         top_p=top_p,
                                         temperature=temperature)
    return generation_config


def load_llm() -> Ollama:
    # <|eot_id|><|start_header_id|>assistant<|end_header_id|>
    llm = Ollama(model='llama3', stop=['<|eot_id|>'])
    return llm


def init_app():
    # 加载llm
    llm = load_llm()
    # 构造st web页面
    st.set_page_config(page_title="WebChat", page_icon="🤖", layout="wide")
    st.title('Web Chat')
    # todo 通过页面控制参数
    generation_config = prepare_generation_config()

    # 接受user输入
    prompt = st.chat_input('请输入你的问题')
    if prompt:
        # 显示用户的信息 在web容器中
        with st.chat_message('user'):
            st.markdown(prompt)
        # todo 将用户提问，添加到上下文中

        # 机器人回复
        with st.chat_message('robot'):
            message_placeholder = st.empty()
            # answer = llm.invoke(prompt)
            answer = ''
            print(prompt)
            for char in llm.stream(prompt):
                answer = answer + char
                message_placeholder.markdown(answer + '▌')
            message_placeholder.markdown(answer)
            # todo 将AI回答，添加到上下文中


if __name__ == '__main__':
    init_app()
    print('start')






