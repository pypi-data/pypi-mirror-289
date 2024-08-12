import numpy as np
from scipy.linalg import schur, solve_sylvester, svd
from PIL import Image

def image_compression_algorithm(image_matrix, tolerance=1e-6):
    """
    使用Algorithm 1對圖像矩陣進行壓縮。
    
    :param image_matrix: 輸入的圖像矩陣 (numpy array)
    :param tolerance: 用於控制精度的容差
    :return: 壓縮後的圖像矩陣
    """
    # 將圖像矩陣填充為方陣
    image_matrix = pad_image_to_square(image_matrix)

    # 步驟 1: 對圖像矩陣進行 Schur 分解
    T, Z = schur(image_matrix)

    # 步驟 2: 構建 Sylvester 方程
    B = np.random.rand(*T.shape) * 0.01  # 添加小幅度隨機噪聲以提高穩定性

    # 步驟 3: 使用 Sylvester 方程來解壓縮矩陣
    X = solve_sylvester(T, T, B)

    # 步驟 4: 檢查結果的精度
    if np.linalg.norm(image_matrix - X.dot(Z)) < tolerance:
        return X.dot(Z)
    else:
        # 如果未達到精度要求，嘗試增大容差或其他方法
        raise ValueError("壓縮未達到預期的精度要求")

def compress_image(image_path, block_size=32, tolerance=1e-6):
    """
    讀取圖像文件，分塊壓縮並返回壓縮後的圖像。
    
    :param image_path: 圖像文件的路徑
    :param block_size: 每個小塊的大小
    :param tolerance: 用於控制精度的容差
    :return: 壓縮後的圖像
    """
    image = Image.open(image_path).convert('L')
    image_matrix = np.array(image)

    # 執行分塊壓縮演算法
    compressed_matrix = compress_image_blockwise(image_matrix, block_size, tolerance)

    # 將壓縮後的矩陣轉換回圖片
    compressed_image = Image.fromarray(np.uint8(compressed_matrix))
    
    return compressed_image

def compress_image_blockwise(image_matrix, block_size=32, tolerance=1e-6):
    """
    將圖像矩陣分割成小塊，並對每塊單獨壓縮。
    
    :param image_matrix: 輸入的圖像矩陣 (numpy array)
    :param block_size: 每個小塊的大小
    :param tolerance: 用於控制精度的容差
    :return: 壓縮後的圖像矩陣
    """
    height, width = image_matrix.shape
    compressed_matrix = np.zeros_like(image_matrix)

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image_matrix[i:i+block_size, j:j+block_size]
            padded_block = pad_image_to_square(block)
            try:
                compressed_block = image_compression_algorithm(padded_block, tolerance)
            except ValueError:
                # 如果壓縮失敗，這裡可以採用回退策略，比如不進行壓縮或進行更少的壓縮
                compressed_block = block  # 回退到原始區塊或進行更少的壓縮

            compressed_matrix[i:i+block_size, j:j+block_size] = compressed_block[:block.shape[0], :block.shape[1]]

    return compressed_matrix

def pad_image_to_square(image_matrix):
    """
    將圖像矩陣填充為方陣
    """
    height, width = image_matrix.shape
    if height == width:
        return image_matrix  # 已經是方陣，無需處理

    size = max(height, width)
    square_matrix = np.zeros((size, size), dtype=image_matrix.dtype)
    square_matrix[:height, :width] = image_matrix
    return square_matrix


##svd
def image_compression_svd(image_matrix, rank=None):
    """
    使用SVD進行圖像壓縮。
    
    :param image_matrix: 輸入的圖像矩陣 (numpy array)
    :param rank: 保留的奇異值數量，None 表示自動選擇
    :return: 壓縮後的圖像矩陣
    """
    U, S, VT = svd(image_matrix, full_matrices=False)
    if rank is None:
        rank = np.sum(S > 1e-10)  # 自動選擇保留的奇異值數量
    
    U = U[:, :rank]
    S = np.diag(S[:rank])
    VT = VT[:rank, :]

    compressed_matrix = np.dot(U, np.dot(S, VT))
    return compressed_matrix

def compress_image_with_svd(image_path, block_size=32, rank=None):
    """
    使用SVD壓縮圖像，並返回壓縮後的圖像。
    
    :param image_path: 圖像文件的路徑
    :param block_size: 每個小塊的大小
    :param rank: SVD中保留的奇異值數量，None表示自動選擇
    :return: 壓縮後的圖像
    """
    image = Image.open(image_path).convert('L')
    image_matrix = np.array(image)

    # 分塊並壓縮
    compressed_matrix = compress_image_blockwise_svd(image_matrix, block_size, rank)

    compressed_image = Image.fromarray(np.uint8(compressed_matrix))
    
    return compressed_image

def compress_image_blockwise_svd(image_matrix, block_size=32, rank=None):
    """
    將圖像矩陣分割成小塊，並使用SVD進行壓縮。
    
    :param image_matrix: 輸入的圖像矩陣 (numpy array)
    :param block_size: 每個小塊的大小
    :param rank: SVD中保留的奇異值數量，None表示自動選擇
    :return: 壓縮後的圖像矩陣
    """
    height, width = image_matrix.shape
    compressed_matrix = np.zeros_like(image_matrix)

    for i in range(0, height, block_size):
        for j in range(0, width, block_size):
            block = image_matrix[i:i+block_size, j:j+block_size]
            compressed_block = image_compression_svd(block, rank)
            compressed_matrix[i:i+block_size, j:j+block_size] = compressed_block[:block.shape[0], :block.shape[1]]

    return compressed_matrix
