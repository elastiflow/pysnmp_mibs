# SNMP MIB module (CISCO-LWAPP-WLAN-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-WLAN-SECURITY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:06 2025
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

(CLSecEncryptType,
 CLSecKeyFormat) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLSecEncryptType",
    "CLSecKeyFormat")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappWlanSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521)
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIB.setRevisions(
        ("2023-06-06 00:00",
         "2022-01-10 00:00",
         "2020-09-02 00:00",
         "2020-03-24 00:00",
         "2019-07-16 00:00",
         "2018-09-05 00:00",
         "2017-05-17 00:00",
         "2008-01-15 00:00",
         "2007-11-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWlanSecurityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBNotifs = _CiscoLwappWlanSecurityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 0)
)
_CiscoLwappWlanSecurityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBObjects = _CiscoLwappWlanSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1)
)
_ClwsCckmConfig_ObjectIdentity = ObjectIdentity
clwsCckmConfig = _ClwsCckmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1)
)
_CLWSecDot11EssCckmTable_Object = MibTable
cLWSecDot11EssCckmTable = _CLWSecDot11EssCckmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmTable.setStatus("current")
_CLWSecDot11EssCckmEntry_Object = MibTableRow
cLWSecDot11EssCckmEntry = _CLWSecDot11EssCckmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1)
)
cLWSecDot11EssCckmEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmEntry.setStatus("current")


class _CLWSecDot11EssCckmWpaSupport_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpaSupport based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCckmWpaSupport_Type.__name__ = "TruthValue"
_CLWSecDot11EssCckmWpaSupport_Object = MibTableColumn
cLWSecDot11EssCckmWpaSupport = _CLWSecDot11EssCckmWpaSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 1),
    _CLWSecDot11EssCckmWpaSupport_Type()
)
cLWSecDot11EssCckmWpaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpaSupport.setStatus("current")


class _CLWSecDot11EssCckmWpa1Security_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpa1Security based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCckmWpa1Security_Type.__name__ = "TruthValue"
_CLWSecDot11EssCckmWpa1Security_Object = MibTableColumn
cLWSecDot11EssCckmWpa1Security = _CLWSecDot11EssCckmWpa1Security_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 2),
    _CLWSecDot11EssCckmWpa1Security_Type()
)
cLWSecDot11EssCckmWpa1Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa1Security.setStatus("current")


class _CLWSecDot11EssCckmWpa1EncType_Type(CLSecEncryptType):
    """Custom type cLWSecDot11EssCckmWpa1EncType based on CLSecEncryptType"""
    defaultBinValue = "0"


_CLWSecDot11EssCckmWpa1EncType_Type.__name__ = "CLSecEncryptType"
_CLWSecDot11EssCckmWpa1EncType_Object = MibTableColumn
cLWSecDot11EssCckmWpa1EncType = _CLWSecDot11EssCckmWpa1EncType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 3),
    _CLWSecDot11EssCckmWpa1EncType_Type()
)
cLWSecDot11EssCckmWpa1EncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa1EncType.setStatus("current")


class _CLWSecDot11EssCckmWpa2Security_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmWpa2Security based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCckmWpa2Security_Type.__name__ = "TruthValue"
_CLWSecDot11EssCckmWpa2Security_Object = MibTableColumn
cLWSecDot11EssCckmWpa2Security = _CLWSecDot11EssCckmWpa2Security_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 4),
    _CLWSecDot11EssCckmWpa2Security_Type()
)
cLWSecDot11EssCckmWpa2Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa2Security.setStatus("current")


class _CLWSecDot11EssCckmWpa2EncType_Type(CLSecEncryptType):
    """Custom type cLWSecDot11EssCckmWpa2EncType based on CLSecEncryptType"""
    defaultBinValue = "0"


_CLWSecDot11EssCckmWpa2EncType_Type.__name__ = "CLSecEncryptType"
_CLWSecDot11EssCckmWpa2EncType_Object = MibTableColumn
cLWSecDot11EssCckmWpa2EncType = _CLWSecDot11EssCckmWpa2EncType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 5),
    _CLWSecDot11EssCckmWpa2EncType_Type()
)
cLWSecDot11EssCckmWpa2EncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmWpa2EncType.setStatus("current")


