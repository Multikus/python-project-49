brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall: build
	uv tool install --force dist/hexlet_code-*.whl