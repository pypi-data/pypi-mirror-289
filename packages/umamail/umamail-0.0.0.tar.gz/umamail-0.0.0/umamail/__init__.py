
# メール送信ツール [umamail]

import sys
import smtplib
from sout import sout
from email.mime.text import MIMEText

# smtpドメインルール表
smtp_domain_chart = {
	"@gmail.com": ("smtp.gmail.com", 587),
	"@outlook.com": ("smtp-mail.outlook.com", 587),
	"@yahoo.com": ("smtp.mail.yahoo.co.jp", 465),
	"@zohomail.com": ("smtp.zoho.com", 465),
}

# smtpドメインを推定
def estimate_smtp_domain(
	email_addr	# 推定に使うメールアドレス
):
	err = Exception("[umamail error] The estimation of the smtp_domain failed. Please specify the smtp_domain argument explicitly.")
	if "@" not in email_addr: raise err
	mail_domain = "@" + email_addr.split("@")[-1]	# 「@」以降を取得
	if mail_domain not in smtp_domain_chart: raise err
	smtp_domain, port = smtp_domain_chart[mail_domain]
	return smtp_domain, port

# メール送信 [umamail]
def send(
	subject,	# メールのタイトル
	message,	# メール本文
	to_addr,	# 送信先メールアドレス
	from_addr,	# 送信元メールアドレス (outlook.com, gmail.com 以外の場合は、後述の「詳細指定」のsmtp_domainを指定してください)
	password,	# パスワード (メールサーバにログインする際のパスワード。2段階認証が有効のサービスでは、多くの場合特別に発行されたコード等になる)
	login_addr = "__AUTO__",	# メールサーバーにログインする際のID (デフォルトでは自動的にfrom_addrと同一になる)
	smtp_domain = "__AUTO__",	# smtpサーバーのドメイン (デフォルトではlogin_addrの@以降から自動的に推定される)
	port = "__AUTO__",	# smtpサーバーのポート番号 (デフォルトでは自動的に推定される)
):
	# 省略引数の自動指定
	if login_addr == "__AUTO__": login_addr = from_addr
	if smtp_domain == "__AUTO__": smtp_domain, port = estimate_smtp_domain(login_addr)	# smtpドメインを推定
	if port == "__AUTO__": port = 587	# portのみ指定されていない場合は最も一般的な587とする
	# メールの内容を設定
	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = from_addr
	msg['To'] = to_addr
	# SMTPサーバーに接続
	server = smtplib.SMTP(smtp_domain, port)
	server.starttls()  # 暗号化を開始
	# 認証情報を使用してログイン
	server.login(login_addr, password)
	# メールを送信
	server.send_message(msg)
	# 接続を終了
	server.quit()
