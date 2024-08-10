import argparse
import logging
import sys
import pkg_resources
import asyncio

from datamanwithvan.config import config
from datamanwithvan.utils import messages, statuscodes
from datamanwithvan.replication import replicationjob
from datamanwithvan.utils.bidirectional_queue import BidirectionalQueue

# Section 6 : Obtain the current version number
package_name = "datamanwithvan"
version = pkg_resources.get_distribution(package_name).version
# End of Section 6

# Section 51 : Create an instance of the DatamanwithvanMessages class
dmwvMessagesObj = messages.DatamanwithvanMessages()
# End of Section 51

# Section 18 : Display a welcome ASCII art
print(dmwvMessagesObj.msg_info_welcome, flush=True)
print(dmwvMessagesObj.msg_info_welcome_footer, flush=True)
# End of Section 18

# Section 44 : Before anything else, set up the logger...
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_format = logging.Formatter(
    '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)
try:
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s (%(levelname)s) : %(message)s')
    file_handler = logging.FileHandler("/var/log/datamanwithvan/dmwv.log")
    logger.addHandler(file_handler)
except Exception as e:
    print(f"Error while trying to open log file: {e}")
# End of Section 44


def _handle_cmd_args():
    # Initialize ArgumentParser with description
    parser = argparse.ArgumentParser(
        description="A tool for managing and executing data jobs."
    )

    # Add general arguments
    parser.add_argument(
        "-c", "--config", type=str, default=None,
        help="Full path to a config file"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Enable verbose mode"
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true",
        help="Display less output on screen"
    )
    parser.add_argument(
        "-p", "--param", type=str, default=None,
        help="Runtime config eg. \"param1:val1;...;paramN:valN\""
    )

    # Add subparsers for subcommands
    subparsers = parser.add_subparsers(
        dest="subcommand", help='Subcommands', required=False
    )

    # Subcommand: job
    parser_job = subparsers.add_parser(
        'job', help='Commands related to job execution'
    )
    parser_job.add_argument(
        '--run', type=int, help='Run a job with the specified job ID'
    )
    parser_job.add_argument(
        '--rules', type=str, default=None, help='A replication ruleset'
    )

    # Parse the arguments
    args = parser.parse_args()

    return args


async def produce(communication: BidirectionalQueue, sender, message):
    logger.info(f"'{sender}' is about to request '{message}'")
    await communication.queue_to_consumer.put(message)
    logger.info(f"'{sender}' requested '{message}'")


async def consume(communication: BidirectionalQueue, whoami):
    logger.info(f"{whoami} consumer waits to get something from job")
    message = await communication.queue_to_producer.get()
    logger.info(f"{whoami} got {message} from job")


async def start_producing(replication_job_id, mainprogram_job_channel):
    # TODO: We create a bidirectional queue here and feed it in
    # the ReplicationJob instance. It will be used to exchange live
    # information between the job and the main program.
    await asyncio.gather(
        produce(
            mainprogram_job_channel,
            "MAIN",
            f"start_job_{replication_job_id}")
    )


async def start_consuming(replication_job_id, mainprogram_job_channel):
    # TODO: We create a bidirectional queue here and feed it in
    # the ReplicationJob instance. It will be used to exchange live
    # information between the job and the main program.
    await asyncio.gather(consume(mainprogram_job_channel, "MAIN"))


def datamanwithvan_entry():
    # Section 5 : As soon as main starts, pick up
    # any command line arguments...
    args = _handle_cmd_args()
    # End of Section 5

    # Section 11 : Determine verbosity based on parameter passing
    if args.verbose:
        console_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
    # End of Section 11

    # Section 12 : Lower the verbosity level
    if args.quiet:
        console_handler.setLevel(logging.WARNING)
    # End of Section 12

    # Section 13 : Quiet and Verbose options should never coexist
    if args.quiet and args.verbose:
        logger.error(dmwvMessagesObj.err_no_quiet_and_verbose)
        sys.exit(statuscodes.StatusCodes.stat_code_quiet_verbose)
    # End of Section 13

    # Section 15 : Parse any runtime config parameters
    runtime_parameters = {}
    param_list = []
    if args.param:
        param_list = (args.param).split(";")
        for parameter in param_list:
            tmp = parameter.split("=")
            runtime_parameters[tmp[0]] = tmp[1]
    logger.info(runtime_parameters)
    # End of Section 15

    # Section 14 : Load a config file, if passed...
    if args.config:
        config_file = args.config
    # End of Section 14

    dmwvConfigObj = config.datamanwithvanConfig(
        config_file=config_file,
        runtime_params=runtime_parameters)

    # Section 8 : Capture a replication job ID to execute, if there's one...
    if args.subcommand:
        if args.run is not None and args.subcommand == "job":
            mainprogram_job_channel = BidirectionalQueue()
            asyncio.run(start_producing(args.run, mainprogram_job_channel))
            ReplJobObj = replicationjob.ReplicationJob(
                args.run,
                dmwvConfigObj,
                args.verbose,
                mainprogram_job_channel)
            logger.info(ReplJobObj)
            asyncio.run(start_consuming(args.run, mainprogram_job_channel))
        else:
            pass
    # End of Section 8


if __name__ == "__main__":
    datamanwithvan_entry()
