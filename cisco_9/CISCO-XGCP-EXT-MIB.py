# SNMP MIB module (CISCO-XGCP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-XGCP-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:03:16 2025
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

(CCallControlProfileIndex,
 CGwAdminState,
 CGwServiceState,
 cmgwIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CCallControlProfileIndex",
    "CGwAdminState",
    "CGwServiceState",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CXgcpRetryMethod,) = mibBuilder.importSymbols(
    "CISCO-XGCP-MIB",
    "CXgcpRetryMethod")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

ciscoXgcpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325)
)
if mibBuilder.loadTexts:
    ciscoXgcpExtMIB.setRevisions(
        ("2004-05-08 00:00",
         "2003-01-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CxgcpExtObjects_ObjectIdentity = ObjectIdentity
cxgcpExtObjects = _CxgcpExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1)
)
_CxgcpExtConfig_ObjectIdentity = ObjectIdentity
cxgcpExtConfig = _CxgcpExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1)
)
_CxeCallCtrlProfileTable_Object = MibTable
cxeCallCtrlProfileTable = _CxeCallCtrlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cxeCallCtrlProfileTable.setStatus("current")
_CxeCallCtrlProfileEntry_Object = MibTableRow
cxeCallCtrlProfileEntry = _CxeCallCtrlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1)
)
cxeCallCtrlProfileEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-XGCP-EXT-MIB", "cxeCcProfileIndex"),
)
if mibBuilder.loadTexts:
    cxeCallCtrlProfileEntry.setStatus("current")
_CxeCcProfileIndex_Type = CCallControlProfileIndex
_CxeCcProfileIndex_Object = MibTableColumn
cxeCcProfileIndex = _CxeCcProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 1),
    _CxeCcProfileIndex_Type()
)
cxeCcProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cxeCcProfileIndex.setStatus("current")


class _CxeCcProfileName_Type(DisplayString):
    """Custom type cxeCcProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CxeCcProfileName_Type.__name__ = "DisplayString"
_CxeCcProfileName_Object = MibTableColumn
cxeCcProfileName = _CxeCcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 2),
    _CxeCcProfileName_Type()
)
cxeCcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileName.setStatus("current")


class _CxeCcProfileNumVifs_Type(Integer32):
    """Custom type cxeCcProfileNumVifs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CxeCcProfileNumVifs_Type.__name__ = "Integer32"
_CxeCcProfileNumVifs_Object = MibTableColumn
cxeCcProfileNumVifs = _CxeCcProfileNumVifs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 3),
    _CxeCcProfileNumVifs_Type()
)
cxeCcProfileNumVifs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxeCcProfileNumVifs.setStatus("current")


class _CxeCcProfileMgcGrpNum_Type(Integer32):
    """Custom type cxeCcProfileMgcGrpNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CxeCcProfileMgcGrpNum_Type.__name__ = "Integer32"
_CxeCcProfileMgcGrpNum_Object = MibTableColumn
cxeCcProfileMgcGrpNum = _CxeCcProfileMgcGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 4),
    _CxeCcProfileMgcGrpNum_Type()
)
cxeCcProfileMgcGrpNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileMgcGrpNum.setStatus("current")


class _CxeCcProfileMgcAddrType_Type(InetAddressType):
    """Custom type cxeCcProfileMgcAddrType based on InetAddressType"""
    defaultValue = 1


_CxeCcProfileMgcAddrType_Type.__name__ = "InetAddressType"
_CxeCcProfileMgcAddrType_Object = MibTableColumn
cxeCcProfileMgcAddrType = _CxeCcProfileMgcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 5),
    _CxeCcProfileMgcAddrType_Type()
)
cxeCcProfileMgcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileMgcAddrType.setStatus("current")


class _CxeCcProfileMgcAddress_Type(InetAddress):
    """Custom type cxeCcProfileMgcAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CxeCcProfileMgcAddress_Type.__name__ = "InetAddress"
