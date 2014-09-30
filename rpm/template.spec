Name:           ros-hydro-explorer
Version:        0.1.2
Release:        1%{?dist}
Summary:        ROS explorer package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/explorer
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-adhoc-communication
Requires:       ros-hydro-costmap-2d
Requires:       ros-hydro-map-merger
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-move-base
Requires:       ros-hydro-nav-core
Requires:       ros-hydro-navfn
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-sound-play
Requires:       ros-hydro-std-msgs
Requires:       ros-hydro-voxel-grid
BuildRequires:  ros-hydro-adhoc-communication
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-costmap-2d
BuildRequires:  ros-hydro-map-merger
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-move-base
BuildRequires:  ros-hydro-nav-core
BuildRequires:  ros-hydro-navfn
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-sound-play
BuildRequires:  ros-hydro-std-msgs
BuildRequires:  ros-hydro-voxel-grid

%description
The explorer package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Sep 30 2014 dneuhold <dneuhold@todo.todo> - 0.1.2-1
- Autogenerated by Bloom

* Mon Sep 29 2014 dneuhold <dneuhold@todo.todo> - 0.1.1-1
- Autogenerated by Bloom

* Mon Sep 29 2014 dneuhold <dneuhold@todo.todo> - 0.1.1-2
- Autogenerated by Bloom

* Mon Sep 29 2014 dneuhold <dneuhold@todo.todo> - 0.1.2-0
- Autogenerated by Bloom

