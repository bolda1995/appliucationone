import logging
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        # Read and log the response content
        if hasattr(response, "body"):
            response_body = await response.body()
            logging.info(f"Response - Status Code: {response.status_code}, Content: {response_body.decode()}")
        else:
            logging.warning("Response content could not be logged.")

        return response


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='app.log',
    filemode='w'
)