class _CLWSecDot11EssCckmKeyMgmtMode_Type(Bits):
    """Custom type cLWSecDot11EssCckmKeyMgmtMode based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("dot1x", 0),
          ("cckm", 1),
          ("psk", 2),
          ("ftDot1x", 3),
          ("ftPsk", 4),
          ("pmfDot1x", 5),
          ("pmfPsk", 6),
          ("osenDot1x", 7),
          ("sae", 8),
          ("owe", 9),
          ("ftSae", 10),
          ("saeExtKey", 11),
          ("ftSaeExtKey", 12))
    )

_CLWSecDot11EssCckmKeyMgmtMode_Type.__name__ = "Bits"
_CLWSecDot11EssCckmKeyMgmtMode_Object = MibTableColumn
cLWSecDot11EssCckmKeyMgmtMode = _CLWSecDot11EssCckmKeyMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 6),
    _CLWSecDot11EssCckmKeyMgmtMode_Type()
)
cLWSecDot11EssCckmKeyMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmKeyMgmtMode.setStatus("current")


class _CLWSecDot11EssPskFmt_Type(CLSecKeyFormat):
    """Custom type cLWSecDot11EssPskFmt based on CLSecKeyFormat"""
    defaultValue = 1


_CLWSecDot11EssPskFmt_Type.__name__ = "CLSecKeyFormat"
_CLWSecDot11EssPskFmt_Object = MibTableColumn
cLWSecDot11EssPskFmt = _CLWSecDot11EssPskFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 7),
    _CLWSecDot11EssPskFmt_Type()
)
cLWSecDot11EssPskFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssPskFmt.setStatus("current")


class _CLWSecDot11EssPsk_Type(OctetString):
    """Custom type cLWSecDot11EssPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_CLWSecDot11EssPsk_Type.__name__ = "OctetString"
_CLWSecDot11EssPsk_Object = MibTableColumn
cLWSecDot11EssPsk = _CLWSecDot11EssPsk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 8),
    _CLWSecDot11EssPsk_Type()
)
cLWSecDot11EssPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssPsk.setStatus("current")


class _CLWSecDot11EssCckmGtkRandomize_Type(TruthValue):
    """Custom type cLWSecDot11EssCckmGtkRandomize based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCckmGtkRandomize_Type.__name__ = "TruthValue"
_CLWSecDot11EssCckmGtkRandomize_Object = MibTableColumn
cLWSecDot11EssCckmGtkRandomize = _CLWSecDot11EssCckmGtkRandomize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 9),
    _CLWSecDot11EssCckmGtkRandomize_Type()
)
cLWSecDot11EssCckmGtkRandomize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCckmGtkRandomize.setStatus("current")
_CLWSecDot11EssFtEnable_Type = TruthValue
_CLWSecDot11EssFtEnable_Object = MibTableColumn
cLWSecDot11EssFtEnable = _CLWSecDot11EssFtEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 10),
    _CLWSecDot11EssFtEnable_Type()
)
cLWSecDot11EssFtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtEnable.setStatus("deprecated")
_CLWSecDot11EssFtReassocTime_Type = Unsigned32
_CLWSecDot11EssFtReassocTime_Object = MibTableColumn
cLWSecDot11EssFtReassocTime = _CLWSecDot11EssFtReassocTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 11),
    _CLWSecDot11EssFtReassocTime_Type()
)
cLWSecDot11EssFtReassocTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtReassocTime.setStatus("current")
_CLWSecDot11EssFtOverDs_Type = TruthValue
_CLWSecDot11EssFtOverDs_Object = MibTableColumn
cLWSecDot11EssFtOverDs = _CLWSecDot11EssFtOverDs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 12),
    _CLWSecDot11EssFtOverDs_Type()
)
cLWSecDot11EssFtOverDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtOverDs.setStatus("current")


class _CLWSecDot11Ess11wPfm_Type(Integer32):
    """Custom type cLWSecDot11Ess11wPfm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("optional", 1),
          ("required", 2))
    )


_CLWSecDot11Ess11wPfm_Type.__name__ = "Integer32"
_CLWSecDot11Ess11wPfm_Object = MibTableColumn
cLWSecDot11Ess11wPfm = _CLWSecDot11Ess11wPfm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 13),
    _CLWSecDot11Ess11wPfm_Type()
)
cLWSecDot11Ess11wPfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11Ess11wPfm.setStatus("current")
_CLWSecDot11EssRetryTime_Type = Unsigned32
_CLWSecDot11EssRetryTime_Object = MibTableColumn
cLWSecDot11EssRetryTime = _CLWSecDot11EssRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 14),
    _CLWSecDot11EssRetryTime_Type()
)
cLWSecDot11EssRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssRetryTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWSecDot11EssRetryTime.setUnits("milliseconds")
_CLWSecDot11EssComebackTime_Type = Unsigned32
_CLWSecDot11EssComebackTime_Object = MibTableColumn
cLWSecDot11EssComebackTime = _CLWSecDot11EssComebackTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 15),
    _CLWSecDot11EssComebackTime_Type()
)
cLWSecDot11EssComebackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssComebackTime.setStatus("current")


class _CLWSecDot11EssFtMode_Type(Integer32):
    """Custom type cLWSecDot11EssFtMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("adaptive", 2))
    )


_CLWSecDot11EssFtMode_Type.__name__ = "Integer32"
_CLWSecDot11EssFtMode_Object = MibTableColumn
cLWSecDot11EssFtMode = _CLWSecDot11EssFtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 16),
    _CLWSecDot11EssFtMode_Type()
)
cLWSecDot11EssFtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssFtMode.setStatus("current")


class _CLWSecDot11EssWpa3Security_Type(TruthValue):
    """Custom type cLWSecDot11EssWpa3Security based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssWpa3Security_Type.__name__ = "TruthValue"
