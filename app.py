import gradio as gr

def antigravity_effect(text):
    # 텍스트를 거꾸로 뒤집어 중력을 거스르는 효과 연출
    return text[::-1]

demo = gr.Interface(
    fn=antigravity_effect,
    inputs=gr.Textbox(placeholder="중력을 거스를 텍스트를 입력하세요..."),
    outputs=gr.Textbox(label="안티그래비티 결과"),
    title="Antigravity Sample App",
    description="재미나이 CLI로 만든 첫 번째 안티그래비티 Gradio 앱입니다."
)

if __name__ == "__main__":
    demo.launch()
