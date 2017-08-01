#!/bin/bash
printf "%s\n" \
    '  _____                    _____ _______ ______   ___   ___  __ ______ ' \
    ' / ____|                  / ____|__   __|  ____| |__ \ / _ \/_ |____  | ' \
    '| |     _ __ ___  ___ ___| |       | |  | |__       ) | | | || |   / /  ' \
    '| |    |  __/ _ \/ __/ __| |       | |  |  __|     / /| | | || |  / /   ' \
    '| |____| | | (_) \__ \__ \ |____   | |  | |       / /_| |_| || | / /    ' \
    ' \_____|_|  \___/|___/___/\_____|  |_|  |_|      |____|\___/ |_|/_/     ' \
    ''

CYCLE_ID=$1
TEAM_ID=$2

if [ -z "$2" ]; then
    printf "%s\n" \
        "Usage: `basename $0` <CHALLENGE_ID> <TEAM_ID>" \
        "" \
        "  This script runs a particular challenge binary in the challenge environment" \
        "  Docker container, exposed on this host at localhost:1337, so you can develop" \
        "  and test your exploit locally. The binary must be located at:" \
        "      ./volumes/round00/<CHALLENGE_ID>/exploitables/<TEAM_ID>_exploitable" \
        "" \
        "  CHALLENGE_ID: challenge name as provided" \
        "  TEAM_ID: this should be 'team00' for unpatched binary, and 'team01', 'team20'," \
        "           etc. for your team's patched binary." \
        "" \
        "  An example binary is included, try this:" \
        "      `basename $0` example team00" \
        "  You should then be able to connect (from another shell) and communicate:" \
        "      nc localhost 1337" \
        "  As this runs in the foreground, press Ctrl-C to terminate." \
        ""
    exit 1
fi

if test -z ${CYCLE_ID}; then
    exit 1
fi

if test -z ${TEAM_ID}; then
    exit 1
fi

CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGE_TAG='crossctf2017'
IMAGE_SHA256_REF='sha256:bcd274e2c43bd3007d9e5e620ba5279c66a86f83443118cc217cb7ab9a61a3a2'
IMAGE_SHA256=$(docker images --quiet --no-trunc $IMAGE_TAG 2> /dev/null)

if [[ ! -f "./${IMAGE_TAG}.tar" ]]; then
    echo "Downloading environment Docker image to ./${IMAGE_TAG}.tar, this should only happen on first run!"
    curl https://transfer.sh/3nDVs/crossctf2017.tar -o ./${IMAGE_TAG}.tar
fi

if ! echo "1d7a4122b9aa4b7b350dfd735a2fcb7d ./${IMAGE_TAG}.tar" | md5sum -c - &> /dev/null; then
    echo "Invalid MD5 for ./${IMAGE_TAG}.tar, remove ./${IMAGE_TAG}.tar and try again."
    exit 1
fi

if ! command -v docker &> /dev/null ; then
    echo 'Docker not found... please install Docker first?'
    exit 1
fi

if [[ -z $IMAGE_SHA256 || $IMAGE_SHA256_REF != $IMAGE_SHA256 ]]; then
    IMAGE_TO_BE_TAGGED=$(docker load -i $CWD/$IMAGE_TAG.tar)
    IMAGE_TO_BE_LOADED_SHA=$(awk -F ":" '{print $3}' <<< $IMAGE_TO_BE_TAGGED)
    docker tag $IMAGE_TO_BE_LOADED_SHA $IMAGE_TAG
fi

chmod -R +x $CWD/volumes || exit 1

if ! ls $CWD/volumes/round00/$CYCLE_ID/exploitables/${TEAM_ID}_exploitable &> /dev/null; then
    echo 'Could not find binary! Maybe CHALLENGE_ID and/or TEAM_ID are wrong?'
    exit 1
fi

echo "Starting Docker image... press Ctrl-C to terminate"
docker run --rm -it \
    -p "1337:1337" \
    -e "ROUND_ID=COVFEFE" \
    -e "CYCLE_ID=$CYCLE_ID" \
    -e "EXPLOITABLE_NAME=${TEAM_ID}_exploitable" \
    -v "$CWD/volumes/round00/:/round00:ro" \
    -v "$CWD/volumes/start.sh:/start.sh:ro" \
    $IMAGE_TAG
