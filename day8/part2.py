from math import sqrt
from typing import NewType

Box = NewType('Box', tuple[int, int, int])
Connection = NewType('Connection', tuple[Box, Box, float])
Circuit = NewType('Circuit', set[Box])


def distance(p: Box, q: Box) -> float:
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    dz = p[2] - q[2]
    return sqrt(dx * dx + dy * dy + dz * dz)


def circuit_for_box(circuits: list[Circuit], box: Box) -> Circuit | None:
    for circuit in circuits:
        if box in circuit:
            return circuit
    return None


def main():
    boxes: list[Box] = []
    circuits: list[Circuit] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            parts = [int(p) for p in line.split(',')]
            box = Box((parts[0], parts[1], parts[2]))
            boxes.append(box)
            circuit = Circuit(set())
            circuit.add(box)
            circuits.append(circuit)
    connections: list[Connection] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            p = boxes[i]
            q = boxes[j]
            d = distance(p, q)
            connections.append(Connection((p, q, d)))
    connections.sort(key=lambda c: c[2])
    answer = 0
    for connection in connections:
        c1 = circuit_for_box(circuits, connection[0])
        assert c1 is not None
        c2 = circuit_for_box(circuits, connection[1])
        assert c2 is not None
        if c1 != c2:
            if len(circuits) == 2:
                answer = connection[0][0] * connection[1][0]
            c1.update(c2)
            circuits.remove(c2)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
