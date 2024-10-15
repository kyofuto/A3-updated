from PIL import Image, ImageDraw, ImageFont

from data_structures.node import TreeNode


def draw_bst(node, draw, x, y, x_offset, y_offset):
    if not node:
        return
    
    val_to_print = str(node)
    draw.ellipse((x - 15, y - 15, x + 15, y + 15), fill='lightblue', outline='black')
    draw.text((x - 10, y - 10), val_to_print, fill='black')

    if node.left:
        # Draw the left subtree
        left_x = x - x_offset
        left_y = y + y_offset
        draw.line((x, y, left_x, left_y), fill='black')
        draw_bst(node.left, draw, left_x, left_y, x_offset // 2, y_offset)

    if node.right:
        # Draw the right subtree
        right_x = x + x_offset
        right_y = y + y_offset
        draw.line((x, y, right_x, right_y), fill='black')
        draw_bst(node.right, draw, right_x, right_y, x_offset // 2, y_offset)


def draw_tree_image(root):
    width = 800
    height = 600
    background_color = 'white'
    node_color = 'lightblue'

    # Create a new image with white background
    img = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Set initial position and offset
    start_x = width // 2
    start_y = 30
    x_offset = width // 4
    y_offset = 60

    # Draw the tree
    draw_bst(root, draw, start_x, start_y, x_offset, y_offset)

    # Save or show the image
    img.save('bst_visualization.png')
    img.show()


# Example usage
if __name__ == "__main__":
    # Create a sample BST
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)
    root.right.right.right = TreeNode(33)
    root.right.right.right.right = TreeNode(44)
    root.right.right.right.right.right = TreeNode(44)
    root.right.right.right.right.right.right = TreeNode(44)
    root.right.right.right.right.right.right.right = TreeNode(44)
    root.right.right.right.right.right.right.right.right = TreeNode(44)

    draw_tree_image(root)
