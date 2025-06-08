# SNMP MIB module (CISCO-PKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-PKI-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:13:24 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoPkiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854)
)
if mibBuilder.loadTexts:
    ciscoPkiMIB.setRevisions(
        ("2014-10-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPkiMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPkiMIBNotifs = _CiscoPkiMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 1)
)
_CiscoPkiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPkiMIBObjects = _CiscoPkiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2)
)
_CiscoPkiConfiguration_ObjectIdentity = ObjectIdentity
ciscoPkiConfiguration = _CiscoPkiConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1)
)
_CiscoPkiEnrollmentProfile_ObjectIdentity = ObjectIdentity
ciscoPkiEnrollmentProfile = _CiscoPkiEnrollmentProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1)
)
_CiscoPkiEnrollmentTable_Object = MibTable
ciscoPkiEnrollmentTable = _CiscoPkiEnrollmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPkiEnrollmentTable.setStatus("current")
_EnrollProfEntry_Object = MibTableRow
enrollProfEntry = _EnrollProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1)
)
enrollProfEntry.setIndexNames(
    (0, "CISCO-PKI-MIB", "enrollProfLabel"),
)
if mibBuilder.loadTexts:
    enrollProfEntry.setStatus("current")


class _EnrollProfLabel_Type(DisplayString):
    """Custom type enrollProfLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnrollProfLabel_Type.__name__ = "DisplayString"
_EnrollProfLabel_Object = MibTableColumn
enrollProfLabel = _EnrollProfLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 3),
    _EnrollProfLabel_Type()
)
enrollProfLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enrollProfLabel.setStatus("current")
_EnrolCredentials_Type = DisplayString
_EnrolCredentials_Object = MibTableColumn
enrolCredentials = _EnrolCredentials_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 4),
    _EnrolCredentials_Type()
)
enrolCredentials.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrolCredentials.setStatus("current")
_AuthLocation_Type = DisplayString
_AuthLocation_Object = MibTableColumn
authLocation = _AuthLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 5),
    _AuthLocation_Type()
)
authLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authLocation.setStatus("current")
_AuthMethod_Type = DisplayString
_AuthMethod_Object = MibTableColumn
authMethod = _AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 6),
    _AuthMethod_Type()
)
authMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authMethod.setStatus("current")
_AuthVrf_Type = DisplayString
_AuthVrf_Object = MibTableColumn
authVrf = _AuthVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 7),
    _AuthVrf_Type()
)
authVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authVrf.setStatus("current")
_AuthSourceInter_Type = DisplayString
_AuthSourceInter_Object = MibTableColumn
authSourceInter = _AuthSourceInter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 8),
    _AuthSourceInter_Type()
)
authSourceInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSourceInter.setStatus("current")


class _EnrolMethod_Type(DisplayString):
    """Custom type enrolMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnrolMethod_Type.__name__ = "DisplayString"
_EnrolMethod_Object = MibTableColumn
enrolMethod = _EnrolMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 9),
    _EnrolMethod_Type()
)
enrolMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrolMethod.setStatus("current")
_EnrolLocation_Type = DisplayString
_EnrolLocation_Object = MibTableColumn
enrolLocation = _EnrolLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 10),
    _EnrolLocation_Type()
)
enrolLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrolLocation.setStatus("current")
_EnrolVrf_Type = DisplayString
_EnrolVrf_Object = MibTableColumn
enrolVrf = _EnrolVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 11),
    _EnrolVrf_Type()
)
enrolVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrolVrf.setStatus("current")
_EnrolSourceInter_Type = DisplayString
_EnrolSourceInter_Object = MibTableColumn
enrolSourceInter = _EnrolSourceInter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 12),
    _EnrolSourceInter_Type()
)
enrolSourceInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrolSourceInter.setStatus("current")
_ReenrolMethod_Type = DisplayString
_ReenrolMethod_Object = MibTableColumn
reenrolMethod = _ReenrolMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 13),
    _ReenrolMethod_Type()
)
reenrolMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reenrolMethod.setStatus("current")
_ReenrolLocation_Type = DisplayString
_ReenrolLocation_Object = MibTableColumn
reenrolLocation = _ReenrolLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 14),
    _ReenrolLocation_Type()
)
reenrolLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reenrolLocation.setStatus("current")
_ReenrolVrf_Type = DisplayString
_ReenrolVrf_Object = MibTableColumn
reenrolVrf = _ReenrolVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 15),
    _ReenrolVrf_Type()
)
reenrolVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reenrolVrf.setStatus("current")
_ReenrolSourceInter_Type = DisplayString
_ReenrolSourceInter_Object = MibTableColumn
reenrolSourceInter = _ReenrolSourceInter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 1, 1, 1, 16),
    _ReenrolSourceInter_Type()
)
reenrolSourceInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reenrolSourceInter.setStatus("current")
_CiscoPkiTrustpoints_ObjectIdentity = ObjectIdentity
ciscoPkiTrustpoints = _CiscoPkiTrustpoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2)
)
_PkiTPTable_Object = MibTable
pkiTPTable = _PkiTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pkiTPTable.setStatus("current")
_PkiTPEntry_Object = MibTableRow
pkiTPEntry = _PkiTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1)
)
pkiTPEntry.setIndexNames(
    (0, "CISCO-PKI-MIB", "tpLabel"),
)
if mibBuilder.loadTexts:
    pkiTPEntry.setStatus("current")


