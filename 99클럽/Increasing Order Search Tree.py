class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Sol:
    def increasingBST(self, root: [TreeNode]) -> TreeNode:
        ans = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            ans.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(ans) - 1):
            ans[i].left = None
            ans[i].right = ans[i + 1]
        ans[len(ans) - 1].left = None
        ans[len(ans) - 1].right = None
        return ans

if __name__ == "__main__":
    import time

    root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]

    S = Sol()

    start = time.time()
    print(S.increasingBST(root))
    sec = time.time() - start

    times = str(datetime.timedelta(seconds=sec))
    short = times.split('.')[0]
    print(f"{times} sec")
    print(f"{short} sec")