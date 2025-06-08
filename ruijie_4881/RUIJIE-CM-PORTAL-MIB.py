# SNMP MIB module (RUIJIE-CM-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CM-PORTAL-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieCMPortalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74)
)
if mibBuilder.loadTexts:
    ruijieCMPortalMIB.setRevisions(
        ("2010-03-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCMPortalMIBTrap_ObjectIdentity = ObjectIdentity
ruijieCMPortalMIBTrap = _RuijieCMPortalMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 0)
)
_RuijieCMPortalMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCMPortalMIBObjects = _RuijieCMPortalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1)
)
_RuijieCMPortalMaxAuthNum_Type = Integer32
_RuijieCMPortalMaxAuthNum_Object = MibScalar
ruijieCMPortalMaxAuthNum = _RuijieCMPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 1),
    _RuijieCMPortalMaxAuthNum_Type()
)
ruijieCMPortalMaxAuthNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalMaxAuthNum.setStatus("current")
_RuijieCMPortalCurAuthNum_Type = Integer32
_RuijieCMPortalCurAuthNum_Object = MibScalar
ruijieCMPortalCurAuthNum = _RuijieCMPortalCurAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 2),
    _RuijieCMPortalCurAuthNum_Type()
)
ruijieCMPortalCurAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalCurAuthNum.setStatus("current")
_RuijieCMPortalServerInetAddressType_Type = InetAddressType
_RuijieCMPortalServerInetAddressType_Object = MibScalar
ruijieCMPortalServerInetAddressType = _RuijieCMPortalServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 3),
    _RuijieCMPortalServerInetAddressType_Type()
)
ruijieCMPortalServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerInetAddressType.setStatus("current")
_RuijieCMPortalServerInetAddress_Type = InetAddress
_RuijieCMPortalServerInetAddress_Object = MibScalar
ruijieCMPortalServerInetAddress = _RuijieCMPortalServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 4),
    _RuijieCMPortalServerInetAddress_Type()
)
ruijieCMPortalServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerInetAddress.setStatus("current")
_RuijieCMPortalServerInetPortNumber_Type = Integer32
_RuijieCMPortalServerInetPortNumber_Object = MibScalar
ruijieCMPortalServerInetPortNumber = _RuijieCMPortalServerInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 5),
    _RuijieCMPortalServerInetPortNumber_Type()
)
ruijieCMPortalServerInetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerInetPortNumber.setStatus("current")


class _RuijieCMPortalServerUnavailableCode_Type(Integer32):
    """Custom type ruijieCMPortalServerUnavailableCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-configured", 0),
          ("ping-failed", 1))
    )


_RuijieCMPortalServerUnavailableCode_Type.__name__ = "Integer32"
_RuijieCMPortalServerUnavailableCode_Object = MibScalar
ruijieCMPortalServerUnavailableCode = _RuijieCMPortalServerUnavailableCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 6),
    _RuijieCMPortalServerUnavailableCode_Type()
)
ruijieCMPortalServerUnavailableCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalServerUnavailableCode.setStatus("current")
_RuijieCMPortalAuthReqCount_Type = Counter32
_RuijieCMPortalAuthReqCount_Object = MibScalar
ruijieCMPortalAuthReqCount = _RuijieCMPortalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 7),
    _RuijieCMPortalAuthReqCount_Type()
)
ruijieCMPortalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthReqCount.setStatus("current")
_RuijieCMPortalAuthRespCount_Type = Counter32
_RuijieCMPortalAuthRespCount_Object = MibScalar
ruijieCMPortalAuthRespCount = _RuijieCMPortalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 8),
    _RuijieCMPortalAuthRespCount_Type()
)
ruijieCMPortalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthRespCount.setStatus("current")
_RuijieCMPortalChallengeReqCount_Type = Counter32
_RuijieCMPortalChallengeReqCount_Object = MibScalar
ruijieCMPortalChallengeReqCount = _RuijieCMPortalChallengeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 9),
    _RuijieCMPortalChallengeReqCount_Type()
)
ruijieCMPortalChallengeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalChallengeReqCount.setStatus("current")
_RuijieCMPortalChallengeRespCount_Type = Counter32
_RuijieCMPortalChallengeRespCount_Object = MibScalar
ruijieCMPortalChallengeRespCount = _RuijieCMPortalChallengeRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 10),
    _RuijieCMPortalChallengeRespCount_Type()
)
ruijieCMPortalChallengeRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalChallengeRespCount.setStatus("current")


class _RuijieCMPortalGlobalServerURL_Type(DisplayString):
    """Custom type ruijieCMPortalGlobalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCMPortalGlobalServerURL_Type.__name__ = "DisplayString"
