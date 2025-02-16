brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall: build
	uv tool install --force dist/hexlet_code-*.whl

make lint:
	uv run ruff check brain_games

run-rec:
	asciinema rec demo.cast

play-rec:
	asciinema play demo.cast

upload-rec:
	asciinema upload demo.cast