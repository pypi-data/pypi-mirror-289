#!/usr/bin/env hython

"""Script to render a ROP.

# Task template should resolve to something like:
# hython "/Users/julian/Conductor/houdini/ciohoudini/scripts/chrender.py" -f 2 2 1 -d /out/mantra1 "/path/to/aaa_MantraOnly.hip"
"""
import subprocess
import sys
import os
import re
import argparse

from string import ascii_uppercase
import hou

SIM_TYPES = ("baketexture", "geometry", "output", "dop")

DRIVE_LETTER_RX = re.compile(r"^[a-zA-Z]:")


def error(msg):
    if msg:
        sys.stderr.write("\n")
        sys.stderr.write("Error: %s\n" % msg)
        sys.stderr.write("\n")
        sys.exit(1)


def usage(msg=""):
    sys.stderr.write(
        """Usage:

    hython /path/to/chrender.py -d driver -f start end step hipfile
    All flags/args are required

    -d driver:          Path to the output driver that will be rendered
    -f range:           The frame range specification (see below)
    hipfile             The hipfile containing the driver to render
    """
    )
    error(msg)


def prep_ifd(node):
    """Prepare the IFD (Mantra) ROP for rendering."""
    print("Preparing Mantra ROP node {}".format(node.name()))
    node.parm("vm_verbose").set(3)
    print("Set loglevel to 3")
    node.parm("vm_alfprogress").set(True)
    print("Turn on Alfred style progress")
    node.parm("soho_mkpath").set(True)
    print("Make intermediate directories if needed")


def prep_baketexture(node):
    """Prepare the BAKETEXTURE ROP for rendering."""
    pass


def prep_arnold(node):
    """Prepare the Arnold ROP for rendering."""

    print("Preparing Arnold ROP node {} ...".format(node.name()))

    try:
        if node is not None:
            print("Abort on license failure")
            node.parm("ar_abort_on_license_fail").set(True)
            print("Abort on error")
            node.parm("ar_abort_on_error").set(True)
            print("Log verbosity to debug")
            node.parm("ar_log_verbosity").set('debug')
            print("Enable log to console")
            node.parm("ar_log_console_enable").set(True)

    except Exception as e:
        print("Error preparing Arnold ROP: {}".format(e))


def prep_redshift(node):
    """Prepare the redshift ROP for rendering."""
    print("Preparing Redshift ROP node {}".format(node.name()))

    print("Turning on abort on license fail")
    node.parm("AbortOnLicenseFail").set(True)

    print("Turning on abort on altus license fail")
    node.parm("AbortOnAltusLicenseFail").set(True)

    print("Turning on abort on Houdini cooking error")
    node.parm("AbortOnHoudiniCookingError").set(True)

    print("Turning on abort on missing resource")
    node.parm("AbortOnMissingResource").set(True)

    print("Turning on Redshift log")
    node.parm("RS_iprMuteLog").set(False)


def prep_karma(node):
    """Prepare the karma ROP for rendering."""
    print("Preparing Karma ROP node {}".format(node.name()))

    print("Turning on Abort for missing texture")
    node.parm("abortmissingtexture").set(True)

    print("Turning on make path")
    node.parm("mkpath").set(True)

    print("Turning on save to directory")
    node.parm("savetodirectory").set(True)

    print("Turning on Husk stdout")
    node.parm("husk_stdout").set(True)

    print("Turning on Husk stderr")
    node.parm("husk_stderr").set(True)

    print("Turning on Husk debug")
    node.parm("husk_debug").set(True)

    print("Turning on log")
    node.parm("log").set(True)

    print("Turning on verbosity")
    node.parm("verbosity").set(True)

    print("Turning on Alfred style progress")
    node.parm("alfprogress").set(True)


def prep_usdrender(node):
    """Prepare the usdrender OUT for rendering."""
    print("Preparing usdrender OUT node {}".format(node.name()))

    print("Turning on Alfred style progress")
    node.parm("alfprogress").set(True)

    print("Turning on Husk debug")
    node.parm("husk_debug").set(True)

    print("Turning on husk_log")
    node.parm("husk_log").set(True)

    print("Turning on Make Path")
    node.parm("mkpath").set(True)


def prep_usdrender_rop(node):
    """Prepare the usdrender OUT for rendering."""
    print("Preparing usdrender rop node {}".format(node.name()))

    print("Turning on Alfred style progress")
    node.parm("alfprogress").set(True)

    print("Turning on Husk debug")
    node.parm("husk_debug").set(True)

    print("Turning on husk_log")
    node.parm("husk_log").set(True)

    print("Turning on Make Path")
    node.parm("mkpath").set(True)


def prep_ris(node):
    """Prepares the Renderman ROP (RIS) for rendering."""
    print("Preparing Ris ROP node {}".format(node.name()))
    node.parm("loglevel").set(4)
    print("Set loglevel to 4")
    node.parm("progress").set(True)
    print("Turn progress on")
    num_displays = node.parm("ri_displays").eval()
    for i in range(num_displays):
        print("Set display {} to make intermediate directories if needed".format(i))
        node.parm("ri_makedir_{}".format(i)).set(True)


