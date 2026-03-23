COMMENT=	Ferrum-language compiler with compile-time memory safety

V=		0.3.0
DISTNAME=	ferrumc-v${V}-freebsd-x86_64
PKGNAME=	ferrumc-${V}
CATEGORIES=	lang

HOMEPAGE=	https://ferrum-language.github.io/Ferrum/
MASTER_SITES=	https://github.com/Ferrum-Language/Ferrum/releases/download/v${V}/
DISTFILES=	ferrumc-v${V}-freebsd-x86_64.tar.gz

MAINTAINER=	noreply@ferrum-lang.org

PERMIT_PACKAGE=	Yes

NO_BUILD=	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/ferrumc ${PREFIX}/bin/ferrumc

.include <bsd.port.mk>
