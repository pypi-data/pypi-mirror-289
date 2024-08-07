import csv
import PIL
import json
import typing
import requests
from PIL import Image, ImageDraw, ImageColor
from io import BytesIO
from typing import Iterator, List


def read_csv(csv_file_path: str, skip_line: int=0) -> Iterator[List[str]]:
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        # 创建 csv.reader 对象
        csv_reader = csv.reader(csvfile)
    
    for i in range(skip_line):
        next(csv_reader)
    
    return csv_reader

def download_image(url, save_path):
    try:
        # 发送HTTP GET请求获取图片内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 将响应内容转换为字节流
        img_data = BytesIO(response.content)

        # 使用Pillow打开图片
        img = Image.open(img_data)

        # 保存图片到指定路径
        img.save(save_path)
        print(f"Image successfully downloaded and saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except IOError as e:
        print(f"Error saving image: {e}")

def draw_bbox(image: Image, bbs: list, color: tuple = (255, 0, 0),
              width: int = 2, on_display: bool = False):
    """Draw multiple boxes simultaneously.

    Attention: bbs is a two-dim list. for example,[[x0, y0, x1, y1, x2, y2,
    x3, y3, x4, y4]].
    """
    draw = ImageDraw.Draw(image)
    if isinstance(color, str):
        color = ImageColor.getrgb(color)
    point_color = (255 - color[0], 255 - color[1], 255 - color[2])
    for bb in bbs:
        bbox = bb + bb[:2]
        draw.line(bbox, fill=color, width=width)
        bound = (bbox[0] - 5, bbox[1] - 5, bbox[0] + 5, bbox[1] + 5)
        draw.ellipse(bound, fill=point_color)
    if on_display:
        image.show()
    return image

def read_image(src: str, mode: str = 'cv2', bin_to_image = False) -> typing.Any:
    """Read image.

    Args:
        src: img file path.
        mode: one of ['pil', 'cv2', 'bin'].
    """
    if mode == 'pil':
        img = Image.open(src)
    return img

def write_image(data: typing.Any, dst: str) -> None:
    """Write data into a picture, supportint cv2 and pil and bin."""
    if isinstance(data, PIL.Image.Image):
        try:
            data.save(dst)
        except OSError:
            print(dst)  # TO DO, using logger ?

def read_json(src: str) -> dict:
    """Load json file.

    Args:
        src: json file path.
    """
    with open(src, "r") as fr:
        data = json.load(fr)
    return data