_CLWSecDot11EssWpa3Security_Object = MibTableColumn
cLWSecDot11EssWpa3Security = _CLWSecDot11EssWpa3Security_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 17),
    _CLWSecDot11EssWpa3Security_Type()
)
cLWSecDot11EssWpa3Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWpa3Security.setStatus("current")
_CLWSecDot11EssMPskEnable_Type = TruthValue
_CLWSecDot11EssMPskEnable_Object = MibTableColumn
cLWSecDot11EssMPskEnable = _CLWSecDot11EssMPskEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 18),
    _CLWSecDot11EssMPskEnable_Type()
)
cLWSecDot11EssMPskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssMPskEnable.setStatus("current")


class _CLWSecDot11EssSaeAntiClogThreshold_Type(Unsigned32):
    """Custom type cLWSecDot11EssSaeAntiClogThreshold based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_CLWSecDot11EssSaeAntiClogThreshold_Type.__name__ = "Unsigned32"
_CLWSecDot11EssSaeAntiClogThreshold_Object = MibTableColumn
cLWSecDot11EssSaeAntiClogThreshold = _CLWSecDot11EssSaeAntiClogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 19),
    _CLWSecDot11EssSaeAntiClogThreshold_Type()
)
cLWSecDot11EssSaeAntiClogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssSaeAntiClogThreshold.setStatus("current")


class _CLWSecDot11EssSaeRetransTimeout_Type(Unsigned32):
    """Custom type cLWSecDot11EssSaeRetransTimeout based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CLWSecDot11EssSaeRetransTimeout_Type.__name__ = "Unsigned32"
_CLWSecDot11EssSaeRetransTimeout_Object = MibTableColumn
cLWSecDot11EssSaeRetransTimeout = _CLWSecDot11EssSaeRetransTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 20),
    _CLWSecDot11EssSaeRetransTimeout_Type()
)
cLWSecDot11EssSaeRetransTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssSaeRetransTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLWSecDot11EssSaeRetransTimeout.setUnits("milliseconds")


class _CLWSecDot11EssSaeMaxRetry_Type(Integer32):
    """Custom type cLWSecDot11EssSaeMaxRetry based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLWSecDot11EssSaeMaxRetry_Type.__name__ = "Integer32"
_CLWSecDot11EssSaeMaxRetry_Object = MibTableColumn
cLWSecDot11EssSaeMaxRetry = _CLWSecDot11EssSaeMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 21),
    _CLWSecDot11EssSaeMaxRetry_Type()
)
cLWSecDot11EssSaeMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssSaeMaxRetry.setStatus("current")
_CLWSecDot11OsenEnable_Type = TruthValue
_CLWSecDot11OsenEnable_Object = MibTableColumn
cLWSecDot11OsenEnable = _CLWSecDot11OsenEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 22),
    _CLWSecDot11OsenEnable_Type()
)
cLWSecDot11OsenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11OsenEnable.setStatus("current")


class _CLWSecDot11TMWlanId_Type(Unsigned32):
    """Custom type cLWSecDot11TMWlanId based on Unsigned32"""
    defaultValue = 0


_CLWSecDot11TMWlanId_Type.__name__ = "Unsigned32"
_CLWSecDot11TMWlanId_Object = MibTableColumn
cLWSecDot11TMWlanId = _CLWSecDot11TMWlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 23),
    _CLWSecDot11TMWlanId_Type()
)
cLWSecDot11TMWlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11TMWlanId.setStatus("current")


class _CLWSecDot11EssWpa3EncType_Type(Bits):
    """Custom type cLWSecDot11EssWpa3EncType based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("aes", 0),
          ("ccmp256", 1),
          ("gcmp128", 2),
          ("gcmp256", 3))
    )

_CLWSecDot11EssWpa3EncType_Type.__name__ = "Bits"
_CLWSecDot11EssWpa3EncType_Object = MibTableColumn
cLWSecDot11EssWpa3EncType = _CLWSecDot11EssWpa3EncType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 24),
    _CLWSecDot11EssWpa3EncType_Type()
)
cLWSecDot11EssWpa3EncType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWpa3EncType.setStatus("current")


class _CLWSecDot11EssPskType_Type(Integer32):
    """Custom type cLWSecDot11EssPskType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("aes", 1))
    )


_CLWSecDot11EssPskType_Type.__name__ = "Integer32"
_CLWSecDot11EssPskType_Object = MibTableColumn
cLWSecDot11EssPskType = _CLWSecDot11EssPskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 25),
    _CLWSecDot11EssPskType_Type()
)
cLWSecDot11EssPskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssPskType.setStatus("current")


class _CLWSecDot11EssEasyPskEnable_Type(TruthValue):
    """Custom type cLWSecDot11EssEasyPskEnable based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssEasyPskEnable_Type.__name__ = "TruthValue"
