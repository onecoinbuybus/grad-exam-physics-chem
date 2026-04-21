# 大学院入試 物理化学 備考資料

東大化学システム工学専攻 修士入試の備考用LaTeX Beamer スライド。

## 構成

| フォルダ | 内容 |
|---------|------|
| `物理化学6/` | 量子化学の基礎（Schrödinger方程式・井戸型ポテンシャル） |
| `物理化学7/` | 量子化学の展開（調和振動子・回転・水素原子・変分法） |

## コンパイル方法

```bash
cd 物理化学6
lualatex main.tex
```

または Overleaf で "Import from GitHub" → LuaLaTeX でコンパイル。

## Overleaf同期

1. Overleaf → New Project → Import from GitHub
2. このリポジトリを選択
3. Menu → Compiler → **LuaLaTeX** に設定（`luatexja` パッケージが必須のため XeLaTeX では通らない）
