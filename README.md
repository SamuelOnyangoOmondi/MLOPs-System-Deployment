# Credit Mix Prediction Model

## Overview
This project focuses on developing a machine learning model capable of predicting an individual's credit mix based on financial behaviors and demographic data. The analysis and model training processes utilize machine learning techniques, and the model is served through a FastAPI application.

## Dataset Description
The dataset includes various attributes related to personal financial management as well as demographic factors:
- **Annual_Income**: The individual's yearly income.
- **Age**: The age of the individual.
- **Num_Bank_Accounts**: Number of bank accounts the individual possesses.
- **Num_Credit_Card**: Number of credit cards held by the individual.
- **Occupation**: Professional occupation of the individual.
- **Education_Level**: Highest educational qualification of the individual.

The target variable, **Credit_Mix**, indicates the type of credit (good, average, or bad) based on the individual's financial history.

## Repository Structure
- `/notebook/`: Contains the Jupyter notebooks for exploratory data analysis, feature engineering, and model training.
- `/src/`:
  - `preprocessing.py`: Script for data preprocessing.
  - `model.py`: Script for model training and serialization.
  - `prediction.py`: FastAPI application for serving predictions.
- `/data/`:
  - `/train/`: Training data files.
  - `/test/`: Testing data files.
- `/models/`: Contains serialized models for deployment.

## Setup and Installation
Before running the project, ensure you have Python 3.8 or newer installed. Install all required dependencies with the following command:
```bash
pip install pandas numpy scikit-learn fastapi uvicorn joblib
```

## Usage Instructions

### Running the Jupyter Notebook
To perform data analysis and initial model training:
1. Navigate to the `/notebook/` directory.
2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Open `project_name.ipynb` and execute the cells sequentially.

### Starting the FastAPI Server
To run the FastAPI application:
1. Ensure the model is saved in `/models/`.
2. Navigate to the `/src/` directory.
3. Start the server:
   ```bash
   uvicorn prediction:app --reload
   ```
4. The API can be accessed at `http://localhost:8000`.

### Making Predictions
Use the `/predict/` endpoint to submit a POST request with the required features. The service will return the predicted credit mix.

## Contributions
Contributions to this project are welcome! Please fork the repository and submit a pull request with your suggested changes. For any bugs or feedback, feel free to open an issue in the repository.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
For further inquiries, contact [Your Email or GitHub Profile Link].
```

### Points to Customize:
- **Dataset Description**: Update the description if there are more details you would like to include about your dataset.
- **Contact Information**: Replace placeholder with your actual contact information or GitHub profile link.
- **License Link**: If you have a `LICENSE.md` file in your repository, make sure the link is correct. If not, you may need to create this file or adjust the reference.

This `README.md` is structured to provide a clear and complete introduction to your project, instructions for installation and use, and ways to contribute, making it suitable for open-source collaboration and use.
