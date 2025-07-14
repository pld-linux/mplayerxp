# Conditional build:
%bcond_without	altivec		# without altivec support
%bcond_without	x264		# without x264 support
%bcond_with	xmms		# with XMMS inputplugin support
%bcond_without	aalib		# without aalib video output
%bcond_without	jack		# without JACKD support
%bcond_without	alsa		# without ALSA audio output
%bcond_without	arts		# without arts audio output
%bcond_without	caca		# without libcaca video output
%bcond_without	cdparanoia	# without cdparanoia support
%bcond_without	enca		# disable using ENCA charset oracle library
%bcond_without	esd		# disable EsounD sound support
%bcond_without	faad		# disable FAAD2 (AAC) support
%bcond_without	gif		# disable GIF support
%bcond_without	gui		# without GTK+ GUI
%bcond_without	joystick	# disable joystick support
%bcond_without	libdts		# disable libdts support
%bcond_without	libdv		# disable libdv en/decoding support
%bcond_without	lirc		# without lirc support
%bcond_with	live		# without LIVE555 libraries
%bcond_without	lzo		# with LZO support (requires lzo 2.x)
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_without	pulseaudio	# without pulseaudio output
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	smb		# disable Samba (SMB) input support
%bcond_without	theora		# without theora support
%bcond_without	win32		# without win32 codecs support
%bcond_without	vidix		# disable vidix
%bcond_without	vorbis		# without Ogg-Vorbis audio support
%bcond_without	xvid		# disable XviD codec
%bcond_without	sdl		# disable SDL
%bcond_without	doc		# don't build docs (slow)
%bcond_with	shared		# experimental libmplayer.so support
%bcond_without	gnomess		# disable controling gnome screensaver
%bcond_without	ssse3		# sse3 optimizations (needs binutils >= 2.16.92)
%bcond_with	system_ffmpeg	# use ffmpeg-devel, rather bundled sources (likely needs ffmpeg from same svn revision than mplayer)

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%undefine	with_vidix
%endif

%if %{_lib} == "lib64"
%define		_suf	64
%else
%define		_suf	32
%endif

%define		subver	rc2
%define		svnver	27725
%define		rel	18

Summary:	MPlayerXP is a branch of the well known mplayer (http://mplayerhq.hu) which is based on the new (thread based) core
Name:		mplayerxp
Version:	0.7.2
Release:	0.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/mplayerxp/%{name}-%{version}.tar.bz2
# Source0-md5:	ba68358f9fe2cc1fbbcb09432826aa09
URL:		http://mplayerxp.sourceforge.net/
Patch0:		%{name}-lrint.patch
Patch1:		%{name}-limits.patch
Patch2:		%{name}-lrmi.patch
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.1.7}
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%if %{with amr}
BuildRequires:	amrnb-devel
BuildRequires:	amrwb-devel >= 5.3.0
%endif
%{?with_arts:BuildRequires:	artsc-devel}
%{?with_ssse3:BuildRequires:	binutils >= 3:2.16.92}
%{?with_cdparanoia:BuildRequires:	cdparanoia-III-devel}
%{?with_doc:BuildRequires:	docbook-dtd412-xml}
%{?with_doc:BuildRequires:	docbook-style-xsl}
%{?with_enca:BuildRequires:	enca-devel}
%{?with_esd:BuildRequires:	esound-devel}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0}
%{?with_system_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.4.9-4.20081024.3}
BuildRequires:	freetype-devel
BuildRequires:	fribidi-devel
%{?with_vidix:BuildRequires:	vidix-devel}
%ifarch ppc
%{?with_altivec:BuildRequires:	gcc >= 5:3.3.2-3}
%endif
%{?with_gif:BuildRequires:	giflib-devel}
%if %{with gui}
BuildRequires:	gtk+2-devel
%endif
%{?with_gnomess:BuildRequires:	dbus-glib-devel}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
%{?with_jack:%requires_eq	jack-audio-connection-kit-libs}
BuildRequires:	lame-libs-devel
%{?with_caca:BuildRequires:	libcaca-devel}
%{?with_libdts:BuildRequires:	libdts-devel}
%{?with_libdv:BuildRequires:	libdv-devel}
BuildRequires:	libjpeg-devel
%{?with_mad:BuildRequires:	libmad-devel}
BuildRequires:	libmpcdec-devel >= 1.2.1
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_theora:BuildRequires:	libtheora-devel}
# tremor is used by default, internal as we don't have system one
#%{?with_vorbis:BuildRequires:	libvorbis-devel}
%{?with_x264:BuildRequires:	libx264-devel >= 0.1.2-1.20081023_2245.1}
BuildRequires:	libxslt-progs
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_lzo:BuildRequires:	lzo-devel >= 2.0}
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
BuildRequires:	speex-devel >= 1.1
%{?with_xmms:BuildRequires:	xmms-libs}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1:0.9.0}
BuildRequires:	zlib-devel
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags_ia32	-fomit-frame-pointer
%if %{with altivec}
%define		specflags_ppc	-maltivec
%endif

