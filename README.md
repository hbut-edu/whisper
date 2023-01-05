# 《openai whisper》冬季短学期实习项目 完整步骤

## 构建openai whisper环境

### 下载并安装anaconda（windows）

官方网站：

```https://www.anaconda.com/```

安装后，从菜单里面打开```Anaconda Powershell Prompt```

可以看到一个命令行窗口，命令行的前面显示```(base)```，代表anaconda的base虚拟环境处于激活状态，也代表你的安装正常完成了

### 安装Git工具

* Git是一种版本管理工具，在本项目中，我们主要是使用它抓取开源代码，并构建我们的运行环境

在命令行中使用下面的指令安装Git工具

```winget install --id Git.Git -e --source winget```

如果安装时遇到网络延时等错误，请到下面的地址直接按照正常流程安装

```https://git-scm.com/download/win```

一般我们选择64bit版本的下载并安装

安装完毕后，关闭并重新打开```Anaconda Powershell Prompt```，键入```git -v```指令检查安装是否正常完成

### 安装ffmpeg工具

* ffmpeg工具的作用是音视频的编解码，在本项目中主要使用它处理音频信号

在下面的地址下载ffmpeg

```https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z```

下载文件是一个压缩包，将其解压，并放到一个稳定的位置，之后我们会将这个地址放入系统的Path环境变量中。 如下：

![1.png](images%2F1.png)

![2.png](images%2F2.png)

设置完毕后，关闭并重新打开```Anaconda Powershell Prompt```，键入```ffmpeg```指令检查安装是否正常完成

### 构建whisper运行环境

* 在这一步里面，我们需要从网络上下载openai准备的whisper代码以及环境

首先在```Anaconda Powershell Prompt```中创建一个虚拟环境并激活它，使用下面的代码：

创建虚拟环境（名称为whisper），并同时安装python环境：
```conda create -n whisper python```

激活虚拟环境：
```conda activate whipser```

当虚拟环境成功创建并激活后，命令行前端的```(base)```应该变为```(whisper)```

***注意：下面的操作都需要在whisper虚拟环境下进行***

输入```python --version```检查python环境是否正常安装完成

* 接下来，我们使用Git工具从网络上下载whisper代码

源地址：```https://github.com/openai/whisper```

国内中转地址：```https://gitee.com/ryukinkou/whisper.git```

源地址的下载可能会遇到网络问题，可以从国内中转地址抓取代码，命令如下：

```pip install git+https://gitee.com/ryukinkou/whisper.git```

等待安装完成

### 安装gradio环境

* gradio是一个用于快速构建Web UI前端的工具，在本项目中仅作为一个演示样例

***注意：下面的操作都需要在whisper虚拟环境下进行***

直接安装gradio运行库，命令如下：

```pip install gradio```

如果你的python版本大于3.9，还需要将pillow库降级到9.0，使用下面的命令：

```pip install pillow==9.0.0```

至此，环境构建完成了。

## 样例代码

### 设定IDE

在本例中，我们使用pycharm工具开发项目

在pycharm中创建项目的时候，需要选择解释器环境，我们需要选择到前一步构建的虚拟环境做为项目的解释器，如下：

在这个界面我们首先选择```Previously configured interpreter```，然后选择```Add interpreter```。
![3.png](images%2F3.png)

在弹出的节目左侧列表中选择```Conda environment```，并在下拉列表中选择我们在上一步创建的虚拟环境```whisper```。
![4.png](images%2F4.png)

### 运行示例代码

运行main.py文件中的代码，如果一切正常，在Run窗口中会出现一个地址，打开它。

![5.png](images%2F5.png)

如果一切正常，下面的界面会出现在你的浏览器里。

![6.png](images%2F6.png)