##CS 101
##Program 8 - SuperSweeper
##JJC7WB@mail.umkc.edu
##John Clement
##
##PROBLEM: This is a slight variation of the game "MineSweeper".  The user chooses
##how many rows, columns, as well as how many of the tiles at those rows and columns
##will be mines and special tiles.  The special tiles work like this:  When selected
##by the user to be uncovered, they display any mine tiles that are touching it from
##any direction without ending the game, giving you an edge on finding all the mine
##tiles so you can progress toward uncovering all of the regular tiles and win the game.
##If the user selects a regular tile, then it displays how many mine tiles it is in contact with.
##If the user selects a mine tile, the game is over and all the tiles are uncovered on
##the board.  At the end of the game, an option is given to restart the game.
##
##ALGORITHM:
##
##We'll have 4 classes, which are:
##  Tile
##      attributes:
##          row
##          hidden
##          __value
##          mine_count
##  MineTile
##      attributes:
##          row
##          col
##          board
##  ShowMinesTile
##      attributes:
##          row
##          col
##          board
##  SuperSweeperBoard
##      attributes:
##          __board (list of lists)
##          output_board (list of lists)
##          game_state (integer, 0 = playing,1 = Game Over w/ Win,2 = Game Over w/ Loss)
##          rows = (integer)
##          cols = (integer)
##          mine_count = (integer)
##
##
##At the beginning of the game I will start out by asking the user for the following
##things:
##  Amount of rows for the Mine Board
##      validation:
##          if rows < 3:
##              -board assigned 3 rows
##          elif rows > 12:
##              -board assigned 12 rows
##          else:
##              -otherwise, assigned the amount of rows specified by the user
##  Amount of columns for the Mine Board
##      validation:
##          if columns < 3:
##              -board assigned 3 columns
##          elif rows > 12:
##              -board assigned 12 columns
##          else:
##              -otherwise, assigned the amount of columns specified by the user
##  Amount of MineTile objects to put as tile objects onto the board
##      validation:
##          if mine_count < 1:
##              -board assigned 1 mine tile
##          elif mine_count > number of positions available (rows*columns):
##              -board assigned the value of (rows*columns)
##          else:
##              -otherwise, assigned the amount of mines specified by the user
##  Amount of ShowMinesTile objects to put as tile objects onto the board
##      validation:
##          if ShowMineTiles < 0:
##              -board assigned 0 ShowMineTiles
##          elif ShowMineTiles > number of positions left: ((rows*columns)-mine_count)
##              -board assigned the number of positions left
##          else:
##              -otherwise, assigned the amount of showmine tiles specified by the user
##
##
##
##
##Next, I'll create an instance of the SuperSweeperBoard object:
##      -While in the process of the SuperSweeperBoard instance being created, the following numbered substeps
##       will be executed:
##               1a. Create the amount of indexes on the grid by initially placing empty quotes in each index on
##                   the board, like this:
##              -----------------------------
##             |  ex: 3 rows, 3 columns >>
##             |      0    1    2
##             |
##             |  0   ""   ""   "" 
##             |
##             |  1   ""   ""   ""
##             |
##             |  2   ""   ""   ""
##              ------------------------------
##
##               1b. Put Mine Tiles on the board, say we have 3
##              -----------------------------
##             |  ex: 3 rows, 3 columns >>
##             |      0      1      2
##             |
##             |  0   Mine   ""     "" 
##             |
##             |  1   ""     Mine   Mine
##             |
##             |  2   ""     ""     ""
##              ------------------------------
##
##               1c. Put ShowMine Tiles on the board, say we have 1.
##              -----------------------------
##             |  ex: 3 rows, 3 columns >>
##             |      0      1      2
##             |
##             |  0   Mine   ""     ShowMineTile 
##             |
##             |  1   ""     Mine   Mine
##             |
##             |  2   ""     ""     ""
##              ------------------------------
##
##               1d. Put regular Tile objects on the board in any places that still have empty quotes as their value.
##              -----------------------------
##             |  ex: 3 rows, 3 columns >>
##             |      0      1      2
##             |
##             |  0   Mine   Tile   ShowMineTile 
##             |
##             |  1   Tile   Mine   Mine
##             |
##             |  2   Tile   Tile   Tile
##              ------------------------------
##
##              1e. For each tile type placed on the board we will have a list, recording all the indexes of each type.
##                  Mine_Indexes = [(0,0),(1,1),(1,2)]
##                  ShowMineIndexes = [(0,2)]
##                  Regular_Tile_Indexes = [(0,1),(1,0),(2,0),(2,1),(2,2)]
##
##
##Next, we display the board with all tiles in a hidden state, displaying "H" for their value
##Next, we ask the user which row and column they'd like to choose to uncover.
##    -If the user selects an index that has a regular Tile object at it's index, the board is reloaded with the
##     tile's value displayed.  The regular tile's value is the number of mines that are in contact with the tile.
##    -If the user selects an index that has a ShowMineTile object at it's index, the board is reloaded with the
##     ShowMineTile's value displayed, as well as displaying the value for any MineTile objects that are touching
##     the tile.
##    -If the user selects an index that has a MineTile object at it's index, the board is reloaded with all of the
##     tiles uncovered, displaying all values of MineTiles, ShowMineTiles, and regular Tiles.
##    -If at any point the user chooses the index to uncover that happens to be a MineTile object or Wins the game
##     by uncovering all the non-mine tiles, then they will be prompted with a choice to play again or not.  If they
##     choose to play again, they will have to enter the number of rows, columns, mines, and showmine tiles over again.
##     If the user chooses not to play again, the game will be exited.
##
##ERROR HANDLING:
##
##
##
##
########################################################################################################################################################################################################################################








