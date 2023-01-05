import whisper
import gradio as gr


def speech_to_text(audio, model_size):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio)

    return result["text"]


gr.Interface(
    fn=speech_to_text,
    inputs=[

        # 输入音频的工具栏
        gr.Audio(source="microphone", type="filepath"),

        # 选择模型的下拉列表
        # openai提供了不同大小的模型，不同的模型有不同的运算速度，也有不同的识别精度
        # 同学们可以自行尝试
        gr.Dropdown(choices=["tiny", "base", "small", "medium", "large"]),
    ],
    outputs="text").launch()
