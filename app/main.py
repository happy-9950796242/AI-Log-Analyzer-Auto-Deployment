from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="AI Log Analyzer & Auto Deployment",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Log Analyzer is running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    # Read uploaded file
    content = await file.read()

    # Convert bytes to text
    text = content.decode("utf-8", errors="ignore")

    # Split into lines
    lines = text.splitlines()

    # Count log levels
    info_count = 0
    warning_count = 0
    error_count = 0

    for line in lines:
        upper_line = line.upper()

        if "ERROR" in upper_line:
            error_count += 1

        elif "WARNING" in upper_line or "WARN" in upper_line:
            warning_count += 1

        elif "INFO" in upper_line:
            info_count += 1

    return {
        "message": "Log analyzed successfully",
        "filename": file.filename,
        "total_lines": len(lines),
        "info_count": info_count,
        "warning_count": warning_count,
        "error_count": error_count
    }