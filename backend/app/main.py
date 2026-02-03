import uvicorn

from backend.app.app_factory import create_app
from backend.app.core.config import get_settings

settings = get_settings()


if __name__ == "__main__":
    app = create_app(settings)
    uvicorn.run(app, host="0.0.0.0", port=8000)