def prep_vray_renderer(node):
    """Prepares the V-Ray ROP for rendering."""
    print("Preparing V-Ray ROP node {}".format(node.name()))
    print("Nothing to do")


def prep_geometry(node):
    """Prepares the geometry ROP for rendering."""
    pass


def prep_output(rop_node):
    """Prepares the output ROP for rendering."""
    pass


def prep_dop(node):
    """Prepares the DOP ROP for rendering."""
    node.parm("trange").set(1)
    node.parm("mkpath").set(True)
    node.parm("alfprogress").set(True)


def prep_opengl(node):
    """Prepares the OpenGL ROP for rendering."""
    pass


def run_driver_prep(rop_node):
    """Executes the appropriate preparation function for a given ROP based on its type."""
    rop_type = rop_node.type().name().split(":")[0]
    try:
        fn = globals()["prep_{}".format(rop_type)]
        print("Running prep function for ROP type: {}".format(rop_type))
        print("Function: {}".format(fn))
    except KeyError:
        return
    try:
        fn(rop_node)
    except:
        sys.stderr.write(
            "Failed to run prep function for ROP type: {}. Skipping.\n".format(rop_type)
        )
        return


def is_sim(rop):
    """Determines if the given ROP is of a simulation type."""
    return rop.type().name().startswith(SIM_TYPES)


def parse_args():
    """Parses command-line arguments for the script, ensuring required arguments are provided."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-d", dest="driver", required=True)
    parser.add_argument("-f", dest="frames", nargs=3, type=int)
    parser.add_argument("hipfile", nargs=1)

    args, unknown = parser.parse_known_args()

    if unknown:
        usage("Unknown argument(s): %s" % (" ".join(unknown)))

    return args


def ensure_posix_paths():
    """Converts file paths in Houdini file references to POSIX format."""
    refs = hou.fileReferences()
    for parm, value in refs:
        if not parm:
            continue
        try:
            node_name = parm.node().name()
            parm_name = parm.name()
            node_type = parm.node().type().name()
        except:
            print("Failed to get parm info")
            continue
        ident = "[{}]{}.{}".format(node_type, node_name, parm_name)
        if node_type.startswith("conductor::job"):
            continue

        if not DRIVE_LETTER_RX.match(value):
            print("Not a drive letter. Skipping")
            continue

        print("{} Found a drive letter in path: {}. Stripping".format(ident, value))
        value = DRIVE_LETTER_RX.sub("", value).replace("\\", "/")
        print("{} Setting value to {}".format(ident, value))
        try:
            parm.set(value)
        except hou.OperationFailed as ex:
            print("{} Failed to set value for parm {}. Skipping".format(ident, value))
            print(ex)
            continue
        print("{} Successfully set value {}".format(ident, value))


def print_output_path(rop):
    """Prints the output path of the given ROP."""
    output_parm = None
    for parm in ["vm_picture", "RS_outputFileNamePrefix", "ar_picture", "ri_display_0_name"]:
        if rop.parm(parm):
            output_parm = rop.parm(parm)
            break

    if output_parm:
        output_path = output_parm.eval()
        print("ROP '{}' will write to: {}".format(rop.name(), output_path))
    else:
        print("ROP '{}' does not have a recognized output parameter.".format(rop.name()))


def render(args):
    """Render the specified Render Operator (ROP) within a Houdini scene based on the arguments provided."""
    hipfile = args.hipfile[0]
    driver = args.driver
    frames = args.frames

    print("hipfile: '{}'".format(hipfile))
    print("driver: '{}'".format(driver))
    print("frames: 'From: {} to: {}'by: {}".format(*frames))

    try:
        hou.hipFile.load(hipfile)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)

    rop = hou.node(driver)
    if rop:
        print_output_path(rop)
        render_rop(rop, frames)
    else:
        print_available_rops()
        return


def print_available_rops():
    """Prints the list of available Render Operators (ROPs) in the current Houdini session to stderr."""
    try:
        msg = "ROP does not exist: '{}' \n".format(driver)
        sys.stderr.write(msg)
        all_rops = hou.nodeType(hou.sopNodeTypeCategory(), "ropnet").instances()
        sys.stderr.write("Available ROPs:\n")
        for r in all_rops:
            sys.stderr.write("  {}\n".format(r.path()))
        return
    except Exception as e:
        sys.stderr.write("Failed to get available ROPs\n")


def render_rop(rop, frames):
    """Executes the rendering process for a specified Render Operator (ROP) based on a provided frame range."""
    try:
        print("Ensure POSIX paths")
        ensure_posix_paths()
        run_driver_prep(rop)
        if rop.type().name() == "topnet":
            rop.displayNode().cookWorkItems(block=True)
        elif is_sim(rop):
            rop.render(verbose=True, output_progress=True)
        else:
            rop.render(
                frame_range=tuple(frames),
                verbose=True,
                output_progress=True,
                method=hou.renderMethod.FrameByFrame,
            )
    except hou.OperationFailed as e:
        sys.stderr.write("Error rendering the rop: %s\n" % e)
        return


render(parse_args())
