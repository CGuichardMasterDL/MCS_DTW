init: clean
	@printf "#======   Installation   =====#\n\n"
	@virtualenv -p python3 venv
	@bash scripts/install.sh
	@printf "\n#======      DONE        =====#\n"

update:
	@@bash scripts/install.sh

test:
	@bash scripts/test.sh

clean:
	@rm -rf venv

.PHONY: init tests clean update
