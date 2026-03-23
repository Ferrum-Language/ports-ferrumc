PORTNAME=	ferrumc
PORTVERSION=	0.3.0
CATEGORIES=	lang
MASTER_SITES=	https://github.com/Ferrum-Language/Ferrum/releases/download/v${PORTVERSION}/

MAINTAINER=	noreply@ferrum-lang.org
COMMENT=	Ferrum-language compiler with compile-time memory safety
WWW=		https://ferrum-language.github.io/Ferrum/

LICENSE=	MIT

.if ${ARCH} == aarch64
DISTFILES=	ferrumc-v${PORTVERSION}-linux-aarch64.tar.gz
DISTNAME=	ferrumc-v${PORTVERSION}-freebsd-x86_64
.else
DISTFILES=	ferrumc-v${PORTVERSION}-freebsd-x86_64.tar.gz
DISTNAME=	ferrumc-v${PORTVERSION}-freebsd-x86_64
.endif

CHECKSUMS_SHA256=	cf9df1c047d814e00529f32d30bd34eadf1bc87152368f923f3c6caedf017555 \
			ferrumc-v0.3.0-freebsd-x86_64.tar.gz

NO_BUILD=	yes
NO_WRKSUBDIR=	yes

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/ferrumc ${STAGEDIR}${PREFIX}/bin/ferrumc

.include <bsd.port.mk>
