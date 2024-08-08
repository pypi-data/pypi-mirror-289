import os
import pkg_resources as pkg
from pathlib import Path
import yaml
import time
import math
import numpy as np
import contextlib
import matplotlib.pyplot as plt
import warnings
import platform

import torch

from ycsai.utils import LOGGER, FONT
from ycsai.utils.plots import (
    plot_pr_curve, plot_mc_curve, smooth
)

def is_ascii(s=''):
    """
    Description
    -----------
    Is string composed of all ASCII (no UTF) characters? (note str().isascii() introduced in python 3.7)

    Arguments
    ---------
        s : string

    Returns
    -------
        (bool)
    """
    s = str(s)  # convert list, tuple, None, etc. to str
    return len(s.encode().decode('ascii', 'ignore')) == len(s)

def check_version(current='0.0.0', minimum='0.0.0', name='version ', pinned=False, hard=False, verbose=False):
    # Check version vs. required version
    """
    Description
    -----------
    The check_version function checks if the current version meets or exceeds a specified minimum version. It supports strict comparisons (exact match or minimum requirement) and optional logging.

    Arguments
    ---------
        current (str): The current version string. Default is '0.0.0'.
        
        minimum (str): The minimum required version string. Default is '0.0.0'.
        
        name (str): A string to identify the version being checked. Default is 'version '.
        
        pinned (bool): If True, checks if the current version exactly matches the minimum version. Default is False.
        
        hard (bool): If True, raises an error if the minimum requirements are not met. Default is False.
        
        verbose (bool): If True, logs a warning message if the minimum requirements are not met. Default is False.

    Returns
    -------
        (bool): Returns True if the current version meets the required version criteria, otherwise False.
    """
    current, minimum = (pkg.parse_version(x) for x in (current, minimum))
    result = (current == minimum) if pinned else (current >= minimum)  # bool
    s = f'{name}{minimum} is required by YOLO, but {name}{current} is currently installed'  # string
    if hard:
        assert result, s  # assert min requirements met
    if verbose and not result:
        LOGGER.warning(s)
    return result

def increment_path(path, exist_ok=False, sep='', mkdir=False):
    # Increment file or directory path, i.e. runs/exp --> runs/exp{sep}2, runs/exp{sep}3, ... etc.
    """
    Description
    -----------
    The increment_path function generates an incremented file or directory path if the given path already exists. For example, if runs/exp exists, it will generate runs/exp2, runs/exp3, etc., until a non-existent path is found. It can also create the directory if specified.

    Arguments
    ---------
        path (str): The initial file or directory path.

        exist_ok (bool): If True, does not increment the path even if it exists. Default is False.
        
        sep (str): The separator to use between the base path and the increment number. Default is ''.
        
        mkdir (bool): If True, creates the directory at the incremented path. Default is False.

    Returns
    -------
        path (Path): The incremented path as a Path object.
    """
    path = Path(path)  # os-agnostic
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')

        # Method 1
        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'  # increment path
            if not os.path.exists(p):  #
                break
        path = Path(p)
    if mkdir:
        path.mkdir(parents=True, exist_ok=True)  # make directory

    return path

def yaml_save(file='data.yaml', data={}):
    # Single-line safe yaml saving
    """
    Description
    -----------
    The yaml_save function saves a dictionary to a YAML file in a safe format, converting any Path objects to strings.

    Arguments
    ---------
        file (str): The file path where the YAML data will be saved. Default is 'data.yaml'.
        
        data (dict): The dictionary to be saved to the YAML file. Default is an empty dictionary {}.
    """
    with open(file, 'w') as f:
        yaml.safe_dump({k: str(v) if isinstance(v, Path) else v for k, v in data.items()}, f, sort_keys=False)

def yaml_load(file='data.yaml'):
    # Single-line safe yaml loading
    """
    Description
    -----------
    The yaml_load function loads and returns the contents of a YAML file as a Python dictionary.

    Arguments
    ---------
        file (str): The file path of the YAML file to be loaded. Default is 'data.yaml'.

    Returns
    -------
        data (dict): The contents of the YAML file as a dictionary.
    """
    with open(file, errors='ignore') as f:
        return yaml.safe_load(f)

def check_dataset(data, autodownload=True):
    """
    Description
    -----------
    The check_dataset function checks and prepares a dataset configuration dictionary. It validates necessary fields, resolves paths, and optionally downloads the dataset if paths are missing.

    Arguments
    ---------
        data (str, Path, dict): The dataset configuration as a file path or dictionary.

        autodownload (bool): If True, attempts to download the dataset if paths are missing. Default is True.

    Returns
    -------
        data (dict): The validated and updated dataset configuration dictionary.
    """
    # Read yaml (optional)
    if isinstance(data, (str, Path)):
        data = yaml_load(data)  # dictionary

    # Checks
    for k in 'train', 'val', 'names':
        assert k in data, (f"data.yaml '{k}:' field missing")
    if isinstance(data['names'], (list, tuple)):  # old array format
        data['names'] = dict(enumerate(data['names']))  # convert to dict
    assert all(isinstance(k, int) for k in data['names'].keys()), 'data.yaml names keys must be integers, i.e. 2: car'
    data['nc'] = len(data['names'])

    # Resolve paths
    path = Path(data.get('path') or '')  # optional 'path' default to '.'
    if not path.is_absolute():
        path = (path).resolve()
        data['path'] = path  # download scripts
    for k in 'train', 'val', 'test':
        if data.get(k):  # prepend path
            if isinstance(data[k], str):
                x = (path / data[k]).resolve()
                if not x.exists() and data[k].startswith('../'):
                    x = (path / data[k][3:]).resolve()
                data[k] = str(x)
            else:
                data[k] = [str((path / x).resolve()) for x in data[k]]

    # Parse yaml
    train, val, test, s = (data.get(x) for x in ('train', 'val', 'test', 'download'))
    if val:
        val = [Path(x).resolve() for x in (val if isinstance(val, list) else [val])]  # val path
        if not all(x.exists() for x in val):
            LOGGER.info('\nDataset not found, missing paths %s' % [str(x) for x in val if not x.exists()])
            if not s or not autodownload:
                raise Exception('Dataset not found')
            t = time.time()
            if s.startswith('http') and s.endswith('.zip'):  # URL
                f = Path(s).name  # filename
                LOGGER.info(f'Downloading {s} to {f}...')
                torch.hub.download_url_to_file(s, f)
                Path(f).unlink()  # remove zip
                r = None  # success
            elif s.startswith('bash '):  # bash script
                LOGGER.info(f'Running {s} ...')
                r = os.system(s)
            else:  # python script
                r = exec(s, {'yaml': data})  # return None
            dt = f'({round(time.time() - t, 1)}s)'
            s = f"success {dt}, saved to" if r in (0, None) else f"failure {dt}"
            LOGGER.info(f"Dataset download {s}")
    return data  # dictionary

