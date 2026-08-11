# Inevitable Zero 简体中文兼容 Fork

[English README](README_EN.md)

本 Fork 在上游 [Kyuuhachi/Inevitable-Zero](https://github.com/Kyuuhachi/Inevitable-Zero) 的基础上，加入 NISA PC 版《零之轨迹》简体中文构建路径，用于兼容 zeroTool 汉化及其汉化版 More Portraits。

目前只上传源代码，**尚未发布任何 Release**。本仓库也不包含从游戏或汉化补丁提取的受版权保护数据。

## 覆盖任务

- 店员的待客指导（ID 54）
- 寻找某人（ID 55）
- 寻找贪睡医师（ID 56）
- 续·主日学校的特别讲师（ID 57）
- 终极面包对决！（ID 58）

## 中文构建的主要变化

- 新增 `--cn`，只构建中文脚本路径，不生成英文脚本。
- 可读取云豹 PSV Evolution 繁体中文 donor 的自定义双字节编码。
- 通过 `--vita-charmap` 传入外部字符映射；donor 与映射数据不随仓库分发。
- 通过 zeroTool `zCodec -tw2s` 在构建时调用 OpenCC，将繁体中文转换为简体中文。
- PC 输入与输出使用 GBK，并保留 zeroTool 的特殊字符映射。
- 以汉化版 More Portraits 的中文脚本作为合并基线。

## 构建示例

```powershell
python patch.py `
  <vita-evo-data> `
  <pc-cn-wrapper-data> `
  <output> `
  -p <more-portraits-cn-wrapper-data> `
  --cn `
  --vita-charmap <charmap_expanded.json> `
  --zcodec <zCodec.exe> `
  --no-misc
```

生成目录中的 `scena`、`text` 应在最终兼容包中分别放入：

```text
data_cn/scena
data_cn/text
```

语言无关的任务资源仍放在 `data/` 下。中文兼容包使用松散文件覆盖，不使用 P3A 或 `order.txt`。

## 当前状态

- 39 个任务相关脚本已完成静态构建与字节往返校验。
- `t_quest._dt` 已包含五个简体中文任务名。
- 已建立测试候选包，但尚未完成游戏内全流程、分支、DP、奖励和贴图验证。
- 在完成游戏验证前不会发布正式 Release。

## 致谢与来源

- 原 MOD 与移植逻辑：[Kyuuhachi](https://github.com/Kyuuhachi/Inevitable-Zero)。
- 中文工具与本体汉化：[zeroTool](https://github.com/J31why/zeroTool)。
- 本 Fork 所参考的繁体中文汉化补丁由科洛蒂娅公主（KloseRInz）等人基于云豹娱乐（CLE）本地化并发行的 PSV Evolution 亚洲版本提取制作。感谢公主等人制作并保存这份汉化补丁。

上游原始说明、英文安装信息与完整 Credits 请参阅 [README_EN.md](README_EN.md)。
