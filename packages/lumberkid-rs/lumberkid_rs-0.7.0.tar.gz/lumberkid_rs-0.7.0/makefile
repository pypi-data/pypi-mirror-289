version:
	semantic-release version

publish:
	source .env && maturin publish

install-from-pypi:
	rye install lumberkid-rs

release:
	make version
	make publish
	make install-from-pypi