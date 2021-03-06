#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/aniket/moveit/src/moveit_ros/visualization"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/aniket/moveit/install/lib/python2.7/dist-packages:/home/aniket/moveit/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/aniket/moveit/build" \
    "/usr/bin/python" \
    "/home/aniket/moveit/src/moveit_ros/visualization/setup.py" \
    build --build-base "/home/aniket/moveit/build/moveit_ros/visualization" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/aniket/moveit/install" --install-scripts="/home/aniket/moveit/install/bin"