%description
MPlayerXP is a branch of the well known mplayer (http://mplayerhq.hu)
which is based on the new (thread based) core. The new core provides
better CPU utilization and excellently improves performance of video
decoding. Main goal of this project is to get monotonous CPU loading
during movie playback.

%package -n gmplayer
Summary:	MPlayer with GTK+ GUI interface
Summary(pl.UTF-8):	MPlayer z graficznym interfejsem GTK+
Group:		X11/Applications/Multimedia
Requires:	%{name}-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-skin

%description -n gmplayer
MPlayer with GUI GTK+ interface.

%description -n gmplayer -l pl.UTF-8
MPlayer z graficznym interfejsem GTK+.

%package common
Summary:	Configuration files and documentation for MPlayer
Summary(pl.UTF-8):	Pliki konfiguracyjne i dokumentacja dla MPlayera
Group:		Applications/Multimedia
Obsoletes:	mplayer-vidix

%description common
Configuration files, man page and HTML documentation for MPlayer.

%description common -l pl.UTF-8
Pliki konfiguracyjne, strona manuala i dokumentacja HTML dla MPlayera.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
cp -f etc/codecs.conf etc/codecs.win32.conf

# Set version #
echo %{svnver} > svn_snapshot_id

sed -e '/Delete this default/d' etc/example.conf > etc/mplayer.conf
rm -f font-*/runme

%if %{with system_ffmpeg}
# using external ffmpeg, but mplayer adds these to includepath
rm -rf libavcodec libavdevice libavformat libavutil libpostproc libswscale
%endif

%build
%if %{with shared}
CFLAGS="%{rpmcflags} -fPIC"
%else
CFLAGS="%{rpmcflags}"
%endif
CC="%{__cc}"
LDFLAGS="%{rpmldflags}"
CFLAGS="$CFLAGS -I/usr/include/dirac -I/usr/include/schroedinger-1.0"
export CC CFLAGS LDFLAGS

./configure \
	%{?debug:--enable-debug=3} \
	--prefix=%{_prefix} \
	--confdir=%{_sysconfdir}/mplayerxp \
	--with-extraincdir=%{_includedir}/xvid \
	--with-extralibdir=%{?_x_libraries}%{!?_x_libraries:%{_libdir}} \
%if %{with system_ffmpeg}
	--disable-libavutil_a \
	--disable-libavcodec_a \
	--disable-libavformat_a \
	--disable-libpostproc_a \
	--enable-libavutil_so \
	--enable-libavcodec_so \
	--enable-libavformat_so \
	--enable-libpostproc_so \
%endif
%ifnarch %{ix86} %{x8664}
	--disable-mmx \
	--disable-mmxext \
	--disable-3dnow \
	--disable-3dnowext \
	--disable-sse \
	--disable-sse2 \
	--disable-fastmemcpy \
%endif
	%{!?with_ssse3:--disable-ssse3} \
%ifarch ppc
	%{!?with_altivec:--disable-altivec} \
%endif
	%{!?with_lzo:--disable-liblzo} \
	%{!?with_aalib:--disable-aa} \
	%{!?with_jack:--disable-jack} \
	%{!?with_alsa:--disable-alsa} \
	%{?with_alsa:--enable-alsa} \
	%{!?with_arts:--disable-arts} \
	%{!?with_caca:--disable-caca} \
	%{!?with_cdparanoia:--disable-cdparanoia} \
	%{!?with_enca:--disable-enca} \
	%{!?with_esd:--disable-esd} \
	%{!?with_gif:--disable-gif} \
	%{?with_joystick:--enable-joystick} \
	%{!?with_libdv:--disable-libdv} \
	%{!?with_libdts:--disable-libdts} \
	--%{?with_lirc:en}%{!?with_lirc:dis}able-lirc \
	%{!?with_mad:--disable-mad} \
	%{!?with_pulseaudio:--disable-polyp} \
	%{!?with_quicktime:--disable-qtx} \
	%{!?with_real:--disable-real} \
	%{!?with_smb:--disable-smb} \
	%{!?with_win32:--disable-win32dll} \
	%{!?with_vorbis:--disable-vorbis} \
	%{!?with_theora:--disable-theora} \
	%{!?with_x264:--disable-x264} \
	%{?with_xmms:--enable-xmms --with-xmmsplugindir=%{_libdir}/xmms/Input --with-xmmslibdir=%{_libdir}} \
	%{!?with_xvid:--disable-xvid} \
	%{!?with_vidix:--disable-vidix} \
	--enable-fbdev \
	--%{?with_sdl:en}%{!?with_sdl:dis}able-sdl \
	--enable-x11 \
	--enable-xv \
	--enable-largefiles \
	--language=all \
	"$@"

	%{__make}

%if %{with doc}
# %{__make} -j1 -C DOCS/xml
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_mandir}/{cs,de,es,fr,hu,it,pl,sv,zh_CN,}/man1 \
	$RPM_BUILD_ROOT%{_datadir}/mplayer/skins \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
