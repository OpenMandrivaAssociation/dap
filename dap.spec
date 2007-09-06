%define name	dap
%define version	2.1.5
%define release %mkrel 5

Summary:	Audio sample editing and processing suite
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Sound
URL: 		http://www.cee.hw.ac.uk/~richardk/
Source: 	%{name}-%{version}.tar.bz2
Patch:		%{name}-2.1.5.patch.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libforms-devel

%description
DAP is a comprehensive audio sample editing and processing suite.
It currently supports AIFF and AIFF-C audio files, 8 or 16 bit
resolution, and 1, 2 or 4 channels of audio data. The package
offers comprehensive editing, playback, and recording facilities
including full time stretch resampling, manual data editing, and
a reasonably complete DSP processing suite.

%prep
%setup -q
cd tooltips
%patch

%build
perl -p -i -e 's/XFORMS\)\/FORMS/XFORMS\)/g' `find -name Makefile.linux`
perl -p -i -e 's/X11DIR\)\/lib/X11DIR\)\/%_lib/' main/Makefile.linux
mv Makefile.linux Makefile
export XFORMS=/usr/X11R6/include/X11
%make OPTIM="$RPM_OPT_FLAGS"

%install
rm -rf %buildroot/

mkdir -p $RPM_BUILD_ROOT/%_bindir
cp main/DAP $RPM_BUILD_ROOT/%_bindir/dap

# Menu
mkdir -p %buildroot/%{_menudir}
cat > %buildroot/%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="sound_section.png" section="Multimedia/Sound" \
title="DAP" longtitle="Digital audio processing suite" \
xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories="X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio / Midi / Mixer / Sequencer / Tuner / Audio;AudioVideoEditing / Audio;Player / Audio;Recorder;"
EOF



%clean
rm -rf %buildroot/

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc CHANGES COPYING FEATURES README THANKS TODO
%{_bindir}/%name
%{_menudir}/%{name}
%{_datadir}/applications/*
