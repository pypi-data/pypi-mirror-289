import torch
import torch.nn as nn

import numpy as np
import random
import scipy.stats as stats
import pandas as pd
from pathlib import Path

from ycsai.utils.general import (yaml_load)


def apply_ccm(image, ccm):
    """ Converts a given RGB image to the color space of a specific camera or vice versa. """
    shape = image.shape
    image = image.view(-1, 3)
    image = torch.tensordot(image, ccm, dims=[[-1], [-1]])
    return image.view(shape)

def random_noise_levels():
    """ Generate shot noise and read noise
        shot noise: The amount of photons incident on a given area of ​​the sensor is not constant over time but is random. This randomness causes it to appear as noise in the image.
        read noise: A form of electronic noise that occurs in digital image sensors, occurring during the process in which the image sensor converts signals into digital values.    
    """
    log_min_shot_noise = np.log(0.0001)
    log_max_shot_noise = np.log(0.012)
    log_shot_noise = np.random.uniform(log_min_shot_noise, log_max_shot_noise)
    shot_noise = np.exp(log_shot_noise)

    line = lambda x: 2.18 * x + 1.20
    log_read_noise = line(log_shot_noise) + np.random.normal(scale=0.26)
    read_noise = np.exp(log_read_noise)
    return shot_noise, read_noise

def Low_Illumination_Degrading(img, safe_invert=False):
    """
        img (Tensor): Input normal light images of shape (C, H, W).
        img_meta(dict): A image info dict contain some information like name ,shape ...
        return:
        img_deg (Tensor): Output degration low light images of shape (C, H, W).
        degration_info(Tensor): Output degration paramter in the whole process.
    """
    device = img.device
    config = dict(darkness_range=(0.01, 0.1),
                           gamma_range=(2.0, 3.5),
                           rgb_range=(0.8, 1.0),
                           red_range=(1.9, 2.4),
                           blue_range=(1.5, 1.9),
                           quantisation=[12, 14, 16])
    xyz2cams = [[[1.0234, -0.2969, -0.2266],
                 [-0.5625, 1.6328, -0.0469],
                 [-0.0703, 0.2188, 0.6406]],
                [[0.4913, -0.0541, -0.0202],
                 [-0.613, 1.3513, 0.2906],
                 [-0.1564, 0.2151, 0.7183]],
                [[0.838, -0.263, -0.0639],
                 [-0.2887, 1.0725, 0.2496],
                 [-0.0627, 0.1427, 0.5438]],
                [[0.6596, -0.2079, -0.0562],
                 [-0.4782, 1.3016, 0.1933],
                 [-0.097, 0.1581, 0.5181]]]
    rgb2xyz = [[0.4124564, 0.3575761, 0.1804375],
               [0.2126729, 0.7151522, 0.0721750],
               [0.0193339, 0.1191920, 0.9503041]]

    img1 = img.permute(1, 2, 0)
    # inverse tone mapping
    img1 = 0.5 - torch.sin(torch.asin(1.0 - 2.0 * img1) / 3.0)
    # inverse gamma correction
    epsilon = torch.tensor([1e-8], dtype=torch.float, device=device)
    gamma = random.uniform(config['gamma_range'][0], config['gamma_range'][1])
    img2 = torch.max(img1, epsilon) ** gamma
    # convert sRGB to cRGB
    xyz2cam = random.choice(xyz2cams)
    rgb2cam = np.matmul(xyz2cam, rgb2xyz)
    rgb2cam = torch.from_numpy(rgb2cam / np.sum(rgb2cam, axis=-1)).to(torch.float).to(torch.device(device))
    img3 = apply_ccm(img2, rgb2cam)

    # inverse white balancing
    rgb_gain = random.normalvariate(config['rgb_range'][0], config['rgb_range'][1])
    red_gain = random.uniform(config['red_range'][0], config['red_range'][1])
    blue_gain = random.uniform(config['blue_range'][0], config['blue_range'][1])

    gains1 = np.stack([1.0 / red_gain, 1.0, 1.0 / blue_gain]) * rgb_gain
    gains1 = gains1[np.newaxis, np.newaxis, :]
    gains1 = torch.tensor(gains1, dtype=torch.float, device=device)

    if safe_invert:
        img3_gray = torch.mean(img3, dim=-1, keepdim=True)
        inflection = 0.9
        zero = torch.zeros_like(img3_gray, device=device)
        mask = (torch.max(img3_gray - inflection, zero) / (1.0 - inflection)) ** 2.0
        safe_gains = torch.max(mask + (1.0 - mask) * gains1, gains1)
        img4 = torch.clamp(img3 * safe_gains, min=0.0, max=1.0)
    else:
        img4 = img3 * gains1
    
    # darkness: low photon number
    lower, upper = config['darkness_range'][0], config['darkness_range'][1]
    mu, sigma = 0.1, 0.08
    darkness = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    darkness = darkness.rvs()
    img5 = img4 * darkness

    # add shot and read noise
    shot_noise, read_noise = random_noise_levels()
    var = img5 * shot_noise + read_noise
    var = torch.max(var, epsilon)
    noise = torch.normal(mean=0, std=torch.sqrt(var))
    img6 = img5 + noise

    # quantisation noise using uniform distribution
    bits = random.choice(config['quantisation'])
    quan_noise = torch.tensor(img6.size(), dtype=torch.float, device=device).uniform_(-1 / (255 * bits), 1 / (255 * bits))
    img7 = img6 + quan_noise
    # white balancing
    gains2 = np.stack([red_gain, 1.0, blue_gain])
    gains2 = gains2[np.newaxis, np.newaxis, :]
    gains2 = torch.tensor(gains2, dtype=torch.float, device=device)
    img8 = img7 * gains2
    # convert cRGB to sRGB
    cam2rgb = torch.inverse(rgb2cam)
    img9 = apply_ccm(img8, cam2rgb)
    img10 = torch.max(img9, epsilon) ** (1 / gamma)
    # gamma correction
    img_low = img10.permute(2, 0, 1)
    para_gt = torch.tensor([darkness, 1.0 / gamma, 1.0 / red_gain, 1.0 / blue_gain], dtype=torch.float, device=device)
    return img_low, para_gt

