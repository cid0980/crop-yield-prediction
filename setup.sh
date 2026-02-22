
set -e

cd "$(dirname "$0")"

echo "Creating virtual environment..."
if python3 -m venv venv; then
  echo "Activating environment..."
  source venv/bin/activate
  PIP_CMD="pip"
  PY_CMD="python"
else
  echo "venv unavailable; using user-level pip install."
  PIP_CMD="python3 -m pip install --user"
  PY_CMD="python3"
fi

echo "Installing tkinter (GUI dependency)..."
if command -v apt >/dev/null 2>&1; then
  sudo apt install -y python3-tk
elif command -v dnf >/dev/null 2>&1; then
  sudo dnf install -y python3-tkinter
else
  echo "Could not detect apt or dnf. Install tkinter manually if GUI fails."
fi

echo "Installing dependencies..."
eval "$PIP_CMD -r requirements.txt"

echo "Training model..."
$PY_CMD src/train.py

echo "Setup complete."
echo "Run the GUI with:"
echo "  $PY_CMD gui/app.py"