##Notes:
##    --------------------------------------------------------------------------------------------------------
##Section 1:
##
##
##
####Algorithm
##1. create SuperSweeperBoard
##	1a. create indexes with empty quotes at each index
##	1b. put mine tiles on board
##
##	*at this point the board looks like this:
##	5 rows, 5 columns, 10 mines, 2 show mines
##	
##	[[Mine,""   ,""   ,Mine ,""]
##	[""  ,""   ,Mine ,Mine ,""]
##	[""  , Mine, ""  , ""  , ""]
##	[Mine, Mine, Mine, Mine, ""]
##	[""  ,Mine ,""   ,""   , ""]]
##
##	Mine indexes = (0,0),(0,3),(1,2),(1,3),(2,1),(3,0),(3,1),(3,2),(3,3),(4,1)
##	**mine indexes stored in <board_object>.MineIndexes (list object)
##
##	
##
##
##	1c. put show_mine_tiles on board
##	[[Mine,ShowMine  ,""   ,Mine      ,""]
##	[""  ,""         ,Mine ,Mine      ,""]
##	[""  , Mine      , ""  ,ShowMine  , ""]
##	[Mine, Mine      , Mine, Mine     , ""]
##	[""  ,Mine       ,""   ,""        , ""]]
##
##	Mine indexes = (0,1),(2,3)
##	**mine indexes stored in <board_object>.ShowMineIndexes (list object)
##
##
##
##	1d. put regular tiles at the rest of the indexes that have empty quotes in them.
##		1da. say we are placing a regular tile at (0,2) on the board...
##			check <board_object>.MineIndexes for the following indexes: <list_of_neighboring_indexes>
##				search <board_object>.MineIndexes to see how many of the items in the list of neighboring objects are in mine tiles
##					assign this number to tile object's <tile_object>.mine_count attribute.
##						if the number is 0, assign empty quotes as the value
##--------------------------------------------------------------------------------------------------------
##
##Section 1 code:
##
##
####Pseudo code
##a = How many rows for board?
##b = How many columns for board?
##c = How many mines for board?
##d = How many show mine tiles for board?
##e = SuperSweeperBoard(a,b,c,d)
##
##	##SuperSweeperBoard __init__ function:
##	attributes are: 
##		__board
##		output_board
##		game_state
##		rows
##		cols
##		mines
##
##
##
##
##	##initialize the rows and columns in the output_board attribute with "H" listed at each index
##	big_list1 = list()
##	temp_list1 = list()	
##	for obj4 in range(0,self.rows):
##		for obj5 in range(0,self.columns):
##			temp_list1.append("H")
##		big_list1.append(temp_list)
##		temp_list1 = list()
##
##	self.output_board = big_list1
##
##
##
##	big list2 = list()
##	temp_list2 = list()
##	for obj1 in range(0,self.rows):
##		for obj2 in range(0,self.columns):
##			temp_list2.append("")
##		big_list2.append(temp_list)
##		temp_list2 = list()
##
##	##at this point there should be ___# rows and ___# columns in the grid (big_list)
##
##
##	##add the mine tile objects
##	for indexa,obj3 in enumerate(self._SuperSweeperBoard__board):
##		for indexb,obj4 in enumerate(obj3):
##			if (indexa,indexb) in mine_indexes_used:
##				self._SuperSweeperBoard__board[indexa][indexb] = MineTile(self,indexa,indexb)
##	
##	##add the showtile objects and set their mine counts
##	for indexa,obj3 in enumerate(self._SuperSweeperBoard__board):
##		for indexb,obj4 in enumerate(obj3):
##			if (indexa,indexb) in show_indexes_used:
##				self._SuperSweeperBoard__board[indexa][indexb] = ShowMineTile(self,indexa,indexb)
##				if indexa == 0:
##					if indexb == 0:
##						indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb+1])]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb])
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##
##                    		elif indexa == -1:
##                        		if indexb == 0:
##                           			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(MasterList[indexa-1][indexb]),   
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                    		else:
##                        		if indexb == 0:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1])
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1])							    
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                
##  
##				self._SuperSweeperBoard__board[indexa][indexb]._Tile__value = mine_count
##
##
##
##
##
##	##add the regular tile objects and set their mine counts
##	for indexa,obj3 in enumerate(self._SuperSweeperBoard__board):
##		for indexb,obj4 in enumerate(obj3):
##			if (indexa,indexb) in reg_tile_indexes_used:
##				self._SuperSweeperBoard__board[indexa][indexb] = Tile(self,indexa,indexb)
##				if indexa == 0:
##					if indexb == 0:
##						indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb+1])]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb])
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##
##                    		elif indexa == -1:
##                        		if indexb == 0:
##                           			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(MasterList[indexa-1][indexb]),   
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                    		else:
##                        		if indexb == 0:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1])
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		elif indexb == -1:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                        		else:
##                            			indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                type(self._SuperSweeperBoard__board[indexa-1][indexb+1])							    
##                                               ]
##						mine_count = 0
##						for item in indexes_to_check:
##							if "MineTile" in str(item):
##								mine_count += 1
##						self._SuperSweeperBoard__board[indexa][indexb].mine_count = mine_count
##                
##  
##				self._SuperSweeperBoard__board[indexa][indexb]._Tile__value = mine_count
##
##			
##
##
##
####ripple effect function:
##def ripple_effect(row,col):
##	for indexa,obj3 in enumerate(self._SuperSweeperBoard__board):
##			for indexb,obj4 in enumerate(obj3):
##				if (indexa,indexb) in show_indexes_used:
##					self._SuperSweeperBoard__board[indexa][indexb] = Tile(self,indexa,indexb)
##					if row == 0:
##						if col == 0:
##							self.output_board[row][col] = self._SuperSweeperBoard[i][ii]._ShowMineTile__value
##							indexes_that_were_mines = list()
##							indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##								    type(self._SuperSweeperBoard__board[indexa+1][indexb+1])]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value		
##
##                        			elif col == -1:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb])
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                        			else:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                	]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##
##                    			elif row == -1:
##                        			if col == 0:
##							indexes_that_were_mines = list()
##                           				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                        			elif col == -1:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                	type(MasterList[indexa-1][indexb]),   
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                        			else:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb+1]),
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                    			else:
##                        			if col == 0:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb+1])
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                        			elif col == -1:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                        			else:
##							indexes_that_were_mines = list()
##                            				indexes_to_check = [type(self._SuperSweeperBoard__board[indexa][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa+1][indexb+1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb-1]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb]),
##                                                	type(self._SuperSweeperBoard__board[indexa-1][indexb+1])							    
##                                               		]
##							mine_count = 0
##							for indexc,item in enumerate(indexes_to_check):
##								if "MineTile" in str(item):
##									mine_count += 1
##									if indexc == 0 and "MineTile" in str(item):
##										indexes_that_were_mines.append((0,1))
##									elif indexc == 1 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,0))
##									elif indexc == 2 and "MineTile" in str(item):
##										indexes_that_were_mines.append((1,1))
##							##Loop through all the items in "indexes_that_were_mines" and display the values for any mine objects touching this show tile.
##							for i,ii in indexes_that_were_mines:									
##								self.output_board[i][ii] = self._SuperSweeperBoard__board[i][ii]._MineTile__value
##                
##  
####after the ripple effect the tiles have changed like this:
#### 5,2 chosen by user
##		 _______________________
##		| H | H |   H   | H | H |
##		--------------------
##		| H | H |   H   | H | H |
##		--------------------
##		| H | H |   H   | H | H |
##		--------------------
##		| H | * |   *   | H | H |
##		--------------------
##		| H | * |   3   | H | H |
##		--------------------						
##
##
##
##
##__show all function:
##for indexa,row in enumerate(self._SuperSweeperBoard__board):
##	for indexb, column in enumerate(self._SuperSweeperBoard__board):
##		if "MineTile" in str(type(column)):
##			self.output_board[indexa][indexb] = "*"
##		elif "ShowMineTile" in str(type(column)):
##			self.output_board[indexa][indexb] = self._SuperSweeperBoard__board._ShowMineTile__value
##		elif "Tile" in str(type(column)):
##			self.output_board[indexa][indexb] = self._SuperSweeperBoard__baord._Tile__value
##
##
####at this point ive covered the following:
##	1. if the user types in the index of a mine tile, the __show all function for the supersweeperboard is called and all the board pieces are displayed
##	2. if the user types in the index of a showmine tile, the tile clicked on + any mine tiles touching this showmine tile are added to the output_board and displayed
##	3. if the user types in the index of a regular tile, the tile is uncovered, displaying the number of mines that are touching it. 	
##
##




