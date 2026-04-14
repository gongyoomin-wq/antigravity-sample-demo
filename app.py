import gradio as gr

def antigravity_effect(text):
    # 텍스트를 거꾸로 뒤집어 중력을 거스르는 효과 연출
    return text[::-1]

demo = gr.Interface(
    fn=antigravity_effect,
    inputs=gr.Textbox(placeholder="중력을 거스를 텍스트를 입력하세요..."),
    outputs=gr.Textbox(label="우주 무중력 상태 (GitHub에서 다운로드 됨!)"),
    title="Antigravity Sample App v2",
    description="Antigravity IDE 연동 워크플로우 테스트입니다."
)

if __name__ == "__main__":
    demo.launch()
