# Design and Application of Intelligent Multipath Routing based on SDN <!-- omit in toc -->

> 基于SDN网络的智能多路路由的设计与应用

![floodlight](https://shields.io/badge/Floodlight-master-red)
![ubuntu](https://shields.io/badge/Ubuntu-22.04-blue)

- [运行 Floodlight](#运行-floodlight)
  - [安装 Java（二选一）](#安装-java二选一)
    - [安装 JavaSE 8（首选）](#安装-javase-8首选)
    - [安装 JavaSE 7（只能使用 v1.2 及以下版本）](#安装-javase-7只能使用-v12-及以下版本)
  - [安装 Ant](#安装-ant)
  - [克隆 Floodlight 代码仓库](#克隆-floodlight-代码仓库)
  - [选择版本（此项目使用 master 版本）](#选择版本此项目使用-master-版本)
    - [使用 master 版本](#使用-master-版本)
    - [选择 v1.2 版本](#选择-v12-版本)
- [使用 Mininet 创建虚拟拓扑网络](#使用-mininet-创建虚拟拓扑网络)

## 运行 Floodlight

### 安装 Java（二选一）

#### 安装 JavaSE 8（首选）

```sh
sudo apt install openjdk-8-jdk
```

#### 安装 JavaSE 7（只能使用 v1.2 及以下版本）

1. 从 [Oracle 官网](https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html) 下载压缩包 `jdk-7u80-linux-x64.tar.gz`

2. 解压压缩包并移动到 `/usr/lib/jvm` 文件夹
   
   ```bash
   tar -zxvf jdk-7u80-linux-x64.tar.gz
   ```

3. 编辑 `.bashrc`，把以下变量写入文件中
   
   ```bash
   vim .bashrc
   ```
   
   ```bash
   export JAVA_HOME="/usr/lib/jvm"
   export JRE_HOME="$JAVA_HOME/jre"
   export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
   export PATH=$PATH:$JAVA_HOME/bin
   ```

4. 重新加载配置并检查 JavaSE 版本
   ```bash
   source .bashrc
   java -version
   ```

### 安装 Ant

```
sudo apt install ant
```

### 克隆 Floodlight 代码仓库

使用 `git clone` 命令从 GitHub 克隆代码仓库（二选一）

1. 使用 `http` 链接 **（无需预先配置）**
   
   ```sh
   git clone https://github.com/floodlight/floodlight.git
   ```

2. 使用 `ssh` 链接 **（需要在 GitHub 配置好 ssh 密钥，下载速度更快且更稳定）**
   
   ```sh
   git clone git@github.com:floodlight/floodlight.git
   ```

### 选择版本（此项目使用 master 版本）

#### 使用 master 版本

从 GitHub 仓库直接克隆的代码仓库无法通过 `ant` 命令直接编译  

因为 `lib` 中 `thrift` 的版本未升级

解决办法：

1. 从 [Maven Repository](https://mvnrepository.com/artifact/org.apache.thrift/libthrift/0.14.1) 下载 `libthrift-0.14.1.jar`

2. 将 `libthrift-0.14.1.jar` 放入 `/lib` 文件夹（可以删除老版本的 `libthrift-0.9.0.jar`）

3. 修改 [build.xml](./floodlight//build.xml) 文件，将第 76 行
   
   ```xml
   <include name="libthrift-0.9.0.jar"/>
   ```
   
   修改为
   
   ```xml
   <include name="libthrift-0.14.1.jar"/>
   ```

4. 删除 [TestEventLoop.java](./floodlight/src/test/java/net/floodlightcontroller/core/test/TestEventLoop.java) 文件第 105 行的 `@Override`
   
   ```java
    // @Override
    public ChannelFuture register(ChannelPromise promise) {
        return null;
    }
   ```

5. 编译源文件
   
   ```sh
   ant
   ```

6. 运行 floodlight
   
   ```sh
   java -jar ./target/floodlight.jar
   ```

#### 选择 v1.2 版本

`v1.2` 版本使用 JavaSE 7 编写，但是 JavaSE 8 也可运行，高版本 ant 也可以编译

1. 检出 v1.2 版本
   
   ```sh
   git checkout v1.2
   ```

2. 编译源文件
   
   ```sh
   ant
   ```

3. 运行 floodlight
   
   ```sh
   java -jar ./target/floodlight.jar
   ```


## 使用 Mininet 创建虚拟拓扑网络
