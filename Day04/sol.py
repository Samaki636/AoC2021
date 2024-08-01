def main():
    print(compute_result(*play(*read_input())))
    print(compute_result(*play_part2(*read_input())))


def read_input():
    board_index = 0
    row_index = 0
    boards = [[]]
    with open("input02.txt", "r") as infile:
        drawn_numbers = infile.readline().split(",")

        infile.readline()

        for line in infile:
            if len(line) == 1:
                boards.append([])
                board_index += 1
                row_index = 0
            else:
                boards[board_index].append([])
                numbers = line.split()
                boards[board_index][row_index] = numbers
                row_index += 1
    return boards, drawn_numbers


def play(boards, drawn_numbers):
    col_x_count = 0
    for drawn_number in drawn_numbers:
        for board in boards:
            for line in board:
                for i in range(len(line)):
                    if line[i] == drawn_number:
                        line[i] = 'X'
                if line.count("X") == 5:
                    return board, drawn_number
            for i in range(len(board[0])):
                for j in range(len(board)):
                    if board[j][i] == "X":
                        col_x_count += 1
                if col_x_count == 5:
                    return board, drawn_number
                else:
                    col_x_count = 0


def play_part2(boards, drawn_numbers):
    last_board = boards[0]
    last_drawn_number = drawn_numbers[0]
    boards_to_win = [True for _ in boards]
    col_x_count = 0
    for drawn_number in drawn_numbers:
        for n, board in enumerate(boards):
            if boards_to_win[n]:
                for line in board:
                    for i in range(len(line)):
                        if line[i] == drawn_number:
                            line[i] = 'X'
                    if line.count("X") == 5:
                        last_board, last_drawn_number = board, drawn_number
                        boards_to_win[n] = False
                for i in range(len(board[0])):
                    for j in range(len(board)):
                        if board[j][i] == "X":
                            col_x_count += 1
                    if col_x_count == 5:
                        last_board, last_drawn_number = board, drawn_number
                        boards_to_win[n] = False
                    else:
                        col_x_count = 0
    return last_board, last_drawn_number


def compute_result(board, last_number):
    result = 0
    for line in board:
        for n in line:
            if n != "X":
                result += int(n)
    return result * int(last_number)


if __name__ == '__main__':
    main()