def check_suffix(file='yolo.pt', suffix=('.pt',), msg=''):
    """
    Description
    -----------
    The check_suffix function checks if the given file(s) have an acceptable suffix and raises an assertion error if they do not.

    Arguments
    ---------
        file (str, list, tuple): The file path or a list/tuple of file paths to check. Default is 'yolo.pt'.
        
        suffix (str, list, tuple): The acceptable suffix or a list/tuple of acceptable suffixes. Default is ('.pt',).
        
        msg (str): An optional message to prepend to the assertion error message. Default is ''.
    """
    # Check file(s) for acceptable suffix
    if file and suffix:
        if isinstance(suffix, str):
            suffix = [suffix]
        for f in file if isinstance(file, (list, tuple)) else [file]:
            s = Path(f).suffix.lower()  # file suffix
            if len(s):
                assert s in suffix, f"{msg}{f} acceptable suffix is {suffix}"

def make_divisible(x, divisor):
    """
    Description
    -----------
    The make_divisible function returns the nearest integer greater than or equal to x that is divisible by divisor.

    Arguments
    ---------
        x (float, int): The number to be adjusted to the nearest divisible number.
        
        divisor (int, torch.Tensor): The divisor by which the result should be divisible. If a torch.Tensor is provided, the maximum value of the tensor is used as the divisor.

    Returns
    -------
        result (int): The nearest integer greater than or equal to x that is divisible by divisor.
    """
    # Returns nearest x divisible by divisor
    if isinstance(divisor, torch.Tensor):
        divisor = int(divisor.max())  # to int
    return math.ceil(x / divisor) * divisor

def make_anchors(feats, strides, grid_cell_offset=0.5):
    """
    Description
    -----------
    The make_anchors function generates anchor points from feature maps and their corresponding strides. These anchors are used in object detection tasks to predict bounding boxes at different scales and locations.

    Arguments
    ---------
        feats (list of torch.Tensor): A list of feature maps from different layers of a neural network.
        
        strides (list of int): A list of stride values corresponding to each feature map.
        
        grid_cell_offset (float): Offset value for the grid cell centers. Default is 0.5.

    Returns
    -------
        anchor_points (torch.Tensor): A tensor containing the anchor points.
        
        stride_tensor (torch.Tensor): A tensor containing the stride values for each anchor point.
    """
    from ycsai.utils.torch_utils import TORCH_1_10
    anchor_points, stride_tensor = [], []
    assert feats is not None
    dtype, device = feats[0].dtype, feats[0].device
    for i, stride in enumerate(strides):
        _, _, h, w = feats[i].shape
        sx = torch.arange(end=w, device=device, dtype=dtype) + grid_cell_offset  # shift x
        sy = torch.arange(end=h, device=device, dtype=dtype) + grid_cell_offset  # shift y
        sy, sx = torch.meshgrid(sy, sx, indexing='ij') if TORCH_1_10 else torch.meshgrid(sy, sx)
        anchor_points.append(torch.stack((sx, sy), -1).view(-1, 2))
        stride_tensor.append(torch.full((h * w, 1), stride, dtype=dtype, device=device))
    return torch.cat(anchor_points), torch.cat(stride_tensor)

def dist2bbox(distance, anchor_points, xywh=True, dim=-1):
    """
    Description
    -----------
    The dist2bbox function transforms distances from anchor points to bounding box coordinates. The output can be in either (x, y, width, height) format or (x1, y1, x2, y2) format.

    Arguments
    ---------
        distance (torch.Tensor): A tensor representing distances (left, top, right, bottom) from anchor points.
        
        anchor_points (torch.Tensor): A tensor representing the anchor points.
        
        xywh (bool): If True, the output bounding boxes are in (x, y, width, height) format. If False, the output is in (x1, y1, x2, y2) format. Default is True.
        
        dim (int): The dimension along which to split the distance tensor. Default is -1.

    Returns
    -------
        bboxes (torch.Tensor): The transformed bounding boxes in the specified format.
    """
    lt, rb = torch.split(distance, 2, dim)
    x1y1 = anchor_points - lt
    x2y2 = anchor_points + rb
    if xywh:
        c_xy = (x1y1 + x2y2) / 2
        wh = x2y2 - x1y1
        return torch.cat((c_xy, wh), dim)  # xywh bbox
    return torch.cat((x1y1, x2y2), dim)  # xyxy bbox

def intersect_dicts(da, db, exclude=()):
    """
    Description
    -----------
    The intersect_dicts function returns the intersection of two dictionaries based on matching keys and shapes of their values, while excluding specified keys.

    Arguments
    ---------
        da (dict): The first dictionary.
        
        db (dict): The second dictionary.
        
        exclude (tuple): A tuple of keys to exclude from the intersection. Default is an empty tuple.

    Returns
    -------
        intersection (dict): A dictionary containing the intersection of da and db based on matching keys and shapes, excluding specified keys.
    """
    return {k: v for k, v in da.items() if k in db and all(x not in k for x in exclude) and v.shape == db[k].shape}

def check_amp(model):
    """
    Description
    -----------
    The check_amp function checks if PyTorch Automatic Mixed Precision (AMP) functionality is available and can be used with the given model. It returns True if AMP can be used, otherwise False.

    Arguments
    ---------
        model (torch.nn.Module): The PyTorch model to check for AMP compatibility.

    Returns
    -------
        result (bool): True if AMP can be used, False otherwise.
    """
    prefix = 'AMP: '
    device = next(model.parameters()).device  # get model device
    if device.type in ('cpu', 'mps'):
        return False  # AMP only used on CUDA devices
    try:
        LOGGER.info(f'{prefix} {True} checks passed')
        return True
    except Exception:
        help_url = 'https://github.com/ultralytics/yolov5/issues/7908'
        LOGGER.warning(f'{prefix} {False} checks failed, disabling Automatic Mixed Precision. See {help_url}')
        return False