import random


class Tile(object):
    """ Represents a single Tile on the board.
            The Tile contains the following information
                board : SuperSweeperBoard.  This is the board th tile is on.
                hidden :  boolean.  True if the tile value is hidden, False if it is showing.
                __value : String. The value to show for the tile as string output ( assuming it's not hidden )
                row : int.  The row this tile is on the board.
                col : int.  The column this tile belongs to on the board.
                __mine_count : int.  The number of mines surrounding this tile. """
    def __init__(self, mine_board, row, col):
        """ Initializes the Tile object.
        :param mine_board: The board this tile is on.
        :param row: The row this tile occupies
        :param col: The col this tile occupies
        :return: Nothing

        Modifications : Sets the instance to the proper state on starting.

        Errors Handled : None
        """
        # Replace the following with your code to make the method perform properly
        self.mine_board = mine_board
        self.row = row
        self.column = col
        self.mine_count = 0
        self.hidden = True
        self.__value = ""
        mines_for_this_tile = list()

    def __str__(self):
        """  Returns a string Representation of the tile.
        :return: str.  This is the string representation of the Tile.  If the tile is hidden it will return "H",
                    otherwise it should return the value of the Tile.
        """
        # Replace the following with your code to make the method perform properly
        return self.mine_count 

    def increment_mine_count(self):
        """ increments the number of mines by 1.
        :return: Nothing

         Modifications : Increments the count of the mines and __value attribute
                            to reflect the current value of the Tile.
        """
        # Replace the following with your code to make the method perform properly
        pass
    
    def set_mine_count(self, mines):
        """ Sets the number of mines around this tile.
        :param mines: The number of mines around this tile.
        :return: Nothing

            Modifications : Changes the __mine_count attribute and also updates the value to display from __str__

        """
        # Replace the following with your code to make the method perform properly
        pass

    def uncover(self):
        """ Uncovers this mine.
        :return: Nothing

        Modifications : Uncovers this Tile piece.  It will uncover it's neighboring pieces if necessary.
                        See rules for when and what parts to uncover.

                        Part of this method may need to wait until you've implemented the get_tile method in SuperSweeperBoardClass
        """

        # Replace the following with your code to make the method perform properly
        pass        


class ShowMinesTile(Tile):
    """  Shows all mines around it, it is a normal tile as well

        This acts like a normal mine, but when uncovered it will show any mines around itself.
    """
    def __init__(self, mine_board, row, col):
        """ Initializes the ShowMinesTile
        :param mine_board: The board this tile is on.
        :param row: The row this tile occupies
        :param col: The col this tile occupies
        :return: Nothing
        """
        # Replace the following with your code to make the method perform properly
        self.mine_board = mine_board
        self.row = row
        self.column = col
        self.mine_count = 0
        self.hidden = True
        self.__value = ""
        self.mines_for_this_tile = list

    def uncover(self):
        """ Uncovers this tile.
        :return: Nothing

        Modifications : This will do the normal modifications of a Tile ( see above ), but will also show any mines that
                            happen to be around it.

                        Part of this method may need to wait until you've implemented the get_tile method in SuperSweeperBoardClass

        """
        # Replace the following with your code to make the method perform properly
        pass

       

class MineTile(Tile):
    """ This is a Mine Tile.  It has all the same functionality of a tile, but the value to display is an asterisk * """
    def __init__(self, mine_board, row, col):
        """ Initializes the MineTile
        :param mine_board: The board this tile is on.
        :param row: The row this tile occupies
        :param col: The col this tile occupies
        :return: Nothing

        Modifications : Initializes the Tile the same as the superclass Tile, but sets the __value to be an *
        """
        # Replace the following with your code to make the method perform properly
        self.mine_board = mine_board
        self.row = row
        self.col = col
        self.hidden = True
        

    def __str__(self):
        """  Returns a string Representation of the tile.
        :return: str.  This is the string representation of the Tile.  If the tile is hidden it will return "H",
                    otherwise it should return the *
        """
        # Replace the following with your code to make the method perform properly
        return "*"        



