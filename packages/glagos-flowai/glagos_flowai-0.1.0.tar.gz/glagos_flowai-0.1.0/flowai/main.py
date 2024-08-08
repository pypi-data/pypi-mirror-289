import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.live import Live
from rich.table import Table
import questionary
from typing import Optional
import time
import sys
import re
import select

from .config_manager import ConfigManager
from .llm_connector import LLMConnector
from .task_manager import TaskManager

app = typer.Typer()
console = Console()

def init_config():
    config_manager = ConfigManager()
    config = config_manager.load_config()

    # Ensure all necessary keys are present with default values
    default_config = {
        'default_provider': 'openai',
        'default_model': 'gpt-3.5-turbo',
        'openai_api_key': '',
        'anthropic_api_key': '',
        'groq_api_key': '',
        'google_api_key': '',
        'ollama_base_url': 'http://localhost:11434',
        'quiet_mode': 'true',
        'stream_mode': 'true'
    }

    for key, value in default_config.items():
        if key not in config['DEFAULT']:
            config['DEFAULT'][key] = value

    current_provider = config['DEFAULT']['default_provider']
    current_model = config['DEFAULT']['default_model']
    current_quiet_mode = config.getboolean('DEFAULT', 'quiet_mode')
    current_stream_mode = config.getboolean('DEFAULT', 'stream_mode')

    console.print(Panel.fit(
        "[bold green]Welcome to FlowAI![/bold green]\n\n"
        "flowai is a CLI tool for multi-agent LLM tasks. It allows you to interact with "
        "various Language Models from different providers and manage complex, multi-step tasks.\n\n"
        f"[bold blue]Current configuration:[/bold blue]\n"
        f"Provider: [yellow]{current_provider}[/yellow]\n"
        f"Model: [yellow]{current_model}[/yellow]\n"
        f"Quiet mode: [yellow]{'On' if current_quiet_mode else 'Off'}[/yellow]\n"
        f"Stream mode: [yellow]{'On' if current_stream_mode else 'Off'}[/yellow]"
    ))

    providers = ["openai", "anthropic", "ollama", "groq", "google"]
    default_provider = questionary.select(
        "Which provider would you like to use as default?",
        choices=providers,
        default=current_provider
    ).ask()

    llm_connector = LLMConnector(config, default_provider, None)
    models = llm_connector.get_available_models()

    if "Error fetching models" in models:
        console.print(f"[bold red]Error:[/bold red] Unable to fetch models for {default_provider}. Using default model.")
        default_model = current_model
    else:
        default_model = questionary.select(
            f"Which model from {default_provider} would you like to use as default?",
            choices=models,
            default=current_model if current_model in models else models[0]
        ).ask()

    quiet_mode = questionary.confirm("Enable quiet mode by default?", default=current_quiet_mode).ask()
    stream_mode = questionary.confirm("Enable stream mode by default?", default=current_stream_mode).ask()

    # Always update the config here, as it might be the initial setup
    config['DEFAULT'] = {
        'default_provider': default_provider,
        'default_model': default_model,
        'quiet_mode': str(quiet_mode).lower(),
        'stream_mode': str(stream_mode).lower(),
        'openai_api_key': config.get('DEFAULT', 'openai_api_key', fallback=''),
        'anthropic_api_key': config.get('DEFAULT', 'anthropic_api_key', fallback=''),
        'groq_api_key': config.get('DEFAULT', 'groq_api_key', fallback=''),
        'google_api_key': config.get('DEFAULT', 'google_api_key', fallback=''),
        'ollama_base_url': config.get('DEFAULT', 'ollama_base_url', fallback='http://localhost:11434')
    }
    config_manager.save_config(config)
    console.print(f"\n[bold green]Configuration updated![/bold green]")

    console.print(f"Your config file is located at: {config_manager.config_file}")
    console.print("You can update these values by editing the file or by running 'flowai --init' again.")

def generate_status_table(elapsed_time):
    table = Table.grid(padding=(0, 1))
    table.add_row(
        "[bold green]Generating response...",
        f"[bold blue]Elapsed time: {elapsed_time:.3f}s"
    )
    return table

