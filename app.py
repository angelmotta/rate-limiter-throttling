from flask import Flask
from flask import jsonify
from throttle import Throttle
from slidingRateLimiter import SlidingWindowRateLimiter

app = Flask(__name__)
myThrottle = Throttle(maxReq=100, waitTimeToReset=120)
mySlidingRateLimiter = SlidingWindowRateLimiter(limit=10, window_size=1)

@app.route('/rate-limit-me')
def rateLimit():
    if mySlidingRateLimiter.allow_request():
        return jsonify(Result="Rate-Limit-Success"), 200
    else:
        return jsonify(Result="Rate-Limit-Failure"), 429


@app.route('/throttle-me')
def throttle():
    if myThrottle.isAllowed():
        return jsonify(Result="Throttle-Limit-Success"), 200
    else:
        return jsonify(Result="Throttle-Limit-Failure"), 429

if __name__ == "__main__":
    app.run(debug=True, port=7000)
