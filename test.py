import queue
from board import board

initList = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]

if __name__ == "__main__":
    board = board(initList, [0,1])
    print(board.instance)

    frontier = queue.Queue()
    explored = set()

    for neighbour in board.zeroTile.neighbors:
        if neighbour is not None:
            frontier.put_nowait(board.switch(neighbour))

    while not frontier.empty():
        board = frontier.get_nowait()
        explored.add(board)

        print(board.instance)
        if board.isFinished():
            print("implement do finished")




    # print(instance)
    # #build initialStateQueue
    # frontier = enqueue_moves(zero_field_row_column)
    # #put loop here
    # next_move = frontier.get_nowait()
    # is_finished, instance = switch(zero_field_row_column, next_move)
    #
    # if up is not None:
    #     frontier.put_nowait(up)
    # if down is not None:
    #     frontier.put_nowait(down)
    # if left is not None:
    #     frontier.put_nowait(left)
    # if right is not None:
    #     frontier.put_nowait(right)
    # return frontier

    #if(is_finished):
    # print("implement save moves")
