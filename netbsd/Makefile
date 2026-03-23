# $NetBSD$

DISTNAME=	ferrumc-0.3.0
PKGNAME=	ferrumc-0.3.0
CATEGORIES=	lang
MASTER_SITES=	https://github.com/Ferrum-Language/Ferrum/releases/download/v0.3.0/
DISTFILES=	ferrumc-v0.3.0-linux-x86_64.tar.gz

MAINTAINER=	noreply@ferrum-lang.org
HOMEPAGE=	https://ferrum-language.github.io/Ferrum/
COMMENT=	Ferrum-language compiler with compile-time memory safety

NO_BUILD=	yes
NO_CONFIGURE=	yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/ferrumc ${DESTDIR}${PREFIX}/bin/ferrumc

.include "../../mk/bsd.pkg.mk"
