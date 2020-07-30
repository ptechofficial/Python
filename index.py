import sys
import itertools


def all_same(current_list):
	if current_list.count(current_list[0])==len(current_list) and current_list[0]!=0:
		return True
	else:
		return False


def check_win(current_board):
	
	#Horizontal Win
	for row in current_board:
		
		if all_same(row):
			print(f'Player {row[0]} is the winner')
			return True
	
	# Vertical Win
	for i in range(len(current_board)):
		val_v=[]
		for j in range(len(current_board)):
			val_v.append(current_board[j][i])
		if all_same(val_v):
			print(f'Player {val_v[0]} is the winner')
			return True


	#Diagonal Win

	#Left Diagonal
	val_ld=[]
	
	for i  in range(len(current_board)):
		val_ld.append(current_board[i][i])
	if all_same(val_ld):
		print(f'Player {val_ld[0]} is the winner')
		return True

	#Right Diagonal
	val_rd=[]
	for k  in range(len(current_board)):
		for l in range(len(current_board)):
			if k+l==len(current_board)-1:
				val_rd.append(current_board[k][l])

	if all_same(val_rd):
		print(f'Player {val_rd[0]} is the winner')
		return True


	return False



def input_board(current_board,current_player):
	
	print("\tCurrent Player : ",current_player)
	row = int(input("In which row would you like to enter? (0,1,2) : "))
	col = int(input("In which col would you like to enter? (0,1,2) : "))

	try:
		if current_board[row][col] == 0:
			current_board[row][col] = current_player
		
		else:
			print('This position is already occupied, try again!')
			input_board(current_board,current_player)
	except IndexError as e:
		print("Make sure to enter row/col as 0, 1 or 2",e)
		input_board(current_board,current_player)
	except Exception as e:
		print("Something went wrong, try again",e)
		input_board(current_board,current_player)


def elem_print(el):
	if el == 1:
		return 'X'
	elif el == 2:
		return 'O'
	else:
		return ' '
def print_board(current_board):
	print('   '+'   '.join([str(i) for i in range(len(current_board))]))
 
	count = 0
	for row in current_board:
		elem_row = ''
		for col in row[:len(current_board)-1]:
			#print(col,end = '  ')
			elem_row+=elem_print(col)+' | '
		elem_row+=elem_print(row[len(current_board)-1])

		print(count,'',elem_row)
		if count!=len(current_board)-1:	
			print('  ------------')
		count+=1


play = True

while play:
	size =int(input("Enter size : "))
	count_input = 0
	
	board = [[0 for i in range(size)] for j in range(size)]
	
	game_won = False
	print_board(board)
	player_choice=itertools.cycle([1,2])	#to iterate over player 1 and 2
	while not game_won:
		

		current_player = next(player_choice)
		input_board(board, current_player)
		count_input += 1 
		print_board(board)
		if check_win(board) or count_input == 9:
			if count_input == 9:
				print("Sed ;_;, This game has been drawed")
			game_won = True
			choice = input("Do you want to play again? (y/n)")
			if choice.lower() == 'y':
				play = True
				print("		*Creating a new game")

			elif choice.lower() == 'n':
				play = False

				print("		*Exiting*")

			else:
				print("This choice is invalid, exiting anyway...")
		




sys.stdin.readline()	#to wait for the user to press a key