_CLWSecDot11EssEasyPskEnable_Object = MibTableColumn
cLWSecDot11EssEasyPskEnable = _CLWSecDot11EssEasyPskEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 26),
    _CLWSecDot11EssEasyPskEnable_Type()
)
cLWSecDot11EssEasyPskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssEasyPskEnable.setStatus("current")


class _CLWSecDot11EssSaePweMode_Type(Integer32):
    """Custom type cLWSecDot11EssSaePweMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hnp", 0),
          ("h2e", 1),
          ("h2e-hnp", 2))
    )


_CLWSecDot11EssSaePweMode_Type.__name__ = "Integer32"
_CLWSecDot11EssSaePweMode_Object = MibTableColumn
cLWSecDot11EssSaePweMode = _CLWSecDot11EssSaePweMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 27),
    _CLWSecDot11EssSaePweMode_Type()
)
cLWSecDot11EssSaePweMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssSaePweMode.setStatus("current")


class _CLWSecDot11TransitionDisable_Type(TruthValue):
    """Custom type cLWSecDot11TransitionDisable based on TruthValue"""
    defaultValue = 2


_CLWSecDot11TransitionDisable_Type.__name__ = "TruthValue"
_CLWSecDot11TransitionDisable_Object = MibTableColumn
cLWSecDot11TransitionDisable = _CLWSecDot11TransitionDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 28),
    _CLWSecDot11TransitionDisable_Type()
)
cLWSecDot11TransitionDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11TransitionDisable.setStatus("current")


class _CLWSecDot11BeaconProtectionEnable_Type(TruthValue):
    """Custom type cLWSecDot11BeaconProtectionEnable based on TruthValue"""
    defaultValue = 2


_CLWSecDot11BeaconProtectionEnable_Type.__name__ = "TruthValue"
_CLWSecDot11BeaconProtectionEnable_Object = MibTableColumn
cLWSecDot11BeaconProtectionEnable = _CLWSecDot11BeaconProtectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 1, 1, 29),
    _CLWSecDot11BeaconProtectionEnable_Type()
)
cLWSecDot11BeaconProtectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11BeaconProtectionEnable.setStatus("current")
_CLWSecDot11EssCkipTable_Object = MibTable
cLWSecDot11EssCkipTable = _CLWSecDot11EssCkipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipTable.setStatus("current")
_CLWSecDot11EssCkipEntry_Object = MibTableRow
cLWSecDot11EssCkipEntry = _CLWSecDot11EssCkipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1)
)
cLWSecDot11EssCkipEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipEntry.setStatus("current")


class _CLWSecDot11EssCkipSecurity_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipSecurity based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCkipSecurity_Type.__name__ = "TruthValue"
_CLWSecDot11EssCkipSecurity_Object = MibTableColumn
cLWSecDot11EssCkipSecurity = _CLWSecDot11EssCkipSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 1),
    _CLWSecDot11EssCkipSecurity_Type()
)
cLWSecDot11EssCkipSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipSecurity.setStatus("current")


class _CLWSecDot11EssCkipKeyIndex_Type(Unsigned32):
    """Custom type cLWSecDot11EssCkipKeyIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CLWSecDot11EssCkipKeyIndex_Type.__name__ = "Unsigned32"
_CLWSecDot11EssCkipKeyIndex_Object = MibTableColumn
cLWSecDot11EssCkipKeyIndex = _CLWSecDot11EssCkipKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 2),
    _CLWSecDot11EssCkipKeyIndex_Type()
)
cLWSecDot11EssCkipKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyIndex.setStatus("current")


class _CLWSecDot11EssCkipKeyLength_Type(Integer32):
    """Custom type cLWSecDot11EssCkipKeyLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("len40", 2),
          ("len104", 3))
    )


_CLWSecDot11EssCkipKeyLength_Type.__name__ = "Integer32"
_CLWSecDot11EssCkipKeyLength_Object = MibTableColumn
cLWSecDot11EssCkipKeyLength = _CLWSecDot11EssCkipKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 3),
    _CLWSecDot11EssCkipKeyLength_Type()
)
cLWSecDot11EssCkipKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyLength.setStatus("current")


class _CLWSecDot11EssCkipKeyFmt_Type(CLSecKeyFormat):
    """Custom type cLWSecDot11EssCkipKeyFmt based on CLSecKeyFormat"""
    defaultValue = 1


_CLWSecDot11EssCkipKeyFmt_Type.__name__ = "CLSecKeyFormat"
_CLWSecDot11EssCkipKeyFmt_Object = MibTableColumn
cLWSecDot11EssCkipKeyFmt = _CLWSecDot11EssCkipKeyFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 4),
    _CLWSecDot11EssCkipKeyFmt_Type()
)
cLWSecDot11EssCkipKeyFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKeyFmt.setStatus("current")


class _CLWSecDot11EssCkipKey_Type(OctetString):
    """Custom type cLWSecDot11EssCkipKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 26),
    )


