# Glados自动签到

## 食用方式：

### 注册一个GLaDOS的账号([注册地址](https://glados.space/landing/0A58E-NV28S-6U3QV-33VMG))

#### 我的邀请码：([0A58E-NV28S-6U3QV-33VMG](https://0a58e-nv28s-6u3qv-33vmg.glados.space)) 

#### 我的优惠码（9折）：([DEVILSTORE](https://0a58e-nv28s-6u3qv-33vmg.glados.space)) 

### **Fork**本仓库

![图片加载失败](imgs/1.png)

### 添加**secret**

1. 跳转至自己的仓库的`Settings`->`Secrets and variables`->`Action`

2. 添加1个`repository secret`，命名为`GLADOS_COOKIES`，其值对应GLaDOS账号的cookie值中的有效部分（获取方式如下）

- 在GLaDOS的签到页面按`F12`

- 切换到`Network`页面下，刷新

![图片加载失败](imgs/2.png)

- 点击第一个选项卡后在`Request Headers`下找到`Cookie`，右键复制cookie的值即可

  > 参考格式：koa:sess=eyJ1c2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxAwMH0=; koa:sess.sig=xJkOxxxxxxxxxxxxxxxtnM;

![图片加载失败](imgs/3.png)

- 多账号请在 `GLADOS_COOKIES` 中添加多个 cookie，中间使用 `&` 连接即可（例如：`c1&c2&c3`）。每个 cookie 会依次尝试 glados.cloud 和 railgun.info，在所属域名签到后就不再尝试其他域名。

3. 配置积分兑换策略（非必须）

- 添加1个`repository secret`，命名为`GLADOS_EXCHANGE_PLAN`，配置自动兑换积分策略：

| 值 | 积分要求 | 兑换天数 |
|---|---------|---------|
| `plan100` | 100 积分 | 10 天 |
| `plan200` | 200 积分 | 30 天 |
| `plan500` | 500 积分 | 100 天 (默认) |

> 不配置时默认为 `plan500`，即积分达到 500 时自动兑换 100 天

4. 手机推送（非必须）

- 添加1个`repository secret`，命名为`PUSHDEER_SENDKEY`，其值对应 PushDeer key: ([获取地址](https://www.pushdeer.com/product.html))。

5. 详细日志（非必须）

- 添加1个`repository secret`，命名为`GLADOS_VERBOSE`，值为`true`时日志中会显示剩余天数、积分和兑换结果。公开仓库的 Actions 日志所有人都能看到，介意的话不要开启。

### **star**自己的仓库

![图片加载失败](imgs/4.png)

## 文件结构

```shell
│  checkin.py	# 签到脚本
│  logging_config.py	# 日志配置 (北京时间)
│  test_checkin.py	# 单元测试 (不访问网络), 运行: python -m unittest
│
├─.github
│  └─workflows
│          gladosCheck.yml	# Actions 配置文件
```

## 更新日志

- **2026-01**: 重构代码，添加log输出方便定位，支持新版网址，支持配置积分兑换策略。
- **2026-04**: 优化代码逻辑，优化日志输出，支持[新版域名](https://railgun.info) ，在 GLADOS_COOKIES 中添加新版域名下的 cookies 即可使用。
- **2026-11**: 签到失败时工作流报错 (GitHub 会发邮件提醒)，请求出错自动重试，每天多次尝试签到；cookie 在所属域名签到后不再尝试其他域名，汇总按账号计数；积分不足时不再请求兑换；日志时间改为北京时间。

## 定时任务漏跑怎么办

GitHub 的定时任务在高峰期经常被推迟几个小时，甚至直接跳过，所以工作流每天安排了 5 次运行 (已签到时只会显示重复签到)。如果仍然经常漏签，可以用外部定时服务 (例如免费的 [cron-job.org](https://cron-job.org)) 通过 GitHub API 触发工作流，会准时得多：

1. 在 GitHub 的 `Settings` -> `Developer settings` -> `Personal access tokens` -> `Fine-grained tokens` 生成一个 token：`Repository access` 只选本仓库，`Permissions` 中把 `Actions` 设为 `Read and write`。
2. 在 cron-job.org 新建任务，每天执行一次 (例如北京时间 9:00)：
   - URL：`https://api.github.com/repos/<你的用户名>/<仓库名>/actions/workflows/gladosCheck.yml/dispatches`
   - 请求方法 `POST`，请求体 `{"ref":"master"}` (`master` 为仓库的默认分支名)
   - 请求头：`Authorization: Bearer <上一步生成的 token>`、`Accept: application/vnd.github+json`、`Content-Type: application/json`
3. 测试运行返回 2xx 状态码即表示成功，Actions 页面会出现一次由 `workflow_dispatch` 触发的运行。

token 到期后需要重新生成，并更新到 cron-job.org。


## 问题排查与定位
- 大家可以通过查询 actions 中的 running checkin 日志快速定位问题，有其他问题提交issue。

  <img width="1684" height="844" alt="image" src="https://github.com/user-attachments/assets/45348a5f-43e4-45f5-8fdf-ce84d343b30d" />

## 声明

本项目不保证稳定运行与更新, 因GitHub相关规定可能会删库, 请注意备份







