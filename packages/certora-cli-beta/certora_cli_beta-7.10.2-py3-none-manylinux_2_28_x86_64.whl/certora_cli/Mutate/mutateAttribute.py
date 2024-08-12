import sys
import argparse
from dataclasses import dataclass
from enum import unique
from pathlib import Path
from typing import List, Dict, Any
from rich.console import Console


scripts_dir_path = Path(__file__).parent.resolve()  # containing directory
sys.path.insert(0, str(scripts_dir_path))

from Shared import certoraValidateFuncs as Vf
from Shared import certoraUtils as Util
from Shared import certoraAttrUtil as AttrUtil
from Mutate import mutateConstants as Constants


MUTATION_DOCUMENTATION_URL = 'https://docs.certora.com/en/latest/docs/gambit/mutation-verifier.html#cli-options'


@dataclass
class MutateArgument(AttrUtil.BaseArgument):
    affects_build_cache_key: bool = False
    disables_build_cache: bool = False


@unique
class MutateAttribute(AttrUtil.BaseAttribute):

    ORIG_RUN = MutateArgument(
        help_msg="A link to a previous run of the Prover, will be used as the basis for the "
                 "generated mutations",
        default_desc="",
        attr_validation_func=Vf.validate_orig_run,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    MSG = MutateArgument(
        help_msg="Add a message description to your run",
        attr_validation_func=Vf.validate_msg,
        default_desc="No message",
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    SERVER = MutateArgument(
        attr_validation_func=Vf.validate_server_value,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    PROVER_VERSION = MutateArgument(
        attr_validation_func=Vf.validate_prover_version,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    DEBUG = MutateArgument(
        flag='--debug',    # added to prevent dup with DUMP_CSV
        arg_type=AttrUtil.AttrArgType.BOOLEAN,
        argparse_args={
            'action': AttrUtil.STORE_TRUE
        }
    )

    COLLECT_MODE = MutateArgument(
        flag='--collect_mode',    # added to prevent dup with DEBUG
        arg_type=AttrUtil.AttrArgType.BOOLEAN,
        argparse_args={
            'action': AttrUtil.STORE_TRUE
        }
    )

    ORIG_RUN_DIR = MutateArgument(
        help_msg="Download files from the original run link to the given folder",
        default_desc="Downloads files to the directory `.certora_mutate_sources`",
        # attr_validation_func=Vf.validate_writable_path,
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    OUTDIR = MutateArgument(
        help_msg="Specify the output directory for Gambit",
        default_desc=f"Gambit generates mutants inside the directory `{Constants.GAMBIT_OUT}`",
        # attr_validation_func=Vf.validate_writable_path,
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    GAMBIT_ONLY = MutateArgument(
        arg_type=AttrUtil.AttrArgType.BOOLEAN,
        help_msg="Stop processing after generating mutations with Gambit",
        default_desc="Runs a verification job on each mutant and generates a test report from the results",
        argparse_args={
            'action': AttrUtil.STORE_TRUE
        }
    )

    DUMP_FAILED_COLLECTS = MutateArgument(
        # This flag is hidden on purpose, the following code line help explain what it does
        # attr_validation_func=Vf.validate_writable_path,
        # help_msg="Path to the log file capturing mutant collection failures.",
        # default_desc="log will be stored at collection_failures.txt",
        flag="--dump_failed_collects",
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    # Sets a file that will store the object sent to mutation testing UI (useful for testing)
    UI_OUT = MutateArgument(
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    DUMP_LINK = MutateArgument(
        flag='--dump_link',    # added to prevent dup with DUMP_CSV
        # todo - validation can write the file
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    DUMP_CSV = MutateArgument(
        attr_validation_func=Vf.validate_writable_path,
        argparse_args={
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    # Synchronous mode
    # Run the tool synchronously in shell
    SYNC = MutateArgument(
        arg_type=AttrUtil.AttrArgType.BOOLEAN,
        argparse_args={
            'action': AttrUtil.STORE_TRUE
        }
    )

    '''
    The file containing the links holding certoraRun report outputs.
    In async mode, run this tool with only this option.
    '''
    COLLECT_FILE = MutateArgument(
        flag='--collect_file',    # added to prevent dup with DUMP_CSV
        # attr_validation_func=Vf.validate_readable_file,
        argparse_args={
            'nargs': AttrUtil.SINGLE_OR_NONE_OCCURRENCES,
            'type': Path,
            'action': AttrUtil.UniqueStore
        }
    )

    '''
   The max number of minutes to poll after submission was completed,
    and before giving up on synchronously getting mutation testing results
   '''
    POLL_TIMEOUT = MutateArgument(
        flag='--poll_timeout',    # added to prevent dup with REQUEST_TIMEOUT
        attr_validation_func=Vf.validate_positive_integer,
        arg_type=AttrUtil.AttrArgType.INT,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    # The maximum number of retries a web request is attempted
    MAX_TIMEOUT_ATTEMPTS_COUNT = MutateArgument(
        arg_type=AttrUtil.AttrArgType.INT,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    # The timeout in seconds for a web request
    REQUEST_TIMEOUT = MutateArgument(
        attr_validation_func=Vf.validate_positive_integer,
        arg_type=AttrUtil.AttrArgType.INT,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    GAMBIT = MutateArgument(
        arg_type=AttrUtil.AttrArgType.MAP,
        argparse_args={
            'nargs': '*',
            'action': AttrUtil.NotAllowed
        }
    )
    # todo vvvv - parse_manual_mutations, change warnings to exceptions
    MANUAL_MUTANTS = MutateArgument(
        arg_type=AttrUtil.AttrArgType.MAP,
        attr_validation_func=Vf.validate_manual_mutants,
        flag='--manual_mutants',  # added to prevent dup with GAMBIT
        argparse_args={
            'nargs': '*',
            'action': AttrUtil.NotAllowed
        }
    )

    '''
    Add this if you wish to wait for the results of the original verification.
    Reasons to use it:
    - Saves resources - all the mutations will be ignored if the original fails
    - The Prover will use the solver data from the original run to reduce the run time of the mutants
    Reasons to not use it:
    - Run time will be increased
    '''
    #
    WAIT_FOR_ORIGINAL_RUN = MutateArgument(
        arg_type=AttrUtil.AttrArgType.BOOLEAN,
        flag='--wait_for_original_run',
        argparse_args={
            'action': AttrUtil.STORE_TRUE
        }
    )

    TEST = MutateArgument(
        attr_validation_func=Vf.validate_test_value,
        argparse_args={
            'action': AttrUtil.UniqueStore
        }
    )

    #  TODO - Move to base (rahav)
    def validate_value(self, value: str) -> None:
        if self.value.attr_validation_func is not None:
            try:
                self.value.attr_validation_func(value)
            except Util.CertoraUserInputError as e:
                msg = f'{self.get_flag()}: {e}'
                if isinstance(value, str) and value.strip()[0] == '-':
                    flag_error = f'{value}: Please remember, CLI flags should be preceded with double dashes. ' \
                                 f'{Util.NEW_LINE}For more help run the tool with the option --help'
                    msg = flag_error + msg
                raise Util.CertoraUserInputError(msg) from None


def get_args(args_list: List[str]) -> Dict:

    def formatter(prog: Any) -> argparse.HelpFormatter:
        return argparse.HelpFormatter(prog, max_help_position=100, width=96)  # TODO - use the constant!

    parser = MutationParser(prog="certora-cli arguments and options", allow_abbrev=False,
                            formatter_class=formatter,
                            epilog="  -*-*-*   You can find detailed documentation of the supported options in "
                                   f"{MUTATION_DOCUMENTATION_URL}   -*-*-*")
    args = list(MutateAttribute)

    parser.add_argument("conf_no_flag", nargs='?', type=Path)
    parser.add_argument("--conf", type=Path)

    for arg in args:
        flag = arg.get_flag()
        if arg.value.arg_type == AttrUtil.AttrArgType.INT:
            parser.add_argument(flag, help=arg.value.help_msg, type=int, **arg.value.argparse_args)
        else:
            parser.add_argument(flag, help=arg.value.help_msg, **arg.value.argparse_args)
    return vars(parser.parse_args(args_list))


class MutationParser(AttrUtil.CertoraArgumentParser):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def format_help(self) -> str:
        console = Console()
        console.print("\n\nThe Certora Mutate - A tool for generating and verifying mutations")
        sys.stdout.write("\n\nUsage: certoraMutate <flags>\n\n")  # Print() would color the word <flags> here

        console.print("[bold][underline]Flag Types[/bold][/underline]\n")

        console.print("[bold]1. boolean (B):[/bold] gets no value, sets flag value to true "
                      "(false is always the default)")
        console.print("[bold]2. string (S):[/bold] gets a single string as a value, "
                      "note also numbers are of type string\n\n")

        MutateAttribute.print_attr_help()
        console.print("\n\nYou can find detailed documentation of the supported flags "
                      f"{Util.print_rich_link(MUTATION_DOCUMENTATION_URL)}\n\n")
        return ''
