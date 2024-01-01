# Image Classification with Transfer Learning using DVC and MLFlow.

This project aims to develop an accurate image classification system that can assist in diagnosing tumors in kidney images. The ML model will analyze kidney images and classify them as either **Normal** or containing a **Tumor**. DVC and MLFlow concepts get implemented to track experiments and model versions throughout development and tuning. By detecting tumors in kidney images, our image classifier aims to support medical professionals in identifying kidney cancer. Overall, this project focuses on applying machine learning to build a computer-aided diagnosis tool for improving the detection of malignant kidney diseases.

## Tech Stack & Infrastructure

1. Python
2. Machine Learning
3. Flask
4. Docker
5. MLFlow
6. DagsHub
7. DVC
8. BentoML

## MLFlow Setup on DagsHub

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/gangulyaritra/kidney-image-classification.mlflow \
MLFLOW_TRACKING_USERNAME=gangulyaritra \
MLFLOW_TRACKING_PASSWORD=df0ddf50ffda20b2e11f9b409117e0d2ef6a6d8f \
python script.py
```

## Manual Steps to Run the Application

#### Step 1: Create a Virtual Environment and Install Dependency.

```bash
# Clone the Repository.
git clone https://github.com/gangulyaritra/kidney-image-classification.git

# Create a Virtual Environment.
python3 -m venv venv

# Activate the Virtual Environment.
source venv/bin/activate

# Install the Dependencies.
pip install -r requirements.txt
```

#### Step 2: Export DagsHub Credentials as Environment Variables.

```bash
export MLFLOW_TRACKING_URI="https://dagshub.com/gangulyaritra/kidney-image-classification.mlflow"
export MLFLOW_TRACKING_USERNAME="gangulyaritra"
export MLFLOW_TRACKING_PASSWORD="df0ddf50ffda20b2e11f9b409117e0d2ef6a6d8f"
```

#### Step 3: Run the Training Pipeline.

```bash
python3 -m src.training_pipeline
```

#### Step 4: Run the DVC Pipeline (Optional).

1. Initialize Git. `git init`
2. Initialize DVC. `dvc init`
3. Execute or restore any version of our pipeline using `dvc repro`
4. Visualize the pipeline(s) defined in the dvc.yaml file. `dvc dag`

#### Step 5: Run the Application Server.

```bash
python app.py
```

## Authors

- [Aritra Ganguly](https://in.linkedin.com/in/gangulyaritra)

## License & Copyright

[MIT License](LICENSE)