_CxeCcProfileMgcAddress_Object = MibTableColumn
cxeCcProfileMgcAddress = _CxeCcProfileMgcAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 6),
    _CxeCcProfileMgcAddress_Type()
)
cxeCcProfileMgcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileMgcAddress.setStatus("current")


class _CxeCcProfileProtocolIdx_Type(Integer32):
    """Custom type cxeCcProfileProtocolIdx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CxeCcProfileProtocolIdx_Type.__name__ = "Integer32"
_CxeCcProfileProtocolIdx_Object = MibTableColumn
cxeCcProfileProtocolIdx = _CxeCcProfileProtocolIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 7),
    _CxeCcProfileProtocolIdx_Type()
)
cxeCcProfileProtocolIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileProtocolIdx.setStatus("current")


class _CxeCcProfileXgcpRetryMethod_Type(CXgcpRetryMethod):
    """Custom type cxeCcProfileXgcpRetryMethod based on CXgcpRetryMethod"""
    defaultValue = 1


_CxeCcProfileXgcpRetryMethod_Type.__name__ = "CXgcpRetryMethod"
_CxeCcProfileXgcpRetryMethod_Object = MibTableColumn
cxeCcProfileXgcpRetryMethod = _CxeCcProfileXgcpRetryMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 8),
    _CxeCcProfileXgcpRetryMethod_Type()
)
cxeCcProfileXgcpRetryMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileXgcpRetryMethod.setStatus("current")


class _CxeCcProfileRetryMax1_Type(Integer32):
    """Custom type cxeCcProfileRetryMax1 based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxeCcProfileRetryMax1_Type.__name__ = "Integer32"
_CxeCcProfileRetryMax1_Object = MibTableColumn
cxeCcProfileRetryMax1 = _CxeCcProfileRetryMax1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 9),
    _CxeCcProfileRetryMax1_Type()
)
cxeCcProfileRetryMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRetryMax1.setStatus("current")


class _CxeCcProfileDnsLookupMax1_Type(TruthValue):
    """Custom type cxeCcProfileDnsLookupMax1 based on TruthValue"""
    defaultValue = 1


_CxeCcProfileDnsLookupMax1_Type.__name__ = "TruthValue"
_CxeCcProfileDnsLookupMax1_Object = MibTableColumn
cxeCcProfileDnsLookupMax1 = _CxeCcProfileDnsLookupMax1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 10),
    _CxeCcProfileDnsLookupMax1_Type()
)
cxeCcProfileDnsLookupMax1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileDnsLookupMax1.setStatus("current")


class _CxeCcProfileRetryMax2_Type(Integer32):
    """Custom type cxeCcProfileRetryMax2 based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CxeCcProfileRetryMax2_Type.__name__ = "Integer32"
_CxeCcProfileRetryMax2_Object = MibTableColumn
cxeCcProfileRetryMax2 = _CxeCcProfileRetryMax2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 11),
    _CxeCcProfileRetryMax2_Type()
)
cxeCcProfileRetryMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRetryMax2.setStatus("current")


class _CxeCcProfileDnsLookupMax2_Type(TruthValue):
    """Custom type cxeCcProfileDnsLookupMax2 based on TruthValue"""
    defaultValue = 1


_CxeCcProfileDnsLookupMax2_Type.__name__ = "TruthValue"
_CxeCcProfileDnsLookupMax2_Object = MibTableColumn
cxeCcProfileDnsLookupMax2 = _CxeCcProfileDnsLookupMax2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 12),
    _CxeCcProfileDnsLookupMax2_Type()
)
cxeCcProfileDnsLookupMax2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileDnsLookupMax2.setStatus("current")


class _CxeCcProfileMwiTimeout_Type(Integer32):
    """Custom type cxeCcProfileMwiTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CxeCcProfileMwiTimeout_Type.__name__ = "Integer32"
_CxeCcProfileMwiTimeout_Object = MibTableColumn
cxeCcProfileMwiTimeout = _CxeCcProfileMwiTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 13),
    _CxeCcProfileMwiTimeout_Type()
)
cxeCcProfileMwiTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileMwiTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileMwiTimeout.setUnits("milliseconds")