_CLWSecDot11EssCkipKey_Type.__name__ = "OctetString"
_CLWSecDot11EssCkipKey_Object = MibTableColumn
cLWSecDot11EssCkipKey = _CLWSecDot11EssCkipKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 5),
    _CLWSecDot11EssCkipKey_Type()
)
cLWSecDot11EssCkipKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKey.setStatus("current")


class _CLWSecDot11EssCkipMMHMode_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipMMHMode based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCkipMMHMode_Type.__name__ = "TruthValue"
_CLWSecDot11EssCkipMMHMode_Object = MibTableColumn
cLWSecDot11EssCkipMMHMode = _CLWSecDot11EssCkipMMHMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 6),
    _CLWSecDot11EssCkipMMHMode_Type()
)
cLWSecDot11EssCkipMMHMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipMMHMode.setStatus("current")


class _CLWSecDot11EssCkipKPEnable_Type(TruthValue):
    """Custom type cLWSecDot11EssCkipKPEnable based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssCkipKPEnable_Type.__name__ = "TruthValue"
_CLWSecDot11EssCkipKPEnable_Object = MibTableColumn
cLWSecDot11EssCkipKPEnable = _CLWSecDot11EssCkipKPEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 2, 1, 7),
    _CLWSecDot11EssCkipKPEnable_Type()
)
cLWSecDot11EssCkipKPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssCkipKPEnable.setStatus("current")
_CLWSecMPskKeysTable_Object = MibTable
cLWSecMPskKeysTable = _CLWSecMPskKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cLWSecMPskKeysTable.setStatus("current")
_CLWSecMPskKeysEntry_Object = MibTableRow
cLWSecMPskKeysEntry = _CLWSecMPskKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5, 1)
)
cLWSecMPskKeysEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecMPskPriority"),
)
if mibBuilder.loadTexts:
    cLWSecMPskKeysEntry.setStatus("current")


class _CLWSecMPskPriority_Type(Unsigned32):
    """Custom type cLWSecMPskPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CLWSecMPskPriority_Type.__name__ = "Unsigned32"
_CLWSecMPskPriority_Object = MibTableColumn
cLWSecMPskPriority = _CLWSecMPskPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5, 1, 1),
    _CLWSecMPskPriority_Type()
)
cLWSecMPskPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWSecMPskPriority.setStatus("current")
_CLWSecMPskRowStatus_Type = RowStatus
_CLWSecMPskRowStatus_Object = MibTableColumn
cLWSecMPskRowStatus = _CLWSecMPskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5, 1, 2),
    _CLWSecMPskRowStatus_Type()
)
cLWSecMPskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWSecMPskRowStatus.setStatus("current")
_CLWSecMPskKeyFormat_Type = CLSecKeyFormat
_CLWSecMPskKeyFormat_Object = MibTableColumn
cLWSecMPskKeyFormat = _CLWSecMPskKeyFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5, 1, 3),
    _CLWSecMPskKeyFormat_Type()
)
cLWSecMPskKeyFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWSecMPskKeyFormat.setStatus("current")


class _CLWSecMPskKey_Type(OctetString):
    """Custom type cLWSecMPskKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_CLWSecMPskKey_Type.__name__ = "OctetString"
_CLWSecMPskKey_Object = MibTableColumn
cLWSecMPskKey = _CLWSecMPskKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 1, 5, 1, 4),
    _CLWSecMPskKey_Type()
)
cLWSecMPskKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLWSecMPskKey.setStatus("current")
_ClwsCkipConfig_ObjectIdentity = ObjectIdentity
clwsCkipConfig = _ClwsCkipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 2)
)
_ClwsWebPolicyConfig_ObjectIdentity = ObjectIdentity
clwsWebPolicyConfig = _ClwsWebPolicyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3)
)
_CLWSecDot11EssWebPolicyTable_Object = MibTable
cLWSecDot11EssWebPolicyTable = _CLWSecDot11EssWebPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyTable.setStatus("current")
_CLWSecDot11EssWebPolicyEntry_Object = MibTableRow
cLWSecDot11EssWebPolicyEntry = _CLWSecDot11EssWebPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1)
)
cLWSecDot11EssWebPolicyEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyEntry.setStatus("current")


class _CLWSecDot11EssWebPolicyCondRedirect_Type(TruthValue):
    """Custom type cLWSecDot11EssWebPolicyCondRedirect based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssWebPolicyCondRedirect_Type.__name__ = "TruthValue"
_CLWSecDot11EssWebPolicyCondRedirect_Object = MibTableColumn
cLWSecDot11EssWebPolicyCondRedirect = _CLWSecDot11EssWebPolicyCondRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 1),
    _CLWSecDot11EssWebPolicyCondRedirect_Type()
)
cLWSecDot11EssWebPolicyCondRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicyCondRedirect.setStatus("current")


class _CLWSecDot11EssWebPolicySplashPageWebRedirect_Type(TruthValue):
    """Custom type cLWSecDot11EssWebPolicySplashPageWebRedirect based on TruthValue"""
    defaultValue = 2