class _TpLabel_Type(DisplayString):
    """Custom type tpLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpLabel_Type.__name__ = "DisplayString"
_TpLabel_Object = MibTableColumn
tpLabel = _TpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 1),
    _TpLabel_Type()
)
tpLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tpLabel.setStatus("current")


class _SubjectName_Type(DisplayString):
    """Custom type subjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SubjectName_Type.__name__ = "DisplayString"
_SubjectName_Object = MibTableColumn
subjectName = _SubjectName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 2),
    _SubjectName_Type()
)
subjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subjectName.setStatus("current")


class _SubjectAltName_Type(DisplayString):
    """Custom type subjectAltName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SubjectAltName_Type.__name__ = "DisplayString"
_SubjectAltName_Object = MibTableColumn
subjectAltName = _SubjectAltName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 3),
    _SubjectAltName_Type()
)
subjectAltName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subjectAltName.setStatus("current")


class _AaaListInfo_Type(DisplayString):
    """Custom type aaaListInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AaaListInfo_Type.__name__ = "DisplayString"
_AaaListInfo_Object = MibTableColumn
aaaListInfo = _AaaListInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 4),
    _AaaListInfo_Type()
)
aaaListInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaListInfo.setStatus("current")


class _EnrollmentConfig_Type(DisplayString):
    """Custom type enrollmentConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EnrollmentConfig_Type.__name__ = "DisplayString"
_EnrollmentConfig_Object = MibTableColumn
enrollmentConfig = _EnrollmentConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 5),
    _EnrollmentConfig_Type()
)
enrollmentConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enrollmentConfig.setStatus("current")


class _VrfConfig_Type(DisplayString):
    """Custom type vrfConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_VrfConfig_Type.__name__ = "DisplayString"
_VrfConfig_Object = MibTableColumn
vrfConfig = _VrfConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 6),
    _VrfConfig_Type()
)
vrfConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrfConfig.setStatus("current")


class _SourceInter_Type(DisplayString):
    """Custom type sourceInter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SourceInter_Type.__name__ = "DisplayString"
_SourceInter_Object = MibTableColumn
sourceInter = _SourceInter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 7),
    _SourceInter_Type()
)
sourceInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceInter.setStatus("current")


class _AutoEnroll_Type(DisplayString):
    """Custom type autoEnroll based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AutoEnroll_Type.__name__ = "DisplayString"
_AutoEnroll_Object = MibTableColumn
autoEnroll = _AutoEnroll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 8),
    _AutoEnroll_Type()
)
autoEnroll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    autoEnroll.setStatus("current")


class _KeyPairLabel_Type(DisplayString):
    """Custom type keyPairLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KeyPairLabel_Type.__name__ = "DisplayString"
_KeyPairLabel_Object = MibTableColumn
keyPairLabel = _KeyPairLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 10),
    _KeyPairLabel_Type()
)
keyPairLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    keyPairLabel.setStatus("current")


class _RevocationMethod_Type(DisplayString):
    """Custom type revocationMethod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RevocationMethod_Type.__name__ = "DisplayString"
