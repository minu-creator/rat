import random

# 미로 생성 함수
def generate_maze(size):
    maze = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row.append(1)
            else:
                row.append(random.randint(0, 1))
        maze.append(row)
    return maze

# 미로 출력 함수
def print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# 깊이 우선 탐색 함수
def dfs(maze, visited, row, col):
    if maze[row][col] == 1:
        return False
    if visited[row][col]:
        return False
    visited[row][col] = True
    if row == len(maze) - 2 and col == len(maze) - 2:
        return True
    if dfs(maze, visited, row - 1, col):
        return True
    if dfs(maze, visited, row + 1, col):
        return True
    if dfs(maze, visited, row, col - 1):
        return True
    if dfs(maze, visited, row, col + 1):
        return True
    return False

# 미로 생성 및 출력
maze = generate_maze(10)
print_maze(maze)

# 출발점과 도착점 설정
start = (1, 1)
end = (len(maze) - 2, len(maze) - 2)

# 깊이 우선 탐색으로 경로 탐색
visited = [[False for _ in range(len(maze))] for _ in range(len(maze))]
if dfs(maze, visited, start[0], start[1]):
    print("출발점에서 도착점까지 경로가 존재합니다.")
else:
    print("출발점에서 도착점까지 경로가 존재하지 않습니다.")


