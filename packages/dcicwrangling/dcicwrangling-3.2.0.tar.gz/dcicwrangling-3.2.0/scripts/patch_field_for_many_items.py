import sys
import argparse
from dcicutils.ff_utils import patch_metadata, delete_field
from functions import script_utils as scu


def get_args(args):
    parser = argparse.ArgumentParser(
        parents=[scu.create_input_arg_parser(), scu.create_ff_arg_parser()],
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('field',
                        help="The field to update.")
    parser.add_argument('value',
                        help="The value(s) to update. Array fields need \"''\" surround \
                        even if only a single value i.e. \"'value here'\" or \"'v1' 'v2'\" \
                        NOTE: can delete field by passing val *delete*")
    parser.add_argument('--isarray',
                        default=False,
                        action='store_true',
                        help="Field is an array.  Default is False \
                        use this so value is correctly formatted even if only a single value")
    parser.add_argument('--numtype',
                        help="options: 'i' or 'f' If the field value is integer or number deal accordingly")
    args = parser.parse_args(args)
    return args


def main():
    args = get_args(sys.argv[1:])
    auth = scu.authenticate(key=args.key, keyfile=args.keyfile, env=args.env)
    print("Working on {}".format(auth.get('server')))
    itemids = scu.get_item_ids_from_args(args.input, auth, args.search)
    field = args.field
    val = args.value
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    if args.isarray:
        val = [v for v in val.split("'") if v]
    ntype = args.numtype
    if ntype:
        if ntype == 'i':
            val = int(val)
        elif ntype == 'f':
            val = float(val)
    for iid in itemids:
        print("PATCHING", iid, "to", field, "=", val)
        if (args.dbupdate):
            # do the patch
            if val == '*delete*':
                res = delete_field(iid, field, auth)
            else:
                res = patch_metadata({args.field: val}, iid, auth)
            if res['status'] == 'success':
                print("SUCCESS!")
            else:
                print("FAILED TO PATCH", iid, "RESPONSE STATUS", res['status'], res['description'])
                # print(res)


if __name__ == '__main__':  # pragma:nocover
    main()