def export_formats():
    # model export formats
    x = [
        ['PyTorch', '-', '.pt', True, True],
        ['TorchScript', 'torchscript', '.torchscript', True, True],
        ['ONNX', 'onnx', '.onnx', True, True],
        ['ONNX END2END', 'onnx_end2end', '_end2end.onnx', True, True],
        ['OpenVINO', 'openvino', '_openvino_model', True, False],
        ['TensorRT', 'engine', '.engine', False, True],
        ['CoreML', 'coreml', '.mlmodel', True, False],
        ['TensorFlow SavedModel', 'saved_model', '_saved_model', True, True],
        ['TensorFlow GraphDef', 'pb', '.pb', True, True],
        ['TensorFlow Lite', 'tflite', '.tflite', True, False],
        ['TensorFlow Edge TPU', 'edgetpu', '_edgetpu.tflite', False, False],
        ['TensorFlow.js', 'tfjs', '_web_model', False, False],
        ['PaddlePaddle', 'paddle', '_paddle_model', True, True],]
    return pd.DataFrame(x, columns=['Format', 'Argument', 'Suffix', 'CPU', 'GPU'])

class Ensemble(nn.ModuleList):
    # Ensemble of models
    def __init__(self):
        super().__init__()

    def forward(self, x, augment=False, profile=False, visualize=False):
        y = [module(x, augment, profile, visualize)[0] for module in self]
        # y = torch.stack(y).max(0)[0]  # max ensemble
        # y = torch.stack(y).mean(0)  # mean ensemble
        y = torch.cat(y, 1)  # nms ensemble
        return y, None  # inference, train output

