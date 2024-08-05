# 基于[ultralytics](https://github.com/ultralytics/ultralytics)
    python: 3.8
    torch: 1.13.1
    torchvision: 0.14.1

# 环境配置

    1. 执行pip uninstall ultralytics把安装在环境里面的ultralytics库卸载干净.<这里需要注意,如果你也在使用yolov8,最好使用anaconda创建一个虚拟环境供本代码使用,避免环境冲突导致一些奇怪的问题>
    2. 卸载完成后同样再执行一次,如果出现WARNING: Skipping ultralytics as it is not installed.证明已经卸载干净.
    3. 如果需要使用官方的CLI运行方式,需要把ultralytics库安装一下,执行命令:<python setup.py develop>,当然安装后对本代码进行修改依然有效.(develop作用解释具体可看: https://blog.csdn.net/qq_16568205/article/details/110433714)  注意:不需要使用官方的CLI运行方式,可以选择跳过这步
    4. 额外需要的包安装命令:
        pip install timm thop efficientnet_pytorch einops grad-cam dill -i https://pypi.tuna.tsinghua.edu.cn/simple
        以下主要是使用dyhead必定需要安装的包,如果安装不成功dyhead没办法正常使用!
        pip install -U openmim
        mim install mmengine -i https://pypi.tuna.tsinghua.edu.cn/simple
        mim install "mmcv>=2.0.0" -i https://pypi.tuna.tsinghua.edu.cn/simple
    5. 运行时候如果还缺什么包就请自行安装即可.