_RevocationMethod_Object = MibTableColumn
revocationMethod = _RevocationMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 11),
    _RevocationMethod_Type()
)
revocationMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revocationMethod.setStatus("current")
_HashAlgo_Type = DisplayString
_HashAlgo_Object = MibTableColumn
hashAlgo = _HashAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 12),
    _HashAlgo_Type()
)
hashAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hashAlgo.setStatus("current")


class _TrustpointState_Type(DisplayString):
    """Custom type trustpointState based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrustpointState_Type.__name__ = "DisplayString"
_TrustpointState_Object = MibTableColumn
trustpointState = _TrustpointState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 1, 2, 1, 1, 13),
    _TrustpointState_Type()
)
trustpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustpointState.setStatus("current")
_CiscoPkiCertificates_ObjectIdentity = ObjectIdentity
ciscoPkiCertificates = _CiscoPkiCertificates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2)
)
_CertChainTable_Object = MibTable
certChainTable = _CertChainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1)
)
if mibBuilder.loadTexts:
    certChainTable.setStatus("current")
_CertChainEntry_Object = MibTableRow
certChainEntry = _CertChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1)
)
certChainEntry.setIndexNames(
    (0, "CISCO-PKI-MIB", "certChainLabel"),
)
if mibBuilder.loadTexts:
    certChainEntry.setStatus("current")
_CertChainLabel_Type = DisplayString
_CertChainLabel_Object = MibTableColumn
certChainLabel = _CertChainLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 1),
    _CertChainLabel_Type()
)
certChainLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    certChainLabel.setStatus("current")
_CertSerialNum_Type = DisplayString
_CertSerialNum_Object = MibTableColumn
certSerialNum = _CertSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 2),
    _CertSerialNum_Type()
)
certSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSerialNum.setStatus("current")
_CertIssuerName_Type = DisplayString
_CertIssuerName_Object = MibTableColumn
certIssuerName = _CertIssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 3),
    _CertIssuerName_Type()
)
certIssuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certIssuerName.setStatus("current")
_CertStartDate_Type = DisplayString
_CertStartDate_Object = MibTableColumn
certStartDate = _CertStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 4),
    _CertStartDate_Type()
)
certStartDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certStartDate.setStatus("current")
_CertEndDate_Type = DisplayString
_CertEndDate_Object = MibTableColumn
certEndDate = _CertEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 5),
    _CertEndDate_Type()
)
certEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certEndDate.setStatus("current")
_CertType_Type = DisplayString
_CertType_Object = MibTableColumn
certType = _CertType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 6),
    _CertType_Type()
)
certType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certType.setStatus("current")
_CertRemainingLife_Type = DisplayString
_CertRemainingLife_Object = MibTableColumn
certRemainingLife = _CertRemainingLife_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 7),
    _CertRemainingLife_Type()
)
certRemainingLife.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    certRemainingLife.setStatus("current")
_CertTpLabel_Type = DisplayString
_CertTpLabel_Object = MibTableColumn
certTpLabel = _CertTpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 8),
    _CertTpLabel_Type()
)
certTpLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certTpLabel.setStatus("current")
_CertSubName_Type = DisplayString
_CertSubName_Object = MibTableColumn
certSubName = _CertSubName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 2, 1, 1, 9),
    _CertSubName_Type()
)
certSubName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certSubName.setStatus("current")
_CiscoPkiRevocationInfo_ObjectIdentity = ObjectIdentity
ciscoPkiRevocationInfo = _CiscoPkiRevocationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3)
)
_CiscoPkiCRLInfo_ObjectIdentity = ObjectIdentity
ciscoPkiCRLInfo = _CiscoPkiCRLInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1)
)
_PkiCRLTable_Object = MibTable
pkiCRLTable = _PkiCRLTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pkiCRLTable.setStatus("current")
_PkiCRLEntry_Object = MibTableRow
pkiCRLEntry = _PkiCRLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1)
)
pkiCRLEntry.setIndexNames(
    (0, "CISCO-PKI-MIB", "crlTpLabel"),
)
if mibBuilder.loadTexts:
    pkiCRLEntry.setStatus("current")
_CrlTpLabel_Type = DisplayString
_CrlTpLabel_Object = MibTableColumn
crlTpLabel = _CrlTpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 1),
    _CrlTpLabel_Type()
)
crlTpLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crlTpLabel.setStatus("current")


class _IssuerName_Type(DisplayString):
    """Custom type issuerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IssuerName_Type.__name__ = "DisplayString"
