import time
from fastapi import HTTPException, status

RATE_LIMIT = {}
MAX_REQUESTS = 5
WINDOW_SECONDS = 60


def rate_limiter(identifier: str):
    now = time.time()

    if identifier not in RATE_LIMIT:
        RATE_LIMIT[identifier] = []

    RATE_LIMIT[identifier] = [
        t for t in RATE_LIMIT[identifier]
        if now - t < WINDOW_SECONDS
    ]

    if len(RATE_LIMIT[identifier]) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again later."
        )

    RATE_LIMIT[identifier].append(now)
