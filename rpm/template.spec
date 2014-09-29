Name:           ros-hydro-map-merger
Version:        0.1.1
Release:        2%{?dist}
Summary:        ROS map_merger package

Group:          Development/Libraries
License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-adhoc-communication
Requires:       ros-hydro-message-generation
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-roscpp
BuildRequires:  ros-hydro-adhoc-communication
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-roscpp

%description
The map_merger package

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
* Mon Sep 29 2014 student <student@todo.todo> - 0.1.1-2
- Autogenerated by Bloom

* Mon Sep 29 2014 student <student@todo.todo> - 0.1.1-0
- Autogenerated by Bloom

* Mon Sep 29 2014 student <student@todo.todo> - 0.1.1-1
- Autogenerated by Bloom