def check_img_size(imgsz, s=32, floor=0):
    """
    Description
    -----------
    The check_img_size function verifies that the given image size is a multiple of a specified stride. If the image size is not a multiple, it adjusts the size accordingly and logs a warning.

    Arguments
    ---------
        imgsz (int or list/tuple of int): The image size. It can be an integer (for square images) or a list/tuple of integers (for width and height).
        
        s (int): The stride value that the image size must be a multiple of. Default is 32.
        
        floor (int): The minimum allowable value for the image size. Default is 0.

    Returns
    -------
        new_size (int or list of int): The adjusted image size that is a multiple of the stride.
    """
    if isinstance(imgsz, int):  # integer i.e. img_size=640
        new_size = max(make_divisible(imgsz, int(s)), floor)
    else:  # list i.e. img_size=[640, 480]
        imgsz = list(imgsz)  # convert to list if tuple
        new_size = [max(make_divisible(x, int(s)), floor) for x in imgsz]
    if new_size != imgsz:
        LOGGER.warning(f'must be multiple of max stride {s}, updating to {new_size}')
    return new_size

def one_cycle(y1=0.0, y2=1.0, steps=100):
    """
    Description
    -----------
    The one_cycle function generates a lambda function that computes a sinusoidal ramp from y1 to y2 over a specified number of steps. This is typically used for learning rate schedules in training neural networks.

    Arguments
    ---------
        y1 (float): The starting value of the ramp. Default is 0.0.
        
        y2 (float): The ending value of the ramp. Default is 1.0.
        
        steps (int): The number of steps over which the ramp progresses. Default is 100.

    Returns
    -------
        ramp_function (function): A lambda function that computes the value at step x in the ramp.
    """
    return lambda x: ((1 - math.cos(x * math.pi / steps)) / 2) * (y2 - y1) + y1

