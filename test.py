import queue
from board import board



zero_field_row_column = [0,0]

frontier = queue.Queue()
explored = ()

graph = []



if __name__ == "__main__":
    board = board()
    print(board.finishedBoard)
    # print(board)
    # #build initialStateQueue
    # frontier = enqueue_moves(zero_field_row_column)
    # #put loop here
    # next_move = frontier.get_nowait()
    # is_finished, board = switch(zero_field_row_column, next_move)
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
