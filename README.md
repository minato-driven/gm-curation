# gm-curation

Gemini AIを使用して記事コンテンツを自動生成し、はてなブログ（およびX/Twitter）へ自動投稿を行うためのPythonツールです。

## 概要

このプロジェクトは、Google Gemini APIを活用して特定のテーマ（現在は「モテるための秘訣」など）に基づいた記事を作成し、それをはてなブログに投稿するワークフローを自動化します。

## 前提条件

- Python 3.13 以上
- [uv](https://github.com/astral-sh/uv) (パッケージマネージャー)

## インストール

1. リポジトリをクローンします。
   ```bash
   git clone <repository-url>
   cd gm-curation
   ```

2. 依存関係をインストールします。
   ```bash
   uv sync
   ```

## 設定

プロジェクトのルートディレクトリに `.env` ファイルを作成し、以下の環境変数を設定してください。

```env
# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key

# Hatena Blog API
HATENA_DOMAIN=https://blog.hatena.ne.jp
HATENA_USERNAME=your_hatena_id
HATENA_BLOG_ID=your_blog_domain (例: example.hatenablog.com)
HATENA_API_KEY=your_hatena_api_key

# X (Twitter) API (Optional)
X_API_KEY=your_x_api_key
X_API_KEY_SECRET=your_x_api_key_secret
X_API_ACCESS_TOKEN=your_x_access_token
X_API_ACCESS_TOKEN_SECRET=your_x_access_token_secret
X_API_BEARER_TOKEN=your_x_bearer_token

# Logging (Optional)
GATEWAY_LOG=logs # ログファイルの保存先ディレクトリ（デフォルト: logs）
```

## 実行方法

メインスクリプトを実行して、記事の生成と投稿を行います。

```bash
uv run main.py
```

実行ログは `GATEWAY_LOG` で指定したディレクトリ（デフォルトは `logs/`）に保存されます。

## プロジェクト構成

- `main.py`: アプリケーションのエントリーポイント。記事生成から投稿までのフローを制御します。
- `gateway/`: 外部サービスとの通信を行うモジュール群。
  - `gemini_gateway.py`: Google Gemini APIとのインターフェース。
  - `hatena_gateway.py`: はてなブログAtomPub APIとのインターフェース。
  - `x_gateway.py`: X (Twitter) APIとのインターフェース。
  - `gateway.py`: Gatewayの基底クラス。
- `pyproject.toml`: プロジェクトの依存関係と設定定義。

## 開発

### リンター / フォーマッター

このプロジェクトでは [Ruff](https://github.com/astral-sh/ruff) を使用しています。

```bash
uv run ruff check .
uv run ruff format .
```
