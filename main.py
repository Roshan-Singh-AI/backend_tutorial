import uvicorn
import os

if __name__ == "__main__":
    # Fetch port from environment or default to 8000
    port = int(os.getenv("PORT", 8000))

    # 1. Host: 0.0.0.0 allows external access (essential for Docker/Cloud)
    # 2. reload: False (Critical for performance)
    # 3. workers: Utilization of CPU cores (only works if app is passed as string)
    # 4. proxy_headers: True (If behind Nginx/AWS LB/Cloudflare)

    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=port,
        reload=False,
        workers=4,  # Adjust based on CPU cores
        proxy_headers=True
    )