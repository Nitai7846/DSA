#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:28:27 2026

@author: nitaishah
"""

class Solution:
    
    def isSafe(self, row, board, col):
        
        r, c = row, col
        
        while r>=0 and c>=0:
            if board[r][c] == 'Q':
                return False
            r-=1
            c-=1
        
        r = row
        c = col 
        
        while r>=0:
            if board[r][c] == 'Q':
                return False
            r -=1
        
        r = row
        c = col 

        while r>=0 and c<len(board[0]):
            if board[r][c] == 'Q':
                return False
            
            r-=1
            c+=1
        
        return True
    
    def func(self, row, ans, board):
        
        if row == len(board):
            ans.append(["".join(r) for r in board])
            return 
        
        for col in range(len(board[0])):
            
            if self.isSafe(row, board, col):
                board[row][col] = 'Q'
                self.func(row+1, ans, board)
                board[row][col] = "."
    
    def solveNQueens(self, n):
        
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.func(0, ans, board)
        return ans 