class _CxeCcProfileTsmaxTimeout_Type(Integer32):
    """Custom type cxeCcProfileTsmaxTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxeCcProfileTsmaxTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTsmaxTimeout_Object = MibTableColumn
cxeCcProfileTsmaxTimeout = _CxeCcProfileTsmaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 14),
    _CxeCcProfileTsmaxTimeout_Type()
)
cxeCcProfileTsmaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTsmaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTsmaxTimeout.setUnits("seconds")


class _CxeCcProfileTdinitTimeout_Type(Integer32):
    """Custom type cxeCcProfileTdinitTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CxeCcProfileTdinitTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTdinitTimeout_Object = MibTableColumn
cxeCcProfileTdinitTimeout = _CxeCcProfileTdinitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 15),
    _CxeCcProfileTdinitTimeout_Type()
)
cxeCcProfileTdinitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTdinitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTdinitTimeout.setUnits("seconds")


class _CxeCcProfileTdminTimeout_Type(Integer32):
    """Custom type cxeCcProfileTdminTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CxeCcProfileTdminTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTdminTimeout_Object = MibTableColumn
cxeCcProfileTdminTimeout = _CxeCcProfileTdminTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 17),
    _CxeCcProfileTdminTimeout_Type()
)
cxeCcProfileTdminTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTdminTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTdminTimeout.setUnits("seconds")


class _CxeCcProfileTdmaxTimeout_Type(Integer32):
    """Custom type cxeCcProfileTdmaxTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxeCcProfileTdmaxTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTdmaxTimeout_Object = MibTableColumn
cxeCcProfileTdmaxTimeout = _CxeCcProfileTdmaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 18),
    _CxeCcProfileTdmaxTimeout_Type()
)
cxeCcProfileTdmaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTdmaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTdmaxTimeout.setUnits("seconds")


class _CxeCcProfileTcritTimeout_Type(Integer32):
    """Custom type cxeCcProfileTcritTimeout based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxeCcProfileTcritTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTcritTimeout_Object = MibTableColumn
cxeCcProfileTcritTimeout = _CxeCcProfileTcritTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 19),
    _CxeCcProfileTcritTimeout_Type()
)
cxeCcProfileTcritTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTcritTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTcritTimeout.setUnits("seconds")


class _CxeCcProfileTparTimeout_Type(Integer32):
    """Custom type cxeCcProfileTparTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxeCcProfileTparTimeout_Type.__name__ = "Integer32"
_CxeCcProfileTparTimeout_Object = MibTableColumn
cxeCcProfileTparTimeout = _CxeCcProfileTparTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 20),
    _CxeCcProfileTparTimeout_Type()
)
cxeCcProfileTparTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileTparTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileTparTimeout.setUnits("seconds")


class _CxeCcProfileThistTimeout_Type(Integer32):
    """Custom type cxeCcProfileThistTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CxeCcProfileThistTimeout_Type.__name__ = "Integer32"
_CxeCcProfileThistTimeout_Object = MibTableColumn
cxeCcProfileThistTimeout = _CxeCcProfileThistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 21),
    _CxeCcProfileThistTimeout_Type()
)
cxeCcProfileThistTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileThistTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileThistTimeout.setUnits("seconds")


class _CxeCcProfileRtTimeout_Type(Integer32):
    """Custom type cxeCcProfileRtTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileRtTimeout_Type.__name__ = "Integer32"
_CxeCcProfileRtTimeout_Object = MibTableColumn
cxeCcProfileRtTimeout = _CxeCcProfileRtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 22),
    _CxeCcProfileRtTimeout_Type()
)
cxeCcProfileRtTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRtTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileRtTimeout.setUnits("seconds")


