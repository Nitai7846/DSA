#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:28:41 2026

@author: nitaishah
"""

class Solution:

    def isSafe(self, col, node, colors, adj):

        for neighbor in adj[node]:

            if colors[neighbor] == col:
                return False
        
        return True 

    def solve(self, node, m, n, colors, adj):

        if n == node:
            return True 
        
        for i in range(1, m+1):

            if self.isSafe(i, node, colors, adj):
                colors[node] = i 

                if self.solve(node+1, m, n, colors, adj):
                    return True 
                
                colors[node] = 0 
        
        return False

        
    def graphColoring(self, edges, m, n):
        #your code goes here

        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        colors = [0] *n 

        return self.solve(0, m, n, colors, adj)
