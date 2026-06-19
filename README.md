# DatasetPassport

AI训练数据集质量与合规风险扫描器。

## MVP

- 支持 CSV、JSON、JSONL
- 检测邮箱、手机号、身份证格式等敏感信息
- 统计完全重复记录
- 检查必填字段缺失
- 输出来源可追溯性和许可证复核提示

## 运行

```bash
python main.py data.jsonl --required instruction,output,source --license apache-2.0 -o report.json
```

## 测试

```bash
python -m unittest -v
```

本工具只提供技术扫描结果，不能替代法律审查。

## License

MIT