install etc/{codecs,mplayer,input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# executables
install mplayer $RPM_BUILD_ROOT%{_bindir}/mplayer%{_suf}
ln -sf mplayer%{_suf} $RPM_BUILD_ROOT%{_bindir}/mplayer
%if %{with gui}
install gmplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer%{_suf}
ln -sf gmplayer%{_suf} $RPM_BUILD_ROOT%{_bindir}/gmplayer
%endif

# fonts
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

# man pages
install DOCS/man/cs/*.1 $RPM_BUILD_ROOT%{_mandir}/cs/man1
install DOCS/man/de/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1
install DOCS/man/en/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/man/es/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install DOCS/man/fr/*.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1
install DOCS/man/hu/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install DOCS/man/it/*.1 $RPM_BUILD_ROOT%{_mandir}/it/man1
install DOCS/man/pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
#install DOCS/man/sv/*.1 $RPM_BUILD_ROOT%{_mandir}/sv/man1
install DOCS/man/zh/*.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post -n gmplayer
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1 ||:

%postun -n gmplayer
umask 022
[ ! -x %{_bindir}/update-desktop-database ] || %{_bindir}/update-desktop-database >/dev/null 2>&1 ||:

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mplayer*

%if %{with gui}
%files -n gmplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gmplayer*
%{_desktopdir}/gmplayer.desktop
%endif

%files common
%defattr(644,root,root,755)
%doc DOCS/tech
%if %{with win32}
%doc etc/codecs.win32.conf
%endif
%if %{with doc}
# HTML and XML-generated docs
%doc DOCS/HTML/en
%lang(cs) %doc DOCS/HTML/cs
%lang(de) %doc DOCS/HTML/de
%lang(es) %doc DOCS/HTML/es
%lang(fr) %doc DOCS/HTML/fr
%lang(hu) %doc DOCS/HTML/hu
%lang(pl) %doc DOCS/HTML/pl
%lang(ru) %doc DOCS/HTML/ru
#%lang(zh_CN) %doc DOCS/zh
%endif
%doc AUTHORS README

%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*.conf
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(pl) %{_mandir}/pl/man1/*
#%lang(sv) %{_mandir}/sv/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%{_desktopdir}/mplayer.desktop
%{_pixmapsdir}/mplayer.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/font*
%dir %{_datadir}/%{name}/skins
%ghost %{_datadir}/%{name}/skins/default