class SuperSweeperBoard(object):
    """ Classic game of minesweeper with some new elements.
            This class contains the following information
                rows : int.  The number of rows on the board
                cols : int.  The number of columns on the board.
                mines : int.  The number of mines on the board.
                __board : list.  Contains a list of rows on the board.  Each row is a list of the tiles.
                game_state : int.  This is the state of the game.   0 : playing
                                                                    1 : Game Over Playing Won
                                                                    2 : Game Over Player Lost
                """

    def __init__(self, rows=5, columns=5, mine_count=10, show_mine_tiles=0):
        """  Initializes the Minesweeper Board
        :param rows: int  The Number of rows in our board
        :param columns: int.  The number of columns on our board.
        :param mine_count: int.  The number of mines on our board.
        :param show_mine_tiles:  The number of show mine tiles to place on our board.

        Modifications : __init__ will setup the attributes to the beginning state of the game.
                        The init will setup the __board for the number of rows and columns.
                        Each element in __board is a Tile.
                        There will be mines placed randomly on the board corresponding to the mine_count number.
                        There will be as many ShowMineTiles randomly placed on the board as parameter show_mine_tiles
                        It should also set the # of mines for each tile based on how many mines are around it.
                        The Gamestate should be set to the initial game state.

        Error Handled : if rows is less than 3 then it will be set to 3.
                        if rows is greater than 12 then it will be set to 12
                        if columns is less than 3 then it will be set to 3
                        if columns is greater than 12 then it will be set to 12
                        mine_count must be greater than 0, and less or equal to the number of positions available.
                            If the board is 10x10, then there are 100 places to put a mine.
                            ( although it'll be a short game ).
                            If mine_count violates either then it is set to the appropriate value.
                            if it's less than 1, then it is assigned 1.
                            If it is greater than the positions available then it is set to the # of cells
                        show_mine_tiles not be less than 0, but it can be zero.
                            If it is greater than the # of positions left after the mines have been placed, then it is
                            set to the number of positions left.

        :return: Nothing
        """
        # Replace the following with your code to make the method perform properly

        self.mine_indexes_used = list()
        self.show_indexes_used = list()
        self.reg_tile_indexes_used = list()
        self.any_indexes_used = list()
        self.show_mines_record_dict = dict()
        self.regular_tiles_record_dict = dict()
        self.show_mines_uncovered = list()
        self.h_board = list()
        self.ST = ShowMinesTile(0,0,0)
        self.RT = Tile(0,0,0)
        self.MT = MineTile(0,0,0)
        
        if rows < 3:
            self.rows = 3
        elif rows > 12:
            self.rows = 12
        else:
            self.rows = rows

        if columns < 3:
            self.columns = 3
        elif columns > 12:
            self.columns = 12
        else:
            self.columns = columns

        self.total_cells = int(self.rows)*int(self.columns)
        total = int(self.rows)*int(self.columns)
        if mine_count < 1:
            self.mine_count = 1
        elif mine_count > total:
            self.mine_count = total
        else:
            self.mine_count = mine_count

        left1 = total - int(self.mine_count)
        if show_mine_tiles < 0:
            self.show_mine_tiles = 0
        elif show_mine_tiles > left1:
            self.show_mine_tiles = left1
        else:
            self.show_mine_tiles = show_mine_tiles

        self.game_state = 0
        self.__board = list()
        big_list1 = list()
        temp_list1 = list()
        for obj1 in range(0,self.rows):
            for obj2 in range(0,self.columns):
                temp_list1.append("H")
            big_list1.append(temp_list1)
            temp_list1 = list()
        self.output_board = big_list1

        big_list2 = list()
        temp_list2 = list()
        for obj3 in range(0,self.rows):
            for obj4 in range(0,self.columns):
                temp_list2.append("")
            big_list2.append(temp_list2)
            temp_list2 = list()

        
        
        done = "n"
        while done == "n":
            row = random.randrange(0,self.rows)
            col = random.randrange(0,self.columns)
            if (row,col) not in self.mine_indexes_used:
                if int(len(self.mine_indexes_used)) == int(self.mine_count):
                    break
                elif (row,col) in self.any_indexes_used:
                    continue
                else:
                    self.mine_indexes_used.append((row,col))
                    self.any_indexes_used.append((row,col))



        left2 = (int(total)-int(self.mine_count))-int(self.show_mine_tiles)
        for ii in range(0,self.show_mine_tiles):
            done = "n"
            while done == "n":
                row = random.randrange(0,self.rows)
                col = random.randrange(0,self.columns)
                if (row,col) not in self.any_indexes_used:
                    self.show_indexes_used.append((row,col))
                    self.any_indexes_used.append((row,col))
                    break

        for iii in range(0,left2):
            done = "n"
            while done == "n":
                row = random.randrange(0,self.rows)
                col = random.randrange(0,self.columns)
                if (row,col) not in self.any_indexes_used:
                    self.reg_tile_indexes_used.append((row,col))
                    self.any_indexes_used.append((row,col))
                    break


                  
        ##add the mine objects
        for indexa in range(0,self.rows):
            for indexb in range(0,self.columns):
                if (indexa,indexb) in self.mine_indexes_used:
                    big_list2[indexa][indexb] = MineTile(self,indexa,indexb)
                    self.any_indexes_used.append((indexa,indexb))



        MT = MineTile(0,0,0)
        RT = Tile(0,0,0)
        ST = ShowMinesTile(0,0,0)




        print("fuck 0")
        counter1 = 0
        counter2 = 0
        length_row = self.columns
        length_rows = self.rows
        ##add the show mine tiles
        for indexa in range(0,self.rows):            
            for indexb in range(0,self.columns):                            
                if (indexa,indexb) in self.show_indexes_used:
                    big_list2[indexa][indexb] = ShowMinesTile(self,indexa,indexb)
                    self.any_indexes_used.append((indexa,indexb))
                    if indexa == 0:
                        print("fuck 0a")
                        if indexb == 0:                         
                            mine_indexes1 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1])]

                            mine_count1 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                if item == type(self.MT):
                                    if indexc == 0:
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes1:                                             
                                                mine_indexes1.append((counter1,counter2+1))
                                                mine_count1 += 1                                            
                                    elif indexc == 1:                                      
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes1:                                            
                                                mine_indexes1.append((counter1+1,counter2))
                                                mine_count1 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1+1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes1:                                            
                                                mine_indexes1.append((counter1+1,counter2+1))
                                                mine_count1 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count1

                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes1

                        elif counter2 == length_row-1:
                            print("fuck 0b")
                          
                            mine_indexes2 = list()                                                       
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb])]
                            mine_count2 = 0
                            for indexc,item in enumerate(indexes_to_check):                                
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes2:                                            
                                                mine_indexes2.append((counter1,counter2-1))
                                                mine_count2 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1-1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes2:                                             
                                                mine_indexes2.append((counter1-1,counter2-1))
                                                mine_count2 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes2:                                             
                                                mine_indexes2.append((counter1-1,counter2))
                                                mine_count2 += 1                                            
                                    elif indexc == 3:                                       
                                        if (counter1+1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes2:                                             
                                                mine_indexes2.append((counter1+1,counter2-1))
                                                mine_count2 += 1                                            
                                    elif indexc == 4:                                       
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes2:                                             
                                                mine_indexes2.append((counter1+1,counter2))
                                                mine_count2 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count2

                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes2                                        
                            
                         
                        else:
                            print("0c")                            
                            mine_indexes3 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1])]
                            mine_count3 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes3:                                            
                                                mine_indexes3.append((counter1,counter2-1))
                                                mine_count3 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes3:                                            
                                                mine_indexes3.append((counter1,counter2+1))
                                                mine_count3 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1+1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes3:                                            
                                                mine_indexes3.append((counter1+1,counter2-1))
                                                mine_count3 += 1                                            
                                    elif indexc == 3:                                       
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes3:                                            
                                                mine_indexes3.append((counter1+1,counter2))
                                                mine_count3 += 1                                            
                                    elif indexc == 4:                                        
                                        if (counter1+1,counter2+1) in self.mine_indexes_used:                                          
                                            if (counter2,counter2-1) not in mine_indexes3:                                            
                                                mine_indexes3.append((counter1+1,counter2+1))
                                                mine_count3 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count3

                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes3
##                                                                   
                            
##
                    elif indexa == length_rows-1:
                        print("0d")                        
                        if indexb == 0:                          
                            mine_indexes4 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count4 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes4:                                             
                                                mine_indexes4.append((counter1+1,counter2))
                                                mine_count4 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes4:                                            
                                                mine_indexes4.append((counter1-1,counter2))
                                                mine_count4 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1-1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes4:                                            
                                                mine_indexes4.append((counter1-1,counter2+1))
                                                mine_count4 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count4
                            
                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes4                                       
                            
                        elif indexb == length_row-1:
                            print("0e")
                            print("Indexa: {}, Indexb: {}".format(indexa,indexb))
                           
                            mine_indexes5 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb])]
                            mine_count5 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes5:                                             
                                                mine_indexes5.append((counter1,counter2-1))
                                                mine_count5 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1-1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes5:                                             
                                                mine_indexes5.append((counter1-1,counter2-1))
                                                mine_count5 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes5:                                             
                                                mine_indexes5.append((counter1-1,counter2))
                                                mine_count5 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count5
                            
                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes5                                      
                            
                            
