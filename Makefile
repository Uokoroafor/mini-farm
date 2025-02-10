# Define the command to generate a random secret key
generate-secret:
	@python -c "import secrets; print(secrets.token_urlsafe(32))"

# Help menu to show available commands
help:
	@echo "Available commands:"
	@echo "  make generate-secret   - Generate a new random secret key"