class _CxeCcProfileRbkTimeout_Type(Integer32):
    """Custom type cxeCcProfileRbkTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileRbkTimeout_Type.__name__ = "Integer32"
_CxeCcProfileRbkTimeout_Object = MibTableColumn
cxeCcProfileRbkTimeout = _CxeCcProfileRbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 23),
    _CxeCcProfileRbkTimeout_Type()
)
cxeCcProfileRbkTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRbkTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileRbkTimeout.setUnits("seconds")


class _CxeCcProfileCgTimeout_Type(Integer32):
    """Custom type cxeCcProfileCgTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileCgTimeout_Type.__name__ = "Integer32"
_CxeCcProfileCgTimeout_Object = MibTableColumn
cxeCcProfileCgTimeout = _CxeCcProfileCgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 24),
    _CxeCcProfileCgTimeout_Type()
)
cxeCcProfileCgTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileCgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileCgTimeout.setUnits("seconds")


class _CxeCcProfileBzTimeout_Type(Integer32):
    """Custom type cxeCcProfileBzTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileBzTimeout_Type.__name__ = "Integer32"
_CxeCcProfileBzTimeout_Object = MibTableColumn
cxeCcProfileBzTimeout = _CxeCcProfileBzTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 25),
    _CxeCcProfileBzTimeout_Type()
)
cxeCcProfileBzTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileBzTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileBzTimeout.setUnits("seconds")


class _CxeCcProfileDlTimeout_Type(Integer32):
    """Custom type cxeCcProfileDlTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileDlTimeout_Type.__name__ = "Integer32"
_CxeCcProfileDlTimeout_Object = MibTableColumn
cxeCcProfileDlTimeout = _CxeCcProfileDlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 26),
    _CxeCcProfileDlTimeout_Type()
)
cxeCcProfileDlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileDlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileDlTimeout.setUnits("seconds")


class _CxeCcProfileSlTimeout_Type(Integer32):
    """Custom type cxeCcProfileSlTimeout based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileSlTimeout_Type.__name__ = "Integer32"
_CxeCcProfileSlTimeout_Object = MibTableColumn
cxeCcProfileSlTimeout = _CxeCcProfileSlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 27),
    _CxeCcProfileSlTimeout_Type()
)
cxeCcProfileSlTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileSlTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileSlTimeout.setUnits("seconds")


class _CxeCcProfileRgTimeout_Type(Integer32):
    """Custom type cxeCcProfileRgTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileRgTimeout_Type.__name__ = "Integer32"
_CxeCcProfileRgTimeout_Object = MibTableColumn
cxeCcProfileRgTimeout = _CxeCcProfileRgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 28),
    _CxeCcProfileRgTimeout_Type()
)
cxeCcProfileRgTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileRgTimeout.setUnits("seconds")


class _CxeCcProfileRoTimeout_Type(Integer32):
    """Custom type cxeCcProfileRoTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CxeCcProfileRoTimeout_Type.__name__ = "Integer32"
_CxeCcProfileRoTimeout_Object = MibTableColumn
cxeCcProfileRoTimeout = _CxeCcProfileRoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 29),
    _CxeCcProfileRoTimeout_Type()
)
cxeCcProfileRoTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRoTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileRoTimeout.setUnits("seconds")


class _CxeCcProfileCot1Timeout_Type(Integer32):
    """Custom type cxeCcProfileCot1Timeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CxeCcProfileCot1Timeout_Type.__name__ = "Integer32"
_CxeCcProfileCot1Timeout_Object = MibTableColumn
cxeCcProfileCot1Timeout = _CxeCcProfileCot1Timeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 30),
    _CxeCcProfileCot1Timeout_Type()
)
cxeCcProfileCot1Timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileCot1Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileCot1Timeout.setUnits("seconds")


