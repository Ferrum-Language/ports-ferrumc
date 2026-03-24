COMMENT =	Ferrum-language compiler with compile-time memory safety

DISTNAME =	ferrumc-v0.3.0-linux-amd64
PKGNAME =	ferrumc-0.3.0
CATEGORIES =	lang

HOMEPAGE =	https://ferrum-language.github.io/Ferrum/
MAINTAINER =	Ferrum-Language <noreply@ferrum-lang.org>

# GPL v3
PERMIT_PACKAGE =	Yes

WANTLIB =

MASTER_SITES =	https://github.com/Ferrum-Language/Ferrum/releases/download/v0.3.0/
DISTFILES =	ferrumc-v0.3.0-linux-x86_64.tar.gz

NO_BUILD =	Yes
NO_TEST =	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKDIR}/ferrumc ${PREFIX}/bin/ferrumc

.include <bsd.port.mk>
