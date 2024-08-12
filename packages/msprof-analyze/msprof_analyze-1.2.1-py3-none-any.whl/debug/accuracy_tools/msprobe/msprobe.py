# Copyright (c) 2024, Huawei Technologies Co., Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0  (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import importlib.util
from msprobe.core.compare.utils import _compare_parser
from msprobe.core.common.log import logger


def is_module_available(module_name):
    spec =importlib.util.find_spec(module_name)
    return spec is not None


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="msprobe(mindstudio probe), [Powered by MindStudio].\n"
                    "Providing one-site accuracy difference debugging toolkit for training on Ascend Devices.\n"
                    f"For any issue, refer README.md first",
    )
    
    parser.set_defaults(print_help=parser.print_help)
    parser.add_argument('-f', '--framework', required=True, choices=['pytorch', 'mindspore'],
                        help='Deep learning framework.')
    subparsers = parser.add_subparsers()
    subparsers.add_parser('parse')
    compare_cmd_parser = subparsers.add_parser('compare')
    run_ut_cmd_parser = subparsers.add_parser('run_ut')
    multi_run_ut_cmd_parser = subparsers.add_parser('multi_run_ut')
    api_precision_compare_cmd_parser = subparsers.add_parser('api_precision_compare')
    run_overflow_check_cmd_parser = subparsers.add_parser('run_overflow_check')
    multi_run_ut_cmd_parser.add_argument('-n', '--num_splits', type=int, choices=range(1, 65), default=8,
                                         help='Number of splits for parallel processing. Range: 1-64')

    _compare_parser(compare_cmd_parser)
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args(sys.argv[1:])
    if sys.argv[2] == "pytorch":
        if is_module_available("torch"):
            from msprobe.pytorch.api_accuracy_checker.run_ut.run_ut import _run_ut_parser, run_ut_command
            from msprobe.pytorch.parse_tool.cli import parse as cli_parse
            from msprobe.pytorch.api_accuracy_checker.run_ut.multi_run_ut import prepare_config, run_parallel_ut
            from msprobe.pytorch.api_accuracy_checker.compare.api_precision_compare import _api_precision_compare_parser, \
                _api_precision_compare_command
            from msprobe.pytorch.api_accuracy_checker.run_ut.run_overflow_check import _run_overflow_check_parser, \
                _run_overflow_check_command
            from msprobe.pytorch.compare.compare_cli import compare_cli
            _run_ut_parser(run_ut_cmd_parser)
            _run_ut_parser(multi_run_ut_cmd_parser)
            _api_precision_compare_parser(api_precision_compare_cmd_parser)
            _run_overflow_check_parser(run_overflow_check_cmd_parser)
        else:
            logger.error("Pytorch does not exit, please install pytorch library")
            raise Exception()
        if sys.argv[3] == "run_ut":
            run_ut_command(args)
        elif sys.argv[3] == "parse":
            cli_parse()
        elif sys.argv[3] == "multi_run_ut":
            config = prepare_config(args)
            run_parallel_ut(config)
        elif sys.argv[3] == "api_precision_compare":
            _api_precision_compare_command(args)
        elif sys.argv[3] == "run_overflow_check":
            _run_overflow_check_command(args)
        elif sys.argv[3] == "compare":
            compare_cli(args)
    else:
        if is_module_available("mindspore"):
            from msprobe.mindspore.compare.compare_cli import compare_cli_ms
        else:
            logger.error("Mindspore does not exit, please install mindspore library")
            raise Exception()
        if sys.argv[3] == "compare":
            compare_cli_ms(args)

if __name__ == "__main__":
    main()