def attempt_load(weights, device=None, inplace=True, fuse=True):
    # Loads an ensemble of models weights=[a,b,c] or a single model weights=[a] or weights=a
    from ycsai.models.tasks import Detect, Model

    model = Ensemble()
    for w in weights if isinstance(weights, list) else [weights]:
        ckpt = torch.load(w, map_location='cpu')  # load
        ckpt = (ckpt.get('ema') or ckpt['model']).to(device).float()  # FP32 model

        # Model compatibility updates
        if not hasattr(ckpt, 'stride'):
            ckpt.stride = torch.tensor([32.])
        if hasattr(ckpt, 'names') and isinstance(ckpt.names, (list, tuple)):
            ckpt.names = dict(enumerate(ckpt.names))  # convert to dict

        model.append(ckpt.fuse().eval() if fuse and hasattr(ckpt, 'fuse') else ckpt.eval())  # model in eval mode

    # Module compatibility updates
    for m in model.modules():
        t = type(m)
        if t in (nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6, nn.SiLU, Detect, Model):
            m.inplace = inplace  # torch 1.7.0 compatibility
            # if t is Detect and not isinstance(m.anchor_grid, list):
            #    delattr(m, 'anchor_grid')
            #    setattr(m, 'anchor_grid', [torch.zeros(1)] * m.nl)
        elif t is nn.Upsample and not hasattr(m, 'recompute_scale_factor'):
            m.recompute_scale_factor = None  # torch 1.11.0 compatibility

    # Return model
    if len(model) == 1:
        return model[-1]

    # Return detection ensemble
    print(f'Ensemble created with {weights}\n')
    for k in 'names', 'nc', 'yaml':
        setattr(model, k, getattr(model[0], k))
    model.stride = model[torch.argmax(torch.tensor([m.stride.max() for m in model])).int()].stride  # max stride
    assert all(model[0].nc == m.nc for m in model), f'Models have different class counts: {[m.nc for m in model]}'
    return model

class DetectMultiBackend(nn.Module):
    # YOLO MultiBackend class for python inference on various backends
    def __init__(self, weights='best.pt', device=torch.device('cpu'), dnn=False, data=None, fp16=False, fuse=True):
        super().__init__()
        w = str(weights[0] if isinstance(weights, list) else weights)
        pt, jit, onnx, onnx_end2end, xml, engine, coreml, saved_model, pb, tflite, edgetpu, tfjs, paddle, triton = self._model_type(w)
        fp16 &= pt or jit or onnx or engine  # FP16
        nhwc = coreml or saved_model or pb or tflite or edgetpu  # BHWC formats (vs torch BCWH)
        stride = 32  # default stride
        cuda = torch.cuda.is_available() and device.type != 'cpu'  # use CUDA

        if pt:  # PyTorch
            model = attempt_load(weights if isinstance(weights, list) else w, device=device, inplace=True, fuse=fuse)
            stride = max(int(model.stride.max()), 32)  # model stride
            names = model.module.names if hasattr(model, 'module') else model.names  # get class names
            model.half() if fp16 else model.float()
            self.model = model  # explicitly assign for to(), cpu(), cuda(), half()
        else:
            raise NotImplementedError(f'ERROR: {w} is not a supported format')
        
        # class names
        if 'names' not in locals():
            names = yaml_load(data)['names'] if data else {i: f'class{i}' for i in range(999)}
        
        self.__dict__.update(locals())  # assign all variables to self
    
    def forward(self, im, augment=False, visualize=False):
        b, ch, h, w = im.shape  # batch, channel, height, width
        if self.fp16 and im.dtype != torch.float16:
            im = im.half()  # to FP16
        if self.nhwc:
            im = im.permute(0, 2, 3, 1)  # torch BCHW to numpy BHWC shape(1,320,192,3)
        
        if self.pt:  # PyTorch
            y = self.model(im, augment=augment, visualize=visualize) if augment or visualize else self.model(im)
        
        if isinstance(y, (list, tuple)):
            return self.from_numpy(y[0]) if len(y) == 1 else [self.from_numpy(x) for x in y]
        else:
            return self.from_numpy(y)
    
    def from_numpy(self, x):
        return torch.from_numpy(x).to(self.device) if isinstance(x, np.ndarray) else x
    
    def warmup(self, imgsz=(1, 3, 640, 640)):
        # Warmup model by running inference once
        warmup_types = self.pt, self.jit, self.onnx, self.engine, self.saved_model, self.pb, self.triton
        if any(warmup_types) and (self.device.type != 'cpu' or self.triton):
            im = torch.empty(*imgsz, dtype=torch.half if self.fp16 else torch.float, device=self.device)  # input
            for _ in range(2 if self.jit else 1):  #
                self.forward(im)  # warmup
    
    @staticmethod
    def _model_type(p='path/to/model.pt'):
        # Return model type from model path, i.e. path='path/to/model.onnx' -> type=onnx
        # types = [pt, jit, onnx, xml, engine, coreml, saved_model, pb, tflite, edgetpu, tfjs, paddle]
        sf = list(export_formats().Suffix)  # export suffixes
        types = [s in Path(p).name for s in sf]
        types[8] &= not types[9]  # tflite &= not edgetpu
        triton = not any(types)
        return types + [triton]