_CLWSecDot11EssWebPolicySplashPageWebRedirect_Type.__name__ = "TruthValue"
_CLWSecDot11EssWebPolicySplashPageWebRedirect_Object = MibTableColumn
cLWSecDot11EssWebPolicySplashPageWebRedirect = _CLWSecDot11EssWebPolicySplashPageWebRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 3, 1, 1, 2),
    _CLWSecDot11EssWebPolicySplashPageWebRedirect_Type()
)
cLWSecDot11EssWebPolicySplashPageWebRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecDot11EssWebPolicySplashPageWebRedirect.setStatus("current")
_ClwsAaaConfig_ObjectIdentity = ObjectIdentity
clwsAaaConfig = _ClwsAaaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4)
)


class _CLWSecAaaRadiusAuthCallStationIdType_Type(Integer32):
    """Custom type cLWSecAaaRadiusAuthCallStationIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("ipAddr", 1),
          ("macAddr", 2),
          ("apMacAddress", 3),
          ("apMacAddressSsid", 4),
          ("apNameSsid", 5),
          ("apName", 6),
          ("apGroupName", 7),
          ("apLocation", 8),
          ("apVlanId", 9),
          ("apMacEthAddress", 10),
          ("apMacEthAddressSsid", 11),
          ("apLabelAddress", 12),
          ("apLabelAddressSsid", 13))
    )


_CLWSecAaaRadiusAuthCallStationIdType_Type.__name__ = "Integer32"
_CLWSecAaaRadiusAuthCallStationIdType_Object = MibScalar
cLWSecAaaRadiusAuthCallStationIdType = _CLWSecAaaRadiusAuthCallStationIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 1),
    _CLWSecAaaRadiusAuthCallStationIdType_Type()
)
cLWSecAaaRadiusAuthCallStationIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecAaaRadiusAuthCallStationIdType.setStatus("current")


class _CLWSecAaaRadiusAccUsernameDelimiter_Type(Integer32):
    """Custom type cLWSecAaaRadiusAccUsernameDelimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noDelimiter", 1),
          ("hyphen", 2),
          ("colon", 3),
          ("singleHyphen", 4))
    )


_CLWSecAaaRadiusAccUsernameDelimiter_Type.__name__ = "Integer32"
_CLWSecAaaRadiusAccUsernameDelimiter_Object = MibScalar
cLWSecAaaRadiusAccUsernameDelimiter = _CLWSecAaaRadiusAccUsernameDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 4, 2),
    _CLWSecAaaRadiusAccUsernameDelimiter_Type()
)
cLWSecAaaRadiusAccUsernameDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWSecAaaRadiusAccUsernameDelimiter.setStatus("current")
_ClwsMpskConfig_ObjectIdentity = ObjectIdentity
clwsMpskConfig = _ClwsMpskConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 1, 5)
)
_CiscoLwappWlanSecurityMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBConform = _CiscoLwappWlanSecurityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2)
)
_CiscoLwappWlanSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBCompliances = _CiscoLwappWlanSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1)
)
_CiscoLwappWlanSecurityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappWlanSecurityMIBGroups = _CiscoLwappWlanSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2)
)

# Managed Objects groups

ciscoLwappWlanSecurityCckmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 1)
)
ciscoLwappWlanSecurityCckmConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpaSupport"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1Security"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa1EncType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2Security"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmWpa2EncType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmKeyMgmtMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPskFmt"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPsk"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCckmConfigGroup.setStatus("current")

ciscoLwappWlanSecurityCkipConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 2)
)
ciscoLwappWlanSecurityCkipConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipSecurity"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyIndex"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyLength"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKeyFmt"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKey"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipMMHMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCkipKPEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCkipConfigGroup.setStatus("current")

ciscoLwappWlanSecurityWebPolicyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 3)
)
ciscoLwappWlanSecurityWebPolicyConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicyCondRedirect"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWebPolicySplashPageWebRedirect"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityWebPolicyConfigGroup.setStatus("current")

ciscoLwappWlanSecurityAaaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 4)
)
ciscoLwappWlanSecurityAaaConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAuthCallStationIdType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecAaaRadiusAccUsernameDelimiter"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityAaaConfigGroup.setStatus("current")

ciscoLwappWlanSecurityFtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 5)
)
ciscoLwappWlanSecurityFtConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtEnable"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtReassocTime"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssFtOverDs"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityFtConfigGroup.setStatus("current")

ciscoLwappWlanSecurityPfmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 6)
)
ciscoLwappWlanSecurityPfmConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11Ess11wPfm"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssRetryTime"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssComebackTime"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityPfmConfigGroup.setStatus("current")

ciscoLwappWlanSecurityCckmConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 7)
)
ciscoLwappWlanSecurityCckmConfigGroup1.setObjects(
    ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssCckmGtkRandomize")
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCckmConfigGroup1.setStatus("current")

ciscoLwappWlanSecurityCckmConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 8)
)
ciscoLwappWlanSecurityCckmConfigGroup2.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssMPskEnable"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecMPskRowStatus"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecMPskKey"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecMPskKeyFormat"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityCckmConfigGroup2.setStatus("current")

ciscoLwappWlanSecurityWPA3ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 9)
)
ciscoLwappWlanSecurityWPA3ConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWpa3Security"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssSaeAntiClogThreshold"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssSaeRetransTimeout"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssSaeMaxRetry"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11TMWlanId"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssWpa3EncType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11OsenEnable"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssSaePweMode"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11TransitionDisable"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11BeaconProtectionEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityWPA3ConfigGroup.setStatus("current")

ciscoLwappWlanSecurityEasyPskConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 2, 10)
)
ciscoLwappWlanSecurityEasyPskConfigGroup.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssPskType"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "cLWSecDot11EssEasyPskEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityEasyPskConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappWlanSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 1)
)
ciscoLwappWlanSecurityMIBCompliance.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 2)
)
ciscoLwappWlanSecurityMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 3)
)
ciscoLwappWlanSecurityMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityAaaConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityFtConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityPfmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 4)
)
ciscoLwappWlanSecurityMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityAaaConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityFtConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityPfmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup1"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup2"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWPA3ConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappWlanSecurityMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 521, 2, 1, 5)
)
ciscoLwappWlanSecurityMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCkipConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWebPolicyConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityEasyPskConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityAaaConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityFtConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityPfmConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup1"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityCckmConfigGroup2"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityWPA3ConfigGroup"),
        ("CISCO-LWAPP-WLAN-SECURITY-MIB", "ciscoLwappWlanSecurityEasyPskConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappWlanSecurityMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WLAN-SECURITY-MIB",
    **{"ciscoLwappWlanSecurityMIB": ciscoLwappWlanSecurityMIB,
       "ciscoLwappWlanSecurityMIBNotifs": ciscoLwappWlanSecurityMIBNotifs,
       "ciscoLwappWlanSecurityMIBObjects": ciscoLwappWlanSecurityMIBObjects,
       "clwsCckmConfig": clwsCckmConfig,
       "cLWSecDot11EssCckmTable": cLWSecDot11EssCckmTable,
       "cLWSecDot11EssCckmEntry": cLWSecDot11EssCckmEntry,
       "cLWSecDot11EssCckmWpaSupport": cLWSecDot11EssCckmWpaSupport,
       "cLWSecDot11EssCckmWpa1Security": cLWSecDot11EssCckmWpa1Security,
       "cLWSecDot11EssCckmWpa1EncType": cLWSecDot11EssCckmWpa1EncType,
       "cLWSecDot11EssCckmWpa2Security": cLWSecDot11EssCckmWpa2Security,
       "cLWSecDot11EssCckmWpa2EncType": cLWSecDot11EssCckmWpa2EncType,
       "cLWSecDot11EssCckmKeyMgmtMode": cLWSecDot11EssCckmKeyMgmtMode,
       "cLWSecDot11EssPskFmt": cLWSecDot11EssPskFmt,
       "cLWSecDot11EssPsk": cLWSecDot11EssPsk,
       "cLWSecDot11EssCckmGtkRandomize": cLWSecDot11EssCckmGtkRandomize,
       "cLWSecDot11EssFtEnable": cLWSecDot11EssFtEnable,
       "cLWSecDot11EssFtReassocTime": cLWSecDot11EssFtReassocTime,
       "cLWSecDot11EssFtOverDs": cLWSecDot11EssFtOverDs,
       "cLWSecDot11Ess11wPfm": cLWSecDot11Ess11wPfm,
       "cLWSecDot11EssRetryTime": cLWSecDot11EssRetryTime,
       "cLWSecDot11EssComebackTime": cLWSecDot11EssComebackTime,
       "cLWSecDot11EssFtMode": cLWSecDot11EssFtMode,
       "cLWSecDot11EssWpa3Security": cLWSecDot11EssWpa3Security,
       "cLWSecDot11EssMPskEnable": cLWSecDot11EssMPskEnable,
       "cLWSecDot11EssSaeAntiClogThreshold": cLWSecDot11EssSaeAntiClogThreshold,
       "cLWSecDot11EssSaeRetransTimeout": cLWSecDot11EssSaeRetransTimeout,
       "cLWSecDot11EssSaeMaxRetry": cLWSecDot11EssSaeMaxRetry,
       "cLWSecDot11OsenEnable": cLWSecDot11OsenEnable,
       "cLWSecDot11TMWlanId": cLWSecDot11TMWlanId,
       "cLWSecDot11EssWpa3EncType": cLWSecDot11EssWpa3EncType,
       "cLWSecDot11EssPskType": cLWSecDot11EssPskType,
       "cLWSecDot11EssEasyPskEnable": cLWSecDot11EssEasyPskEnable,
       "cLWSecDot11EssSaePweMode": cLWSecDot11EssSaePweMode,
       "cLWSecDot11TransitionDisable": cLWSecDot11TransitionDisable,
       "cLWSecDot11BeaconProtectionEnable": cLWSecDot11BeaconProtectionEnable,
       "cLWSecDot11EssCkipTable": cLWSecDot11EssCkipTable,
       "cLWSecDot11EssCkipEntry": cLWSecDot11EssCkipEntry,
       "cLWSecDot11EssCkipSecurity": cLWSecDot11EssCkipSecurity,
       "cLWSecDot11EssCkipKeyIndex": cLWSecDot11EssCkipKeyIndex,
       "cLWSecDot11EssCkipKeyLength": cLWSecDot11EssCkipKeyLength,
       "cLWSecDot11EssCkipKeyFmt": cLWSecDot11EssCkipKeyFmt,
       "cLWSecDot11EssCkipKey": cLWSecDot11EssCkipKey,
       "cLWSecDot11EssCkipMMHMode": cLWSecDot11EssCkipMMHMode,
       "cLWSecDot11EssCkipKPEnable": cLWSecDot11EssCkipKPEnable,
       "cLWSecMPskKeysTable": cLWSecMPskKeysTable,
       "cLWSecMPskKeysEntry": cLWSecMPskKeysEntry,
       "cLWSecMPskPriority": cLWSecMPskPriority,
       "cLWSecMPskRowStatus": cLWSecMPskRowStatus,
       "cLWSecMPskKeyFormat": cLWSecMPskKeyFormat,
       "cLWSecMPskKey": cLWSecMPskKey,
       "clwsCkipConfig": clwsCkipConfig,
       "clwsWebPolicyConfig": clwsWebPolicyConfig,
       "cLWSecDot11EssWebPolicyTable": cLWSecDot11EssWebPolicyTable,
       "cLWSecDot11EssWebPolicyEntry": cLWSecDot11EssWebPolicyEntry,
       "cLWSecDot11EssWebPolicyCondRedirect": cLWSecDot11EssWebPolicyCondRedirect,
       "cLWSecDot11EssWebPolicySplashPageWebRedirect": cLWSecDot11EssWebPolicySplashPageWebRedirect,
       "clwsAaaConfig": clwsAaaConfig,
       "cLWSecAaaRadiusAuthCallStationIdType": cLWSecAaaRadiusAuthCallStationIdType,
       "cLWSecAaaRadiusAccUsernameDelimiter": cLWSecAaaRadiusAccUsernameDelimiter,
       "clwsMpskConfig": clwsMpskConfig,
       "ciscoLwappWlanSecurityMIBConform": ciscoLwappWlanSecurityMIBConform,
       "ciscoLwappWlanSecurityMIBCompliances": ciscoLwappWlanSecurityMIBCompliances,
       "ciscoLwappWlanSecurityMIBCompliance": ciscoLwappWlanSecurityMIBCompliance,
       "ciscoLwappWlanSecurityMIBComplianceRev1": ciscoLwappWlanSecurityMIBComplianceRev1,
       "ciscoLwappWlanSecurityMIBComplianceRev2": ciscoLwappWlanSecurityMIBComplianceRev2,
       "ciscoLwappWlanSecurityMIBComplianceRev3": ciscoLwappWlanSecurityMIBComplianceRev3,
       "ciscoLwappWlanSecurityMIBComplianceRev4": ciscoLwappWlanSecurityMIBComplianceRev4,
       "ciscoLwappWlanSecurityMIBGroups": ciscoLwappWlanSecurityMIBGroups,
       "ciscoLwappWlanSecurityCckmConfigGroup": ciscoLwappWlanSecurityCckmConfigGroup,
       "ciscoLwappWlanSecurityCkipConfigGroup": ciscoLwappWlanSecurityCkipConfigGroup,
       "ciscoLwappWlanSecurityWebPolicyConfigGroup": ciscoLwappWlanSecurityWebPolicyConfigGroup,
       "ciscoLwappWlanSecurityAaaConfigGroup": ciscoLwappWlanSecurityAaaConfigGroup,
       "ciscoLwappWlanSecurityFtConfigGroup": ciscoLwappWlanSecurityFtConfigGroup,
       "ciscoLwappWlanSecurityPfmConfigGroup": ciscoLwappWlanSecurityPfmConfigGroup,
       "ciscoLwappWlanSecurityCckmConfigGroup1": ciscoLwappWlanSecurityCckmConfigGroup1,
       "ciscoLwappWlanSecurityCckmConfigGroup2": ciscoLwappWlanSecurityCckmConfigGroup2,
       "ciscoLwappWlanSecurityWPA3ConfigGroup": ciscoLwappWlanSecurityWPA3ConfigGroup,
       "ciscoLwappWlanSecurityEasyPskConfigGroup": ciscoLwappWlanSecurityEasyPskConfigGroup}
)
