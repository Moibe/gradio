import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    print(input_img.shape, sepia_img.shape)
    print("Hola")
    return sepia_img

demo = gr.Interface(sepia, gr.Image(height=200, width=200), "image")

demo.launch()
    
# if __name__ == "__main__":
#     demo.launch(show_api=False)   