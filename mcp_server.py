import sys
import json
from client import ReynoldsFlock

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "simulate_flock":
        flock = ReynoldsFlock(params.get("range", 10.0))
        for b in params.get("boids", []):
            flock.add_boid(b.get("id"), b.get("pos"), b.get("vel"))
        return {"positions": flock.step(params.get("dt", 0.5))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