@app.command()
def main(
    model: Optional[str] = typer.Option(None, help="Specify the LLM model to use"),
    provider: Optional[str] = typer.Option(None, help="Specify the LLM provider (openai, anthropic, ollama, groq, google)"),
    list_models: bool = typer.Option(False, "--list-models", help="List available models for the current provider"),
    init: bool = typer.Option(False, "--init", help="Initialize FlowAI configuration"),
    status: bool = typer.Option(False, "--status", help="Show current provider and model"),
    quiet: Optional[bool] = typer.Option(None, "--quiet/--no-quiet", "-q/-Q", help="Quiet mode: show only the timer and final response"),
    stream: Optional[bool] = typer.Option(None, "--stream/--no-stream", "-s/-S", help="Stream the output directly without waiting for full response"),
    flow: bool = typer.Option(False, "--flow", "-f", help="Use multiple agents to complete the task"),
    template_file: Optional[str] = typer.Option(None, "--template-file", "-t", help="Path to a template file containing sections"),
    context_file: Optional[str] = typer.Option(None, "--context-file", "-c", help="Path to a context file for global context"),
    final_check: Optional[str] = typer.Option(None, "--final-check", help="Prompt for final check after response assembly"),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug mode to display prompts"),
    prompt_file: Optional[str] = typer.Option(None, "--prompt-file", "-p", help="Path to a file containing a detailed prompt"),
    no_markdown: bool = typer.Option(False, "--no-markdown", help="Return the response without Markdown formatting"),
    prompt: Optional[str] = typer.Argument(None, help="The prompt to send to the LLM (optional if --prompt-file is used)")
):
    config_manager = ConfigManager()

    if init:
        init_config()
        return

    if not config_manager.config_exists():
        console.print("[bold red]No configuration file found. Please run 'flowai --init' to set up FlowAI.[/bold red]")
        raise typer.Exit(code=1)

    config = config_manager.load_config()
    system_prompt = config_manager.get_system_prompt()

    if status:
        current_provider = config.get('DEFAULT', 'default_provider', fallback='Not set')
        current_model = config.get('DEFAULT', 'default_model', fallback='Not set')
        current_quiet_mode = config.getboolean('DEFAULT', 'quiet_mode', fallback=True)
        current_stream_mode = config.getboolean('DEFAULT', 'stream_mode', fallback=True)
        console.print(Panel.fit(
            f"[bold blue]Current FlowAI Status[/bold blue]\n\n"
            f"Provider: [green]{current_provider}[/green]\n"
            f"Model: [green]{current_model}[/green]\n"
            f"Quiet mode: [green]{'On' if current_quiet_mode else 'Off'}[/green]\n"
            f"Stream mode: [green]{'On' if current_stream_mode else 'Off'}[/green]"
        ))
        return

    # Check if quiet or stream mode is explicitly set
    quiet_set = quiet is not None
    stream_set = stream is not None

    # Use config values if not explicitly set in command line
    quiet = quiet if quiet_set else config.getboolean('DEFAULT', 'quiet_mode', fallback=True)
    stream = stream if stream_set else config.getboolean('DEFAULT', 'stream_mode', fallback=True)

    # Update config if modes are explicitly set
    if quiet_set or stream_set:
        if quiet_set:
            config['DEFAULT']['quiet_mode'] = str(quiet).lower()
        if stream_set:
            config['DEFAULT']['stream_mode'] = str(stream).lower()
        config_manager.save_config(config)
        if not quiet and not stream:
            print("[bold blue]Updated configuration:[/bold blue]")
            if quiet_set:
                print(f"Quiet mode: {'On' if quiet else 'Off'}")
            if stream_set:
                print(f"Stream mode: {'On' if stream else 'Off'}")

    # Validate configuration only for operations that require it
    if not (list_models or prompt):
        is_valid, error_message = config_manager.validate_config()
        if not is_valid:
            console.print(f"[bold red]Configuration error: {error_message}[/bold red]")
            console.print("[bold yellow]Please run 'flowai --init' to reconfigure FlowAI.[/bold yellow]")
            raise typer.Exit(code=1)

    if provider:
        if provider not in ["openai", "anthropic", "ollama", "groq", "google"]:
            console.print(f"[bold red]Error: Unsupported provider '{provider}'. Supported providers are: openai, anthropic, ollama, groq, google[/bold red]")
            raise typer.Exit(code=1)
        config['DEFAULT']['default_provider'] = provider
        config_manager.save_config(config)
        if not quiet and not stream:
            print(f"[bold blue]Updated default provider to:[/bold blue] {provider}")
    else:
        provider = config.get('DEFAULT', 'default_provider', fallback='openai')
    
    llm_connector = LLMConnector(config, provider, model, system_prompt)
    
    if list_models:
        print(f"[bold]Available models for {provider}:[/bold]")
        models = llm_connector.get_available_models()
        for model in models:
            print(f"- {model}")
        return

    # Handle prompt file and command-line prompt
    file_prompt = ""
    if prompt_file:
        try:
            with open(prompt_file, 'r') as f:
                file_prompt = f.read().strip()
        except FileNotFoundError:
            console.print(f"[bold red]Error: Prompt file '{prompt_file}' not found.[/bold red]")
            raise typer.Exit(code=1)
        except IOError:
            console.print(f"[bold red]Error: Unable to read prompt file '{prompt_file}'.[/bold red]")
            raise typer.Exit(code=1)

    # Combine file prompt and command-line prompt
    full_prompt = file_prompt
    if prompt:
        full_prompt += f"\n\n{prompt}" if file_prompt else prompt
    
    if not full_prompt and not (init or status or list_models):
        console.print("[bold red]Error: No prompt provided. Use --prompt-file or provide a prompt as an argument.[/bold red]")
        raise typer.Exit(code=1)

    if model:
        config['DEFAULT']['default_model'] = model
        config_manager.save_config(config)
        if not quiet and not stream:
            print(f"[bold blue]Updated default model to:[/bold blue] {model}")
    else:
        model = config.get('DEFAULT', 'default_model')
    
    # Validate configuration again after potential changes
    is_valid, error_message = config_manager.validate_config()
    if not is_valid:
        console.print(f"[bold red]Configuration error: {error_message}[/bold red]")
        console.print("[bold yellow]Please run 'flowai --init' to reconfigure FlowAI.[/bold yellow]")
        raise typer.Exit(code=1)

    # Read context from stdin only if there's data available
    context = ""
    if select.select([sys.stdin,], [], [], 0.0)[0]:
        context = sys.stdin.read().strip()

    wrapped_context = f"\n\n__START_CONTEXT__\n{context}\n__END_CONTEXT__" if context else ""

    task_manager = TaskManager(llm_connector)
    
    if flow:
        print(f"flow: {flow} DEBUG!!! {debug}")
        if template_file:
            with open(template_file, 'r') as f:
                template_content = f.read().strip()
        elif prompt and prompt.startswith("TEMPLATE[") and prompt.endswith("]"):
            template_content = prompt[9:-1].strip()
        else:
            template_content = prompt.strip()

        template, sections = task_manager.parse_template(template_content)
        
        if not quiet and not stream:
            print(f"[bold blue]Using provider:[/bold blue] {provider}")
            print(f"[bold blue]Using model:[/bold blue] {model}")
            print(f"[bold blue]Processing template with {len(sections)} sections[/bold blue]")

        if debug:
            console.print("[bold blue]Debug: Template content:[/bold blue]")
            console.print(template_content)
            console.print("[bold blue]Debug: Parsed sections:[/bold blue]")
            for section in sections:
                console.print(f"Section: {section['name']}")
                console.print(f"Content: {section['content']}")
            console.print("---")

        start_time = time.time()
        
        if stream:
            console.print("[bold green]Processing template sections:[/bold green]")
            result = task_manager.compile_results(template, sections, full_prompt, quiet=False, debug=debug)
            for chunk in result.split():  # Simple streaming simulation
                sys.stdout.write(chunk + " ")
                sys.stdout.flush()
                time.sleep(0.05)
            sys.stdout.write("\n")
        else:
            result = task_manager.compile_results(template, sections, full_prompt, quiet, debug=debug)
            
        elapsed_time = time.time() - start_time
        if not quiet:
            print(f"[bold blue]Total response time:[/bold blue] {elapsed_time:.3f}s")
            print("[bold green]Response:[/bold green]\n")
        if no_markdown:
            console.print(result)
        else:
            md = Markdown(result)
            console.print(md)
    else:
        if not quiet and not stream:
            print(f"[bold blue]Using provider:[/bold blue] {provider}")
            print(f"[bold blue]Using model:[/bold blue] {model}")
            print(f"[bold blue]Processing prompt:[/bold blue] {full_prompt}")
        
        if debug:
            console.print("[bold blue]Debug: Prompt sent to LLM:[/bold blue]")
            console.print(full_prompt + wrapped_context)
            console.print("---")

        start_time = time.time()
        full_response = ""

        full_prompt = f"{full_prompt}{wrapped_context}"

        if stream:
            for chunk in llm_connector.send_prompt(prompt=full_prompt, debug=debug):
                sys.stdout.write(chunk)
                sys.stdout.flush()
            sys.stdout.write("\n")
        else:
            with Live(generate_status_table(0), refresh_per_second=10, transient=quiet) as live:
                for chunk in llm_connector.send_prompt(prompt=full_prompt, debug=debug):
                    full_response += chunk
                    elapsed_time = time.time() - start_time
                    live.update(generate_status_table(elapsed_time))
        
        elapsed_time = time.time() - start_time
        if not quiet:
            print(f"[bold blue]Total response time:[/bold blue] {elapsed_time:.3f}s")
            print("[bold green]Response:[/bold green]\n")
        if no_markdown:
            console.print(full_response)
        else:
            md = Markdown(full_response)
            console.print(md)

if __name__ == "__main__":
    app()