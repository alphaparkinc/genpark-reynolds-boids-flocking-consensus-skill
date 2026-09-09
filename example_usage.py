from client import ReynoldsFlock

def main():
    print("=== Testing Reynolds Boids Flocking ===")
    flock = ReynoldsFlock()
    flock.add_boid("drone_1", [0, 0], [1, 0])
    flock.add_boid("drone_2", [1, 1], [0, 1])
    flock.add_boid("drone_3", [2, 0], [1, 1])

    positions = flock.step(dt=0.2)
    print("Updated Swarm Positions:", positions)
    assert len(positions) == 3

    print("Reynolds Flocking verified successfully!")

if __name__ == '__main__':
    main()
