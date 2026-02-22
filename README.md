# Crop Yield Prediction using Machine Learning

## Tools Used
- Python 3.10+
- pandas
- numpy
- scikit-learn
- joblib
- tkinter

## Project Structure
```
crop_yield_prediction/
├── data/
│   └── crop_yield.csv
├── models/
│   └── crop_model.pkl
├── src/
│   ├── config.py
│   ├── preprocess.py
│   ├── train.py
│   └── predict.py
├── gui/
│   └── app.py
├── requirements.txt
├── setup.sh
├── setup_windows.bat
└── README.md
```

## Workflow
1. Dataset in CSV format
2. Use these input features: `crop_name`, `soil_type`, `rainfall`, `temperature`, `humidity`, `fertilizer_used`, `season`
3. Preprocess mixed numeric + categorical data
4. Train Random Forest regression model
5. Save model to `models/crop_model.pkl`
6. Predict yield from user inputs in GUI

## Dataset Schema
CSV file: `data/crop_yield.csv`

Required columns:
1. `crop_name` (text)
2. `soil_type` (text)
3. `rainfall` (number)
4. `temperature` (number)
5. `humidity` (number)
6. `fertilizer_used` (text)
7. `season` (text)
8. `yield` (number target)

## Linux Setup
1. `cd crop_yield_prediction`
2. `chmod +x setup.sh`
3. `./setup.sh`
4. `source venv/bin/activate`
5. `python gui/app.py`

## Windows Setup
1. Open Command Prompt in `crop_yield_prediction`
2. Run `setup_windows.bat`
3. Run `venv\Scripts\activate`
4. Run `python gui\app.py`

## GUI Inputs
1. Dropdowns for `crop_name`, `soil_type`, `fertilizer_used`, `season`
2. Sliders for `rainfall`, `temperature`, `humidity`
