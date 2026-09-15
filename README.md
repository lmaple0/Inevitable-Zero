# Inevitable Zero 简体中文兼容 Fork

[English README](README_EN.md)

本 Fork 在上游 [Kyuuhachi/Inevitable-Zero](https://github.com/Kyuuhachi/Inevitable-Zero) 的基础上，加入 NISA PC 版《零之轨迹》简体中文构建路径，用于兼容 zeroTool 汉化及其汉化版 More Portraits。

最新中文兼容测试版为 [v0.2.0-rc1 Pre-release](https://github.com/lmaple0/Inevitable-Zero/releases/tag/v0.2.0-rc1)，基于 NISA Steam 1.5.5（build 24743052）、zeroTool 零轨汉化 1.9 与 More Portraits in Zero 1.6.0 刷新。仓库公开内容限于本 MOD 涉及的任务记录、完整合并脚本和构建所需映射，不是整个游戏的数据镜像。

## 覆盖任务

- 店员的待客指导（ID 54）
- 寻找某人（ID 55）
- 寻找贪睡医师（ID 56）
- 续·主日学校的特别讲师（ID 57）
- 终极面包对决！（ID 58）

## 中文构建的主要变化

- 新增 `--cn`，只构建中文脚本路径，不生成英文脚本。
- 可读取索尼发行的 PS Vita Evolution 繁体中文版 donor 的自定义双字节编码。
- 通过 `--vita-charmap` 传入字符映射；本仓库提供本次构建使用的映射，Vita donor 仍须由使用者自行准备。
- 通过 zeroTool `zCodec -tw2s` 在构建时调用 OpenCC，将繁体中文转换为简体中文。
- PC 输入与输出使用 GBK，并保留 zeroTool 的特殊字符映射。
- 以汉化版 More Portraits 的中文脚本作为合并基线。
- 适配 NISA 1.5.5 中 `c1410` 的新版嵌套控制流，同时兼容旧版直接分支布局。

## 构建示例

```powershell
python patch.py `
  <vita-evo-data> `
  <pc-cn-wrapper-data> `
  <output> `
  -p <more-portraits-cn-wrapper-data> `
  --cn `
  --vita-charmap text/cn/vita_charmap.json `
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

- 39 个任务相关脚本已从当前本机汉化与 More Portraits 1.6.0 基线重新合并并完成静态构建。
- Kreuzen 往返验证结果为 39/39 可解析，其中 36 个字节一致，`r0000.bin`、`r1000.bin`、`r1500.bin` 为 3 个已知布局归一化差异，0 个失败。
- `t_quest._dt` 已包含五个简体中文任务名。
- 已建立测试候选包，但尚未完成游戏内全流程、分支、DP、奖励和贴图验证。
- 当前仅发布 Pre-release；完成游戏内验证前不会发布稳定版 Release。

仓库中的 39 个完整中文合并稿可以在不重新读取 Vita donor 的情况下重建为
PC GBK 场景，用于工具链回归：

```powershell
python build_cn_scenarios.py <output-scena-directory>
```

该构建器写出的 7 字节 sepith 行与 NISA Zero 原生文件一致，并非 MOD 私有布局。
如使用 Kreuzen 检查这些输出，需显式指定 `--legacy-layout native`；不会自动回退到
Themélios 布局。

该入口只重建已经登记的场景脚本；任务表和语言无关资源仍由完整构建流程生成。

五个任务的可读简体中文任务表、字符映射及 39 个完整合并脚本位于 [`text/cn`](text/cn)，并随 Fork 一同维护。

## 致谢与来源

- 原 MOD 与移植逻辑：[Kyuuhachi](https://github.com/Kyuuhachi/Inevitable-Zero)。
- 中文工具与本体汉化：[zeroTool](https://github.com/J31why/zeroTool)。
- 繁体中文文本直接取自索尼发行的 PS Vita Evolution 繁体中文版；本次由本项目从用户提供的 NoNpDrm 备份中提取并用于中文兼容制作。

上游原始说明、英文安装信息与完整 Credits 请参阅 [README_EN.md](README_EN.md)。
