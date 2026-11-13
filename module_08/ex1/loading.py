import importlib
import sys

def check_dependencies():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    required_packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready"
    }

    loaded_modules = {}
    is_missing_packages = False

    for package_name, message in required_packages.items():
        try:
            module = importlib.import_module(package_name)
            loaded_modules[package_name] = module

            version = module.__version__
            print(f"[OK] {package_name} ({version}) - {message}")

        except ImportError:
            is_missing_packages = True
            print(f"[FAILED] {package_name} is missing")

    if is_missing_packages:
        print("\nERROR: Missing dependencies.")
        print("To fix this, install the programs using one of these methods:")
        print(" pip ------> pip install -r requirements.txt")
        print(" Poetry ---> poetry install")
        sys.exit(1)

    return loaded_modules


def analyze_matrix(modules):
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    x_data = np.arange(1000)

    df = pd.DataFrame({"Time": x_data})
    df["Manipulated"] = df["Time"] + 50

    print("Generating visualization...")
    plt.figure(figsize=(8, 4))

    plt.plot(df["Time"], df["Manipulated"], color="green", label="Simple Line (+50)")

    plt.title("The Simpliest Matrix Data")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()

    plt.savefig("matrix_analysis.png") 
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")

if __name__ == "__main__":
    modules = check_dependencies()
    analyze_matrix(modules)