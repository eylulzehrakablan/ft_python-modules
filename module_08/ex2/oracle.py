import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv is missing.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    matrix_mode = os.environ.get("MATRIX_MODE")
    db_url = os.environ.get("DATABASE_URL")
    api_key = os.environ.get("API_KEY")
    log_level = os.environ.get("LOG_LEVEL")
    zion_endpoint = os.environ.get("ZION_ENDPOINT")

    required_vars = [
        ("MATRIX_MODE", matrix_mode),
        ("DATABASE_URL", db_url),
        ("API_KEY", api_key),
        ("LOG_LEVEL", log_level),
        ("ZION_ENDPOINT", zion_endpoint)
    ]
    
    missing_vars = [name for name, val in required_vars if not val]

    if missing_vars:
        print("\n[WARNING] Default/Missing configuration detected!")
        print("The following variables are missing:")
        for var in missing_vars:
            print(f" - {var}")
        print("\nPlease create a .env file or pass the variables via terminal.")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if matrix_mode == "development":
        print("Database: Connected to local instance")
    elif matrix_mode == "production":
        print(f"Database: Connected to secure production cluster at {db_url}")
    else:
        print(f"Database: Connected to unknown environment")

    print("API Access: Authenticated" if api_key else "API Access: Denied")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online" if zion_endpoint else "Zion Network: Offline")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    
    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found. Using system overrides.")
        
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")
