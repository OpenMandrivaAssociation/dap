%define name	dap
%define version	2.1.5
%define release %mkrel 6

Summary:	Audio sample editing and processing suite
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Sound
URL: 		http://www.cee.hw.ac.uk/~richardk/
Source: 	%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.1.5.patch
Patch1:		dap-2.1.5-x11-path.patch
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
%patch1 -p1

%build
export XFORMS=/usr/include/X11
%make OPTIM="$RPM_OPT_FLAGS" -f Makefile.linux

%install
rm -rf %buildroot/

mkdir -p $RPM_BUILD_ROOT/%_bindir
cp main/DAP $RPM_BUILD_ROOT/%_bindir/dap

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Audio sample editing and processing suite
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Midi;Mixer;Sequencer;Tuner;AudioVideoEditing;Player;Recorder;
EOF

%clean
rm -rf %buildroot

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc CHANGES COPYING FEATURES README THANKS TODO
%{_bindir}/%name
%{_datadir}/applications/*
