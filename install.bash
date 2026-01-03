:: 1. Clone the repository
git clone https://github.com/apple/ml-sharp.git
cd ml-sharp

:: 2. Create and activate a new Conda environment (Python 3.13 is recommended)
conda create -n sharp python=3.13 -y
conda activate sharp

:: 3. Install basic requirements
pip install -r requirements.txt

:: 4. (Optional) For NVIDIA GPU / CUDA support (Windows)
:: Use this if you want to use the --render feature
pip uninstall -y torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

:: 5. Install the package in editable mode
pip install -e .

:: 6. Verify installation
sharp --help