##                            mine_indexes6 = list()                            
##                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
##                                                type(big_list2[indexa-1][indexb-1]),
##                                                type(big_list2[indexa-1][indexb])]
##                            mine_count6 = 0
##                            for indexc,item in enumerate(indexes_to_check):
##                                
##                                if item == type(self.MT):
##
##                                    if indexc == 0:                                        
##                                        if (counter1,counter2-1) in self.mine_indexes_used:
##                                            if (counter2,counter2-1) not in mine_indexes6:                                            
##                                                mine_indexes6.append((counter1,counter2-1))
##                                                mine_count6 += 1                                            
##                                    elif indexc == 1:                                       
##                                        if (counter1,counter2+1) in self.mine_indexes_used:
##                                            if (counter2,counter2-1) not in mine_indexes6:                                             
##                                                mine_indexes6.append((counter1,counter2+1))
##                                                mine_count6 += 1                                            
##                                    elif indexc == 2:                                       
##                                        if (counter1-1,counter2) in self.mine_indexes_used:
##                                            if (counter2,counter2-1) not in mine_indexes6:                                             
##                                                mine_indexes6.append((counter1-1,counter2-1))
##                                                mine_count6 += 1                                            
##                                    elif indexc == 3:                                          
##                                        if (counter1-1,counter2) in self.mine_indexes_used:
##                                            if (counter2,counter2-1) not in mine_indexes6:                                             
##                                                mine_indexes6.append((counter1-1,counter2))
##                                                mine_count6 += 1                                            
##                                    elif indexc == 4:                                        
##                                        if (counter1-1,counter2+1) in self.mine_indexes_used:
##                                            if (counter2,counter2-1) not in mine_indexes6:                                             
##                                                mine_indexes6.append((counter1-1,counter2+1))
##                                                mine_count6 += 1                                            
##                            big_list2[indexa][indexb].mine_count = mine_count6
##
##                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes6                                        
                            
                    else:
                        print("0f")                        
                        if indexb == 0:

                            mine_indexes7 = list()
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count7 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes7:                                             
                                                mine_indexes7.append((counter1,counter2+1))
                                                mine_count7 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes7:                                            
                                                mine_indexes7.append((counter1+1,counter2))
                                                mine_count7 += 1                                            
                                    elif indexc == 2:                                      
                                        if (counter1+1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes7:                                            
                                                mine_indexes7.append((counter1+1,counter2+1))
                                                mine_count7 += 1                                            
                                    elif indexc == 3:                                        
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes7:                                            
                                                mine_indexes7.append((counter1-1,counter2))
                                                mine_count7 += 1                                            
                                    elif indexc == 4:                                        
                                        if (counter1-1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes7:                                            
                                                mine_indexes7.append((counter1-1,counter2+1))
                                                mine_count7 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count7

                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes7                                       
                            
                            
                        elif indexb == length_row-1:
                            print("0g")
                            
                            mine_indexes8 = list()                            
                            indexes_to_check = [type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb])]
                            mine_count8 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes8:                                            
                                                mine_indexes8.append((counter1-1,counter2))
                                                mine_count8 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1-1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes8:                                             
                                                mine_indexes8.append((counter1-1,counter2-1))
                                                mine_count8 += 1                                            
                                    elif indexc == 2:                                      
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes8:                                             
                                                mine_indexes8.append((counter1-1,counter2))
                                                mine_count8 += 1                                            
                                    elif indexc == 3:                                        
                                        if (counter1+1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes8:                                             
                                                mine_indexes8.append((counter1+1,counter2-1))
                                                mine_count8 += 1                                            
                                    elif indexc == 4:                                       
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes8:                                             
                                                mine_indexes8.append((counter1+1,counter2))
                                                mine_count8 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count8
                            
                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes8                                       
                            
                        else:
                            print("0h")                            

                            mine_indexes9 = list()
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count9 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:
                                                mine_indexes9.append((counter1,counter2-1))
                                                mine_count9 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1,counter2+1))
                                                mine_count9 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1+1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1+1,counter2-1))
                                                mine_count9 += 1                                            
                                    elif indexc == 3:                                        
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1+1,counter2))
                                                mine_count9 += 1                                            
                                    elif indexc == 4:                                        
                                        if (counter1+1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1+1,counter2+1))
                                                mine_count9 += 1                                            
                                    elif indexc == 5:                                       
                                        if (counter1-1,counter2-1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1-1,counter2-1))
                                                mine_count9 += 1                                            
                                    elif indexc == 6:                                       
                                        if (counter1-1,counter2) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1-1,counter2))
                                                mine_count9 += 1                                            
                                    elif indexc == 7:                                       
                                        if (counter1-1,counter2+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes9:                                            
                                                mine_indexes9.append((counter1-1,counter2+1))
                                                mine_count9 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count9
                            
                            self.show_mines_record_dict[int(str(counter1)+str(counter2))] = mine_indexes9

                            
                counter2+=1
            counter2 = 0
            counter1+=1



        print("fuck 1")


        counter1a = 0
        counter2a = 0
        length_row = self.columns
        length_rows = self.rows
        ##add the regular mine tiles
        for indexa in range(0,self.rows):            
            for indexb in range(0,self.columns):                            
                if (indexa,indexb) in self.reg_tile_indexes_used:
                    big_list2[indexa][indexb] = Tile(self,indexa,indexb)
                    if indexa == 0:
                                               
                        if indexb == 0:
                            
                            mine_indexes10 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1])]

                            mine_count10 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                if item == type(self.MT):
                                    if indexc == 0:
                                        if (counter1a,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes10:                                             
                                                mine_indexes10.append((counter1a,counter2a+1))
                                                mine_count10 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1a+1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes10:                                            
                                                mine_indexes10.append((counter1a+1,counter2a))
                                                mine_count10 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1a+1,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes10:                                            
                                                mine_indexes10.append((counter1a+1,counter2a+1))
                                                mine_count10 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count10

                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes10                                        
                            
                        elif counter2a == length_row-1:
                                                                                 
                            mine_indexes11 = list()                                                       
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb])]
                            mine_count11 = 0
                            for indexc,item in enumerate(indexes_to_check):                                
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1a,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes11:                                            
                                                mine_indexes11.append((counter1a,counter2a-1))
                                                mine_count11 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1a-1,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes11:                                             
                                                mine_indexes11.append((counter1a-1,counter2a-1))
                                                mine_count11 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes11:                                             
                                                mine_indexes11.append((counter1a-1,counter2a))
                                                mine_count11 += 1                                            
                                    elif indexc == 3:                                        
                                        if (counter1a+1,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes11:                                             
                                                mine_indexes11.append((counter1a+1,counter2a-1))
                                                mine_count11 += 1                                            
                                    elif indexc == 4:                                       
                                        if (counter1a+1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes11:                                             
                                                mine_indexes11.append((counter1a+1,counter2a))
                                                mine_count11 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count11

                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes11
                                        
                            
##                            
                        else:
                                                     
                            mine_indexes12 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1])]
                            mine_count12 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1a,counter2a-1) in self.mine_indexes_used:                                            
                                            if (counter1a,counter2a-1) not in mine_indexes12:                                            
                                                mine_indexes12.append((counter1a,counter2a-1))
                                                mine_count12 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1a,counter2a+1) in self.mine_indexes_used:                                                                                        
                                            if (counter1a,counter2a-1) not in mine_indexes12:                                            
                                                mine_indexes12.append((counter1a,counter2a+1))
                                                mine_count12 += 1                                            
                                    elif indexc == 2:                                      
                                        if (counter1a+1,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes12:                                            
                                                mine_indexes12.append((counter1a+1,counter2a-1))
                                                mine_count12 += 1                                            
                                    elif indexc == 3:                                      
                                        if (counter1a+1,counter2a) in self.mine_indexes_used:                                                                                    
                                            if (counter1a,counter2a-1) not in mine_indexes12:                                            
                                                mine_indexes12.append((counter1a+1,counter2a))
                                                mine_count12 += 1                                            
                                    elif indexc == 4:                                      
                                        if (counter1a+1,counter2a+1) in self.mine_indexes_used:                                                                                        
                                            if (counter1a,counter2a-1) not in mine_indexes12:                                            
                                                mine_indexes12.append((counter1a+1,counter2a+1))
                                                mine_count12 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count12

                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes12                                        
                            
##
                    elif indexa == length_rows-1:
                                                 
                        if indexb == 0:
                           
                            mine_indexes13 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count13 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1a,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes13:                                             
                                                mine_indexes13.append((counter1a+1,counter2a))
                                                mine_count13 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes13:                                            
                                                mine_indexes13.append((counter1a-1,counter2a))
                                                mine_count13 += 1                                            
                                    elif indexc == 2:                                        
                                        if (counter1a-1,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes13:                                            
                                                mine_indexes13.append((counter1a-1,counter2a+1))
                                                mine_count13 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count13
                            
                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes13                                       
                            
                        elif indexb == length_row-1:
                                                        
                            
                            mine_indexes14 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb])]
                            mine_count14 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1a,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes14:                                             
                                                mine_indexes14.append((counter1a,counter2a-1))
                                                mine_count14 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1a-1,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes14:                                             
                                                mine_indexes14.append((counter1a-1,counter2a-1))
                                                mine_count14 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes14:                                             
                                                mine_indexes14.append((counter1-1,counter2))
                                                mine_count14 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count14
                            
                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes14                                       
                            
                        else:
                                                          
                            
                            mine_indexes15 = list()                            
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count15 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                
                                if item == type(self.MT):

                                    if indexc == 0:                                      
                                        if (counter1a,counter2a-1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes15:                                            
                                                mine_indexes15.append((counter1a,counter2a-1))
                                                mine_count15 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1a,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes15:                                             
                                                mine_indexes15.append((counter1a,counter2a+1))
                                                mine_count15 += 1                                            
                                    elif indexc == 2:                                      
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes15:                                             
                                                mine_indexes15.append((counter1a-1,counter2a-1))
                                                mine_count15 += 1                                            
                                    elif indexc == 3:                                         
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes15:                                             
                                                mine_indexes15.append((counter1a-1,counter2a))
                                                mine_count15 += 1                                            
                                    elif indexc == 4:                                        
                                        if (counter1a-1,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes15:                                             
                                                mine_indexes15.append((counter1a-1,counter2a+1))
                                                mine_count15 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count15

                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes15                                       
                            
                    else:
                                                  
                        if indexb == 0:

                            mine_indexes16 = list()
                            indexes_to_check = [type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count16 = 0
                            for indexc,item in enumerate(indexes_to_check):
                                
                                if item == type(self.MT):

                                    if indexc == 0:                                       
                                        if (counter1a,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes16:                                             
                                                mine_indexes16.append((counter1a,counter2a+1))
                                                mine_count16 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1+1,counter2) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes16:                                            
                                                mine_indexes16.append((counter1a+1,counter2a))
                                                mine_count16 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1+1,counter2+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes16:                                            
                                                mine_indexes16.append((counter1a+1,counter2a+1))
                                                mine_count16 += 1                                            
                                    elif indexc == 3:                                      
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes16:                                            
                                                mine_indexes16.append((counter1a-1,counter2a))
                                                mine_count16 += 1                                            
                                    elif indexc == 4:                                        
                                        if (counter1a-1,counter2a+1) in self.mine_indexes_used:
                                            if (counter1a,counter2a-1) not in mine_indexes16:                                            
                                                mine_indexes16.append((counter1a-1,counter2a+1))
                                                mine_count16 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count16

                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes16                                        
                            
                            
                        elif indexb == length_row-1:
                                                                                   
                            mine_indexes17 = list()                            
                            indexes_to_check = [type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb])]
                            mine_count17 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes17:                                            
                                                mine_indexes17.append((counter1a-1,counter2a))
                                                mine_count17 += 1                                            
                                    elif indexc == 1:                                        
                                        if (counter1a-1,counter2a-1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes17:                                             
                                                mine_indexes17.append((counter1a-1,counter2a-1))
                                                mine_count17 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes17:                                             
                                                mine_indexes17.append((counter1a-1,counter2a))
                                                mine_count17 += 1                                            
                                    elif indexc == 3:                                       
                                        if (counter1a+1,counter2a-1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes17:                                             
                                                mine_indexes17.append((counter1a+1,counter2a-1))
                                                mine_count17 += 1                                            
                                    elif indexc == 4:                                       
                                        if (counter1a+1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes17:                                             
                                                mine_indexes17.append((counter1a+1,counter2a))
                                                mine_count17 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count17
                            
                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes17                                       
                            
                        else:
                                                          
                            mine_indexes18 = list()
                            indexes_to_check = [type(big_list2[indexa][indexb-1]),
                                                type(big_list2[indexa][indexb+1]),
                                                type(big_list2[indexa+1][indexb-1]),
                                                type(big_list2[indexa+1][indexb]),
                                                type(big_list2[indexa+1][indexb+1]),
                                                type(big_list2[indexa-1][indexb-1]),
                                                type(big_list2[indexa-1][indexb]),
                                                type(big_list2[indexa-1][indexb+1])]
                            mine_count18 = 0
                            for indexc,item in enumerate(indexes_to_check):
                               
                                if item == type(self.MT):

                                    if indexc == 0:                                        
                                        if (counter1a,counter2a-1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:
                                                mine_indexes18.append((counter1a,counter2a-1))
                                                mine_count18 += 1                                            
                                    elif indexc == 1:                                       
                                        if (counter1,counter2+1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a,counter2a+1))
                                                mine_count18 += 1                                            
                                    elif indexc == 2:                                       
                                        if (counter1a+1,counter2a-1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a+1,counter2a-1))
                                                mine_count18 += 1                                            
                                    elif indexc == 3:                                        
                                        if (counter1a+1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a+1,counter2a))
                                                mine_count18 += 1                                            
                                    elif indexc == 4:                                       
                                        if (counter1a+1,counter2a+1) in self.mine_indexes_used:
                                            if (counter2,counter2-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a+1,counter2a+1))
                                                mine_count18 += 1                                            
                                    elif indexc == 5:                                       
                                        if (counter1a-1,counter2a-1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a-1,counter2a-1))
                                                mine_count18 += 1                                            
                                    elif indexc == 6:                                       
                                        if (counter1a-1,counter2a) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a-1,counter2a))
                                                mine_count18 += 1                                            
                                    elif indexc == 7:                                        
                                        if (counter1-1,counter2+1) in self.mine_indexes_used:
                                            if (counter2a,counter2a-1) not in mine_indexes18:                                            
                                                mine_indexes18.append((counter1a-1,counter2a+1))
                                                mine_count18 += 1                                            
                            big_list2[indexa][indexb].mine_count = mine_count18
                            
                            self.regular_tiles_record_dict[int(str(counter1a)+str(counter2a))] = mine_indexes18

                                            
                counter2a+=1
            counter2a = 0
            counter1a+=1


            
