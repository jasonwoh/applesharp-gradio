import gradio as gr
import subprocess
import os

def run_sharp(input_image):
    # 1. Save the uploaded image to a temporary path
    input_path = "input_temp.jpg"
    input_image.save(input_path)
    
    # 2. Define output directory
    output_dir = "output_gui"
    
    # 3. Build the command (same as what you'd type in terminal)
    # We use 'python -m sharp.cli' to ensure it runs correctly
    command = f"sharp predict -i {input_path} -o {output_dir}"
    
    try:
        # 4. Run the command and wait for it to finish
        subprocess.run(command, shell=True, check=True)
        
        # 5. Locate the output .ply file
        # Usually SHARP saves it as 'output_gui/input_temp.ply' or similar
        result_file = os.path.join(output_dir, "input_temp.ply")
        
        if os.path.exists(result_file):
            return f"Success! File saved to {result_file}", result_file
        else:
            return "Processing finished, but .ply file not found.", None
            
    except Exception as e:
        return f"Error: {str(e)}", None

# Build the UI
with gr.Blocks(title="Apple SHARP GUI") as demo:
    gr.Markdown("# 🍏 Apple SHARP 3D Generator")
    gr.Markdown("Upload an image to convert it into a 3D Gaussian Splat (.ply file).")
    
    with gr.Row():
        input_img = gr.Image(type="pil", label="Upload Image")
        with gr.Column():
            status_text = gr.Textbox(label="Status")
            output_file = gr.File(label="Download .ply Model")
            
    run_btn = gr.Button("Generate 3D Model", variant="primary")
    
    run_btn.click(
        fn=run_sharp, 
        inputs=input_img, 
        outputs=[status_text, output_file]
    )

if __name__ == "__main__":
    demo.launch()