_IssuerName_Object = MibTableColumn
issuerName = _IssuerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 2),
    _IssuerName_Type()
)
issuerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    issuerName.setStatus("current")


class _SequenceNumb_Type(DisplayString):
    """Custom type sequenceNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SequenceNumb_Type.__name__ = "DisplayString"
_SequenceNumb_Object = MibTableColumn
sequenceNumb = _SequenceNumb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 3),
    _SequenceNumb_Type()
)
sequenceNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sequenceNumb.setStatus("current")


class _NextUpdate_Type(DisplayString):
    """Custom type nextUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NextUpdate_Type.__name__ = "DisplayString"
_NextUpdate_Object = MibTableColumn
nextUpdate = _NextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 4),
    _NextUpdate_Type()
)
nextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextUpdate.setStatus("current")


class _CrlSize_Type(Unsigned32):
    """Custom type crlSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_CrlSize_Type.__name__ = "Unsigned32"
_CrlSize_Object = MibTableColumn
crlSize = _CrlSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 5),
    _CrlSize_Type()
)
crlSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlSize.setStatus("current")


class _DeltaCRLFlag_Type(Unsigned32):
    """Custom type deltaCRLFlag based on Unsigned32"""
    defaultValue = 0


_DeltaCRLFlag_Type.__name__ = "Unsigned32"
_DeltaCRLFlag_Object = MibTableColumn
deltaCRLFlag = _DeltaCRLFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 1, 1, 1, 6),
    _DeltaCRLFlag_Type()
)
deltaCRLFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deltaCRLFlag.setStatus("current")
_CiscoPkiOSCPInfo_ObjectIdentity = ObjectIdentity
ciscoPkiOSCPInfo = _CiscoPkiOSCPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2)
)
_PkiOCSPTable_Object = MibTable
pkiOCSPTable = _PkiOCSPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    pkiOCSPTable.setStatus("current")
_PkiOCSPEntry_Object = MibTableRow
pkiOCSPEntry = _PkiOCSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1, 1)
)
pkiOCSPEntry.setIndexNames(
    (0, "CISCO-PKI-MIB", "ocspTpLabel"),
)
if mibBuilder.loadTexts:
    pkiOCSPEntry.setStatus("current")


class _OcspTpLabel_Type(DisplayString):
    """Custom type ocspTpLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OcspTpLabel_Type.__name__ = "DisplayString"
_OcspTpLabel_Object = MibTableColumn
ocspTpLabel = _OcspTpLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1, 1, 1),
    _OcspTpLabel_Type()
)
ocspTpLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ocspTpLabel.setStatus("current")


class _ResponderID_Type(DisplayString):
    """Custom type responderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ResponderID_Type.__name__ = "DisplayString"
_ResponderID_Object = MibTableColumn
responderID = _ResponderID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1, 1, 2),
    _ResponderID_Type()
)
responderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    responderID.setStatus("current")


class _ThisUpdate_Type(DisplayString):
    """Custom type thisUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ThisUpdate_Type.__name__ = "DisplayString"
_ThisUpdate_Object = MibTableColumn
thisUpdate = _ThisUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1, 1, 3),
    _ThisUpdate_Type()
)
thisUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thisUpdate.setStatus("current")