##        ##loop through big_list2 and if any objects are still strings, create a tile at that index
        for i in range(0,self.rows):
            for ii in range(0,self.columns):
                if "str" in str(type(ii)):
                    print("changed string")
                    big_list2[i][ii] = Tile(self,i,ii)


                                    
        self.output_board = big_list2
        


    def __str__(self,other=False,show_all=False,ShowMinesTile=False,ShowMinesIndex=tuple(),MineTile=False):
        """  Returns a String representation of the object
        :return: str.  String representation of the board.

        This will have the following example format for 5 columns and 3 rows

                  Minesweeper Board

       R\C   0  1  2  3  4
           _______________
         0|  H  H  H  H  H
         1|  H  H  H  H  H
         2|  H  H  H  H  H
         3|  H  H  H  H  H
        """



        ##display the __value attributes of each object in self._board
        
        if MineTile == True:        
            final_list = list()
            for indexa,i in enumerate(self.output_board):
                for indexb,ii in enumerate(i):
                    ii.hidden = False
                    if ii.hidden == True:
                        final_list.append("H")
                    elif ii.hidden == False and type(ii) != type(self.MT):
                        final_list.append(ii.mine_count)
                    elif ii.hidden == False:
                        final_list.append("*")
                   
                                                        
            string_output = ""
            string_output += " "*17
            string_output += "Minesweeper Board\n\n"
            string_output += (" "*13)+"R\C"+(" "*3)
            rows = str(self.rows)
            columns = str(self.columns)
            row_counter = 0
            column_counter = 0
            for column in range(0,int(columns)):
                string_output += str(column_counter)+(" "*3)
                column_counter+=1
            string_output += "\n"
            if column_counter > 0 and column_counter < 11:
                string_output += " "*19+("____"*column_counter)

            counter1 = 0
            string_output += "\n"
            for row in range(0,int(rows)):
                string_output += " "*17+str(row_counter)+"|"
                for placeholder in range(0,int(columns)):
                    string_output+="{}".format(final_list[counter1])+(" "*3)
                    counter1+=1
                string_output+="\n"
                row_counter+=1

       
            print(string_output)


            
        elif show_all == True:
            if ShowMinesTile == True:
                ##go through and flip any touching mines to this ShowMineTile
                indexes_to_flip = self.show_mines_record_dict[int(str(ShowMinesIndex[0])+str(ShowMinesIndex[1]))]
                for indexa,i in enumerate(self.output_board):
                    for indexb,ii in enumerate(i):
                        if (indexa,indexb) in indexes_to_flip:
                            self.output_board[indexa][indexb].hidden = False
            
            

            final_list = list()
            for indexa,i in enumerate(self.output_board):
                for indexb,ii in enumerate(i):                       
                    if ii.hidden == True:
                        final_list.append("H")
                    elif ii.hidden == False and type(ii) != type(self.MT):
                        final_list.append(ii.mine_count)
                    elif ii.hidden == False:
                        final_list.append("*")
                   

            
            
                                   
            string_output = ""
            string_output += " "*17
            string_output += "Minesweeper Board\n\n"
            string_output += (" "*13)+"R\C"+(" "*3)
            rows = str(self.rows)
            columns = str(self.columns)
            row_counter = 0
            column_counter = 0
            for column in range(0,int(columns)):
                string_output += str(column_counter)+(" "*3)
                column_counter+=1
            string_output += "\n"
            if column_counter > 0 and column_counter < 11:
                string_output += " "*19+("____"*column_counter)

            counter1 = 0
            string_output += "\n"
            for row in range(0,int(rows)):
                string_output += " "*17+str(row_counter)+"|"
                for placeholder in range(0,int(columns)):
                    string_output+="{}".format(final_list[counter1])+(" "*3)
                    counter1+=1
                string_output+="\n"
                row_counter+=1
            
                            
            print(string_output)
      
            
            
    def __repr__(self):
        """ Returns the representation of the Board """
        # Replace the following with your code to make the method perform properly
        return self

    def get_tile(self, y, x):
        """  Returns what is at the Position X and Y, if it is outside the board, then None is returned
        :param y: int.  Row of the tile begin requested
        :param x: int.  Column of the tile being requested.
        :return: A from that position or None if values are outside of the board.

        Errors Handled : if the position being requested is outside of the board, then None is returned.
        """
        try:
            print("rows in self.output_board: {}".format(len(self.output_board)))
            a = self.output_board[int(y)][int(x)]          
            return True
        except Exception:
            return False

    def __place_mines(self, mines):
        """  Places the required number of mines for the user
        :param mines: int.  The number of mines to place
        :return: Nothing

            Modifications : This will change the __board and place the proper number of mines on the board.
                            Do not place a mine where one has already been placed.
        """

        # Replace the following with your code to make the method perform properly
        pass

    def __place_specials(self, show_mines):
        """ Places all special show mine tiles
        :param show_mines: int.  The number of show_mines to place on the board.
        :return: Nothing

            Modifications : changes the __board and places random ShowMineTiles on the board.
                            There should be as many ShowMineTiles as the variable show_mines passed.
                            If there is a mine in a spot, then the ShowMineTile will not replace a Mine
        """
        # Replace the following with your code to make the method perform properly
        pass        

    def __set_mine_counts(self):
        """  Sets the counts of the mines around the cell
        :return: Nothing

            Modifications : For each tile that is not a mine it sets the number of mines around it.
        """
        # Replace the following with your code to make the method perform properly
        pass

    def __show_all(self):
        """ Shows all the cells.  Sets the hidden attribute to True for each cell.
            This occurs when the game is over """
        # Replace the following with your code to make the method perform properly
        return self.__str__(True)

    def __check_win(self,tile_obj):
        """ Returns True if the game has been won ( all non mines are uncovered ) False otherwise """
        # Replace the following with your code to make the method perform properly
        ##if all objects on board's hidden attributes are set equal to False

        count = 0

        ##check how many non mine tiles are still hidden
        for indexa,i in enumerate(board_obj.output_board):
            for indexb,ii in enumerate(i):
                if type(ii) == type(self.MT):
                    pass 
                elif type(ii) == type(self.ST):
                    if ii.hidden == False:
                        pass
                    else:
