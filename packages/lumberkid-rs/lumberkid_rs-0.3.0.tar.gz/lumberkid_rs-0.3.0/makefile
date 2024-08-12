version:
	semantic-release version

publish:
	source .env && maturin publish $(MATURIN_PYPI_TOKEN)

release:
	make version
	make release