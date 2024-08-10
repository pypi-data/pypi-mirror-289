# umamail - 簡単にメール送信を実現するツール

## 概要 (Overview)

**umamail**は、Pythonで簡単にメールを送信するためのツールです。名前の由来は、日本語で「馬」を意味する「uma」と、未確認生物を指す「UMA」から来ており、驚くほど簡単にメールを送信できるツールというコンセプトが込められています。このツールは、複雑な設定やコーディングを必要とせず、シンプルなインターフェースでメール送信をサポートします。

umamail is a tool designed to simplify the process of sending emails using Python. The name "umamail" is inspired by the Japanese word "uma," meaning "horse," as well as the concept of an "unidentified mysterious animal" (UMA). This reflects the tool's mission: making the process of sending emails surprisingly easy and efficient, akin to a mythical creature in its simplicity and effectiveness.

## 特徴 (Features)

- **シンプルなインターフェース**: メールの送信に必要な最小限の設定だけで簡単に利用可能。
- **カスタマイズ可能**: SMTPサーバーの詳細設定やポート番号の指定も柔軟に対応。
- **Python初心者にもやさしい**: 複雑なコーディングを必要とせず、数行のコードでメール送信が完了。

- **Simple Interface**: The tool is designed to be used with minimal setup, requiring only essential parameters to send an email.
- **Customizable**: Advanced users can specify details such as the SMTP server, port number, and login credentials.
- **Beginner-Friendly**: The tool is ideal for Python beginners, as it eliminates the need for complex coding to send emails.

## インストール (Installation)

umamailはPythonのパッケージとしてPyPIからインストールできます。以下のコマンドを使用してインストールします:

```bash
pip install umamail
```

umamail can be installed via PyPI using the following command:

```bash
pip install umamail
```

## 使用例 (Usage Examples)

### 基本的なメール送信 (Basic Email Sending)

umamailを使用して、基本的なメールを送信するコードは次のとおりです:

Here is how you can use umamail to send a basic email:

```python
import umamail

umamail.send(
    subject="メールタイトル - テストメール",
    message="本文",
    to_addr="to-addr@example.com",
    from_addr="from-addr@example.com",
    password="xxxx"
)
```

### 詳細な設定を使用したメール送信 (Sending Emails with Advanced Settings)

SMTPサーバーの詳細やポート番号などを指定してメールを送信することも可能です:

You can also send emails with more detailed settings, such as specifying the SMTP server and port number:

```python
import umamail

umamail.send(
    subject="メールタイトル - テストメール",
    message="本文",
    to_addr="to-addr@example.com",
    from_addr="from-addr@example.com",
    password="xxxx",
    login_addr="login-addr@example.com",
    smtp_domain="smtp-mail.outlook.com",
    port=587
)
```

## メールサーバー設定 (Mail Server Settings)

umamailはデフォルトで送信元アドレスに基づいてSMTPサーバーやポート番号を推定しますが、詳細を指定することも可能です。これにより、OutlookやGmailなど、異なるメールサービスに対応することができます。

umamail automatically infers the SMTP server and port based on the from address, but it also allows you to specify these details. This makes it compatible with various email services like Outlook and Gmail.

## 終わりに (Conclusion)

umamailは、メール送信の手間を大幅に軽減し、シンプルでありながら柔軟性のあるツールです。初心者から上級者まで、誰にでも使いやすいインターフェースを提供し、メール送信を驚くほど簡単にします。

umamail is a powerful yet simple tool that significantly reduces the hassle of sending emails. Whether you're a beginner or an advanced user, umamail offers an intuitive interface that makes email sending surprisingly easy.