_RuijieCMPortalGlobalServerURL_Object = MibScalar
ruijieCMPortalGlobalServerURL = _RuijieCMPortalGlobalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 11),
    _RuijieCMPortalGlobalServerURL_Type()
)
ruijieCMPortalGlobalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalGlobalServerURL.setStatus("current")
_RuijieCMPortalServerURLTable_Object = MibTable
ruijieCMPortalServerURLTable = _RuijieCMPortalServerURLTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieCMPortalServerURLTable.setStatus("current")
_RuijieCMPortalServerURLEntry_Object = MibTableRow
ruijieCMPortalServerURLEntry = _RuijieCMPortalServerURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1)
)
ruijieCMPortalServerURLEntry.setIndexNames(
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerURLId"),
)
if mibBuilder.loadTexts:
    ruijieCMPortalServerURLEntry.setStatus("current")
_RuijieCMPortalServerURLId_Type = Unsigned32
_RuijieCMPortalServerURLId_Object = MibTableColumn
ruijieCMPortalServerURLId = _RuijieCMPortalServerURLId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1, 1),
    _RuijieCMPortalServerURLId_Type()
)
ruijieCMPortalServerURLId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalServerURLId.setStatus("current")


class _RuijieCMPortalServerURL_Type(DisplayString):
    """Custom type ruijieCMPortalServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieCMPortalServerURL_Type.__name__ = "DisplayString"
_RuijieCMPortalServerURL_Object = MibTableColumn
ruijieCMPortalServerURL = _RuijieCMPortalServerURL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1, 2),
    _RuijieCMPortalServerURL_Type()
)
ruijieCMPortalServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerURL.setStatus("current")


class _RuijieCMPortalServerName_Type(DisplayString):
    """Custom type ruijieCMPortalServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieCMPortalServerName_Type.__name__ = "DisplayString"