class _NexUpdate_Type(DisplayString):
    """Custom type nexUpdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NexUpdate_Type.__name__ = "DisplayString"
_NexUpdate_Object = MibTableColumn
nexUpdate = _NexUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 2, 3, 2, 1, 1, 4),
    _NexUpdate_Type()
)
nexUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nexUpdate.setStatus("current")
_CiscoPkiMIBConform_ObjectIdentity = ObjectIdentity
ciscoPkiMIBConform = _CiscoPkiMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3)
)
_CiscoPkiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPkiMIBCompliances = _CiscoPkiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3, 1)
)
_CiscoPkiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPkiMIBGroups = _CiscoPkiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3, 2)
)

# Managed Objects groups

ciscoPkiMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3, 2, 1)
)
ciscoPkiMIBMainObjectGroup.setObjects(
      *(("CISCO-PKI-MIB", "enrolMethod"),
        ("CISCO-PKI-MIB", "trustpointState"),
        ("CISCO-PKI-MIB", "revocationMethod"),
        ("CISCO-PKI-MIB", "enrollmentConfig"),
        ("CISCO-PKI-MIB", "subjectName"),
        ("CISCO-PKI-MIB", "subjectAltName"),
        ("CISCO-PKI-MIB", "aaaListInfo"),
        ("CISCO-PKI-MIB", "vrfConfig"),
        ("CISCO-PKI-MIB", "sourceInter"),
        ("CISCO-PKI-MIB", "autoEnroll"),
        ("CISCO-PKI-MIB", "keyPairLabel"),
        ("CISCO-PKI-MIB", "issuerName"),
        ("CISCO-PKI-MIB", "sequenceNumb"),
        ("CISCO-PKI-MIB", "nextUpdate"),
        ("CISCO-PKI-MIB", "crlSize"),
        ("CISCO-PKI-MIB", "deltaCRLFlag"),
        ("CISCO-PKI-MIB", "responderID"),
        ("CISCO-PKI-MIB", "thisUpdate"),
        ("CISCO-PKI-MIB", "nexUpdate"),
        ("CISCO-PKI-MIB", "certRemainingLife"),
        ("CISCO-PKI-MIB", "certSerialNum"),
        ("CISCO-PKI-MIB", "certIssuerName"),
        ("CISCO-PKI-MIB", "certStartDate"),
        ("CISCO-PKI-MIB", "certEndDate"),
        ("CISCO-PKI-MIB", "certType"),
        ("CISCO-PKI-MIB", "certTpLabel"),
        ("CISCO-PKI-MIB", "certSubName"),
        ("CISCO-PKI-MIB", "hashAlgo"),
        ("CISCO-PKI-MIB", "enrolCredentials"),
        ("CISCO-PKI-MIB", "authLocation"),
        ("CISCO-PKI-MIB", "authMethod"),
        ("CISCO-PKI-MIB", "authVrf"),
        ("CISCO-PKI-MIB", "authSourceInter"),
        ("CISCO-PKI-MIB", "enrolLocation"),
        ("CISCO-PKI-MIB", "enrolVrf"),
        ("CISCO-PKI-MIB", "enrolSourceInter"),
        ("CISCO-PKI-MIB", "reenrolMethod"),
        ("CISCO-PKI-MIB", "reenrolLocation"),
        ("CISCO-PKI-MIB", "reenrolVrf"),
        ("CISCO-PKI-MIB", "reenrolSourceInter"))
)
if mibBuilder.loadTexts:
    ciscoPkiMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoPkiCertInstallAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 1, 1)
)
ciscoPkiCertInstallAlert.setObjects(
      *(("CISCO-PKI-MIB", "certSerialNum"),
        ("CISCO-PKI-MIB", "certIssuerName"),
        ("CISCO-PKI-MIB", "certStartDate"),
        ("CISCO-PKI-MIB", "certEndDate"),
        ("CISCO-PKI-MIB", "certType"),
        ("CISCO-PKI-MIB", "certTpLabel"),
        ("CISCO-PKI-MIB", "certSubName"))
)
if mibBuilder.loadTexts:
    ciscoPkiCertInstallAlert.setStatus(
        "current"
    )

ciscoPkiCertExpiryAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 1, 2)
)
ciscoPkiCertExpiryAlert.setObjects(
      *(("CISCO-PKI-MIB", "certSerialNum"),
        ("CISCO-PKI-MIB", "certSubName"),
        ("CISCO-PKI-MIB", "certIssuerName"),
        ("CISCO-PKI-MIB", "certType"),
        ("CISCO-PKI-MIB", "certTpLabel"),
        ("CISCO-PKI-MIB", "certRemainingLife"))
)
if mibBuilder.loadTexts:
    ciscoPkiCertExpiryAlert.setStatus(
        "current"
    )


# Notifications groups

ciscoPkiMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3, 2, 2)
)
ciscoPkiMIBNotificationGroup.setObjects(
      *(("CISCO-PKI-MIB", "ciscoPkiCertInstallAlert"),
        ("CISCO-PKI-MIB", "ciscoPkiCertExpiryAlert"))
)
if mibBuilder.loadTexts:
    ciscoPkiMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPkiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 854, 3, 1, 1)
)
ciscoPkiMIBCompliance.setObjects(
      *(("CISCO-PKI-MIB", "ciscoPkiMIBMainObjectGroup"),
        ("CISCO-PKI-MIB", "ciscoPkiMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoPkiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PKI-MIB",
    **{"ciscoPkiMIB": ciscoPkiMIB,
       "ciscoPkiMIBNotifs": ciscoPkiMIBNotifs,
       "ciscoPkiCertInstallAlert": ciscoPkiCertInstallAlert,
       "ciscoPkiCertExpiryAlert": ciscoPkiCertExpiryAlert,
       "ciscoPkiMIBObjects": ciscoPkiMIBObjects,
       "ciscoPkiConfiguration": ciscoPkiConfiguration,
       "ciscoPkiEnrollmentProfile": ciscoPkiEnrollmentProfile,
       "ciscoPkiEnrollmentTable": ciscoPkiEnrollmentTable,
       "enrollProfEntry": enrollProfEntry,
       "enrollProfLabel": enrollProfLabel,
       "enrolCredentials": enrolCredentials,
       "authLocation": authLocation,
       "authMethod": authMethod,
       "authVrf": authVrf,
       "authSourceInter": authSourceInter,
       "enrolMethod": enrolMethod,
       "enrolLocation": enrolLocation,
       "enrolVrf": enrolVrf,
       "enrolSourceInter": enrolSourceInter,
       "reenrolMethod": reenrolMethod,
       "reenrolLocation": reenrolLocation,
       "reenrolVrf": reenrolVrf,
       "reenrolSourceInter": reenrolSourceInter,
       "ciscoPkiTrustpoints": ciscoPkiTrustpoints,
       "pkiTPTable": pkiTPTable,
       "pkiTPEntry": pkiTPEntry,
       "tpLabel": tpLabel,
       "subjectName": subjectName,
       "subjectAltName": subjectAltName,
       "aaaListInfo": aaaListInfo,
       "enrollmentConfig": enrollmentConfig,
       "vrfConfig": vrfConfig,
       "sourceInter": sourceInter,
       "autoEnroll": autoEnroll,
       "keyPairLabel": keyPairLabel,
       "revocationMethod": revocationMethod,
       "hashAlgo": hashAlgo,
       "trustpointState": trustpointState,
       "ciscoPkiCertificates": ciscoPkiCertificates,
       "certChainTable": certChainTable,
       "certChainEntry": certChainEntry,
       "certChainLabel": certChainLabel,
       "certSerialNum": certSerialNum,
       "certIssuerName": certIssuerName,
       "certStartDate": certStartDate,
       "certEndDate": certEndDate,
       "certType": certType,
       "certRemainingLife": certRemainingLife,
       "certTpLabel": certTpLabel,
       "certSubName": certSubName,
       "ciscoPkiRevocationInfo": ciscoPkiRevocationInfo,
       "ciscoPkiCRLInfo": ciscoPkiCRLInfo,
       "pkiCRLTable": pkiCRLTable,
       "pkiCRLEntry": pkiCRLEntry,
       "crlTpLabel": crlTpLabel,
       "issuerName": issuerName,
       "sequenceNumb": sequenceNumb,
       "nextUpdate": nextUpdate,
       "crlSize": crlSize,
       "deltaCRLFlag": deltaCRLFlag,
       "ciscoPkiOSCPInfo": ciscoPkiOSCPInfo,
       "pkiOCSPTable": pkiOCSPTable,
       "pkiOCSPEntry": pkiOCSPEntry,
       "ocspTpLabel": ocspTpLabel,
       "responderID": responderID,
       "thisUpdate": thisUpdate,
       "nexUpdate": nexUpdate,
       "ciscoPkiMIBConform": ciscoPkiMIBConform,
       "ciscoPkiMIBCompliances": ciscoPkiMIBCompliances,
       "ciscoPkiMIBCompliance": ciscoPkiMIBCompliance,
       "ciscoPkiMIBGroups": ciscoPkiMIBGroups,
       "ciscoPkiMIBMainObjectGroup": ciscoPkiMIBMainObjectGroup,
       "ciscoPkiMIBNotificationGroup": ciscoPkiMIBNotificationGroup}
)
