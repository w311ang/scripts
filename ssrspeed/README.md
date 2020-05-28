# SSRSpeed于Termux上的一键安装脚本
```bash
pkg install -y wget && wget -O ssrspeed-install.sh https://raw.githubusercontent.com/w311ang/SSRSpeed-script/master/install.sh && bash ssrspeed-install.sh
```
## 注意
由于Termux软件包的特性，SSRSpeed的依赖包`libsodium`无`ldconfig`工具，将无法通过依赖检查，故需要使用将`--skip-requirements-check`参数内置的`main.sh`或`web.sh`
>Pillow 在安装期间检测库的方式发生了变化，阻止了termux上的安装，而termux没有 /sbin/ldconfig .现在已修复。
>
>—— [5.4.1 — Pillow (PIL Fork) 7.0.0 文档](https://www.osgeo.cn/pillow/releasenotes/5.4.1.html)
## 考古
[原issue](https://github.com/NyanChanMeow/SSRSpeed/issues/108)
