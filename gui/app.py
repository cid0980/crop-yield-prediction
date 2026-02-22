import os
import sys

try:
    import tkinter as tk
    from tkinter import ttk
except ModuleNotFoundError as exc:
    raise SystemExit(
        "tkinter is not installed. On Debian/Ubuntu run:\n"
        "  sudo apt install python3-tk\n"
        "On Fedora/RHEL run:\n"
        "  sudo dnf install python3-tkinter\n"
        "Then re-run: python3 gui/app.py"
    ) from exc


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, "src"))

from predict import predict
from config import DATA_PATH

import pandas as pd


def read_scale(var):
    return float(var.get())


def read_choice(var, field_name):
    raw = var.get().strip()
    if not raw:
        raise ValueError(f"{field_name} is required")
    return raw


def load_dropdown_options():
    defaults = {
        "crop_name": ["Wheat", "Rice", "Maize", "Cotton", "Soybean", "Sugarcane"],
        "soil_type": ["Loamy", "Clay", "Sandy", "Silt", "Black"],
        "fertilizer_used": ["Urea", "NPK", "DAP", "Compost", "Organic"],
        "season": ["Kharif", "Rabi", "Summer", "Monsoon"],
    }

    try:
        data = pd.read_csv(DATA_PATH)
        options = {}
        for key, fallback in defaults.items():
            if key in data.columns:
                values = sorted(data[key].dropna().astype(str).str.strip().unique().tolist())
                options[key] = values or fallback
            else:
                options[key] = fallback
        return options
    except Exception:
        return defaults


def load_numeric_ranges():
    defaults = {
        "rainfall": (0.0, 2000.0, 700.0),
        "temperature": (0.0, 50.0, 27.0),
        "humidity": (0.0, 100.0, 65.0),
    }
    try:
        data = pd.read_csv(DATA_PATH)
        ranges = {}
        for key, fallback in defaults.items():
            if key in data.columns:
                col = pd.to_numeric(data[key], errors="coerce").dropna()
                if not col.empty:
                    min_v = float(col.min())
                    max_v = float(col.max())
                    if min_v == max_v:
                        min_v = max(0.0, min_v - 1.0)
                        max_v = max_v + 1.0
                    ranges[key] = (min_v, max_v, float(col.median()))
                else:
                    ranges[key] = fallback
            else:
                ranges[key] = fallback
        return ranges
    except Exception:
        return defaults


def get_prediction():
    try:
        input_features = {
            "crop_name": read_choice(crop_name_var, "Crop Name"),
            "soil_type": read_choice(soil_type_var, "Soil Type"),
            "rainfall": read_scale(rainfall_var),
            "temperature": read_scale(temperature_var),
            "humidity": read_scale(humidity_var),
            "fertilizer_used": read_choice(fertilizer_var, "Fertilizer Used"),
            "season": read_choice(season_var, "Season"),
        }
        result = predict(input_features)
        output.config(text=f"Predicted Yield: {result:.2f}")
    except Exception as exc:
        output.config(text=f"Error: {exc}")


root = tk.Tk()
root.title("Crop Yield Predictor (ML)")

dropdown_options = load_dropdown_options()
numeric_ranges = load_numeric_ranges()

tk.Label(root, text="Crop Name").pack()
crop_name_var = tk.StringVar(value=dropdown_options["crop_name"][0])
crop_name = ttk.Combobox(
    root, textvariable=crop_name_var, values=dropdown_options["crop_name"], state="readonly"
)
crop_name.pack()

tk.Label(root, text="Soil Type").pack()
soil_type_var = tk.StringVar(value=dropdown_options["soil_type"][0])
soil_type = ttk.Combobox(
    root, textvariable=soil_type_var, values=dropdown_options["soil_type"], state="readonly"
)
soil_type.pack()

tk.Label(root, text="Rainfall (mm)").pack()
rainfall_var = tk.DoubleVar(value=numeric_ranges["rainfall"][2])
rainfall = tk.Scale(
    root,
    from_=numeric_ranges["rainfall"][0],
    to=numeric_ranges["rainfall"][1],
    orient=tk.HORIZONTAL,
    resolution=0.1,
    variable=rainfall_var,
    length=300,
)
rainfall.pack()

tk.Label(root, text="Temperature (C)").pack()
temperature_var = tk.DoubleVar(value=numeric_ranges["temperature"][2])
temperature = tk.Scale(
    root,
    from_=numeric_ranges["temperature"][0],
    to=numeric_ranges["temperature"][1],
    orient=tk.HORIZONTAL,
    resolution=0.1,
    variable=temperature_var,
    length=300,
)
temperature.pack()

tk.Label(root, text="Humidity (%)").pack()
humidity_var = tk.DoubleVar(value=numeric_ranges["humidity"][2])
humidity = tk.Scale(
    root,
    from_=numeric_ranges["humidity"][0],
    to=numeric_ranges["humidity"][1],
    orient=tk.HORIZONTAL,
    resolution=0.1,
    variable=humidity_var,
    length=300,
)
humidity.pack()

tk.Label(root, text="Fertilizer Used").pack()
fertilizer_var = tk.StringVar(value=dropdown_options["fertilizer_used"][0])
fertilizer_used = ttk.Combobox(
    root,
    textvariable=fertilizer_var,
    values=dropdown_options["fertilizer_used"],
    state="readonly",
)
fertilizer_used.pack()

tk.Label(root, text="Season").pack()
season_var = tk.StringVar(value=dropdown_options["season"][0])
season = ttk.Combobox(
    root, textvariable=season_var, values=dropdown_options["season"], state="readonly"
)
season.pack()

tk.Button(root, text="Predict", command=get_prediction).pack()

output = tk.Label(root, text="")
output.pack()

root.mainloop()
