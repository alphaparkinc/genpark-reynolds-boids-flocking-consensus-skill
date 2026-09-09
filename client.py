import math

class Boid:
    def __init__(self, bid, pos, vel):
        self.bid = bid
        self.pos = list(pos)
        self.vel = list(vel)

class ReynoldsFlock:
    """Craig Reynolds Distributed Boids Flocking Model."""
    def __init__(self, visual_range=10.0, sep_range=3.0):
        self.boids = []
        self.visual_range = visual_range
        self.sep_range = sep_range

    def add_boid(self, bid, pos, vel):
        self.boids.append(Boid(bid, pos, vel))

    def step(self, dt=0.5):
        new_boids = []
        for b in self.boids:
            neighbors = []
            close_neighbors = []
            for other in self.boids:
                if other.bid != b.bid:
                    dist = math.hypot(b.pos[0] - other.pos[0], b.pos[1] - other.pos[1])
                    if dist < self.visual_range:
                        neighbors.append(other)
                    if dist < self.sep_range:
                        close_neighbors.append(other)

            sep = [0.0, 0.0]
            for other in close_neighbors:
                sep[0] += (b.pos[0] - other.pos[0])
                sep[1] += (b.pos[1] - other.pos[1])

            align = [0.0, 0.0]
            if neighbors:
                avg_vx = sum(n.vel[0] for n in neighbors) / len(neighbors)
                avg_vy = sum(n.vel[1] for n in neighbors) / len(neighbors)
                align = [avg_vx - b.vel[0], avg_vy - b.vel[1]]

            cohesion = [0.0, 0.0]
            if neighbors:
                center_x = sum(n.pos[0] for n in neighbors) / len(neighbors)
                center_y = sum(n.pos[1] for n in neighbors) / len(neighbors)
                cohesion = [center_x - b.pos[0], center_y - b.pos[1]]

            ax = sep[0] * 1.5 + align[0] * 1.0 + cohesion[0] * 0.5
            ay = sep[1] * 1.5 + align[1] * 1.0 + cohesion[1] * 0.5

            new_vx = b.vel[0] + ax * dt
            new_vy = b.vel[1] + ay * dt
            new_x = b.pos[0] + new_vx * dt
            new_y = b.pos[1] + new_vy * dt
            new_boids.append(Boid(b.bid, [new_x, new_y], [new_vx, new_vy]))

        self.boids = new_boids
        return {b.bid: [round(b.pos[0], 2), round(b.pos[1], 2)] for b in self.boids}
