#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成静态数据文件供 Cloudflare Pages 部署使用
"""

import json
import os
from pathlib import Path
from workflow_db import WorkflowDatabase

def main():
    """生成所有静态数据文件"""
    
    print("🚀 开始生成静态数据文件...")
    print("=" * 50)
    
    # 创建数据目录
    data_dir = Path('static/data')
    data_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ 数据目录: {data_dir}")
    
    # 初始化数据库
    db = WorkflowDatabase()
    
    # 1. 生成所有工作流数据
    print("\n📊 步骤 1/4: 生成工作流数据...")
    all_workflows = []
    offset = 0
    limit = 100
    
    while True:
        workflows, total = db.search_workflows(query='', limit=limit, offset=offset)
        if not workflows:
            break
        all_workflows.extend(workflows)
        offset += limit
        print(f"  已处理: {len(all_workflows)}/{total} 个工作流")
        if offset >= total:
            break
    
    # 保存工作流数据
    workflows_file = data_dir / 'workflows.json'
    with open(workflows_file, 'w', encoding='utf-8') as f:
        json.dump({
            'workflows': all_workflows,
            'total': len(all_workflows),
            'generated_at': __import__('datetime').datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 已保存 {len(all_workflows)} 个工作流到: {workflows_file}")
    print(f"  📦 文件大小: {workflows_file.stat().st_size / 1024 / 1024:.2f} MB")
    
    # 2. 生成统计信息
    print("\n📈 步骤 2/4: 生成统计信息...")
    stats = db.get_stats()
    stats_file = data_dir / 'stats.json'
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 统计信息:")
    print(f"     - 总工作流: {stats['total']}")
    print(f"     - 活跃工作流: {stats['active']}")
    print(f"     - 总节点数: {stats['total_nodes']}")
    print(f"     - 集成服务: {stats['unique_integrations']}")
    
    # 3. 生成分类信息
    print("\n🏷️  步骤 3/4: 生成分类信息...")
    service_categories = db.get_service_categories()
    categories = list(service_categories.keys())
    categories_file = data_dir / 'categories.json'
    with open(categories_file, 'w', encoding='utf-8') as f:
        json.dump({
            'categories': sorted(categories),
            'service_categories': service_categories,
            'total': len(categories)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 已保存 {len(categories)} 个分类")
    
    # 4. 生成集成服务列表
    print("\n🔌 步骤 4/4: 生成集成服务列表...")
    # 从工作流中收集所有集成服务
    all_integrations = set()
    for w in all_workflows:
        all_integrations.update(w.get('integrations', []))
    
    integrations_file = data_dir / 'integrations.json'
    with open(integrations_file, 'w', encoding='utf-8') as f:
        json.dump({
            'integrations': sorted(list(all_integrations)),
            'total': len(all_integrations)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 已保存 {len(all_integrations)} 个集成服务")
    
    # 5. 生成搜索索引（用于快速搜索）
    print("\n🔍 生成搜索索引...")
    search_index = {
        'workflows': [
            {
                'id': w['filename'],
                'name': w['name'],
                'description': w['description'],
                'integrations': w['integrations'],
                'trigger_type': w['trigger_type'],
                'complexity': w['complexity'],
                'active': w.get('active', True),
                'node_count': w.get('node_count', 0)
            }
            for w in all_workflows
        ]
    }
    
    index_file = data_dir / 'search-index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 已保存搜索索引")
    
    # 总结
    print("\n" + "=" * 50)
    print("🎉 静态数据生成完成!")
    print("=" * 50)
    
    total_size = sum(f.stat().st_size for f in data_dir.glob('*.json'))
    print(f"\n📦 生成的文件:")
    for f in sorted(data_dir.glob('*.json')):
        size_mb = f.stat().st_size / 1024 / 1024
        print(f"   - {f.name}: {size_mb:.2f} MB")
    
    print(f"\n💾 总大小: {total_size / 1024 / 1024:.2f} MB")
    print(f"📁 输出目录: {data_dir.absolute()}")
    
    print("\n✨ 下一步:")
    print("   1. git add static/data/")
    print("   2. git commit -m 'Add static data for Cloudflare Pages'")
    print("   3. git push")
    print("   4. 在 Cloudflare Pages 部署你的项目")
    print("\n🚀 部署后访问速度将非常快!")

if __name__ == '__main__':
    main()