_RuijieCMPortalServerName_Object = MibTableColumn
ruijieCMPortalServerName = _RuijieCMPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1, 3),
    _RuijieCMPortalServerName_Type()
)
ruijieCMPortalServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerName.setStatus("current")
_RuijieCMPortalServerInUsedCount_Type = Unsigned32
_RuijieCMPortalServerInUsedCount_Object = MibTableColumn
ruijieCMPortalServerInUsedCount = _RuijieCMPortalServerInUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1, 4),
    _RuijieCMPortalServerInUsedCount_Type()
)
ruijieCMPortalServerInUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalServerInUsedCount.setStatus("current")
_RuijieCMPortalServerConfigStatus_Type = RowStatus
_RuijieCMPortalServerConfigStatus_Object = MibTableColumn
ruijieCMPortalServerConfigStatus = _RuijieCMPortalServerConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 12, 1, 5),
    _RuijieCMPortalServerConfigStatus_Type()
)
ruijieCMPortalServerConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieCMPortalServerConfigStatus.setStatus("current")
_RuijieCMPortalHttpReqCount_Type = Counter32
_RuijieCMPortalHttpReqCount_Object = MibScalar
ruijieCMPortalHttpReqCount = _RuijieCMPortalHttpReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 13),
    _RuijieCMPortalHttpReqCount_Type()
)
ruijieCMPortalHttpReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalHttpReqCount.setStatus("current")
_RuijieCMPortalHttpRespCount_Type = Counter32
_RuijieCMPortalHttpRespCount_Object = MibScalar
ruijieCMPortalHttpRespCount = _RuijieCMPortalHttpRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 14),
    _RuijieCMPortalHttpRespCount_Type()
)
ruijieCMPortalHttpRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalHttpRespCount.setStatus("current")
_RuijieCMPortalExceptionFailCount_Type = Counter32
_RuijieCMPortalExceptionFailCount_Object = MibScalar
ruijieCMPortalExceptionFailCount = _RuijieCMPortalExceptionFailCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 15),
    _RuijieCMPortalExceptionFailCount_Type()
)
ruijieCMPortalExceptionFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalExceptionFailCount.setStatus("current")
_RuijieCMPortalAuthSuccessedCount_Type = Counter32
_RuijieCMPortalAuthSuccessedCount_Object = MibScalar
ruijieCMPortalAuthSuccessedCount = _RuijieCMPortalAuthSuccessedCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 16),
    _RuijieCMPortalAuthSuccessedCount_Type()
)
ruijieCMPortalAuthSuccessedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthSuccessedCount.setStatus("current")
_RuijieCMPortalNormalAuthReqCount_Type = Counter32
_RuijieCMPortalNormalAuthReqCount_Object = MibScalar
ruijieCMPortalNormalAuthReqCount = _RuijieCMPortalNormalAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 17),
    _RuijieCMPortalNormalAuthReqCount_Type()
)
ruijieCMPortalNormalAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalNormalAuthReqCount.setStatus("current")
_RuijieCMPortalEDUAuthReqCount_Type = Counter32
_RuijieCMPortalEDUAuthReqCount_Object = MibScalar
ruijieCMPortalEDUAuthReqCount = _RuijieCMPortalEDUAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 18),
    _RuijieCMPortalEDUAuthReqCount_Type()
)
ruijieCMPortalEDUAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalEDUAuthReqCount.setStatus("current")
_RuijieCMPortalStarbucksAuthReqCount_Type = Counter32
_RuijieCMPortalStarbucksAuthReqCount_Object = MibScalar
ruijieCMPortalStarbucksAuthReqCount = _RuijieCMPortalStarbucksAuthReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 19),
    _RuijieCMPortalStarbucksAuthReqCount_Type()
)
ruijieCMPortalStarbucksAuthReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalStarbucksAuthReqCount.setStatus("current")
_RuijieCMPortalNormalAuthRespCount_Type = Counter32
_RuijieCMPortalNormalAuthRespCount_Object = MibScalar
ruijieCMPortalNormalAuthRespCount = _RuijieCMPortalNormalAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 20),
    _RuijieCMPortalNormalAuthRespCount_Type()
)
ruijieCMPortalNormalAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalNormalAuthRespCount.setStatus("current")
_RuijieCMPortalEDUAuthRespCount_Type = Counter32
_RuijieCMPortalEDUAuthRespCount_Object = MibScalar
ruijieCMPortalEDUAuthRespCount = _RuijieCMPortalEDUAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 21),
    _RuijieCMPortalEDUAuthRespCount_Type()
)
ruijieCMPortalEDUAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalEDUAuthRespCount.setStatus("current")
_RuijieCMPortalStarbucksAuthRespCount_Type = Counter32
_RuijieCMPortalStarbucksAuthRespCount_Object = MibScalar
ruijieCMPortalStarbucksAuthRespCount = _RuijieCMPortalStarbucksAuthRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 22),
    _RuijieCMPortalStarbucksAuthRespCount_Type()
)
ruijieCMPortalStarbucksAuthRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalStarbucksAuthRespCount.setStatus("current")
_RuijieACPortalMaxAuthNum_Type = Integer32
_RuijieACPortalMaxAuthNum_Object = MibScalar
ruijieACPortalMaxAuthNum = _RuijieACPortalMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 23),
    _RuijieACPortalMaxAuthNum_Type()
)
ruijieACPortalMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieACPortalMaxAuthNum.setStatus("current")
_RuijieACPortalCurrentMaxAuthNum_Type = Integer32
_RuijieACPortalCurrentMaxAuthNum_Object = MibScalar
ruijieACPortalCurrentMaxAuthNum = _RuijieACPortalCurrentMaxAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 24),
    _RuijieACPortalCurrentMaxAuthNum_Type()
)
ruijieACPortalCurrentMaxAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieACPortalCurrentMaxAuthNum.setStatus("current")
_RuijieCMPortalAuthFailCauseTable_Object = MibTable
ruijieCMPortalAuthFailCauseTable = _RuijieCMPortalAuthFailCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 25)
)
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCauseTable.setStatus("current")
_RuijieCMPortalAuthFailCauseEntry_Object = MibTableRow
ruijieCMPortalAuthFailCauseEntry = _RuijieCMPortalAuthFailCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 25, 1)
)
ruijieCMPortalAuthFailCauseEntry.setIndexNames(
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthFailCauseErrId"),
)
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCauseEntry.setStatus("current")