##                        print("show mine tile still hidden")
                        count+=1
                        
                elif "Tile" in str(type(ii)):
                    if ii.hidden == False:
                        pass
                    else:
##                        print("regular tile still hidden")
                        count+=1
                        

        if "MineTile" not in str(type(tile_obj)):
            if count < 1:
                return 1
            else:
                return 0
        else:
            return 2
            

  

    def uncover_cell(self, y, x):
        """ Uncovers the cell as position given.
        :param y: int.  The row being uncovered.
        :param x: int.  The column being uncovered.
        :return: None

            Modifications : Uncovers the cell.  If the cell is a mine, then the game is over and all the cells are
                                    uncovered.  Set the gamestate to the proper value.
                            If the cell is a tile and has zero mines around it, then the tiles around it are uncovered
                            Once the cell is uncovered, if there are no more non mine tiles uncovered
                                    then the game must be over.  Show the entire board and set the gamestate to the
                                    proper value.
        """
        # Replace the following with your code to make the method perform properly
        self.output_board[y][x].hidden = False
        if "ShowMinesTile" in str(type(self.output_board[y][x])):
            self.ripple_effect(y,x)
        elif "MineTile" in str(type(self.output_board[y][x])):
            pass
        elif "Tile" in str(type(self.output_board[y][x])):
            pass

