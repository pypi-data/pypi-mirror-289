import click
from .language_interface import LanguageInterface


@click.group()
def cli():
    """AKALI: Augmenter Knowledge Augmenter and Language Interface

    This CLI tool provides access to library functionalities.
    Use 'akali COMMAND --help' for more information on a specific command.
    """
    pass


@cli.command()
@click.option('--model', required=True, help='Model ID or path')
@click.option('--task', required=True, help='Task name (e.g., EntitySentimentReasoner, TextClassification)')
@click.option('--host', default='0.0.0.0', help='Host to run the service on')
@click.option('--port', default=8000, type=int, help='Port to run the service on')
@click.option('--quantization', type=click.Choice(['4bit', '8bit']), help='Quantization level')
@click.option('--hf-token', help='Hugging Face API token for accessing gated models')
@click.option('--run_async', help='Run the service asynchronously', is_flag=True)
def run(model, task, host, port, quantization, hf_token, run_async):
    """Run the Language Interface service"""
    click.echo(f"Loading model: {model}")
    li = LanguageInterface.load_model(model, quantization, hf_token=hf_token)

    click.echo(f"Setting task: {task}")
    li.set_task(task)

    click.echo(f"Running service on {host}:{port}")
    li.run_service(host, port, run_async=run_async)


@cli.command()
@click.option('--model', required=True, help='Model ID or path')
@click.option('--task', required=True, help='Task name (e.g., EntitySentimentReasoner, TextClassification)')
@click.option('--system-text', help='System text for the input')
@click.option('--user-message', required=True, help='User message for the input')
@click.option('--quantization', type=click.Choice(['4bit', '8bit']), help='Quantization level')
@click.option('--hf-token', help='Hugging Face API token for accessing gated models')
def predict(model, task, system_text, user_message, quantization, hf_token):
    """Make a prediction using Language Interface"""
    click.echo(f"Loading model: {model}")
    li = LanguageInterface.load_model(model, quantization, hf_token=hf_token)

    click.echo(f"Setting task: {task}")
    li.set_task(task)

    click.echo("Making prediction...")
    result = li.predict(system_text, user_message)
    click.echo(f"Result: {result}")


if __name__ == '__main__':
    cli()
