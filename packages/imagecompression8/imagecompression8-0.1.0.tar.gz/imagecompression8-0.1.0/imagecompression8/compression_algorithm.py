import numpy as np
from scipy.linalg import schur, solve_sylvester
from PIL import Image

def image_compression_algorithm(image_matrix, tolerance=1e-10):
    """
    使用Algorithm 1對圖像矩陣進行壓縮。
    
    :param image_matrix: 輸入的圖像矩陣 (numpy array)
    :param tolerance: 用於控制精度的容差
    :return: 壓縮後的圖像矩陣
    """
    # 步驟 1: 對圖像矩陣進行 Schur 分解
    T, Z = schur(image_matrix)

    # 步驟 2: 構建 Sylvester 方程
    # 這裡假設一個特定的B矩陣來演示
    B = np.random.rand(*T.shape)

    # 步驟 3: 使用 Sylvester 方程來解壓縮矩陣
    X = solve_sylvester(T, T, B)

    # 步驟 4: 檢查結果的精度
    if np.linalg.norm(image_matrix - X.dot(Z)) < tolerance:
        return X.dot(Z)
    else:
        raise ValueError("壓縮未達到預期的精度要求")

def compress_image(image_path, tolerance=1e-10):
    """
    讀取圖像文件，壓縮並返回壓縮後的圖像。
    
    :param image_path: 圖像文件的路徑
    :param tolerance: 用於控制精度的容差
    :return: 壓縮後的圖像
    """
    # 打開圖片並轉換為灰度模式
    image = Image.open(image_path).convert('L')
    image_matrix = np.array(image)

    # 執行壓縮演算法
    compressed_matrix = image_compression_algorithm(image_matrix, tolerance)

    # 將壓縮後的矩陣轉換回圖片
    compressed_image = Image.fromarray(np.uint8(compressed_matrix))
    
    return compressed_image