class _CxeCcProfileCot2Timeout_Type(Integer32):
    """Custom type cxeCcProfileCot2Timeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CxeCcProfileCot2Timeout_Type.__name__ = "Integer32"
_CxeCcProfileCot2Timeout_Object = MibTableColumn
cxeCcProfileCot2Timeout = _CxeCcProfileCot2Timeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 31),
    _CxeCcProfileCot2Timeout_Type()
)
cxeCcProfileCot2Timeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileCot2Timeout.setStatus("current")
if mibBuilder.loadTexts:
    cxeCcProfileCot2Timeout.setUnits("seconds")
_CxeCcProfileRowStatus_Type = RowStatus
_CxeCcProfileRowStatus_Object = MibTableColumn
cxeCcProfileRowStatus = _CxeCcProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 2, 1, 32),
    _CxeCcProfileRowStatus_Type()
)
cxeCcProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cxeCcProfileRowStatus.setStatus("current")
_CxeMediaGwServiceTable_Object = MibTable
cxeMediaGwServiceTable = _CxeMediaGwServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cxeMediaGwServiceTable.setStatus("current")
_CxeMediaGwServiceEntry_Object = MibTableRow
cxeMediaGwServiceEntry = _CxeMediaGwServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 3, 1)
)
cxeMediaGwServiceEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
)
if mibBuilder.loadTexts:
    cxeMediaGwServiceEntry.setStatus("current")
_CxeMgwServiceState_Type = CGwServiceState
_CxeMgwServiceState_Object = MibTableColumn
cxeMgwServiceState = _CxeMgwServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 3, 1, 1),
    _CxeMgwServiceState_Type()
)
cxeMgwServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxeMgwServiceState.setStatus("current")
_CxeMgwAdminState_Type = CGwAdminState
_CxeMgwAdminState_Object = MibTableColumn
cxeMgwAdminState = _CxeMgwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 3, 1, 2),
    _CxeMgwAdminState_Type()
)
cxeMgwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxeMgwAdminState.setStatus("current")


class _CxeMgwGraceTime_Type(Integer32):
    """Custom type cxeMgwGraceTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CxeMgwGraceTime_Type.__name__ = "Integer32"
_CxeMgwGraceTime_Object = MibTableColumn
cxeMgwGraceTime = _CxeMgwGraceTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 1, 1, 3, 1, 3),
    _CxeMgwGraceTime_Type()
)
cxeMgwGraceTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxeMgwGraceTime.setStatus("current")
if mibBuilder.loadTexts:
    cxeMgwGraceTime.setUnits("seconds")
_CxeCallCtrlMIBConformance_ObjectIdentity = ObjectIdentity
cxeCallCtrlMIBConformance = _CxeCallCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2)
)
_CxeCallCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
cxeCallCtrlMIBCompliances = _CxeCallCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 1)
)
_CxeCallCtrlMIBGroups_ObjectIdentity = ObjectIdentity
cxeCallCtrlMIBGroups = _CxeCallCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2)
)

# Managed Objects groups

cxeCcProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2, 1)
)
cxeCcProfileGroup.setObjects(
      *(("CISCO-XGCP-EXT-MIB", "cxeCcProfileName"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileNumVifs"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcGrpNum"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcAddrType"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMgcAddress"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileProtocolIdx"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileXgcpRetryMethod"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRetryMax1"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDnsLookupMax1"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRetryMax2"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDnsLookupMax2"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileMwiTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTsmaxTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdinitTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdminTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTdmaxTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTcritTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileTparTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileThistTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRtTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRbkTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCgTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileBzTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileDlTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileSlTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRgTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRoTimeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCot1Timeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileCot2Timeout"),
        ("CISCO-XGCP-EXT-MIB", "cxeCcProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cxeCcProfileGroup.setStatus("current")

cxeMediaGwServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 2, 2)
)
cxeMediaGwServiceGroup.setObjects(
      *(("CISCO-XGCP-EXT-MIB", "cxeMgwServiceState"),
        ("CISCO-XGCP-EXT-MIB", "cxeMgwAdminState"),
        ("CISCO-XGCP-EXT-MIB", "cxeMgwGraceTime"))
)
if mibBuilder.loadTexts:
    cxeMediaGwServiceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cxeCallCtrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 325, 2, 1, 1)
)
cxeCallCtrlMIBCompliance.setObjects(
      *(("CISCO-XGCP-EXT-MIB", "cxeCcProfileGroup"),
        ("CISCO-XGCP-EXT-MIB", "cxeMediaGwServiceGroup"))
)
if mibBuilder.loadTexts:
    cxeCallCtrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-XGCP-EXT-MIB",
    **{"ciscoXgcpExtMIB": ciscoXgcpExtMIB,
       "cxgcpExtObjects": cxgcpExtObjects,
       "cxgcpExtConfig": cxgcpExtConfig,
       "cxeCallCtrlProfileTable": cxeCallCtrlProfileTable,
       "cxeCallCtrlProfileEntry": cxeCallCtrlProfileEntry,
       "cxeCcProfileIndex": cxeCcProfileIndex,
       "cxeCcProfileName": cxeCcProfileName,
       "cxeCcProfileNumVifs": cxeCcProfileNumVifs,
       "cxeCcProfileMgcGrpNum": cxeCcProfileMgcGrpNum,
       "cxeCcProfileMgcAddrType": cxeCcProfileMgcAddrType,
       "cxeCcProfileMgcAddress": cxeCcProfileMgcAddress,
       "cxeCcProfileProtocolIdx": cxeCcProfileProtocolIdx,
       "cxeCcProfileXgcpRetryMethod": cxeCcProfileXgcpRetryMethod,
       "cxeCcProfileRetryMax1": cxeCcProfileRetryMax1,
       "cxeCcProfileDnsLookupMax1": cxeCcProfileDnsLookupMax1,
       "cxeCcProfileRetryMax2": cxeCcProfileRetryMax2,
       "cxeCcProfileDnsLookupMax2": cxeCcProfileDnsLookupMax2,
       "cxeCcProfileMwiTimeout": cxeCcProfileMwiTimeout,
       "cxeCcProfileTsmaxTimeout": cxeCcProfileTsmaxTimeout,
       "cxeCcProfileTdinitTimeout": cxeCcProfileTdinitTimeout,
       "cxeCcProfileTdminTimeout": cxeCcProfileTdminTimeout,
       "cxeCcProfileTdmaxTimeout": cxeCcProfileTdmaxTimeout,
       "cxeCcProfileTcritTimeout": cxeCcProfileTcritTimeout,
       "cxeCcProfileTparTimeout": cxeCcProfileTparTimeout,
       "cxeCcProfileThistTimeout": cxeCcProfileThistTimeout,
       "cxeCcProfileRtTimeout": cxeCcProfileRtTimeout,
       "cxeCcProfileRbkTimeout": cxeCcProfileRbkTimeout,
       "cxeCcProfileCgTimeout": cxeCcProfileCgTimeout,
       "cxeCcProfileBzTimeout": cxeCcProfileBzTimeout,
       "cxeCcProfileDlTimeout": cxeCcProfileDlTimeout,
       "cxeCcProfileSlTimeout": cxeCcProfileSlTimeout,
       "cxeCcProfileRgTimeout": cxeCcProfileRgTimeout,
       "cxeCcProfileRoTimeout": cxeCcProfileRoTimeout,
       "cxeCcProfileCot1Timeout": cxeCcProfileCot1Timeout,
       "cxeCcProfileCot2Timeout": cxeCcProfileCot2Timeout,
       "cxeCcProfileRowStatus": cxeCcProfileRowStatus,
       "cxeMediaGwServiceTable": cxeMediaGwServiceTable,
       "cxeMediaGwServiceEntry": cxeMediaGwServiceEntry,
       "cxeMgwServiceState": cxeMgwServiceState,
       "cxeMgwAdminState": cxeMgwAdminState,
       "cxeMgwGraceTime": cxeMgwGraceTime,
       "cxeCallCtrlMIBConformance": cxeCallCtrlMIBConformance,
       "cxeCallCtrlMIBCompliances": cxeCallCtrlMIBCompliances,
       "cxeCallCtrlMIBCompliance": cxeCallCtrlMIBCompliance,
       "cxeCallCtrlMIBGroups": cxeCallCtrlMIBGroups,
       "cxeCcProfileGroup": cxeCcProfileGroup,
       "cxeMediaGwServiceGroup": cxeMediaGwServiceGroup}
)
