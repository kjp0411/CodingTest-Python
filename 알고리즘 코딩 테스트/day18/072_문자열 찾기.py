# https://www.acmicpc.net/problem/14425
# # 코드1 (시간 초과)
# from sys import stdin
# input = stdin.readline
#
# class Node(object):
#     def __init__(self, isEnd):
#         self.isEnd = isEnd
#         self.childNode = {}
#
# class Trie(object):
#     def __init__(self):
#         self.parent = Node(None)
#
#     # 문자 삽입
#     def insert(self, string):
#         nowNode = self.parent
#         temp_length = 0
#         for char in string:
#             # 자식 Node에 미생성된 문자열이면 새로 생성
#             if char not in nowNode.childNode:
#                 nowNode.childNode[char] = Node(char)
#             # 자식 노드로 이동
#             nowNode = nowNode.childNode[char]
#             temp_length += 1
#             if temp_length == len(string):
#                 nowNode.isEnd = True
#
#     # 문자열이 존재하는지 탐색
#     def search(self, string):
#         nowNode = self.parent
#         temp_length = 0
#         for char in string:
#             if char in nowNode.childNode:
#                 nowNode = nowNode.childNode[char]
#                 temp_length += 1
#                 if temp_length == len(string) and nowNode.isEnd == True:
#                     return True
#             else:
#                 return False
#         return False
#
# N, M = map(int, input().split())
# myTrie = Trie()
#
# for _ in range(N):
#     word = input().strip()
#     myTrie.insert(word)
#
# result = 0
#
# for _ in range(M):
#     word = input().strip()
#     if myTrie.search(word):
#         result += 1
#
# print(result)

# 코드2
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = {input().strip() for _ in range(N)}   # 집합에 N개 문자열 저장
    ans = sum(1 for _ in range(M) if input().strip() in S)
    print(ans)

if __name__ == "__main__":
    main()

