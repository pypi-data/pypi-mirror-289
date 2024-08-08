import argparse
import os
import runpy
import sys
import types

from localproxy.proxy import ProxyConfig

CONFIG_FILE = os.path.expanduser("~/.local_proxy/proxy.toml")


def run_script(script, args):
    """Run a Python script with proxy settings applied."""
    with open(script, "r") as f:
        code_string = f.read()
    main_mod = types.ModuleType("__main__")
    setattr(main_mod, "__file__", script)
    setattr(main_mod, "__builtins__", globals()["__builtins__"])
    sys.modules["__main__"] = main_mod
    code = compile(code_string, script, "exec")
    sys.argv = [script] + args
    from localproxy import proxy
    proxy.init()
    exec(code, main_mod.__dict__)


def run_code(code_string, args):
    """Run a Python code string with proxy settings applied."""
    main_mod = types.ModuleType("__main__")
    setattr(main_mod, "__file__", "<string>")
    setattr(main_mod, "__builtins__", globals()["__builtins__"])
    sys.modules["__main__"] = main_mod
    code = compile(code_string, "<string>", "exec")
    sys.argv = ["<string>"] + args
    from localproxy import proxy
    proxy.init()
    exec(code, main_mod.__dict__)


def run_module(module, args):
    """Run a Python module with proxy settings applied."""
    sys.argv = [module] + args
    sys.path.insert(0, os.getcwd())
    from localproxy import proxy
    proxy.init()
    runpy.run_module(module, run_name='__main__', alter_sys=True)


def list_proxies():
    """Display existing proxy configuration."""
    config = ProxyConfig(CONFIG_FILE)
    proxies = config.load()
    if proxies:
        for protocol, address in proxies.items():
            print(f"{protocol}: {address}")
    else:
        print("No proxy configurations found.")


def set_proxy(protocol, address):
    """Set a proxy configuration."""
    config = ProxyConfig(CONFIG_FILE)
    proxies = config.load()
    proxies[protocol] = address
    config.save(proxies)
    print(f"Set {protocol} proxy to {address}")


def clear_proxies():
    """Clear all proxy configurations."""
    config = ProxyConfig(CONFIG_FILE)
    config.save({})
    print("Cleared all proxy configurations.")


def main():
    parser = argparse.ArgumentParser(
        description="Local Proxy CLI\n\n"
                    "To run a Python script directly: \n"
                    "  localproxy <script.py> [args]\n\n"
                    "Sub-commands:")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands", required=False)
    run_parser = subparsers.add_parser("run", help="Run code/module")
    run_parser.add_argument("-m", "--module", help="Module to run")
    run_parser.add_argument("-c", "--code", help="Code to run")

    set_parser = subparsers.add_parser("set", help="Set a proxy configuration")
    set_parser.add_argument("protocol", type=str, help="Protocol to set (e.g., http, https)")
    set_parser.add_argument("address", type=str, help="Proxy address (e.g., http://proxy.example.com:8080)")
    set_parser.set_defaults(func=set_proxy)
    subparsers.add_parser("list", help="List existing proxy configurations").set_defaults(func=list_proxies)
    subparsers.add_parser("clear", help="Clear all proxy configurations").set_defaults(func=clear_proxies)
    if len(sys.argv) > 1 and sys.argv[1].endswith(".py"):
        original_args = sys.argv[1:]
        run_script(original_args[0], original_args[1:])
    else:
        args, _ = parser.parse_known_args()
        if args.command == "set":
            set_proxy(args.protocol, args.address)
        elif args.command in ["list", "clear"]:
            args.func()
        elif args.command == "run":
            if args.module:
                run_module(args.module, sys.argv[4:])
            elif args.code:
                run_code(args.code, sys.argv[4:])
            else:
                parser.print_help()
        else:
            parser.print_help()


if __name__ == "__main__":
    main()
