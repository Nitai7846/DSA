#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:19:30 2026

@author: nitaishah
"""

class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    # Recursive method to solve the Sudoku
    def solve(self, board):
        # Size of the board
        n = 9  
        for i in range(n):
            for j in range(n):
                # Empty cell found
                if board[i][j] == '.':  
                    for digit in '123456789':
                        # Check if digit can be placed
                        if self.are_rules_met(board, i, j, digit):  
                             # Place digit
                            board[i][j] = digit 
                            # Recur to place next digits
                            if self.solve(board):  
                                return True
                            else:
                                # Reset if placing digit doesn't solve Sudoku
                                board[i][j] = '.'
                    # If no digit can be placed, return False              
                    return False  
        # Sudoku solved            
        return True  

    # Method to check if placing a digit follows Sudoku rules
    def are_rules_met(self, board, row, col, digit):
        for i in range(9):
            if board[row][i] == digit or board[i][col] == digit:
                # Digit already in row or column
                return False  
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == digit:
                     # Digit already in 3x3 sub-box
                    return False 
         # Digit can be placed            
        return True 