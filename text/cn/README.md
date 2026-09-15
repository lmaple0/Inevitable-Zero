# 零之轨迹中文文本数据

本目录保存 Inevitable Zero 中文兼容构建所需或用于校对的中文数据：

- `vita_charmap.json`：索尼发行的 PS Vita Evolution 繁体中文版自定义双字节编码映射。
- `quest54.json`–`quest58.json`：五个 Evolution 独占任务的简体中文任务表记录，包含标题、委托人、说明与阶段日志。
- `scena/*.py`：本 MOD 修改范围内的 39 个完整简体中文场景脚本反编译稿，已按 NISA Steam 1.5.5、zeroTool 零轨汉化 1.9 与 More Portraits in Zero 1.6.0 刷新。

繁体中文文本直接取自索尼发行的 PS Vita Evolution 繁体中文版；本次由本项目从用户提供的 NoNpDrm 备份中提取。公开范围限于本 MOD 涉及的任务记录和修改脚本，不是整个游戏的数据镜像。

构建时将 `vita_charmap.json` 传给 `--vita-charmap`。场景对白仍从使用者本地准备的 Vita donor 读取，并在构建时通过 zeroTool OpenCC 转为简体中文。
