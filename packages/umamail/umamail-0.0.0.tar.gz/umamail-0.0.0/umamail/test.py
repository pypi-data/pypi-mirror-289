
# メール送信ツール [umamail]
# 【動作確認 / 使用例】

import sys
from sout import sout
from ezpip import load_develop
# メール送信ツール [umamail]
umamail = load_develop("umamail", "../", develop_flag = True)

# メール送信 [umamail]
umamail.send(
	subject = "メールタイトル - テストメール",	# メールのタイトル
	message = "本文",	# メール本文
	to_addr = "to-addr@example.com",	# 送信先メールアドレス
	from_addr = "from-addr@example.com",	# 送信元メールアドレス (outlook.com, gmail.com 以外の場合は、後述の「詳細指定」のsmtp_domainを指定してください)
	password = "xxxx",	# パスワード (メールサーバにログインする際のパスワード。2段階認証が有効のサービスでは、多くの場合特別に発行されたコード等になる)
)

# 詳細指定
umamail.send(	# メール送信 [umamail]
	subject = "メールタイトル - テストメール",	# メールのタイトル
	message = "本文",	# メール本文
	to_addr = "to-addr@example.com",	# 送信先メールアドレス
	from_addr = "from-addr@example.com",	# 送信元メールアドレス (outlook.com, gmail.com 以外の場合は、後述の「詳細指定」のsmtp_domainを指定してください)
	password = "xxxx",	# パスワード (メールサーバにログインする際のパスワード。2段階認証が有効のサービスでは、多くの場合特別に発行されたコード等になる)
	login_addr = "login-addr@example.com",	# メールサーバーにログインする際のID (デフォルトでは自動的にfrom_addrと同一になる)
	smtp_domain = "smtp-mail.outlook.com",	# smtpサーバーのドメイン (デフォルトではlogin_addrの@以降から自動的に推定される)
	port = 587,	# smtpサーバーのポート番号 (デフォルトでは自動的に推定される)
)