class _RuijieCMPortalAuthFailCauseErrId_Type(DisplayString):
    """Custom type ruijieCMPortalAuthFailCauseErrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RuijieCMPortalAuthFailCauseErrId_Type.__name__ = "DisplayString"
_RuijieCMPortalAuthFailCauseErrId_Object = MibTableColumn
ruijieCMPortalAuthFailCauseErrId = _RuijieCMPortalAuthFailCauseErrId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 25, 1, 1),
    _RuijieCMPortalAuthFailCauseErrId_Type()
)
ruijieCMPortalAuthFailCauseErrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCauseErrId.setStatus("current")
_RuijieCMPortalAuthFailCauseCount_Type = Unsigned32
_RuijieCMPortalAuthFailCauseCount_Object = MibTableColumn
ruijieCMPortalAuthFailCauseCount = _RuijieCMPortalAuthFailCauseCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 25, 1, 2),
    _RuijieCMPortalAuthFailCauseCount_Type()
)
ruijieCMPortalAuthFailCauseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCauseCount.setStatus("current")
_RuijieCMPortalAuthFailCodeTable_Object = MibTable
ruijieCMPortalAuthFailCodeTable = _RuijieCMPortalAuthFailCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 26)
)
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCodeTable.setStatus("current")
_RuijieCMPortalAuthFailCodeEntry_Object = MibTableRow
ruijieCMPortalAuthFailCodeEntry = _RuijieCMPortalAuthFailCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 26, 1)
)
ruijieCMPortalAuthFailCodeEntry.setIndexNames(
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthFailCodeIndex"),
)
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCodeEntry.setStatus("current")
_RuijieCMPortalAuthFailCodeIndex_Type = Unsigned32
_RuijieCMPortalAuthFailCodeIndex_Object = MibTableColumn
ruijieCMPortalAuthFailCodeIndex = _RuijieCMPortalAuthFailCodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 26, 1, 1),
    _RuijieCMPortalAuthFailCodeIndex_Type()
)
ruijieCMPortalAuthFailCodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCodeIndex.setStatus("current")
_RuijieCMPortalAuthFailCode_Type = Unsigned32
_RuijieCMPortalAuthFailCode_Object = MibTableColumn
ruijieCMPortalAuthFailCode = _RuijieCMPortalAuthFailCode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 26, 1, 2),
    _RuijieCMPortalAuthFailCode_Type()
)
ruijieCMPortalAuthFailCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCode.setStatus("current")
_RuijieCMPortalAuthFailCodeCount_Type = Unsigned32
_RuijieCMPortalAuthFailCodeCount_Object = MibTableColumn
ruijieCMPortalAuthFailCodeCount = _RuijieCMPortalAuthFailCodeCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 26, 1, 3),
    _RuijieCMPortalAuthFailCodeCount_Type()
)
ruijieCMPortalAuthFailCodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCodeCount.setStatus("current")
_RuijieCMPortalLogoutReqCount_Type = Counter32
_RuijieCMPortalLogoutReqCount_Object = MibScalar
ruijieCMPortalLogoutReqCount = _RuijieCMPortalLogoutReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 27),
    _RuijieCMPortalLogoutReqCount_Type()
)
ruijieCMPortalLogoutReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalLogoutReqCount.setStatus("current")
_RuijieCMPortalLogoutRespCount_Type = Counter32
_RuijieCMPortalLogoutRespCount_Object = MibScalar
ruijieCMPortalLogoutRespCount = _RuijieCMPortalLogoutRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 28),
    _RuijieCMPortalLogoutRespCount_Type()
)
ruijieCMPortalLogoutRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalLogoutRespCount.setStatus("current")
_RuijieCMPortalNtfLogoutReqCount_Type = Counter32
_RuijieCMPortalNtfLogoutReqCount_Object = MibScalar
ruijieCMPortalNtfLogoutReqCount = _RuijieCMPortalNtfLogoutReqCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 29),
    _RuijieCMPortalNtfLogoutReqCount_Type()
)
ruijieCMPortalNtfLogoutReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalNtfLogoutReqCount.setStatus("current")
_RuijieCMPortalNtfLogoutRespCount_Type = Counter32
_RuijieCMPortalNtfLogoutRespCount_Object = MibScalar
ruijieCMPortalNtfLogoutRespCount = _RuijieCMPortalNtfLogoutRespCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 30),
    _RuijieCMPortalNtfLogoutRespCount_Type()
)
ruijieCMPortalNtfLogoutRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalNtfLogoutRespCount.setStatus("current")
_RuijieApNasPortIdTable_Object = MibTable
ruijieApNasPortIdTable = _RuijieApNasPortIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31)
)
if mibBuilder.loadTexts:
    ruijieApNasPortIdTable.setStatus("current")
_RuijieApNasPortIdEntry_Object = MibTableRow
ruijieApNasPortIdEntry = _RuijieApNasPortIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31, 1)
)
ruijieApNasPortIdEntry.setIndexNames(
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdApMacAddress"),
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdRadioId"),
    (0, "RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdWlanId"),
)
if mibBuilder.loadTexts:
    ruijieApNasPortIdEntry.setStatus("current")
_RuijieApNasPortIdApMacAddress_Type = MacAddress
_RuijieApNasPortIdApMacAddress_Object = MibTableColumn
ruijieApNasPortIdApMacAddress = _RuijieApNasPortIdApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31, 1, 1),
    _RuijieApNasPortIdApMacAddress_Type()
)
ruijieApNasPortIdApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApNasPortIdApMacAddress.setStatus("current")
_RuijieApNasPortIdRadioId_Type = Unsigned32
_RuijieApNasPortIdRadioId_Object = MibTableColumn
ruijieApNasPortIdRadioId = _RuijieApNasPortIdRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31, 1, 2),
    _RuijieApNasPortIdRadioId_Type()
)
ruijieApNasPortIdRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApNasPortIdRadioId.setStatus("current")
_RuijieApNasPortIdWlanId_Type = Unsigned32
_RuijieApNasPortIdWlanId_Object = MibTableColumn
ruijieApNasPortIdWlanId = _RuijieApNasPortIdWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31, 1, 3),
    _RuijieApNasPortIdWlanId_Type()
)
ruijieApNasPortIdWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApNasPortIdWlanId.setStatus("current")
_RuijieApNasPortIdNasPortId_Type = DisplayString
_RuijieApNasPortIdNasPortId_Object = MibTableColumn
ruijieApNasPortIdNasPortId = _RuijieApNasPortIdNasPortId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 31, 1, 4),
    _RuijieApNasPortIdNasPortId_Type()
)
ruijieApNasPortIdNasPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApNasPortIdNasPortId.setStatus("current")
_RuijieCMPortalAuthFailCount_Type = Counter32
_RuijieCMPortalAuthFailCount_Object = MibScalar
ruijieCMPortalAuthFailCount = _RuijieCMPortalAuthFailCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 32),
    _RuijieCMPortalAuthFailCount_Type()
)
ruijieCMPortalAuthFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalAuthFailCount.setStatus("current")
_RuijieCMPortalMaxHttpConnectionNum_Type = Counter32
_RuijieCMPortalMaxHttpConnectionNum_Object = MibScalar
ruijieCMPortalMaxHttpConnectionNum = _RuijieCMPortalMaxHttpConnectionNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 1, 33),
    _RuijieCMPortalMaxHttpConnectionNum_Type()
)
ruijieCMPortalMaxHttpConnectionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieCMPortalMaxHttpConnectionNum.setStatus("current")
_RuijieCMPortalMIBConformance_ObjectIdentity = ObjectIdentity
ruijieCMPortalMIBConformance = _RuijieCMPortalMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 2)
)
_RuijieCMPortalMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieCMPortalMIBCompliances = _RuijieCMPortalMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 2, 1)
)
_RuijieCMPortalMIBGroups_ObjectIdentity = ObjectIdentity
ruijieCMPortalMIBGroups = _RuijieCMPortalMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 2, 2)
)

# Managed Objects groups

ruijieCMPortalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 2, 2, 1)
)
ruijieCMPortalMIBGroup.setObjects(
      *(("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalMaxAuthNum"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalCurAuthNum"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddressType"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddress"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetPortNumber"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerUnavailableCode"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalChallengeReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalChallengeRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalGlobalServerURL"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerURL"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerName"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInUsedCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerConfigStatus"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalHttpReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalHttpRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalExceptionFailCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthSuccessedCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalNormalAuthReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalEDUAuthReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalStarbucksAuthReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalNormalAuthRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalEDUAuthRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalStarbucksAuthRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieACPortalMaxAuthNum"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieACPortalCurrentMaxAuthNum"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthFailCauseCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthFailCode"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalAuthFailCodeCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalLogoutReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalLogoutRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalNtfLogoutReqCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalNtfLogoutRespCount"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdApMacAddress"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdRadioId"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdWlanId"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieApNasPortIdNasPortId"))
)
if mibBuilder.loadTexts:
    ruijieCMPortalMIBGroup.setStatus("deprecated")


# Notification objects

ruijieCMPortalServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 0, 1)
)
ruijieCMPortalServerDownTrap.setObjects(
      *(("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddressType"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddress"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetPortNumber"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    ruijieCMPortalServerDownTrap.setStatus(
        "current"
    )

ruijieCMPortalServerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 0, 2)
)
ruijieCMPortalServerRecoverTrap.setObjects(
      *(("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddressType"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetAddress"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerInetPortNumber"),
        ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalServerUnavailableCode"))
)
if mibBuilder.loadTexts:
    ruijieCMPortalServerRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ruijieCMPortalMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 74, 2, 1, 1)
)
ruijieCMPortalMIBCompliance.setObjects(
    ("RUIJIE-CM-PORTAL-MIB", "ruijieCMPortalMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieCMPortalMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CM-PORTAL-MIB",
    **{"ruijieCMPortalMIB": ruijieCMPortalMIB,
       "ruijieCMPortalMIBTrap": ruijieCMPortalMIBTrap,
       "ruijieCMPortalServerDownTrap": ruijieCMPortalServerDownTrap,
       "ruijieCMPortalServerRecoverTrap": ruijieCMPortalServerRecoverTrap,
       "ruijieCMPortalMIBObjects": ruijieCMPortalMIBObjects,
       "ruijieCMPortalMaxAuthNum": ruijieCMPortalMaxAuthNum,
       "ruijieCMPortalCurAuthNum": ruijieCMPortalCurAuthNum,
       "ruijieCMPortalServerInetAddressType": ruijieCMPortalServerInetAddressType,
       "ruijieCMPortalServerInetAddress": ruijieCMPortalServerInetAddress,
       "ruijieCMPortalServerInetPortNumber": ruijieCMPortalServerInetPortNumber,
       "ruijieCMPortalServerUnavailableCode": ruijieCMPortalServerUnavailableCode,
       "ruijieCMPortalAuthReqCount": ruijieCMPortalAuthReqCount,
       "ruijieCMPortalAuthRespCount": ruijieCMPortalAuthRespCount,
       "ruijieCMPortalChallengeReqCount": ruijieCMPortalChallengeReqCount,
       "ruijieCMPortalChallengeRespCount": ruijieCMPortalChallengeRespCount,
       "ruijieCMPortalGlobalServerURL": ruijieCMPortalGlobalServerURL,
       "ruijieCMPortalServerURLTable": ruijieCMPortalServerURLTable,
       "ruijieCMPortalServerURLEntry": ruijieCMPortalServerURLEntry,
       "ruijieCMPortalServerURLId": ruijieCMPortalServerURLId,
       "ruijieCMPortalServerURL": ruijieCMPortalServerURL,
       "ruijieCMPortalServerName": ruijieCMPortalServerName,
       "ruijieCMPortalServerInUsedCount": ruijieCMPortalServerInUsedCount,
       "ruijieCMPortalServerConfigStatus": ruijieCMPortalServerConfigStatus,
       "ruijieCMPortalHttpReqCount": ruijieCMPortalHttpReqCount,
       "ruijieCMPortalHttpRespCount": ruijieCMPortalHttpRespCount,
       "ruijieCMPortalExceptionFailCount": ruijieCMPortalExceptionFailCount,
       "ruijieCMPortalAuthSuccessedCount": ruijieCMPortalAuthSuccessedCount,
       "ruijieCMPortalNormalAuthReqCount": ruijieCMPortalNormalAuthReqCount,
       "ruijieCMPortalEDUAuthReqCount": ruijieCMPortalEDUAuthReqCount,
       "ruijieCMPortalStarbucksAuthReqCount": ruijieCMPortalStarbucksAuthReqCount,
       "ruijieCMPortalNormalAuthRespCount": ruijieCMPortalNormalAuthRespCount,
       "ruijieCMPortalEDUAuthRespCount": ruijieCMPortalEDUAuthRespCount,
       "ruijieCMPortalStarbucksAuthRespCount": ruijieCMPortalStarbucksAuthRespCount,
       "ruijieACPortalMaxAuthNum": ruijieACPortalMaxAuthNum,
       "ruijieACPortalCurrentMaxAuthNum": ruijieACPortalCurrentMaxAuthNum,
       "ruijieCMPortalAuthFailCauseTable": ruijieCMPortalAuthFailCauseTable,
       "ruijieCMPortalAuthFailCauseEntry": ruijieCMPortalAuthFailCauseEntry,
       "ruijieCMPortalAuthFailCauseErrId": ruijieCMPortalAuthFailCauseErrId,
       "ruijieCMPortalAuthFailCauseCount": ruijieCMPortalAuthFailCauseCount,
       "ruijieCMPortalAuthFailCodeTable": ruijieCMPortalAuthFailCodeTable,
       "ruijieCMPortalAuthFailCodeEntry": ruijieCMPortalAuthFailCodeEntry,
       "ruijieCMPortalAuthFailCodeIndex": ruijieCMPortalAuthFailCodeIndex,
       "ruijieCMPortalAuthFailCode": ruijieCMPortalAuthFailCode,
       "ruijieCMPortalAuthFailCodeCount": ruijieCMPortalAuthFailCodeCount,
       "ruijieCMPortalLogoutReqCount": ruijieCMPortalLogoutReqCount,
       "ruijieCMPortalLogoutRespCount": ruijieCMPortalLogoutRespCount,
       "ruijieCMPortalNtfLogoutReqCount": ruijieCMPortalNtfLogoutReqCount,
       "ruijieCMPortalNtfLogoutRespCount": ruijieCMPortalNtfLogoutRespCount,
       "ruijieApNasPortIdTable": ruijieApNasPortIdTable,
       "ruijieApNasPortIdEntry": ruijieApNasPortIdEntry,
       "ruijieApNasPortIdApMacAddress": ruijieApNasPortIdApMacAddress,
       "ruijieApNasPortIdRadioId": ruijieApNasPortIdRadioId,
       "ruijieApNasPortIdWlanId": ruijieApNasPortIdWlanId,
       "ruijieApNasPortIdNasPortId": ruijieApNasPortIdNasPortId,
       "ruijieCMPortalAuthFailCount": ruijieCMPortalAuthFailCount,
       "ruijieCMPortalMaxHttpConnectionNum": ruijieCMPortalMaxHttpConnectionNum,
       "ruijieCMPortalMIBConformance": ruijieCMPortalMIBConformance,
       "ruijieCMPortalMIBCompliances": ruijieCMPortalMIBCompliances,
       "ruijieCMPortalMIBCompliance": ruijieCMPortalMIBCompliance,
       "ruijieCMPortalMIBGroups": ruijieCMPortalMIBGroups,
       "ruijieCMPortalMIBGroup": ruijieCMPortalMIBGroup}
)
