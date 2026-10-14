# eval-harness-lite

> 与 Text2SQL / Agent 落地内容配套的**轻量评测骨架**（MIT）。  
> 目标：clone 后约 10 分钟跑通「任务 → 假工具 → 计分」。

## 这是什么
- 不是完整生产平台
- 是可演示的 Python 小骨架：定义任务、记录轨迹、算成功率与越权标记
- 可与模板商店的 Cursor Rules、scorecard 一起用

## 快速开始
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python examples/run_demo.py
```

## 目录
```
eval-harness-lite/
  README.md
  LICENSE          # MIT
  requirements.txt
  harness/
    __init__.py
    types.py
    runner.py
    metrics.py
  examples/
    tasks_refund.yaml
    run_demo.py
```

## 付费边（可选）

开源核保持 MIT，clone 即可跑通「任务 → 假工具 → 计分」。

若需要更严的**私有规则包**（工具网关示例、Text2SQL 负例、CI 片段）或**一周答疑工单**（帮你把真实任务写成可执行断言）：

- **爱发电**：[https://afdian.com/a/laoyinai](https://afdian.com/a/laoyinai)
- 私信 / 微信备注 **「规则」** → Private Rules
- 备注 **「工单」** → 规则 + 一周异步答疑

边界：不承诺指标数字；不代写整站、不值守生产；不提供赌博/灰产自动化；不代打官方安全审计。  
公开仓无密钥、无客户数据；付费内容单独许可（可内部商用，禁整包转卖）。成交后发网盘或私有 git 邀请。

## 许可
MIT — 见 `LICENSE`。
