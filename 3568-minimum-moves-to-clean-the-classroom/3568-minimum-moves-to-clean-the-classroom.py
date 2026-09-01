from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        rows = len(classroom)
        cols = len(classroom[0])

        litter_id = {}
        start_r = start_c = 0
        count = 0

        # Find start and give each litter an ID
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = count
                    count += 1

        # No litter
        if count == 0:
            return 0

        # If there are count litter pieces,
        # target_mask will have count 1s.
        target_mask = (1 << count) - 1

        # (moves, row, col, mask, remaining_energy)
        q = deque()
        q.append((0, start_r, start_c, 0, energy))

        # (row, col, mask) -> maximum energy seen
        visited = {}
        visited[(start_r, start_c, 0)] = energy

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:
            moves, r, c, mask, curr_energy = q.popleft()

            if curr_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid or wall
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                next_energy = curr_energy - 1
                next_mask = mask

                # Recharge
                if classroom[nr][nc] == 'R':
                    next_energy = energy

                # Collect litter
                if classroom[nr][nc] == 'L':
                    litter_number = litter_id[(nr, nc)]
                    next_mask |= (1 << litter_number)

                # All litter collected
                if next_mask == target_mask:
                    return moves + 1

                state = (nr, nc, next_mask)

                # Only keep this state if we have more energy
                if state not in visited or next_energy > visited[state]:
                    visited[state] = next_energy
                    q.append(
                        (moves + 1, nr, nc, next_mask, next_energy)
                    )

        return -1