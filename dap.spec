%define name	dap
%define version	2.1.5
%define release  12

Summary:	Audio sample editing and processing suite
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Sound
URL: 		http://www.cee.hw.ac.uk/~richardk/
Source: 	%{name}-%{version}.tar.bz2
Patch1:		dap-2.1.5-x11-path.patch
BuildRequires:	libforms-devel
Buildrequires:	pkgconfig(x11)

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
make CXX="g++ %ldflags" OPTIM="$RPM_OPT_FLAGS" -f Makefile.linux

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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%doc CHANGES COPYING FEATURES README THANKS TODO
%{_bindir}/%name
%{_datadir}/applications/*


%changelog
* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 2.1.5-11mdv2011.0
+ Revision: 623979
- rebuild for new xform

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.5-10mdv2011.0
+ Revision: 617517
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.1.5-9mdv2010.0
+ Revision: 427209
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.1.5-8mdv2009.0
+ Revision: 243960
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.1.5-6mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - old patch not needed

* Thu Sep 06 2007 Funda Wang <fwang@mandriva.org> 2.1.5-6mdv2008.0
+ Revision: 80961
- Rebuild for new x11 library
- Import dap



* Fri Aug 04 2006 Lenny Cartier <lenny@mandriva.com> 2.1.5-5mdv2007.0
- xdg

* Fri Jun 23 2006 Pascal Terjan <pterjan@mandriva.org> 2.1.5-4mdv2007.0
- fix lib64

* Thu Jan 06 2006 Lenny Cartier <lenny@mandriva.com> 2.1.5-3mdk
- rebuild

* Wed Jun 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.1.5-2mdk
- rebuild

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 2.1.5-1mdk
- 2.1.5

* Tue Jan 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.1.4-1mdk
- from Austin Acton <aacton@yorku.ca> :
	- initial package