from copy import *

def validate_opening():
        done = "n"
        while done == "n":
            input1 = input("Enter the rows and columns desired for the board separated by a comma  ==> ")
            try:
                input1a = str(copy(input1))                
                temp1 = input1a.replace(",","")
                temp2 = int(temp1)
                pass
            except Exception:
                print("You cannot enter an characters but numbers and one comma(,) character.  Try again.")
                continue
            if input1.count(',') < 2 and input1.count(',') > 0:
                list1 = input1.split(',')
                list1[0] = int(list1[0])
                list1[1] = int(list1[1])
                try:
                    if len(list1) > 1 and len(list1) < 3:
                        done2 = "n"
                        while done2 == "n":
                            input3 = input("Enter the amount of mines you would like on the board. ==>  ")
                            try:
                                temp3 = int(input3)
                                pass
                            except Exception:
                                print("You must enter an integer for the mine count.  Try again please. ==> ")
                                continue
                            
                            list1.append(int(input3))
                            break
                        done3 = "n"
                        while done3 == "n":
                            input4 = input("Enter the amount of ShowMine Tiles you would like on the board. ==>  ")
                            try:
                                temp4 = int(input4)
                                pass
                            except Exception:
                                print("You must enter an integer for the show mine tiles count.  Try again please. ==>  ")
                                continue
                            
                            list1.append(int(input4))
                            break
                        print(list1)
                        return tuple(list1) 
                    else:
                        print("Only enter two values separated by a comma")
                        continue
                    break
                except Exception:
                    print("You must enter 2 numbers")
                    continue
            elif input1.count(',') == 0:
                print("You need two values.  One for rows, and one for columns.  Try again.")
                continue
            else:
                print("too many commas")

def validate_guess():
    done = "n"
    while done == "n":        
        input1 = input("Please pick a row ==>  ")
        try:
            a = int(input1)
            break
        except Exception:
            print("You must enter an integer for row")
    done2 = "n"
    while done2 == "n":
        input2 = input("Please pick a column ==>  ")
        try:
            b = int(input2)
            break
        except Exception:
            print("You must enter an integer for column.")
    
    return input1,input2








if __name__ == "__main__":
    #Your main game logic goes here
    ##get info from user about the board they want for the game
    while True:
        opening = validate_opening()
        rows = opening[0]
        columns = opening[1]
        mines = opening[2]
        show_mines = opening[3]
        ##create the board
        board_obj = SuperSweeperBoard(rows,columns,mines,show_mines)
        listaaa = list(board_obj.show_mines_record_dict.values())
       
        listbbb = list()
        for item in listaaa:

            if "list" in str(type(item)):

                for subitem in item:

                    if "list" in str(type(subitem)):
                        for subitem2 in subitem:
                            if subitem2 not in listbbb:
                                listbbb.append(subitem2)

                    if subitem not in listbbb:
                        listbbb.append(subitem)

                
            else:
                if item not in listbbb:
                    listbbb.append(item)
               
        
        print(listbbb)

        
        ##give the mines that dont count when checking for a win another attribute called "extra"
        for indexa,i in enumerate(board_obj.output_board):
            for indexb,ii in enumerate(i):
                if "MineTile" in str(type(ii)):
                    if (indexa,indexb) in listbbb:
                        ii.extra = "-"


        board_obj.__str__(show_all=True)
        count = 0
        while board_obj.game_state == 0:
            count+=1
            users_guess = validate_guess()
            exists = board_obj.get_tile(int(users_guess[0]),int(users_guess[1]))
            if exists == True:
                result = board_obj.output_board[int(users_guess[0])][int(users_guess[1])]
                if "MineTile" in str(type(result)):                    
                    board_obj.__str__(MineTile=True)
                    print("You lost.")                    
                    board_obj.game_state = 2                    
                elif type(result)==type(board_obj.ST):
                    board_obj.output_board[int(users_guess[0])][int(users_guess[1])].hidden = False
                    board_obj.output_board[int(users_guess[0])][int(users_guess[1])].mines_for_this_tile = board_obj.show_mines_record_dict[int(str(users_guess[0])+str(users_guess[1]))]

                    board_obj.show_mines_uncovered.append(int(str(users_guess[0])+str(users_guess[1])))
                    board_obj.__str__(show_all=True,ShowMinesTile=True,ShowMinesIndex=(int(users_guess[0]),int(users_guess[1])))
                    
                    ##checks if there are any tiles or show mine tiles left to be uncovered...
                    aaaa = board_obj._SuperSweeperBoard__check_win(board_obj.output_board[int(users_guess[0])][int(users_guess[1])])

                    ##Continue playing(0), You win(1), You lose(2).  If 1 or 2 we go to ask the user if they want to play again.
                    if aaaa == 0:
                        continue
                    elif aaaa == 1:
                        board_obj.__str__(MineTile=True)
                        print("You lost!")                          
                        break
                    elif aaaa == 2:
                        board_obj.__str__(MineTile=True)
                        print("You lost!")                        
                        break
                
                        
                        
                elif "Tile" in str(type(result)):
                    ##If this tile is selected by the user, set this ShowMinesTile's hidden attribute = False
                    board_obj.output_board[int(users_guess[0])][int(users_guess[1])].hidden = False
                    board_obj.output_board[int(users_guess[0])][int(users_guess[1])].mines_for_this_tile = board_obj.regular_tiles_record_dict[int(str(users_guess[0])+str(users_guess[1]))]

                    board_obj.show_mines_uncovered.append(int(str(users_guess[0])+str(users_guess[1])))
                    board_obj.__str__(show_all=True)                   
                    
                    ##checks if there are any tiles or show mine tiles left to be uncovered...
                    aaaa = board_obj._SuperSweeperBoard__check_win(board_obj.output_board[int(users_guess[0])][int(users_guess[1])])

                    ##Continue playing(0), You win(1), You lose(2).  If 1 or 2 we go to ask the user if they want to play again.
                    if aaaa == 0:
                        continue
                    elif aaaa == 1:
                        board_obj.__str__(MineTile=True)
                        print("You won!")                        
                        break
                    elif aaaa == 2:
                        board_obj.__str__(MineTile=True)
                        print("You lost!")                        
                        break
##                    
                else:
                    print(type(result))                
            else:
                print("You must enter a row and column that exist. ")
                continue
        input3 = input("Do you want to play again?")
        if input3 == "y":
            continue
        else:
            print("Goodbye")
            exit()
        
            
        

    
    
    


