def one_flat_cycle(y1=0.0, y2=1.0, steps=100):
    """
    Description
    -----------
    The one_flat_cycle function generates a lambda function that computes a sinusoidal ramp from y1 to y2 over a specified number of steps, with the first half of the steps remaining flat at y1. This can be useful for certain learning rate schedules where an initial flat period is desired.

    Arguments
    ---------
        y1 (float): The starting value and the flat value for the first half of the steps. Default is 0.0.
        
        y2 (float): The ending value of the ramp. Default is 1.0.
        
        steps (int): The total number of steps over which the ramp progresses. Default is 100.

    Returns
    -------
        ramp_function (function): A lambda function that computes the value at step x in the ramp.
    """
    #return lambda x: ((1 - math.cos(x * math.pi / steps)) / 2) * (y2 - y1) + y1
    return lambda x: ((1 - math.cos((x - (steps // 2)) * math.pi / (steps // 2))) / 2) * (y2 - y1) + y1 if (x > (steps // 2)) else y1

def labels_to_class_weights(labels, nc=80):
    """
    Description
    -----------
    The labels_to_class_weights function calculates class weights based on the inverse frequency of class occurrences in the training labels. These weights are useful for balancing the training process when classes are imbalanced.

    Arguments
    ---------
        labels (list of numpy arrays): A list of label arrays, where each label array corresponds to an image and has the format [class, x, y, w, h].
        
        nc (int): The number of classes. Default is 80.

    Returns
    -------
        weights (torch.Tensor): A tensor containing the normalized class weights.
    """
    if labels[0] is None:  # no labels loaded
        return torch.Tensor()

    labels = np.concatenate(labels, 0)  # labels.shape = (866643, 5) for COCO
    classes = labels[:, 0].astype(int)  # labels = [class xywh]
    weights = np.bincount(classes, minlength=nc)  # occurrences per class

    # Prepend gridpoint count (for uCE training)
    # gpi = ((320 / 32 * np.array([1, 2, 4])) ** 2 * 3).sum()  # gridpoints per image
    # weights = np.hstack([gpi * len(labels)  - weights.sum() * 9, weights * 9]) ** 0.5  # prepend gridpoints to start

    weights[weights == 0] = 1  # replace empty bins with 1
    weights = 1 / weights  # number of targets per class
    weights /= weights.sum()  # normalize
    return torch.from_numpy(weights).float()

def box_iou(box1, box2, eps=1e-7):
    # https://github.com/pytorch/vision/blob/master/torchvision/ops/boxes.py
    """
    Description
    -----------
    The box_iou function computes the Intersection-over-Union (IoU), also known as the Jaccard index, between two sets of bounding boxes. The IoU is a measure of the overlap between two bounding boxes and is used extensively in object detection tasks.

    Arguments
    ---------
        box1 (torch.Tensor): A tensor of shape (N, 4) representing the first set of bounding boxes, where each box is defined by (x1, y1, x2, y2).
        
        box2 (torch.Tensor): A tensor of shape (M, 4) representing the second set of bounding boxes, where each box is defined by (x1, y1, x2, y2).
        
        eps (float): A small value added to the denominator for numerical stability. Default is 1e-7.

    Returns
    -------
        iou (torch.Tensor): A tensor of shape (N, M) containing the pairwise IoU values for each pair of bounding boxes from box1 and box2.
    """
    # inter(N,M) = (rb(N,M,2) - lt(N,M,2)).clamp(0).prod(2)
    (a1, a2), (b1, b2) = box1.unsqueeze(1).chunk(2, 2), box2.unsqueeze(0).chunk(2, 2)
    inter = (torch.min(a2, b2) - torch.max(a1, b1)).clamp(0).prod(2)

    # IoU = inter / (area1 + area2 - inter)
    return inter / ((a2 - a1).prod(2) + (b2 - b1).prod(2) - inter + eps)

def bbox_iou(box1, box2, xywh=True, GIoU=False, DIoU=False, CIoU=False, MDPIoU=False, feat_h=640, feat_w=640, eps=1e-7):
    """
    Description
    -----------
    The bbox_iou function calculates the Intersection over Union (IoU) and its variants (GIoU, DIoU, CIoU, MDPIoU) between a single bounding box and a set of bounding boxes. It can handle both (x, y, w, h) and (x1, y1, x2, y2) formats.

    Arguments
    ---------
        box1 (torch.Tensor): A tensor of shape (1, 4) representing a single bounding box.
        
        box2 (torch.Tensor): A tensor of shape (n, 4) representing multiple bounding boxes.
        
        xywh (bool): If True, the bounding boxes are in (x, y, w, h) format. If False, they are in (x1, y1, x2, y2) format. Default is True.
        
        GIoU (bool): If True, calculate Generalized IoU. Default is False.
        
        DIoU (bool): If True, calculate Distance IoU. Default is False.
        
        CIoU (bool): If True, calculate Complete IoU. Default is False.
        
        MDPIoU (bool): If True, calculate Modified Distance IoU. Default is False.
        
        feat_h (int): Height of the feature map used for MDPIoU calculation. Default is 640.
        
        feat_w (int): Width of the feature map used for MDPIoU calculation. Default is 640.
        
        eps (float): A small value to avoid division by zero. Default is 1e-7.

    Returns
    -------
        iou (torch.Tensor): A tensor containing the IoU or its variants for each pair of bounding boxes.
    """
    # Get the coordinates of bounding boxes
    if xywh:  # transform from xywh to xyxy
        (x1, y1, w1, h1), (x2, y2, w2, h2) = box1.chunk(4, -1), box2.chunk(4, -1)
        w1_, h1_, w2_, h2_ = w1 / 2, h1 / 2, w2 / 2, h2 / 2
        b1_x1, b1_x2, b1_y1, b1_y2 = x1 - w1_, x1 + w1_, y1 - h1_, y1 + h1_
        b2_x1, b2_x2, b2_y1, b2_y2 = x2 - w2_, x2 + w2_, y2 - h2_, y2 + h2_
    else:  # x1, y1, x2, y2 = box1
        b1_x1, b1_y1, b1_x2, b1_y2 = box1.chunk(4, -1)
        b2_x1, b2_y1, b2_x2, b2_y2 = box2.chunk(4, -1)
        w1, h1 = b1_x2 - b1_x1, b1_y2 - b1_y1 + eps
        w2, h2 = b2_x2 - b2_x1, b2_y2 - b2_y1 + eps

    # Intersection area
    inter = (torch.min(b1_x2, b2_x2) - torch.max(b1_x1, b2_x1)).clamp(0) * \
            (torch.min(b1_y2, b2_y2) - torch.max(b1_y1, b2_y1)).clamp(0)

    # Union Area
    union = w1 * h1 + w2 * h2 - inter + eps

    # IoU
    iou = inter / union
    if CIoU or DIoU or GIoU:
        cw = torch.max(b1_x2, b2_x2) - torch.min(b1_x1, b2_x1)  # convex (smallest enclosing box) width
        ch = torch.max(b1_y2, b2_y2) - torch.min(b1_y1, b2_y1)  # convex height
        if CIoU or DIoU:  # Distance or Complete IoU https://arxiv.org/abs/1911.08287v1
            c2 = cw ** 2 + ch ** 2 + eps  # convex diagonal squared
            rho2 = ((b2_x1 + b2_x2 - b1_x1 - b1_x2) ** 2 + (b2_y1 + b2_y2 - b1_y1 - b1_y2) ** 2) / 4  # center dist ** 2
            if CIoU:  # https://github.com/Zzh-tju/DIoU-SSD-pytorch/blob/master/utils/box/box_utils.py#L47
                v = (4 / math.pi ** 2) * torch.pow(torch.atan(w2 / h2) - torch.atan(w1 / h1), 2)
                with torch.no_grad():
                    alpha = v / (v - iou + (1 + eps))
                return iou - (rho2 / c2 + v * alpha)  # CIoU
            return iou - rho2 / c2  # DIoU
        c_area = cw * ch + eps  # convex area
        return iou - (c_area - union) / c_area  # GIoU https://arxiv.org/pdf/1902.09630.pdf
    elif MDPIoU:
        d1 = (b2_x1 - b1_x1) ** 2 + (b2_y1 - b1_y1) ** 2
        d2 = (b2_x2 - b1_x2) ** 2 + (b2_y2 - b1_y2) ** 2
        mpdiou_hw_pow = feat_h ** 2 + feat_w ** 2
        return iou - d1 / mpdiou_hw_pow - d2 / mpdiou_hw_pow  # MPDIoU
    return iou  # IoU

def bbox2dist(anchor_points, bbox, reg_max):
    """
    Description
    -----------
    The bbox2dist function transforms bounding box coordinates in (x1, y1, x2, y2) format to distance format (left, top, right, bottom) relative to anchor points.

    Arguments
    ---------
        anchor_points (torch.Tensor): A tensor of shape (n, 2) representing the anchor points with (x, y) coordinates.
        
        bbox (torch.Tensor): A tensor of shape (n, 4) representing bounding boxes in (x1, y1, x2, y2) format.
        
        reg_max (float): The maximum allowable value for the distance.

    Returns
    -------
        distances (torch.Tensor): A tensor of shape (n, 4) representing the distances from the anchor points to the sides of the bounding boxes in (left, top, right, bottom) format.
    """
    x1y1, x2y2 = torch.split(bbox, 2, -1)
    return torch.cat((anchor_points - x1y1, x2y2 - anchor_points), -1).clamp(0, reg_max - 0.01)  # dist (lt, rb)

def xywh2xyxy(x):
    """
    Description
    -----------
    The xywh2xyxy function converts bounding boxes from (x, y, w, h) format to (x1, y1, x2, y2) format, where x1, y1 is the top-left corner and x2, y2 is the bottom-right corner.

    Arguments
    ---------
        x (torch.Tensor or np.ndarray): A tensor or numpy array of shape (n, 4) representing bounding boxes in (x, y, w, h) format.

    Returns
    -------
        y (torch.Tensor or np.ndarray): A tensor or numpy array of the same shape as x, with bounding boxes in (x1, y1, x2, y2) format.
    """
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[..., 0] = x[..., 0] - x[..., 2] / 2  # top left x
    y[..., 1] = x[..., 1] - x[..., 3] / 2  # top left y
    y[..., 2] = x[..., 0] + x[..., 2] / 2  # bottom right x
    y[..., 3] = x[..., 1] + x[..., 3] / 2  # bottom right y
    return y

def xyxy2xywh(x):
    """
    Description
    -----------
    The xyxy2xywh function converts bounding boxes from (x1, y1, x2, y2) format to (x, y, w, h) format, where x1, y1 is the top-left corner and x2, y2 is the bottom-right corner.

    Arguments
    ---------
        x (torch.Tensor or np.ndarray): A tensor or numpy array of shape (n, 4) representing bounding boxes in (x1, y1, x2, y2) format.

    Returns
    -------
        y (torch.Tensor or np.ndarray): A tensor or numpy array of the same shape as x, with bounding boxes in (x, y, w, h) format.
    """
    y = x.clone() if isinstance(x, torch.Tensor) else np.copy(x)
    y[..., 0] = (x[..., 0] + x[..., 2]) / 2  # x center
    y[..., 1] = (x[..., 1] + x[..., 3]) / 2  # y center
    y[..., 2] = x[..., 2] - x[..., 0]  # width
    y[..., 3] = x[..., 3] - x[..., 1]  # height
    return y

class TryExcept(contextlib.ContextDecorator):
    """
    Description
    -----------
    The TryExcept class is a context manager and decorator designed to catch and handle exceptions, printing a custom message along with the exception details. It can be used both as a decorator and within a with statement.

    Arguments
    ---------
        msg (str): A custom message to print along with the exception details. Default is an empty string ''.

    Methods
    -------
        init(self, msg=''): Initializes the context manager with an optional custom message.
        
        enter(self): No operation is performed when entering the context.
        
        exit(self, exc_type, value, traceback): Catches any exceptions, prints the custom message and exception details, and suppresses the exception.
    """
    def __init__(self, msg=''):
        self.msg = msg

    def __enter__(self):
        pass

    def __exit__(self, exc_type, value, traceback):
        if value:
            print(f"{self.msg}{': ' if self.msg else ''}{value}")
        return True

class ConfusionMatrix:
    """
    Description
    -----------
    The ConfusionMatrix class is designed to compute and visualize the confusion matrix for object detection tasks. It processes batches of detections and ground truth labels, updates the confusion matrix, and provides methods to plot and print the matrix.

    Arguments
    ---------
        nc (int): Number of classes.
        
        conf (float): Confidence threshold for detections. Default is 0.25.
        
        iou_thres (float): IoU threshold for determining matches between detections and ground truth. Default is 0.45.

    Methods
    -------
    """
    def __init__(self, nc, conf=0.25, iou_thres=0.45):
        self.matrix = np.zeros((nc + 1, nc + 1))
        self.nc = nc  # number of classes
        self.conf = conf
        self.iou_thres = iou_thres

    def process_batch(self, detections, labels):
        """
        Updates the confusion matrix with a batch of detections and labels.
            detections (Array[N, 6]): x1, y1, x2, y2, conf, class
            
            labels (Array[M, 5]): class, x1, y1, x2, y2

            Return: None, updates confusion matrix accordingly
        """
        if detections is None:
            gt_classes = labels.int()
            for gc in gt_classes:
                self.matrix[self.nc, gc] += 1  # background FN
            return

        detections = detections[detections[:, 4] > self.conf]
        gt_classes = labels[:, 0].int()
        detection_classes = detections[:, 5].int()
        iou = box_iou(labels[:, 1:], detections[:, :4])

        x = torch.where(iou > self.iou_thres)
        if x[0].shape[0]:
            matches = torch.cat((torch.stack(x, 1), iou[x[0], x[1]][:, None]), 1).cpu().numpy()
            if x[0].shape[0] > 1:
                matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(matches[:, 1], return_index=True)[1]]
                matches = matches[matches[:, 2].argsort()[::-1]]
                matches = matches[np.unique(matches[:, 0], return_index=True)[1]]
        else:
            matches = np.zeros((0, 3))

        n = matches.shape[0] > 0
        m0, m1, _ = matches.transpose().astype(int)
        for i, gc in enumerate(gt_classes):
            j = m0 == i
            if n and sum(j) == 1:
                self.matrix[detection_classes[m1[j]], gc] += 1  # correct
            else:
                self.matrix[self.nc, gc] += 1  # true background

        if n:
            for i, dc in enumerate(detection_classes):
                if not any(m1 == i):
                    self.matrix[dc, self.nc] += 1  # predicted background

    def matrix(self):
        """
        Returns the confusion matrix.
        """
        return self.matrix

    def tp_fp(self):
        """
        Returns true positives and false positives for each class.
        """
        tp = self.matrix.diagonal()  # true positives
        fp = self.matrix.sum(1) - tp  # false positives
        # fn = self.matrix.sum(0) - tp  # false negatives (missed detections)
        return tp[:-1], fp[:-1]  # remove background class

    @TryExcept('WARNING ConfusionMatrix plot failure')
    def plot(self, normalize=True, save_dir='', names=()):
        """
        Plots the confusion matrix.
            normalize (bool): If True, normalizes the confusion matrix by dividing each column by its sum. Default is True.
            
            save_dir (str): Directory where the plot image will be saved. Default is ''.
            
            names (tuple): Class names to be used as labels on the plot. Default is an empty tuple ().
        """
        import seaborn as sn

        array = self.matrix / ((self.matrix.sum(0).reshape(1, -1) + 1E-9) if normalize else 1)  # normalize columns
        array[array < 0.005] = np.nan  # don't annotate (would appear as 0.00)

        fig, ax = plt.subplots(1, 1, figsize=(12, 9), tight_layout=True)
        nc, nn = self.nc, len(names)  # number of classes, names
        sn.set(font_scale=1.0 if nc < 50 else 0.8)  # for label size
        labels = (0 < nn < 99) and (nn == nc)  # apply names to ticklabels
        ticklabels = (names + ['background']) if labels else "auto"
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')  # suppress empty matrix RuntimeWarning: All-NaN slice encountered
            sn.heatmap(array,
                       ax=ax,
                       annot=nc < 30,
                       annot_kws={
                           "size": 8},
                       cmap='Blues',
                       fmt='.2f',
                       square=True,
                       vmin=0.0,
                       xticklabels=ticklabels,
                       yticklabels=ticklabels).set_facecolor((1, 1, 1))
        ax.set_ylabel('True')
        ax.set_ylabel('Predicted')
        ax.set_title('Confusion Matrix')
        fig.savefig(Path(save_dir) / 'confusion_matrix.png', dpi=250)
        plt.close(fig)

    def print(self):
        """
        Prints the confusion matrix.
        """
        for i in range(self.nc + 1):
            print(' '.join(map(str, self.matrix[i])))

class Profile(contextlib.ContextDecorator):
    """
    Description
    -----------
    The Profile class is a context manager and decorator for profiling code execution time. It measures the time taken for a block of code or function to execute and can accumulate the total time over multiple usages.

    Arguments
    ---------
        t (float): Initial accumulated time. Default is 0.0.

    Methods
    -------
        init(self, t=0.0): Initializes the profiler with an optional initial accumulated time.
        
        enter(self): Starts the timer when entering the context.
        
        exit(self, type, value, traceback): Stops the timer when exiting the context and updates the accumulated time.
    """
    def __init__(self, t=0.0):
        self.t = t
        self.cuda = torch.cuda.is_available()

    def __enter__(self):
        self.start = self.time()
        return self

    def __exit__(self, type, value, traceback):
        self.dt = self.time() - self.start  # delta-time
        self.t += self.dt  # accumulate dt

    def time(self):
        """
        Returns the current time, with synchronization if CUDA is available.
        """
        if self.cuda:
            torch.cuda.synchronize()
        return time.time()

def non_max_suppression(
        prediction,
        conf_thres=0.25,
        iou_thres=0.45,
        classes=None,
        agnostic=False,
        multi_label=False,
        labels=(),
        max_det=300,
        nm=0,  # number of masks
):
    """
    Description
    -----------
    The non_max_suppression function performs Non-Maximum Suppression (NMS) on the inference results to reject overlapping detections. It filters out low-confidence detections and removes redundant bounding boxes based on their Intersection over Union (IoU).

    Arguments
    ---------
        prediction (torch.Tensor): The model's output tensor of shape (batch_size, num_predictions, 5 + num_classes + num_masks).
        
        conf_thres (float): Confidence threshold to filter detections. Default is 0.25.
        
        iou_thres (float): IoU threshold for NMS. Default is 0.45.
        
        classes (list of int, optional): List of class indices to keep. Default is None.
        
        agnostic (bool): If True, NMS is class-agnostic. Default is False.
        
        multi_label (bool): If True, allows multiple labels per box. Default is False.
        
        labels (list of torch.Tensor, optional): List of ground truth labels for auto-labelling. Default is ().
        
        max_det (int): Maximum number of detections per image. Default is 300.
        
        nm (int): Number of masks. Default is 0.

    Returns
    -------
        output (list of torch.Tensor): List of tensors, one for each image in the batch, each of shape (n, 6 + num_masks) containing detections [x1, y1, x2, y2, conf, cls, mask...].
    """
    import torchvision

    if isinstance(prediction, (list, tuple)):  # YOLO model in validation model, output = (inference_out, loss_out)
        prediction = prediction[0]  # select only inference output

    device = prediction.device
    mps = 'mps' in device.type  # Apple MPS
    if mps:  # MPS not fully supported yet, convert tensors to CPU before NMS
        prediction = prediction.cpu()
    bs = prediction.shape[0]  # batch size
    nc = prediction.shape[1] - nm - 4  # number of classes
    mi = 4 + nc  # mask start index
    xc = prediction[:, 4:mi].amax(1) > conf_thres  # candidates

    # Checks
    assert 0 <= conf_thres <= 1, f'Invalid Confidence threshold {conf_thres}, valid values are between 0.0 and 1.0'
    assert 0 <= iou_thres <= 1, f'Invalid IoU {iou_thres}, valid values are between 0.0 and 1.0'

    # Settings
    # min_wh = 2  # (pixels) minimum box width and height
    max_wh = 7680  # (pixels) maximum box width and height
    max_nms = 30000  # maximum number of boxes into torchvision.ops.nms()
    time_limit = 2.5 + 0.05 * bs  # seconds to quit after
    redundant = True  # require redundant detections
    multi_label &= nc > 1  # multiple labels per box (adds 0.5ms/img)
    merge = False  # use merge-NMS

    t = time.time()
    output = [torch.zeros((0, 6 + nm), device=prediction.device)] * bs
    for xi, x in enumerate(prediction):  # image index, image inference
        # Apply constraints
        # x[((x[:, 2:4] < min_wh) | (x[:, 2:4] > max_wh)).any(1), 4] = 0  # width-height
        x = x.T[xc[xi]]  # confidence

        # Cat apriori labels if autolabelling
        if labels and len(labels[xi]):
            lb = labels[xi]
            v = torch.zeros((len(lb), nc + nm + 5), device=x.device)
            v[:, :4] = lb[:, 1:5]  # box
            v[range(len(lb)), lb[:, 0].long() + 4] = 1.0  # cls
            x = torch.cat((x, v), 0)

        # If none remain process next image
        if not x.shape[0]:
            continue

        # Detections matrix nx6 (xyxy, conf, cls)
        box, cls, mask = x.split((4, nc, nm), 1)
        box = xywh2xyxy(box)  # center_x, center_y, width, height) to (x1, y1, x2, y2)
        if multi_label:
            i, j = (cls > conf_thres).nonzero(as_tuple=False).T
            x = torch.cat((box[i], x[i, 4 + j, None], j[:, None].float(), mask[i]), 1)
        else:  # best class only
            conf, j = cls.max(1, keepdim=True)
            x = torch.cat((box, conf, j.float(), mask), 1)[conf.view(-1) > conf_thres]

        # Filter by class
        if classes is not None:
            x = x[(x[:, 5:6] == torch.tensor(classes, device=x.device)).any(1)]

        # Apply finite constraint
        # if not torch.isfinite(x).all():
        #     x = x[torch.isfinite(x).all(1)]

        # Check shape
        n = x.shape[0]  # number of boxes
        if not n:  # no boxes
            continue
        elif n > max_nms:  # excess boxes
            x = x[x[:, 4].argsort(descending=True)[:max_nms]]  # sort by confidence
        else:
            x = x[x[:, 4].argsort(descending=True)]  # sort by confidence

        # Batched NMS
        c = x[:, 5:6] * (0 if agnostic else max_wh)  # classes
        boxes, scores = x[:, :4] + c, x[:, 4]  # boxes (offset by class), scores
        i = torchvision.ops.nms(boxes, scores, iou_thres)  # NMS
        if i.shape[0] > max_det:  # limit detections
            i = i[:max_det]
        if merge and (1 < n < 3E3):  # Merge NMS (boxes merged using weighted mean)
            # update boxes as boxes(i,4) = weights(i,n) * boxes(n,4)
            iou = box_iou(boxes[i], boxes) > iou_thres  # iou matrix
            weights = iou * scores[None]  # box weights
            x[i, :4] = torch.mm(weights, x[:, :4]).float() / weights.sum(1, keepdim=True)  # merged boxes
            if redundant:
                i = i[iou.sum(1) > 1]  # require redundancy

        output[xi] = x[i]
        if mps:
            output[xi] = output[xi].to(device)
        if (time.time() - t) > time_limit:
            LOGGER.warning(f'NMS time limit {time_limit:.3f}s exceeded')
            break  # time limit exceeded

    return output

def clip_boxes(boxes, shape):
    """
    Description
    -----------
    The clip_boxes function clips the coordinates of bounding boxes to fit within the specified image shape. This ensures that the bounding boxes do not extend outside the boundaries of the image.

    Arguments
    ---------
        boxes (torch.Tensor or np.ndarray): A tensor or numpy array of shape (n, 4) representing bounding boxes in (x1, y1, x2, y2) format.
        
        shape (tuple): A tuple representing the image shape as (height, width).
    """
    if isinstance(boxes, torch.Tensor):  # faster individually
        boxes[:, 0].clamp_(0, shape[1])  # x1
        boxes[:, 1].clamp_(0, shape[0])  # y1
        boxes[:, 2].clamp_(0, shape[1])  # x2
        boxes[:, 3].clamp_(0, shape[0])  # y2
    else:  # np.array (faster grouped)
        boxes[:, [0, 2]] = boxes[:, [0, 2]].clip(0, shape[1])  # x1, x2
        boxes[:, [1, 3]] = boxes[:, [1, 3]].clip(0, shape[0])  # y1, y2

def scale_boxes(img1_shape, boxes, img0_shape, ratio_pad=None):
    """
    Description
    -----------
    The scale_boxes function rescales bounding boxes from one image shape to another. This is useful for adjusting bounding boxes after resizing or padding operations on the images.

    Arguments
    ---------
        img1_shape (tuple): Shape of the image after resizing/padding as (height, width).
        
        boxes (torch.Tensor or np.ndarray): A tensor or numpy array of shape (n, 4) representing bounding boxes in (x1, y1, x2, y2) format.
        
        img0_shape (tuple): Original shape of the image as (height, width).
        
        ratio_pad (tuple, optional): A tuple containing the scaling ratio and padding. If not provided, it will be calculated from img0_shape.

    Returns
    -------
        boxes (torch.Tensor or np.ndarray): Rescaled bounding boxes adjusted to the original image shape.
    """
    if ratio_pad is None:  # calculate from img0_shape
        gain = min(img1_shape[0] / img0_shape[0], img1_shape[1] / img0_shape[1])  # gain  = old / new
        pad = (img1_shape[1] - img0_shape[1] * gain) / 2, (img1_shape[0] - img0_shape[0] * gain) / 2  # wh padding
    else:
        gain = ratio_pad[0][0]
        pad = ratio_pad[1]

    boxes[:, [0, 2]] -= pad[0]  # x padding
    boxes[:, [1, 3]] -= pad[1]  # y padding
    boxes[:, :4] /= gain
    clip_boxes(boxes, img0_shape)
    return boxes

def scale_image(im1_shape, masks, im0_shape, ratio_pad=None):
    """
    Description
    -----------
    The scale_image function rescales masks from the model input shape to the original image shape. This is useful for mapping masks back to the original image size after they have been processed by the model.

    Arguments
    ---------
        im1_shape (tuple): Shape of the model input image as [height, width].
        
        masks (np.ndarray): Array of masks with shape [height, width, num] or [height, width].
        
        im0_shape (tuple): Shape of the original image as [height, width, channels].
        
        ratio_pad (tuple, optional): A tuple containing the scaling ratio and padding. If not provided, it will be calculated from im0_shape.

    Returns
    -------
        masks (np.ndarray): Rescaled masks adjusted to the original image shape.
    """
    import cv2
    # Rescale coordinates (xyxy) from im1_shape to im0_shape
    if ratio_pad is None:  # calculate from im0_shape
        gain = min(im1_shape[0] / im0_shape[0], im1_shape[1] / im0_shape[1])  # gain  = old / new
        pad = (im1_shape[1] - im0_shape[1] * gain) / 2, (im1_shape[0] - im0_shape[0] * gain) / 2  # wh padding
    else:
        pad = ratio_pad[1]
    top, left = int(pad[1]), int(pad[0])  # y, x
    bottom, right = int(im1_shape[0] - pad[1]), int(im1_shape[1] - pad[0])

    if len(masks.shape) < 2:
        raise ValueError(f'"len of masks shape" should be 2 or 3, but got {len(masks.shape)}')
    masks = masks[top:bottom, left:right]
    # masks = masks.permute(2, 0, 1).contiguous()
    # masks = F.interpolate(masks[None], im0_shape[:2], mode='bilinear', align_corners=False)[0]
    # masks = masks.permute(1, 2, 0).contiguous()
    masks = cv2.resize(masks, (im0_shape[1], im0_shape[0]))

    if len(masks.shape) == 2:
        masks = masks[:, :, None]
    return masks

def is_writeable(dir, test=False):
    """
    Description
    -----------
    The is_writeable function checks if a directory has write permissions. Optionally, it can test writing to the directory by creating and deleting a temporary file.

    Arguments
    ---------
        dir (str or Path): The directory to check for write permissions.
        
        test (bool): If True, test writing by creating and deleting a temporary file. Default is False.

    Returns
    -------
        (bool): True if the directory has write permissions, otherwise False.
    """
    if not test:
        return os.access(dir, os.W_OK)  # possible issues on Windows
    file = Path(dir) / 'tmp.txt'
    try:
        with open(file, 'w'):  # open file with write permissions
            pass
        file.unlink()  # remove file
        return True
    except OSError:
        return False

def user_config_dir(dir='Ultralytics', env_var='YOLOV5_CONFIG_DIR'):
    """
    Description
    -----------
    The user_config_dir function returns the path to the user configuration directory. It prioritizes the directory specified by an environment variable, and if not set, it uses OS-specific default directories. If necessary, the directory is created.

    Arguments
    ---------
        dir (str): The name of the directory to create/use within the user configuration directory. Default is 'Ultralytics'.
        
        env_var (str): The name of the environment variable to check for a custom configuration directory. Default is 'YOLOV5_CONFIG_DIR'.

    Returns
    -------
        path (Path): The path to the user configuration directory.
    """
    env = os.getenv(env_var)
    if env:
        path = Path(env)  # use environment variable
    else:
        cfg = {'Windows': 'AppData/Roaming', 'Linux': '.config', 'Darwin': 'Library/Application Support'}  # 3 OS dirs
        path = Path.home() / cfg.get(platform.system(), '')  # OS-specific config dir
        path = (path if is_writeable(path) else Path('/tmp')) / dir  # GCP and AWS lambda fix, only /tmp is writeable
    path.mkdir(exist_ok=True)  # make if required
    return path
CONFIG_DIR = user_config_dir()  # Ultralytics settings dir

def check_font(font=FONT, progress=False):
    """
    Description
    -----------
    The check_font function checks if a specified font file exists locally. If not, it downloads the font file to a configuration directory.

    Arguments
    ---------
        font (Path or str): The path to the font file. Default is FONT.
        
        progress (bool): If True, displays a progress bar during download. Default is False.
    """
    font = Path(font)
    file = CONFIG_DIR / font.name
    if not font.exists() and not file.exists():
        url = f'https://ultralytics.com/assets/{font.name}'
        LOGGER.info(f'Downloading {url} to {file}...')
        torch.hub.download_url_to_file(url, str(file), progress=progress)

def compute_ap(recall, precision):
    """
    Description
    -----------
    The compute_ap function computes the Average Precision (AP) given the recall and precision curves. AP is a popular metric used in evaluating object detection models.

    Arguments
    ---------
        recall (list or np.ndarray): The recall curve.
        
        precision (list or np.ndarray): The precision curve.

    Returns
    -------
        ap (float): The average precision.
        
        mpre (np.ndarray): The precision curve with sentinel values.
        
        mrec (np.ndarray): The recall curve with sentinel values.
    """

    # Append sentinel values to beginning and end
    mrec = np.concatenate(([0.0], recall, [1.0]))
    mpre = np.concatenate(([1.0], precision, [0.0]))

    # Compute the precision envelope
    mpre = np.flip(np.maximum.accumulate(np.flip(mpre)))

    # Integrate area under curve
    method = 'interp'  # methods: 'continuous', 'interp'
    if method == 'interp':
        x = np.linspace(0, 1, 101)  # 101-point interp (COCO)
        ap = np.trapz(np.interp(x, mrec, mpre), x)  # integrate
    else:  # 'continuous'
        i = np.where(mrec[1:] != mrec[:-1])[0]  # points where x axis (recall) changes
        ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])  # area under curve

    return ap, mpre, mrec

def ap_per_class(tp, conf, pred_cls, target_cls, plot=False, save_dir='.', names=(), eps=1e-16, prefix=""):
    """
    Description
    -----------
    The ap_per_class function computes the average precision (AP) for each class given the true positives, confidence scores, predicted classes, and target classes. It can also plot precision-recall curves and other related metrics. Source: https://github.com/rafaelpadilla/Object-Detection-Metrics.

    Arguments
    ---------
        tp (np.ndarray): True positives (nx1 or nx10).
        
        conf (np.ndarray): Objectness value from 0 to 1.
        
        pred_cls (np.ndarray): Predicted object classes.
        
        target_cls (np.ndarray): True object classes.
        
        plot (bool): If True, plots the precision-recall curve at mAP@0.5. Default is False.
        
        save_dir (str): Directory to save the plot. Default is '.'.
        
        names (dict): Class names dictionary.
        
        eps (float): Small value to avoid division by zero. Default is 1e-16.
        
        prefix (str): Prefix for plot filenames. Default is "".

    Returns
    -------
        tp (np.ndarray): True positives per class.
        
        fp (np.ndarray): False positives per class.
        
        p (np.ndarray): Precision per class.
        
        r (np.ndarray): Recall per class.
        
        f1 (np.ndarray): F1 score per class.
        
        ap (np.ndarray): Average precision per class.
        
        unique_classes (np.ndarray): Array of unique class indices.
    """

    # Sort by objectness
    i = np.argsort(-conf)
    tp, conf, pred_cls = tp[i], conf[i], pred_cls[i]

    # Find unique classes
    unique_classes, nt = np.unique(target_cls, return_counts=True)
    nc = unique_classes.shape[0]  # number of classes, number of detections

    # Create Precision-Recall curve and compute AP for each class
    px, py = np.linspace(0, 1, 1000), []  # for plotting
    ap, p, r = np.zeros((nc, tp.shape[1])), np.zeros((nc, 1000)), np.zeros((nc, 1000))
    for ci, c in enumerate(unique_classes):
        i = pred_cls == c
        n_l = nt[ci]  # number of labels
        n_p = i.sum()  # number of predictions
        if n_p == 0 or n_l == 0:
            continue

        # Accumulate FPs and TPs
        fpc = (1 - tp[i]).cumsum(0)
        tpc = tp[i].cumsum(0)

        # Recall
        recall = tpc / (n_l + eps)  # recall curve
        r[ci] = np.interp(-px, -conf[i], recall[:, 0], left=0)  # negative x, xp because xp decreases

        # Precision
        precision = tpc / (tpc + fpc)  # precision curve
        p[ci] = np.interp(-px, -conf[i], precision[:, 0], left=1)  # p at pr_score

        # AP from recall-precision curve
        for j in range(tp.shape[1]):
            ap[ci, j], mpre, mrec = compute_ap(recall[:, j], precision[:, j])
            if plot and j == 0:
                py.append(np.interp(px, mrec, mpre))  # precision at mAP@0.5

    # Compute F1 (harmonic mean of precision and recall)
    f1 = 2 * p * r / (p + r + eps)
    names = [v for k, v in names.items() if k in unique_classes]  # list: only classes that have data
    names = dict(enumerate(names))  # to dict
    if plot:
        plot_pr_curve(px, py, ap, Path(save_dir) / f'{prefix}PR_curve.png', names)
        plot_mc_curve(px, f1, Path(save_dir) / f'{prefix}F1_curve.png', names, ylabel='F1')
        plot_mc_curve(px, p, Path(save_dir) / f'{prefix}P_curve.png', names, ylabel='Precision')
        plot_mc_curve(px, r, Path(save_dir) / f'{prefix}R_curve.png', names, ylabel='Recall')

    i = smooth(f1.mean(0), 0.1).argmax()  # max F1 index
    p, r, f1 = p[:, i], r[:, i], f1[:, i]
    tp = (r * nt).round()  # true positives
    fp = (tp / (p + eps) - tp).round()  # false positives
    return tp, fp, p, r, f1, ap, unique_classes.astype(int)

def fitness(x):
    """
    Description
    -----------
    The fitness function calculates the fitness of a model based on a weighted combination of precision, recall, and mean Average Precision (mAP) metrics. This fitness score is used to evaluate and compare model performance.

    Arguments
    ---------
        x (np.ndarray): A 2D array where each row contains the metrics [P, R, mAP@0.5, mAP@0.5:0.95] for a different model or experiment.

    Returns
    -------
        fitness_scores (np.ndarray): A 1D array containing the fitness score for each row in x.
    """
    w = [0.0, 0.0, 0.1, 0.9]  # weights for [P, R, mAP@0.5, mAP@0.5:0.95]
    return (x[:, :4] * w).sum(1)

def strip_optimizer(f='best.pt', s=''):  # from utils.general import *; strip_optimizer()
    """
    Description
    -----------
    The strip_optimizer function removes unnecessary components from a PyTorch model checkpoint, such as the optimizer state, to finalize the model for inference. This process reduces the file size and prepares the model for deployment. Optionally, the function can save the modified checkpoint to a new file.

    Arguments
    ---------
        f (str): Path to the model checkpoint file. Default is 'best.pt'.
        
        s (str): Path to save the stripped model checkpoint. If not provided, the original file will be overwritten. Default is ''.
    """
    x = torch.load(f, map_location=torch.device('cpu'))
    if x.get('ema'):
        x['model'] = x['ema']  # replace model with ema
    for k in 'optimizer', 'best_fitness', 'ema', 'updates':  # keys
        x[k] = None
    x['epoch'] = -1
    x['model'].half()  # to FP16
    for p in x['model'].parameters():
        p.requires_grad = False
    torch.save(x, s or f)
    mb = os.path.getsize(s or f) / 1E6  # filesize
    LOGGER.info(f"Optimizer stripped from {f},{f' saved as {s},' if s else ''} {mb:.1f}MB")





