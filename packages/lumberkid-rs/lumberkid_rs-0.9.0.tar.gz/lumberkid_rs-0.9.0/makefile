version:
	semantic-release version

publish:
	source .env && maturin publish

install-from-pypi:
	rye uninstall lumberkid-rs
	rye install lumberkid-rs

release:
	make version
	make publish
	make install-from-pypi