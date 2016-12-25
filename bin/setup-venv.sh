#!/bin/sh

# Do some sanity checking
if ! [ -f setup.py -a -f kle2xy.py ]; then
    echo 'You must run this in the top level of kle2xy!'
    exit 1
elif [ -d .kle2xy -a "$1" != "-f" ]; then
    echo 'Not replacing existing virtualenv. Use -f to override.'
    exit 1
elif ! virtualenv --version 2>&1 > /dev/null; then
    echo "You must install virtualenv first!"
    echo
    echo "Try: sudo easy_install virtualenv"
    exit 1
elif [ -n "$VIRTUAL_ENV" ]; then
    echo "You must 'deactivate' your current virtualenv before running this!"
    exit 1
fi

# If necessary, wipe away the old virtualenv
if [ -d .kle2xy ]; then
    while true; do
        echo "About to remove the existing virtualenv. OK to proceed?"
        read answer

        case $answer in
            yes|YES)
                rm -rf .kle2xy activate
                break
                ;;
            no|NO)
                echo "Can't proceed while existing virtualenv is in the way."
                exit 1
                ;;
            *)
                echo 'Please answer "yes" or "no".'
                ;;
        esac
    done
fi

# Create the new virtualenv
virtualenv .kle2xy || exit
site_packages=$(echo .kle2xy/lib/python*/site-packages | cut -f 1 -d ' ')
ln -s .kle2xy/bin/activate || exit

# Setup the environment
source activate || exit
pip install -r requirements.txt || exit
python setup.py develop || exit

cat << EOF
===============================================================================


Congratulations! VirtualEnv setup was completed successfully!

To get started activate your virtualenv:

    $ source $PWD/activate

EOF
