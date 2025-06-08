# SNMP MIB module (RUIJIE-AC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AC-MGMT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:22 2025
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

(capwapBaseNtfAuthenMethod,
 capwapBaseNtfChannelDownReason,
 capwapBaseNtfChannelType) = mibBuilder.importSymbols(
    "CAPWAP-BASE-MIB",
    "capwapBaseNtfAuthenMethod",
    "capwapBaseNtfChannelDownReason",
    "capwapBaseNtfChannelType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieAcMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56)
)
if mibBuilder.loadTexts:
    ruijieAcMgmtMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieAcMgmtAcMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAcMIBObjects = _RuijieAcMgmtAcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1)
)
_RuijieAcMgmtAc_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAc = _RuijieAcMgmtAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1)
)


class _RuijieAcStaLimit_Type(Integer32):
    """Custom type ruijieAcStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieAcStaLimit_Type.__name__ = "Integer32"
_RuijieAcStaLimit_Object = MibScalar
ruijieAcStaLimit = _RuijieAcStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 1),
    _RuijieAcStaLimit_Type()
)
ruijieAcStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaLimit.setStatus("current")


class _RuijieAcWtpLimit_Type(Integer32):
    """Custom type ruijieAcWtpLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieAcWtpLimit_Type.__name__ = "Integer32"
_RuijieAcWtpLimit_Object = MibScalar
ruijieAcWtpLimit = _RuijieAcWtpLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 2),
    _RuijieAcWtpLimit_Type()
)
ruijieAcWtpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcWtpLimit.setStatus("current")


class _RuijieAcRMacField_Type(Integer32):
    """Custom type ruijieAcRMacField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcRMacField_Type.__name__ = "Integer32"
_RuijieAcRMacField_Object = MibScalar
ruijieAcRMacField = _RuijieAcRMacField_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 3),
    _RuijieAcRMacField_Type()
)
ruijieAcRMacField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcRMacField.setStatus("current")


class _RuijieAcDataDtls_Type(Integer32):
    """Custom type ruijieAcDataDtls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcDataDtls_Type.__name__ = "Integer32"
_RuijieAcDataDtls_Object = MibScalar
ruijieAcDataDtls = _RuijieAcDataDtls_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 4),
    _RuijieAcDataDtls_Type()
)
ruijieAcDataDtls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcDataDtls.setStatus("current")


class _RuijieAcEcnSupport_Type(Integer32):
    """Custom type ruijieAcEcnSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcEcnSupport_Type.__name__ = "Integer32"
_RuijieAcEcnSupport_Object = MibScalar
ruijieAcEcnSupport = _RuijieAcEcnSupport_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 5),
    _RuijieAcEcnSupport_Type()
)
ruijieAcEcnSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcEcnSupport.setStatus("current")
_RuijieAcAcIpTable_Object = MibTable
ruijieAcAcIpTable = _RuijieAcAcIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieAcAcIpTable.setStatus("current")
_RuijieAcAcIpTableEntry_Object = MibTableRow
ruijieAcAcIpTableEntry = _RuijieAcAcIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 6, 1)
)
ruijieAcAcIpTableEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAcAcIpIndex"),
)
if mibBuilder.loadTexts:
    ruijieAcAcIpTableEntry.setStatus("current")


class _RuijieAcAcIpIndex_Type(Integer32):
    """Custom type ruijieAcAcIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RuijieAcAcIpIndex_Type.__name__ = "Integer32"
_RuijieAcAcIpIndex_Object = MibTableColumn
ruijieAcAcIpIndex = _RuijieAcAcIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 6, 1, 1),
    _RuijieAcAcIpIndex_Type()
)
ruijieAcAcIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcAcIpIndex.setStatus("current")
_RuijieAcBackAcIp_Type = IpAddress
_RuijieAcBackAcIp_Object = MibTableColumn
ruijieAcBackAcIp = _RuijieAcBackAcIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 6, 1, 2),
    _RuijieAcBackAcIp_Type()
)
ruijieAcBackAcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcBackAcIp.setStatus("current")
_RuijieAcAcIpRS_Type = RowStatus
_RuijieAcAcIpRS_Object = MibTableColumn
ruijieAcAcIpRS = _RuijieAcAcIpRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 6, 1, 3),
    _RuijieAcAcIpRS_Type()
)
ruijieAcAcIpRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAcIpRS.setStatus("current")


class _RuijieAcMtu_Type(Integer32):
    """Custom type ruijieAcMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_RuijieAcMtu_Type.__name__ = "Integer32"
_RuijieAcMtu_Object = MibScalar
ruijieAcMtu = _RuijieAcMtu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 7),
    _RuijieAcMtu_Type()
)
ruijieAcMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcMtu.setStatus("current")


class _RuijieAcAcName_Type(DisplayString):
    """Custom type ruijieAcAcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieAcAcName_Type.__name__ = "DisplayString"
_RuijieAcAcName_Object = MibScalar
ruijieAcAcName = _RuijieAcAcName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 8),
    _RuijieAcAcName_Type()
)
ruijieAcAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAcName.setStatus("current")


class _RuijieAcLocation_Type(DisplayString):
    """Custom type ruijieAcLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcLocation_Type.__name__ = "DisplayString"
_RuijieAcLocation_Object = MibScalar
ruijieAcLocation = _RuijieAcLocation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 9),
    _RuijieAcLocation_Type()
)
ruijieAcLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcLocation.setStatus("current")


class _RuijieAcResetAp_Type(DisplayString):
    """Custom type ruijieAcResetAp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcResetAp_Type.__name__ = "DisplayString"
_RuijieAcResetAp_Object = MibScalar
ruijieAcResetAp = _RuijieAcResetAp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 10),
    _RuijieAcResetAp_Type()
)
ruijieAcResetAp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcResetAp.setStatus("current")


class _RuijieAcApNum_Type(Integer32):
    """Custom type ruijieAcApNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_RuijieAcApNum_Type.__name__ = "Integer32"
_RuijieAcApNum_Object = MibScalar
ruijieAcApNum = _RuijieAcApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 11),
    _RuijieAcApNum_Type()
)
ruijieAcApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcApNum.setStatus("current")
_RuijieAc80211aRateTable_Object = MibTable
ruijieAc80211aRateTable = _RuijieAc80211aRateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieAc80211aRateTable.setStatus("current")
_RuijieAc80211aRateEntry_Object = MibTableRow
ruijieAc80211aRateEntry = _RuijieAc80211aRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 12, 1)
)
ruijieAc80211aRateEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAc80211aRate"),
)
if mibBuilder.loadTexts:
    ruijieAc80211aRateEntry.setStatus("current")


class _RuijieAc80211aRate_Type(Integer32):
    """Custom type ruijieAc80211aRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuijieAc80211aRate_Type.__name__ = "Integer32"
_RuijieAc80211aRate_Object = MibTableColumn
ruijieAc80211aRate = _RuijieAc80211aRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 12, 1, 1),
    _RuijieAc80211aRate_Type()
)
ruijieAc80211aRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAc80211aRate.setStatus("current")


class _RuijieAc80211aRateType_Type(Integer32):
    """Custom type ruijieAc80211aRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieAc80211aRateType_Type.__name__ = "Integer32"
_RuijieAc80211aRateType_Object = MibTableColumn
ruijieAc80211aRateType = _RuijieAc80211aRateType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 12, 1, 2),
    _RuijieAc80211aRateType_Type()
)
ruijieAc80211aRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAc80211aRateType.setStatus("current")
_RuijieAc80211bRateTable_Object = MibTable
ruijieAc80211bRateTable = _RuijieAc80211bRateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieAc80211bRateTable.setStatus("current")
_RuijieAc80211bRateEntry_Object = MibTableRow
ruijieAc80211bRateEntry = _RuijieAc80211bRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 13, 1)
)
ruijieAc80211bRateEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAc80211bRate"),
)
if mibBuilder.loadTexts:
    ruijieAc80211bRateEntry.setStatus("current")


class _RuijieAc80211bRate_Type(Integer32):
    """Custom type ruijieAc80211bRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieAc80211bRate_Type.__name__ = "Integer32"
_RuijieAc80211bRate_Object = MibTableColumn
ruijieAc80211bRate = _RuijieAc80211bRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 13, 1, 1),
    _RuijieAc80211bRate_Type()
)
ruijieAc80211bRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieAc80211bRate.setStatus("current")


class _RuijieAc80211bRateType_Type(Integer32):
    """Custom type ruijieAc80211bRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieAc80211bRateType_Type.__name__ = "Integer32"
_RuijieAc80211bRateType_Object = MibTableColumn
ruijieAc80211bRateType = _RuijieAc80211bRateType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 13, 1, 2),
    _RuijieAc80211bRateType_Type()
)
ruijieAc80211bRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAc80211bRateType.setStatus("current")


class _RuijieAcFallback_Type(Integer32):
    """Custom type ruijieAcFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieAcFallback_Type.__name__ = "Integer32"
_RuijieAcFallback_Object = MibScalar
ruijieAcFallback = _RuijieAcFallback_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 14),
    _RuijieAcFallback_Type()
)
ruijieAcFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFallback.setStatus("current")


class _RuijieAcStaNum_Type(Integer32):
    """Custom type ruijieAcStaNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_RuijieAcStaNum_Type.__name__ = "Integer32"
_RuijieAcStaNum_Object = MibScalar
ruijieAcStaNum = _RuijieAcStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 15),
    _RuijieAcStaNum_Type()
)
ruijieAcStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaNum.setStatus("current")
_RuijieAcMacAddr_Type = MacAddress
_RuijieAcMacAddr_Object = MibScalar
ruijieAcMacAddr = _RuijieAcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 16),
    _RuijieAcMacAddr_Type()
)
ruijieAcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcMacAddr.setStatus("current")


class _RuijieAcDescriptor_Type(DisplayString):
    """Custom type ruijieAcDescriptor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcDescriptor_Type.__name__ = "DisplayString"
_RuijieAcDescriptor_Object = MibScalar
ruijieAcDescriptor = _RuijieAcDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 17),
    _RuijieAcDescriptor_Type()
)
ruijieAcDescriptor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcDescriptor.setStatus("current")


class _RuijieAcPID_Type(DisplayString):
    """Custom type ruijieAcPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcPID_Type.__name__ = "DisplayString"
_RuijieAcPID_Object = MibScalar
ruijieAcPID = _RuijieAcPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 18),
    _RuijieAcPID_Type()
)
ruijieAcPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcPID.setStatus("current")


class _RuijieAcHwId_Type(DisplayString):
    """Custom type ruijieAcHwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcHwId_Type.__name__ = "DisplayString"
_RuijieAcHwId_Object = MibScalar
ruijieAcHwId = _RuijieAcHwId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 19),
    _RuijieAcHwId_Type()
)
ruijieAcHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcHwId.setStatus("current")


class _RuijieAcSN_Type(DisplayString):
    """Custom type ruijieAcSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcSN_Type.__name__ = "DisplayString"
_RuijieAcSN_Object = MibScalar
ruijieAcSN = _RuijieAcSN_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 20),
    _RuijieAcSN_Type()
)
ruijieAcSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcSN.setStatus("current")
_RuijieAcTemp_Type = Integer32
_RuijieAcTemp_Object = MibScalar
ruijieAcTemp = _RuijieAcTemp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 21),
    _RuijieAcTemp_Type()
)
ruijieAcTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTemp.setStatus("current")


class _RuijieAcAPUpDownCtrl_Type(Integer32):
    """Custom type ruijieAcAPUpDownCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcAPUpDownCtrl_Type.__name__ = "Integer32"
_RuijieAcAPUpDownCtrl_Object = MibScalar
ruijieAcAPUpDownCtrl = _RuijieAcAPUpDownCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 22),
    _RuijieAcAPUpDownCtrl_Type()
)
ruijieAcAPUpDownCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAPUpDownCtrl.setStatus("current")


class _RuijieAcAPJoinFailCtrl_Type(Integer32):
    """Custom type ruijieAcAPJoinFailCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcAPJoinFailCtrl_Type.__name__ = "Integer32"
_RuijieAcAPJoinFailCtrl_Object = MibScalar
ruijieAcAPJoinFailCtrl = _RuijieAcAPJoinFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 23),
    _RuijieAcAPJoinFailCtrl_Type()
)
ruijieAcAPJoinFailCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAPJoinFailCtrl.setStatus("current")


class _RuijieAcAPDecryEroReportCtrl_Type(Integer32):
    """Custom type ruijieAcAPDecryEroReportCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcAPDecryEroReportCtrl_Type.__name__ = "Integer32"
_RuijieAcAPDecryEroReportCtrl_Object = MibScalar
ruijieAcAPDecryEroReportCtrl = _RuijieAcAPDecryEroReportCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 24),
    _RuijieAcAPDecryEroReportCtrl_Type()
)
ruijieAcAPDecryEroReportCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcAPDecryEroReportCtrl.setStatus("current")


class _RuijieAcApImageUpdtCtrl_Type(Integer32):
    """Custom type ruijieAcApImageUpdtCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcApImageUpdtCtrl_Type.__name__ = "Integer32"
_RuijieAcApImageUpdtCtrl_Object = MibScalar
ruijieAcApImageUpdtCtrl = _RuijieAcApImageUpdtCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 25),
    _RuijieAcApImageUpdtCtrl_Type()
)
ruijieAcApImageUpdtCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcApImageUpdtCtrl.setStatus("current")
_RuijieAcApConfigMsgEroCtrl_Type = Integer32
_RuijieAcApConfigMsgEroCtrl_Object = MibScalar
ruijieAcApConfigMsgEroCtrl = _RuijieAcApConfigMsgEroCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 26),
    _RuijieAcApConfigMsgEroCtrl_Type()
)
ruijieAcApConfigMsgEroCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcApConfigMsgEroCtrl.setStatus("current")
_RuijieAcApRadioOperStatuCtrl_Type = Integer32
_RuijieAcApRadioOperStatuCtrl_Object = MibScalar
ruijieAcApRadioOperStatuCtrl = _RuijieAcApRadioOperStatuCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 27),
    _RuijieAcApRadioOperStatuCtrl_Type()
)
ruijieAcApRadioOperStatuCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcApRadioOperStatuCtrl.setStatus("current")
_RuijieAcApAuthenFailCtrl_Type = Integer32
_RuijieAcApAuthenFailCtrl_Object = MibScalar
ruijieAcApAuthenFailCtrl = _RuijieAcApAuthenFailCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 28),
    _RuijieAcApAuthenFailCtrl_Type()
)
ruijieAcApAuthenFailCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcApAuthenFailCtrl.setStatus("current")
_RuijieAcApTimestampCtrl_Type = Integer32
_RuijieAcApTimestampCtrl_Object = MibScalar
ruijieAcApTimestampCtrl = _RuijieAcApTimestampCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 29),
    _RuijieAcApTimestampCtrl_Type()
)
ruijieAcApTimestampCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcApTimestampCtrl.setStatus("current")
_RuijieAcStaOperCtrl_Type = Integer32
_RuijieAcStaOperCtrl_Object = MibScalar
ruijieAcStaOperCtrl = _RuijieAcStaOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 30),
    _RuijieAcStaOperCtrl_Type()
)
ruijieAcStaOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOperCtrl.setStatus("current")


class _RuijieAcType_Type(Integer32):
    """Custom type ruijieAcType based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ws5302", 1),
          ("ws5708", 2),
          ("m8600ws", 3),
          ("ws3302", 4),
          ("m12000ws", 5),
          ("ws5504", 6),
          ("ws6108", 7),
          ("ws6816", 8),
          ("m18000-WS-ED", 9),
          ("m8600E-WS-ED", 10),
          ("eg2000", 11),
          ("ws6008", 12),
          ("ws6812", 13),
          ("aw608", 14),
          ("ws6024", 15),
          ("eg350", 16))
    )


_RuijieAcType_Type.__name__ = "Integer32"
_RuijieAcType_Object = MibScalar
ruijieAcType = _RuijieAcType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 31),
    _RuijieAcType_Type()
)
ruijieAcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcType.setStatus("current")


class _RuijieAcNeid_Type(DisplayString):
    """Custom type ruijieAcNeid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcNeid_Type.__name__ = "DisplayString"
_RuijieAcNeid_Object = MibScalar
ruijieAcNeid = _RuijieAcNeid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 32),
    _RuijieAcNeid_Type()
)
ruijieAcNeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNeid.setStatus("current")


class _RuijieAcManufacturer_Type(DisplayString):
    """Custom type ruijieAcManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcManufacturer_Type.__name__ = "DisplayString"
_RuijieAcManufacturer_Object = MibScalar
ruijieAcManufacturer = _RuijieAcManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 33),
    _RuijieAcManufacturer_Type()
)
ruijieAcManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcManufacturer.setStatus("current")


class _RuijieAcSwVer_Type(DisplayString):
    """Custom type ruijieAcSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcSwVer_Type.__name__ = "DisplayString"
_RuijieAcSwVer_Object = MibScalar
ruijieAcSwVer = _RuijieAcSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 34),
    _RuijieAcSwVer_Type()
)
ruijieAcSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcSwVer.setStatus("current")


class _RuijieAcSwManufacturer_Type(DisplayString):
    """Custom type ruijieAcSwManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieAcSwManufacturer_Type.__name__ = "DisplayString"
_RuijieAcSwManufacturer_Object = MibScalar
ruijieAcSwManufacturer = _RuijieAcSwManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 35),
    _RuijieAcSwManufacturer_Type()
)
ruijieAcSwManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcSwManufacturer.setStatus("current")
_RuijieAcStaResourceNotEnough_Type = Integer32
_RuijieAcStaResourceNotEnough_Object = MibScalar
ruijieAcStaResourceNotEnough = _RuijieAcStaResourceNotEnough_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 36),
    _RuijieAcStaResourceNotEnough_Type()
)
ruijieAcStaResourceNotEnough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaResourceNotEnough.setStatus("current")
_RuijieAcPppoeClientAct_Type = Integer32
_RuijieAcPppoeClientAct_Object = MibScalar
ruijieAcPppoeClientAct = _RuijieAcPppoeClientAct_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 37),
    _RuijieAcPppoeClientAct_Type()
)
ruijieAcPppoeClientAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcPppoeClientAct.setStatus("current")
_RuijieAcPppoeClientMax_Type = Integer32
_RuijieAcPppoeClientMax_Object = MibScalar
ruijieAcPppoeClientMax = _RuijieAcPppoeClientMax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 38),
    _RuijieAcPppoeClientMax_Type()
)
ruijieAcPppoeClientMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcPppoeClientMax.setStatus("current")
_RuijieAcStaActThredhold_Type = Integer32
_RuijieAcStaActThredhold_Object = MibScalar
ruijieAcStaActThredhold = _RuijieAcStaActThredhold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 39),
    _RuijieAcStaActThredhold_Type()
)
ruijieAcStaActThredhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaActThredhold.setStatus("current")
_RuijieAcStaDisactThredhold_Type = Integer32
_RuijieAcStaDisactThredhold_Object = MibScalar
ruijieAcStaDisactThredhold = _RuijieAcStaDisactThredhold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 40),
    _RuijieAcStaDisactThredhold_Type()
)
ruijieAcStaDisactThredhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaDisactThredhold.setStatus("current")
_RuijieAcStaTotalRoamThredhold_Type = Integer32
_RuijieAcStaTotalRoamThredhold_Object = MibScalar
ruijieAcStaTotalRoamThredhold = _RuijieAcStaTotalRoamThredhold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 41),
    _RuijieAcStaTotalRoamThredhold_Type()
)
ruijieAcStaTotalRoamThredhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaTotalRoamThredhold.setStatus("current")
_RuijieAcStaPerRoamThredhold_Type = Integer32
_RuijieAcStaPerRoamThredhold_Object = MibScalar
ruijieAcStaPerRoamThredhold = _RuijieAcStaPerRoamThredhold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 42),
    _RuijieAcStaPerRoamThredhold_Type()
)
ruijieAcStaPerRoamThredhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaPerRoamThredhold.setStatus("current")


class _RuijieAcStaOffLineRemainTime_Type(Integer32):
    """Custom type ruijieAcStaOffLineRemainTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_RuijieAcStaOffLineRemainTime_Type.__name__ = "Integer32"
_RuijieAcStaOffLineRemainTime_Object = MibScalar
ruijieAcStaOffLineRemainTime = _RuijieAcStaOffLineRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 43),
    _RuijieAcStaOffLineRemainTime_Type()
)
ruijieAcStaOffLineRemainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOffLineRemainTime.setStatus("current")


class _RuijieAcStaOffLineNumber_Type(Integer32):
    """Custom type ruijieAcStaOffLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RuijieAcStaOffLineNumber_Type.__name__ = "Integer32"
_RuijieAcStaOffLineNumber_Object = MibScalar
ruijieAcStaOffLineNumber = _RuijieAcStaOffLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 44),
    _RuijieAcStaOffLineNumber_Type()
)
ruijieAcStaOffLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOffLineNumber.setStatus("current")
_RuijieAcStaOffLineDelSingle_Type = MacAddress
_RuijieAcStaOffLineDelSingle_Object = MibScalar
ruijieAcStaOffLineDelSingle = _RuijieAcStaOffLineDelSingle_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 45),
    _RuijieAcStaOffLineDelSingle_Type()
)
ruijieAcStaOffLineDelSingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOffLineDelSingle.setStatus("current")


class _RuijieAcStaOffLineDelAll_Type(Integer32):
    """Custom type ruijieAcStaOffLineDelAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RuijieAcStaOffLineDelAll_Type.__name__ = "Integer32"
_RuijieAcStaOffLineDelAll_Object = MibScalar
ruijieAcStaOffLineDelAll = _RuijieAcStaOffLineDelAll_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 46),
    _RuijieAcStaOffLineDelAll_Type()
)
ruijieAcStaOffLineDelAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOffLineDelAll.setStatus("current")


class _RuijieAcRmOffLineApConfig_Type(DisplayString):
    """Custom type ruijieAcRmOffLineApConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_RuijieAcRmOffLineApConfig_Type.__name__ = "DisplayString"
_RuijieAcRmOffLineApConfig_Object = MibScalar
ruijieAcRmOffLineApConfig = _RuijieAcRmOffLineApConfig_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 47),
    _RuijieAcRmOffLineApConfig_Type()
)
ruijieAcRmOffLineApConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcRmOffLineApConfig.setStatus("current")
_RuijieAcFlowBlGroupTable_Object = MibTable
ruijieAcFlowBlGroupTable = _RuijieAcFlowBlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48)
)
if mibBuilder.loadTexts:
    ruijieAcFlowBlGroupTable.setStatus("current")
_RuijieAcFlowBlGroupEntry_Object = MibTableRow
ruijieAcFlowBlGroupEntry = _RuijieAcFlowBlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1)
)
ruijieAcFlowBlGroupEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlGroupName"),
)
if mibBuilder.loadTexts:
    ruijieAcFlowBlGroupEntry.setStatus("current")
_RuijieAcFlowBlGroupName_Type = DisplayString
_RuijieAcFlowBlGroupName_Object = MibTableColumn
ruijieAcFlowBlGroupName = _RuijieAcFlowBlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 1),
    _RuijieAcFlowBlGroupName_Type()
)
ruijieAcFlowBlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcFlowBlGroupName.setStatus("current")
_RuijieAcFlowBlApName1_Type = DisplayString
_RuijieAcFlowBlApName1_Object = MibTableColumn
ruijieAcFlowBlApName1 = _RuijieAcFlowBlApName1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 2),
    _RuijieAcFlowBlApName1_Type()
)
ruijieAcFlowBlApName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName1.setStatus("current")
_RuijieAcFlowBlApName2_Type = DisplayString
_RuijieAcFlowBlApName2_Object = MibTableColumn
ruijieAcFlowBlApName2 = _RuijieAcFlowBlApName2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 3),
    _RuijieAcFlowBlApName2_Type()
)
ruijieAcFlowBlApName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName2.setStatus("current")
_RuijieAcFlowBlApName3_Type = DisplayString
_RuijieAcFlowBlApName3_Object = MibTableColumn
ruijieAcFlowBlApName3 = _RuijieAcFlowBlApName3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 4),
    _RuijieAcFlowBlApName3_Type()
)
ruijieAcFlowBlApName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName3.setStatus("current")
_RuijieAcFlowBlApName4_Type = DisplayString
_RuijieAcFlowBlApName4_Object = MibTableColumn
ruijieAcFlowBlApName4 = _RuijieAcFlowBlApName4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 5),
    _RuijieAcFlowBlApName4_Type()
)
ruijieAcFlowBlApName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName4.setStatus("current")
_RuijieAcFlowBlApName5_Type = DisplayString
_RuijieAcFlowBlApName5_Object = MibTableColumn
ruijieAcFlowBlApName5 = _RuijieAcFlowBlApName5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 6),
    _RuijieAcFlowBlApName5_Type()
)
ruijieAcFlowBlApName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName5.setStatus("current")
_RuijieAcFlowBlApName6_Type = DisplayString
_RuijieAcFlowBlApName6_Object = MibTableColumn
ruijieAcFlowBlApName6 = _RuijieAcFlowBlApName6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 7),
    _RuijieAcFlowBlApName6_Type()
)
ruijieAcFlowBlApName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName6.setStatus("current")
_RuijieAcFlowBlApName7_Type = DisplayString
_RuijieAcFlowBlApName7_Object = MibTableColumn
ruijieAcFlowBlApName7 = _RuijieAcFlowBlApName7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 8),
    _RuijieAcFlowBlApName7_Type()
)
ruijieAcFlowBlApName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName7.setStatus("current")
_RuijieAcFlowBlApName8_Type = DisplayString
_RuijieAcFlowBlApName8_Object = MibTableColumn
ruijieAcFlowBlApName8 = _RuijieAcFlowBlApName8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 9),
    _RuijieAcFlowBlApName8_Type()
)
ruijieAcFlowBlApName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName8.setStatus("current")
_RuijieAcFlowBlApName9_Type = DisplayString
_RuijieAcFlowBlApName9_Object = MibTableColumn
ruijieAcFlowBlApName9 = _RuijieAcFlowBlApName9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 10),
    _RuijieAcFlowBlApName9_Type()
)
ruijieAcFlowBlApName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName9.setStatus("current")
_RuijieAcFlowBlApName10_Type = DisplayString
_RuijieAcFlowBlApName10_Object = MibTableColumn
ruijieAcFlowBlApName10 = _RuijieAcFlowBlApName10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 11),
    _RuijieAcFlowBlApName10_Type()
)
ruijieAcFlowBlApName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlApName10.setStatus("current")


class _RuijieAcFlowBlNum_Type(Integer32):
    """Custom type ruijieAcFlowBlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RuijieAcFlowBlNum_Type.__name__ = "Integer32"
_RuijieAcFlowBlNum_Object = MibTableColumn
ruijieAcFlowBlNum = _RuijieAcFlowBlNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 12),
    _RuijieAcFlowBlNum_Type()
)
ruijieAcFlowBlNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlNum.setStatus("current")
_RuijieAcFlowBlRS_Type = RowStatus
_RuijieAcFlowBlRS_Object = MibTableColumn
ruijieAcFlowBlRS = _RuijieAcFlowBlRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 13),
    _RuijieAcFlowBlRS_Type()
)
ruijieAcFlowBlRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlRS.setStatus("current")
_RuijieAcFlowBlEnable_Type = Integer32
_RuijieAcFlowBlEnable_Object = MibTableColumn
ruijieAcFlowBlEnable = _RuijieAcFlowBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 14),
    _RuijieAcFlowBlEnable_Type()
)
ruijieAcFlowBlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlEnable.setStatus("current")
_RuijieAcFlowBlBase_Type = Integer32
_RuijieAcFlowBlBase_Object = MibTableColumn
ruijieAcFlowBlBase = _RuijieAcFlowBlBase_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 15),
    _RuijieAcFlowBlBase_Type()
)
ruijieAcFlowBlBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlBase.setStatus("current")
_RuijieAcFlowBlIsEnable_Type = TruthValue
_RuijieAcFlowBlIsEnable_Object = MibTableColumn
ruijieAcFlowBlIsEnable = _RuijieAcFlowBlIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 48, 1, 16),
    _RuijieAcFlowBlIsEnable_Type()
)
ruijieAcFlowBlIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcFlowBlIsEnable.setStatus("current")
_RuijieAcNumBlGroupTable_Object = MibTable
ruijieAcNumBlGroupTable = _RuijieAcNumBlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49)
)
if mibBuilder.loadTexts:
    ruijieAcNumBlGroupTable.setStatus("current")
_RuijieAcNumBlGroupEntry_Object = MibTableRow
ruijieAcNumBlGroupEntry = _RuijieAcNumBlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1)
)
ruijieAcNumBlGroupEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlGroupName"),
)
if mibBuilder.loadTexts:
    ruijieAcNumBlGroupEntry.setStatus("current")
_RuijieAcNumBlGroupName_Type = DisplayString
_RuijieAcNumBlGroupName_Object = MibTableColumn
ruijieAcNumBlGroupName = _RuijieAcNumBlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 1),
    _RuijieAcNumBlGroupName_Type()
)
ruijieAcNumBlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcNumBlGroupName.setStatus("current")
_RuijieAcNumBlApName1_Type = DisplayString
_RuijieAcNumBlApName1_Object = MibTableColumn
ruijieAcNumBlApName1 = _RuijieAcNumBlApName1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 2),
    _RuijieAcNumBlApName1_Type()
)
ruijieAcNumBlApName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName1.setStatus("current")
_RuijieAcNumBlApName2_Type = DisplayString
_RuijieAcNumBlApName2_Object = MibTableColumn
ruijieAcNumBlApName2 = _RuijieAcNumBlApName2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 3),
    _RuijieAcNumBlApName2_Type()
)
ruijieAcNumBlApName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName2.setStatus("current")
_RuijieAcNumBlApName3_Type = DisplayString
_RuijieAcNumBlApName3_Object = MibTableColumn
ruijieAcNumBlApName3 = _RuijieAcNumBlApName3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 4),
    _RuijieAcNumBlApName3_Type()
)
ruijieAcNumBlApName3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName3.setStatus("current")
_RuijieAcNumBlApName4_Type = DisplayString
_RuijieAcNumBlApName4_Object = MibTableColumn
ruijieAcNumBlApName4 = _RuijieAcNumBlApName4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 5),
    _RuijieAcNumBlApName4_Type()
)
ruijieAcNumBlApName4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName4.setStatus("current")
_RuijieAcNumBlApName5_Type = DisplayString
_RuijieAcNumBlApName5_Object = MibTableColumn
ruijieAcNumBlApName5 = _RuijieAcNumBlApName5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 6),
    _RuijieAcNumBlApName5_Type()
)
ruijieAcNumBlApName5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName5.setStatus("current")
_RuijieAcNumBlApName6_Type = DisplayString
_RuijieAcNumBlApName6_Object = MibTableColumn
ruijieAcNumBlApName6 = _RuijieAcNumBlApName6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 7),
    _RuijieAcNumBlApName6_Type()
)
ruijieAcNumBlApName6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName6.setStatus("current")
_RuijieAcNumBlApName7_Type = DisplayString
_RuijieAcNumBlApName7_Object = MibTableColumn
ruijieAcNumBlApName7 = _RuijieAcNumBlApName7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 8),
    _RuijieAcNumBlApName7_Type()
)
ruijieAcNumBlApName7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName7.setStatus("current")
_RuijieAcNumBlApName8_Type = DisplayString
_RuijieAcNumBlApName8_Object = MibTableColumn
ruijieAcNumBlApName8 = _RuijieAcNumBlApName8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 9),
    _RuijieAcNumBlApName8_Type()
)
ruijieAcNumBlApName8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName8.setStatus("current")
_RuijieAcNumBlApName9_Type = DisplayString
_RuijieAcNumBlApName9_Object = MibTableColumn
ruijieAcNumBlApName9 = _RuijieAcNumBlApName9_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 10),
    _RuijieAcNumBlApName9_Type()
)
ruijieAcNumBlApName9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName9.setStatus("current")
_RuijieAcNumBlApName10_Type = DisplayString
_RuijieAcNumBlApName10_Object = MibTableColumn
ruijieAcNumBlApName10 = _RuijieAcNumBlApName10_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 11),
    _RuijieAcNumBlApName10_Type()
)
ruijieAcNumBlApName10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlApName10.setStatus("current")


class _RuijieAcNumBlNum_Type(Integer32):
    """Custom type ruijieAcNumBlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RuijieAcNumBlNum_Type.__name__ = "Integer32"
_RuijieAcNumBlNum_Object = MibTableColumn
ruijieAcNumBlNum = _RuijieAcNumBlNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 12),
    _RuijieAcNumBlNum_Type()
)
ruijieAcNumBlNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlNum.setStatus("current")
_RuijieAcNumBlRS_Type = RowStatus
_RuijieAcNumBlRS_Object = MibTableColumn
ruijieAcNumBlRS = _RuijieAcNumBlRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 13),
    _RuijieAcNumBlRS_Type()
)
ruijieAcNumBlRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlRS.setStatus("current")
_RuijieAcNumBlEnable_Type = Integer32
_RuijieAcNumBlEnable_Object = MibTableColumn
ruijieAcNumBlEnable = _RuijieAcNumBlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 14),
    _RuijieAcNumBlEnable_Type()
)
ruijieAcNumBlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlEnable.setStatus("current")
_RuijieAcNumBlIsEnable_Type = TruthValue
_RuijieAcNumBlIsEnable_Object = MibTableColumn
ruijieAcNumBlIsEnable = _RuijieAcNumBlIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 49, 1, 15),
    _RuijieAcNumBlIsEnable_Type()
)
ruijieAcNumBlIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNumBlIsEnable.setStatus("current")
_RuijieAcInAcRoamNum_Type = Integer32
_RuijieAcInAcRoamNum_Object = MibScalar
ruijieAcInAcRoamNum = _RuijieAcInAcRoamNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 50),
    _RuijieAcInAcRoamNum_Type()
)
ruijieAcInAcRoamNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcInAcRoamNum.setStatus("current")
_RuijieAcBetweenAcRoamInNum_Type = Integer32
_RuijieAcBetweenAcRoamInNum_Object = MibScalar
ruijieAcBetweenAcRoamInNum = _RuijieAcBetweenAcRoamInNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 51),
    _RuijieAcBetweenAcRoamInNum_Type()
)
ruijieAcBetweenAcRoamInNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcBetweenAcRoamInNum.setStatus("current")
_RuijieAcStaOnOverThrodOperCtrl_Type = Integer32
_RuijieAcStaOnOverThrodOperCtrl_Object = MibScalar
ruijieAcStaOnOverThrodOperCtrl = _RuijieAcStaOnOverThrodOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 52),
    _RuijieAcStaOnOverThrodOperCtrl_Type()
)
ruijieAcStaOnOverThrodOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOnOverThrodOperCtrl.setStatus("current")
_RuijieAcStaOffOverThrodOperCtrl_Type = Integer32
_RuijieAcStaOffOverThrodOperCtrl_Object = MibScalar
ruijieAcStaOffOverThrodOperCtrl = _RuijieAcStaOffOverThrodOperCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 53),
    _RuijieAcStaOffOverThrodOperCtrl_Type()
)
ruijieAcStaOffOverThrodOperCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStaOffOverThrodOperCtrl.setStatus("current")
_RuijieAcBetweenAcRoamOutNum_Type = Integer32
_RuijieAcBetweenAcRoamOutNum_Object = MibScalar
ruijieAcBetweenAcRoamOutNum = _RuijieAcBetweenAcRoamOutNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 54),
    _RuijieAcBetweenAcRoamOutNum_Type()
)
ruijieAcBetweenAcRoamOutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcBetweenAcRoamOutNum.setStatus("current")
_RuijieAcCpusageSwitch_Type = Integer32
_RuijieAcCpusageSwitch_Object = MibScalar
ruijieAcCpusageSwitch = _RuijieAcCpusageSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 55),
    _RuijieAcCpusageSwitch_Type()
)
ruijieAcCpusageSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcCpusageSwitch.setStatus("current")
_RuijieAcCpuUsageTrapTimer_Type = Integer32
_RuijieAcCpuUsageTrapTimer_Object = MibScalar
ruijieAcCpuUsageTrapTimer = _RuijieAcCpuUsageTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 56),
    _RuijieAcCpuUsageTrapTimer_Type()
)
ruijieAcCpuUsageTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcCpuUsageTrapTimer.setStatus("current")
_RuijieAcStatTrapTimer_Type = Integer32
_RuijieAcStatTrapTimer_Object = MibScalar
ruijieAcStatTrapTimer = _RuijieAcStatTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 57),
    _RuijieAcStatTrapTimer_Type()
)
ruijieAcStatTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcStatTrapTimer.setStatus("current")
_RuijieAcHeartBeat_Type = Integer32
_RuijieAcHeartBeat_Object = MibScalar
ruijieAcHeartBeat = _RuijieAcHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 58),
    _RuijieAcHeartBeat_Type()
)
ruijieAcHeartBeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcHeartBeat.setStatus("current")
_RuijieAcTotalApSupNum_Type = Integer32
_RuijieAcTotalApSupNum_Object = MibScalar
ruijieAcTotalApSupNum = _RuijieAcTotalApSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 59),
    _RuijieAcTotalApSupNum_Type()
)
ruijieAcTotalApSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTotalApSupNum.setStatus("current")
_RuijieAcTotalStaSupNum_Type = Integer32
_RuijieAcTotalStaSupNum_Object = MibScalar
ruijieAcTotalStaSupNum = _RuijieAcTotalStaSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 60),
    _RuijieAcTotalStaSupNum_Type()
)
ruijieAcTotalStaSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTotalStaSupNum.setStatus("current")
_RuijieAcTotalPppoeSupNum_Type = Integer32
_RuijieAcTotalPppoeSupNum_Object = MibScalar
ruijieAcTotalPppoeSupNum = _RuijieAcTotalPppoeSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 61),
    _RuijieAcTotalPppoeSupNum_Type()
)
ruijieAcTotalPppoeSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTotalPppoeSupNum.setStatus("current")
_RuijieAcCurTotalApSupNum_Type = Integer32
_RuijieAcCurTotalApSupNum_Object = MibScalar
ruijieAcCurTotalApSupNum = _RuijieAcCurTotalApSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 62),
    _RuijieAcCurTotalApSupNum_Type()
)
ruijieAcCurTotalApSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcCurTotalApSupNum.setStatus("current")
_RuijieAcCurTotalStaSupNum_Type = Integer32
_RuijieAcCurTotalStaSupNum_Object = MibScalar
ruijieAcCurTotalStaSupNum = _RuijieAcCurTotalStaSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 63),
    _RuijieAcCurTotalStaSupNum_Type()
)
ruijieAcCurTotalStaSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcCurTotalStaSupNum.setStatus("current")
_RuijieAcCurTotalPppoeSupNum_Type = Integer32
_RuijieAcCurTotalPppoeSupNum_Object = MibScalar
ruijieAcCurTotalPppoeSupNum = _RuijieAcCurTotalPppoeSupNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 64),
    _RuijieAcCurTotalPppoeSupNum_Type()
)
ruijieAcCurTotalPppoeSupNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcCurTotalPppoeSupNum.setStatus("current")
_RuijieAcNasId_Type = DisplayString
_RuijieAcNasId_Object = MibScalar
ruijieAcNasId = _RuijieAcNasId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 65),
    _RuijieAcNasId_Type()
)
ruijieAcNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcNasId.setStatus("current")
_RuijieAcStaLimitLicense_Type = Integer32
_RuijieAcStaLimitLicense_Object = MibScalar
ruijieAcStaLimitLicense = _RuijieAcStaLimitLicense_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 66),
    _RuijieAcStaLimitLicense_Type()
)
ruijieAcStaLimitLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaLimitLicense.setStatus("current")
_RuijieAcWtpLimitLicense_Type = Integer32
_RuijieAcWtpLimitLicense_Object = MibScalar
ruijieAcWtpLimitLicense = _RuijieAcWtpLimitLicense_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 67),
    _RuijieAcWtpLimitLicense_Type()
)
ruijieAcWtpLimitLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcWtpLimitLicense.setStatus("current")


class _RuijieAcStaIpv6Num_Type(Integer32):
    """Custom type ruijieAcStaIpv6Num based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24000),
    )


_RuijieAcStaIpv6Num_Type.__name__ = "Integer32"
_RuijieAcStaIpv6Num_Object = MibScalar
ruijieAcStaIpv6Num = _RuijieAcStaIpv6Num_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 68),
    _RuijieAcStaIpv6Num_Type()
)
ruijieAcStaIpv6Num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaIpv6Num.setStatus("current")
_RuijieAcIpv6_Type = DisplayString
_RuijieAcIpv6_Object = MibScalar
ruijieAcIpv6 = _RuijieAcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 69),
    _RuijieAcIpv6_Type()
)
ruijieAcIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcIpv6.setStatus("current")
_RuijieAcIpv6Prefix_Type = DisplayString
_RuijieAcIpv6Prefix_Object = MibScalar
ruijieAcIpv6Prefix = _RuijieAcIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 70),
    _RuijieAcIpv6Prefix_Type()
)
ruijieAcIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcIpv6Prefix.setStatus("current")


class _RuijieAcIpv6Type_Type(Integer32):
    """Custom type ruijieAcIpv6Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicase", 1),
          ("anycase", 2),
          ("multicase", 3))
    )


_RuijieAcIpv6Type_Type.__name__ = "Integer32"
_RuijieAcIpv6Type_Object = MibScalar
ruijieAcIpv6Type = _RuijieAcIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 71),
    _RuijieAcIpv6Type_Type()
)
ruijieAcIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcIpv6Type.setStatus("current")
_RuijieAcIpv6AddrType_Type = DisplayString
_RuijieAcIpv6AddrType_Object = MibScalar
ruijieAcIpv6AddrType = _RuijieAcIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 72),
    _RuijieAcIpv6AddrType_Type()
)
ruijieAcIpv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcIpv6AddrType.setStatus("current")
_RuijieAcKickClient_Type = MacAddress
_RuijieAcKickClient_Object = MibScalar
ruijieAcKickClient = _RuijieAcKickClient_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 73),
    _RuijieAcKickClient_Type()
)
ruijieAcKickClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcKickClient.setStatus("current")
_RuijieAcOpenStaNum_Type = Integer32
_RuijieAcOpenStaNum_Object = MibScalar
ruijieAcOpenStaNum = _RuijieAcOpenStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 74),
    _RuijieAcOpenStaNum_Type()
)
ruijieAcOpenStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcOpenStaNum.setStatus("current")
_RuijieAcOpenStaAbnormalDownTimes_Type = Integer32
_RuijieAcOpenStaAbnormalDownTimes_Object = MibScalar
ruijieAcOpenStaAbnormalDownTimes = _RuijieAcOpenStaAbnormalDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 75),
    _RuijieAcOpenStaAbnormalDownTimes_Type()
)
ruijieAcOpenStaAbnormalDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcOpenStaAbnormalDownTimes.setStatus("current")
_RuijieAcWepPskStaNum_Type = Integer32
_RuijieAcWepPskStaNum_Object = MibScalar
ruijieAcWepPskStaNum = _RuijieAcWepPskStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 76),
    _RuijieAcWepPskStaNum_Type()
)
ruijieAcWepPskStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcWepPskStaNum.setStatus("current")
_RuijieAcWepPskStaAbnormalDownTimes_Type = Integer32
_RuijieAcWepPskStaAbnormalDownTimes_Object = MibScalar
ruijieAcWepPskStaAbnormalDownTimes = _RuijieAcWepPskStaAbnormalDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 77),
    _RuijieAcWepPskStaAbnormalDownTimes_Type()
)
ruijieAcWepPskStaAbnormalDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcWepPskStaAbnormalDownTimes.setStatus("current")
_RuijieAcPriorStaTable_Object = MibTable
ruijieAcPriorStaTable = _RuijieAcPriorStaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 78)
)
if mibBuilder.loadTexts:
    ruijieAcPriorStaTable.setStatus("current")
_RuijieAcPriorStaEntry_Object = MibTableRow
ruijieAcPriorStaEntry = _RuijieAcPriorStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 78, 1)
)
ruijieAcPriorStaEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieAcPriorStaMac"),
)
if mibBuilder.loadTexts:
    ruijieAcPriorStaEntry.setStatus("current")
_RuijieAcPriorStaMac_Type = MacAddress
_RuijieAcPriorStaMac_Object = MibTableColumn
ruijieAcPriorStaMac = _RuijieAcPriorStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 78, 1, 1),
    _RuijieAcPriorStaMac_Type()
)
ruijieAcPriorStaMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcPriorStaMac.setStatus("current")
_RuijieAcPriorStaRowStatus_Type = RowStatus
_RuijieAcPriorStaRowStatus_Object = MibTableColumn
ruijieAcPriorStaRowStatus = _RuijieAcPriorStaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 78, 1, 2),
    _RuijieAcPriorStaRowStatus_Type()
)
ruijieAcPriorStaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcPriorStaRowStatus.setStatus("current")


class _RuijieAcMicroAPUpDownCtrl_Type(Integer32):
    """Custom type ruijieAcMicroAPUpDownCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieAcMicroAPUpDownCtrl_Type.__name__ = "Integer32"
_RuijieAcMicroAPUpDownCtrl_Object = MibScalar
ruijieAcMicroAPUpDownCtrl = _RuijieAcMicroAPUpDownCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 79),
    _RuijieAcMicroAPUpDownCtrl_Type()
)
ruijieAcMicroAPUpDownCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieAcMicroAPUpDownCtrl.setStatus("current")
_RuijieAcOfflineApNum_Type = Integer32
_RuijieAcOfflineApNum_Object = MibScalar
ruijieAcOfflineApNum = _RuijieAcOfflineApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 80),
    _RuijieAcOfflineApNum_Type()
)
ruijieAcOfflineApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcOfflineApNum.setStatus("current")
_RuijieAcTotalApNum_Type = Integer32
_RuijieAcTotalApNum_Object = MibScalar
ruijieAcTotalApNum = _RuijieAcTotalApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 81),
    _RuijieAcTotalApNum_Type()
)
ruijieAcTotalApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTotalApNum.setStatus("current")
_RuijieAcTotalMicrolApNum_Type = Integer32
_RuijieAcTotalMicrolApNum_Object = MibScalar
ruijieAcTotalMicrolApNum = _RuijieAcTotalMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 82),
    _RuijieAcTotalMicrolApNum_Type()
)
ruijieAcTotalMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcTotalMicrolApNum.setStatus("current")
_RuijieAcOnlineMicrolApNum_Type = Integer32
_RuijieAcOnlineMicrolApNum_Object = MibScalar
ruijieAcOnlineMicrolApNum = _RuijieAcOnlineMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 83),
    _RuijieAcOnlineMicrolApNum_Type()
)
ruijieAcOnlineMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcOnlineMicrolApNum.setStatus("current")
_RuijieAcOfflineMicrolApNum_Type = Integer32
_RuijieAcOfflineMicrolApNum_Object = MibScalar
ruijieAcOfflineMicrolApNum = _RuijieAcOfflineMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 84),
    _RuijieAcOfflineMicrolApNum_Type()
)
ruijieAcOfflineMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcOfflineMicrolApNum.setStatus("current")
_RuijieAcStaLinkTimes_Type = Integer32
_RuijieAcStaLinkTimes_Object = MibScalar
ruijieAcStaLinkTimes = _RuijieAcStaLinkTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 85),
    _RuijieAcStaLinkTimes_Type()
)
ruijieAcStaLinkTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaLinkTimes.setStatus("current")
_RuijieAcStaLinkSuccessTimes_Type = Integer32
_RuijieAcStaLinkSuccessTimes_Object = MibScalar
ruijieAcStaLinkSuccessTimes = _RuijieAcStaLinkSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 86),
    _RuijieAcStaLinkSuccessTimes_Type()
)
ruijieAcStaLinkSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaLinkSuccessTimes.setStatus("current")
_RuijieAcStaLinkFailTimes_Type = Integer32
_RuijieAcStaLinkFailTimes_Object = MibScalar
ruijieAcStaLinkFailTimes = _RuijieAcStaLinkFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 87),
    _RuijieAcStaLinkFailTimes_Type()
)
ruijieAcStaLinkFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaLinkFailTimes.setStatus("current")
_RuijieAcStaAuthTimes_Type = Integer32
_RuijieAcStaAuthTimes_Object = MibScalar
ruijieAcStaAuthTimes = _RuijieAcStaAuthTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 88),
    _RuijieAcStaAuthTimes_Type()
)
ruijieAcStaAuthTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaAuthTimes.setStatus("current")
_RuijieAcStaAuthSuccessTimes_Type = Integer32
_RuijieAcStaAuthSuccessTimes_Object = MibScalar
ruijieAcStaAuthSuccessTimes = _RuijieAcStaAuthSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 89),
    _RuijieAcStaAuthSuccessTimes_Type()
)
ruijieAcStaAuthSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaAuthSuccessTimes.setStatus("current")
_RuijieAcStaAuthFailTimes_Type = Integer32
_RuijieAcStaAuthFailTimes_Object = MibScalar
ruijieAcStaAuthFailTimes = _RuijieAcStaAuthFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 1, 90),
    _RuijieAcStaAuthFailTimes_Type()
)
ruijieAcStaAuthFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAcStaAuthFailTimes.setStatus("current")
_RuijieAcMgmtAcIf_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAcIf = _RuijieAcMgmtAcIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 1, 2)
)
_RuijieAcMgmtApMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtApMIBObjects = _RuijieAcMgmtApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2)
)
_RuijieAcMgmtAp_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAp = _RuijieAcMgmtAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1)
)
_RuijieApCfgTable_Object = MibTable
ruijieApCfgTable = _RuijieApCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieApCfgTable.setStatus("current")
_RuijieApCfgEntry_Object = MibTableRow
ruijieApCfgEntry = _RuijieApCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1)
)
ruijieApCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApCfgEntry.setStatus("current")
_RuijieApMacAddr_Type = MacAddress
_RuijieApMacAddr_Object = MibTableColumn
ruijieApMacAddr = _RuijieApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 1),
    _RuijieApMacAddr_Type()
)
ruijieApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMacAddr.setStatus("current")


class _RuijieApApName_Type(DisplayString):
    """Custom type ruijieApApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApApName_Type.__name__ = "DisplayString"
_RuijieApApName_Object = MibTableColumn
ruijieApApName = _RuijieApApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 2),
    _RuijieApApName_Type()
)
ruijieApApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApApName.setStatus("current")


class _RuijieApApgName_Type(DisplayString):
    """Custom type ruijieApApgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieApApgName_Type.__name__ = "DisplayString"
_RuijieApApgName_Object = MibTableColumn
ruijieApApgName = _RuijieApApgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 3),
    _RuijieApApgName_Type()
)
ruijieApApgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApApgName.setStatus("current")


class _RuijieApDiscTimer_Type(Integer32):
    """Custom type ruijieApDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 180),
    )


_RuijieApDiscTimer_Type.__name__ = "Integer32"
_RuijieApDiscTimer_Object = MibTableColumn
ruijieApDiscTimer = _RuijieApDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 4),
    _RuijieApDiscTimer_Type()
)
ruijieApDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDiscTimer.setStatus("current")


class _RuijieApEchoReqTimer_Type(Integer32):
    """Custom type ruijieApEchoReqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_RuijieApEchoReqTimer_Type.__name__ = "Integer32"
_RuijieApEchoReqTimer_Object = MibTableColumn
ruijieApEchoReqTimer = _RuijieApEchoReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 5),
    _RuijieApEchoReqTimer_Type()
)
ruijieApEchoReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApEchoReqTimer.setStatus("current")


class _RuijieApEroReportTimer_Type(Integer32):
    """Custom type ruijieApEroReportTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1080),
    )


_RuijieApEroReportTimer_Type.__name__ = "Integer32"
_RuijieApEroReportTimer_Object = MibTableColumn
ruijieApEroReportTimer = _RuijieApEroReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 6),
    _RuijieApEroReportTimer_Type()
)
ruijieApEroReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApEroReportTimer.setStatus("current")


class _RuijieApStaTimeoutTimer_Type(Integer32):
    """Custom type ruijieApStaTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2700),
    )


_RuijieApStaTimeoutTimer_Type.__name__ = "Integer32"
_RuijieApStaTimeoutTimer_Object = MibTableColumn
ruijieApStaTimeoutTimer = _RuijieApStaTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 7),
    _RuijieApStaTimeoutTimer_Type()
)
ruijieApStaTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApStaTimeoutTimer.setStatus("current")


class _RuijieApStatisticsTimer_Type(Integer32):
    """Custom type ruijieApStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieApStatisticsTimer_Type.__name__ = "Integer32"
_RuijieApStatisticsTimer_Object = MibTableColumn
ruijieApStatisticsTimer = _RuijieApStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 8),
    _RuijieApStatisticsTimer_Type()
)
ruijieApStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApStatisticsTimer.setStatus("current")


class _RuijieApFallback_Type(Integer32):
    """Custom type ruijieApFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieApFallback_Type.__name__ = "Integer32"
_RuijieApFallback_Object = MibTableColumn
ruijieApFallback = _RuijieApFallback_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 9),
    _RuijieApFallback_Type()
)
ruijieApFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApFallback.setStatus("current")


class _RuijieApImageId_Type(DisplayString):
    """Custom type ruijieApImageId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuijieApImageId_Type.__name__ = "DisplayString"
_RuijieApImageId_Object = MibTableColumn
ruijieApImageId = _RuijieApImageId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 10),
    _RuijieApImageId_Type()
)
ruijieApImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApImageId.setStatus("current")


class _RuijieApIpDhcp_Type(Integer32):
    """Custom type ruijieApIpDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApIpDhcp_Type.__name__ = "Integer32"
_RuijieApIpDhcp_Object = MibTableColumn
ruijieApIpDhcp = _RuijieApIpDhcp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 11),
    _RuijieApIpDhcp_Type()
)
ruijieApIpDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApIpDhcp.setStatus("current")


class _RuijieApLocation_Type(DisplayString):
    """Custom type ruijieApLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieApLocation_Type.__name__ = "DisplayString"
_RuijieApLocation_Object = MibTableColumn
ruijieApLocation = _RuijieApLocation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 12),
    _RuijieApLocation_Type()
)
ruijieApLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApLocation.setStatus("current")


class _RuijieApWpsMfp_Type(Integer32):
    """Custom type ruijieApWpsMfp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApWpsMfp_Type.__name__ = "Integer32"
_RuijieApWpsMfp_Object = MibTableColumn
ruijieApWpsMfp = _RuijieApWpsMfp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 13),
    _RuijieApWpsMfp_Type()
)
ruijieApWpsMfp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApWpsMfp.setStatus("current")


class _RuijieApLastRebootReason_Type(Integer32):
    """Custom type ruijieApLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupport", 0),
          ("acInit", 1),
          ("linkFail", 2),
          ("sWFail", 3),
          ("hWFail", 4),
          ("otherFail", 5),
          ("unknown", 255))
    )


_RuijieApLastRebootReason_Type.__name__ = "Integer32"
_RuijieApLastRebootReason_Object = MibTableColumn
ruijieApLastRebootReason = _RuijieApLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 14),
    _RuijieApLastRebootReason_Type()
)
ruijieApLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApLastRebootReason.setStatus("current")


class _RuijieApEthernetIfName_Type(DisplayString):
    """Custom type ruijieApEthernetIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieApEthernetIfName_Type.__name__ = "DisplayString"
_RuijieApEthernetIfName_Object = MibTableColumn
ruijieApEthernetIfName = _RuijieApEthernetIfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 15),
    _RuijieApEthernetIfName_Type()
)
ruijieApEthernetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfName.setStatus("current")
_RuijieApEthernetIfMacAddress_Type = MacAddress
_RuijieApEthernetIfMacAddress_Object = MibTableColumn
ruijieApEthernetIfMacAddress = _RuijieApEthernetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 16),
    _RuijieApEthernetIfMacAddress_Type()
)
ruijieApEthernetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfMacAddress.setStatus("current")
_RuijieApEthernetIfAdminStatus_Type = Integer32
_RuijieApEthernetIfAdminStatus_Object = MibTableColumn
ruijieApEthernetIfAdminStatus = _RuijieApEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 17),
    _RuijieApEthernetIfAdminStatus_Type()
)
ruijieApEthernetIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfAdminStatus.setStatus("current")
_RuijieApEthernetIfOperStatus_Type = Integer32
_RuijieApEthernetIfOperStatus_Object = MibTableColumn
ruijieApEthernetIfOperStatus = _RuijieApEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 18),
    _RuijieApEthernetIfOperStatus_Type()
)
ruijieApEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfOperStatus.setStatus("current")
_RuijieApEthernetIfRxUcastPkts_Type = Counter32
_RuijieApEthernetIfRxUcastPkts_Object = MibTableColumn
ruijieApEthernetIfRxUcastPkts = _RuijieApEthernetIfRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 19),
    _RuijieApEthernetIfRxUcastPkts_Type()
)
ruijieApEthernetIfRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxUcastPkts.setUnits("packets")
_RuijieApEthernetIfRxNUcastPkts_Type = Counter32
_RuijieApEthernetIfRxNUcastPkts_Object = MibTableColumn
ruijieApEthernetIfRxNUcastPkts = _RuijieApEthernetIfRxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 20),
    _RuijieApEthernetIfRxNUcastPkts_Type()
)
ruijieApEthernetIfRxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxNUcastPkts.setUnits("packets")
_RuijieApEthernetIfTxUcastPkts_Type = Counter32
_RuijieApEthernetIfTxUcastPkts_Object = MibTableColumn
ruijieApEthernetIfTxUcastPkts = _RuijieApEthernetIfTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 21),
    _RuijieApEthernetIfTxUcastPkts_Type()
)
ruijieApEthernetIfTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxUcastPkts.setUnits("packets")
_RuijieApEthernetIfTxNUcastPkts_Type = Counter32
_RuijieApEthernetIfTxNUcastPkts_Object = MibTableColumn
ruijieApEthernetIfTxNUcastPkts = _RuijieApEthernetIfTxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 22),
    _RuijieApEthernetIfTxNUcastPkts_Type()
)
ruijieApEthernetIfTxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxNUcastPkts.setUnits("packets")


class _RuijieApEthernetIfDuplex_Type(Integer32):
    """Custom type ruijieApEthernetIfDuplex based on Integer32"""
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
        *(("unknown", 1),
          ("halfduplex", 2),
          ("fullduplex", 3),
          ("auto", 4))
    )


_RuijieApEthernetIfDuplex_Type.__name__ = "Integer32"
_RuijieApEthernetIfDuplex_Object = MibTableColumn
ruijieApEthernetIfDuplex = _RuijieApEthernetIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 23),
    _RuijieApEthernetIfDuplex_Type()
)
ruijieApEthernetIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfDuplex.setStatus("current")
_RuijieApEthernetIfLinkSpeed_Type = Integer32
_RuijieApEthernetIfLinkSpeed_Object = MibTableColumn
ruijieApEthernetIfLinkSpeed = _RuijieApEthernetIfLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 24),
    _RuijieApEthernetIfLinkSpeed_Type()
)
ruijieApEthernetIfLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfLinkSpeed.setStatus("current")


class _RuijieApEthernetIfPOEPower_Type(Integer32):
    """Custom type ruijieApEthernetIfPOEPower based on Integer32"""
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
          ("drawn", 2),
          ("notdrawn", 3))
    )


_RuijieApEthernetIfPOEPower_Type.__name__ = "Integer32"
_RuijieApEthernetIfPOEPower_Object = MibTableColumn
ruijieApEthernetIfPOEPower = _RuijieApEthernetIfPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 25),
    _RuijieApEthernetIfPOEPower_Type()
)
ruijieApEthernetIfPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfPOEPower.setStatus("current")


class _RuijieApAdminStatus_Type(Integer32):
    """Custom type ruijieApAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RuijieApAdminStatus_Type.__name__ = "Integer32"
_RuijieApAdminStatus_Object = MibTableColumn
ruijieApAdminStatus = _RuijieApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 26),
    _RuijieApAdminStatus_Type()
)
ruijieApAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApAdminStatus.setStatus("current")
_RuijieApEthernetIfRxBoardPkts_Type = Counter32
_RuijieApEthernetIfRxBoardPkts_Object = MibTableColumn
ruijieApEthernetIfRxBoardPkts = _RuijieApEthernetIfRxBoardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 27),
    _RuijieApEthernetIfRxBoardPkts_Type()
)
ruijieApEthernetIfRxBoardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxBoardPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxBoardPkts.setUnits("packets")
_RuijieApEthernetIfRxMultiPkts_Type = Counter32
_RuijieApEthernetIfRxMultiPkts_Object = MibTableColumn
ruijieApEthernetIfRxMultiPkts = _RuijieApEthernetIfRxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 28),
    _RuijieApEthernetIfRxMultiPkts_Type()
)
ruijieApEthernetIfRxMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxMultiPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfRxMultiPkts.setUnits("packets")
_RuijieApEthernetIfTxBoardPkts_Type = Counter32
_RuijieApEthernetIfTxBoardPkts_Object = MibTableColumn
ruijieApEthernetIfTxBoardPkts = _RuijieApEthernetIfTxBoardPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 29),
    _RuijieApEthernetIfTxBoardPkts_Type()
)
ruijieApEthernetIfTxBoardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxBoardPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxBoardPkts.setUnits("packets")
_RuijieApEthernetIfTxMultiPkts_Type = Counter32
_RuijieApEthernetIfTxMultiPkts_Object = MibTableColumn
ruijieApEthernetIfTxMultiPkts = _RuijieApEthernetIfTxMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 30),
    _RuijieApEthernetIfTxMultiPkts_Type()
)
ruijieApEthernetIfTxMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxMultiPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfTxMultiPkts.setUnits("packets")
_RuijieApEthernetIfDropPkts_Type = Counter32
_RuijieApEthernetIfDropPkts_Object = MibTableColumn
ruijieApEthernetIfDropPkts = _RuijieApEthernetIfDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 31),
    _RuijieApEthernetIfDropPkts_Type()
)
ruijieApEthernetIfDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEthernetIfDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    ruijieApEthernetIfDropPkts.setUnits("packets")
_RuijieApSn_Type = DisplayString
_RuijieApSn_Object = MibTableColumn
ruijieApSn = _RuijieApSn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 32),
    _RuijieApSn_Type()
)
ruijieApSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApSn.setStatus("current")
_RuijieApIp_Type = IpAddress
_RuijieApIp_Object = MibTableColumn
ruijieApIp = _RuijieApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 33),
    _RuijieApIp_Type()
)
ruijieApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIp.setStatus("current")
_RuijieApStaNum_Type = Integer32
_RuijieApStaNum_Object = MibTableColumn
ruijieApStaNum = _RuijieApStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 34),
    _RuijieApStaNum_Type()
)
ruijieApStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApStaNum.setStatus("current")


class _RuijieApToFat_Type(Integer32):
    """Custom type ruijieApToFat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApToFat_Type.__name__ = "Integer32"
_RuijieApToFat_Object = MibTableColumn
ruijieApToFat = _RuijieApToFat_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 35),
    _RuijieApToFat_Type()
)
ruijieApToFat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApToFat.setStatus("current")


class _RuijieApId_Type(Integer32):
    """Custom type ruijieApId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_RuijieApId_Type.__name__ = "Integer32"
_RuijieApId_Object = MibTableColumn
ruijieApId = _RuijieApId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 36),
    _RuijieApId_Type()
)
ruijieApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApId.setStatus("current")
_RuijieApSwVer_Type = DisplayString
_RuijieApSwVer_Object = MibTableColumn
ruijieApSwVer = _RuijieApSwVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 37),
    _RuijieApSwVer_Type()
)
ruijieApSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApSwVer.setStatus("current")
_RuijieApBootVer_Type = DisplayString
_RuijieApBootVer_Object = MibTableColumn
ruijieApBootVer = _RuijieApBootVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 38),
    _RuijieApBootVer_Type()
)
ruijieApBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApBootVer.setStatus("current")
_RuijieApPID_Type = DisplayString
_RuijieApPID_Object = MibTableColumn
ruijieApPID = _RuijieApPID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 39),
    _RuijieApPID_Type()
)
ruijieApPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApPID.setStatus("current")
_RuijieApHwVer_Type = DisplayString
_RuijieApHwVer_Object = MibTableColumn
ruijieApHwVer = _RuijieApHwVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 40),
    _RuijieApHwVer_Type()
)
ruijieApHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApHwVer.setStatus("current")


class _RuijieApStaLimit_Type(Integer32):
    """Custom type ruijieApStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RuijieApStaLimit_Type.__name__ = "Integer32"
_RuijieApStaLimit_Object = MibTableColumn
ruijieApStaLimit = _RuijieApStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 41),
    _RuijieApStaLimit_Type()
)
ruijieApStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApStaLimit.setStatus("current")


class _RuijieApFactoryDefault_Type(Integer32):
    """Custom type ruijieApFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_RuijieApFactoryDefault_Type.__name__ = "Integer32"
_RuijieApFactoryDefault_Object = MibTableColumn
ruijieApFactoryDefault = _RuijieApFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 42),
    _RuijieApFactoryDefault_Type()
)
ruijieApFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApFactoryDefault.setStatus("current")
_RuijieApCpuUsageTrapTimer_Type = Integer32
_RuijieApCpuUsageTrapTimer_Object = MibTableColumn
ruijieApCpuUsageTrapTimer = _RuijieApCpuUsageTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 43),
    _RuijieApCpuUsageTrapTimer_Type()
)
ruijieApCpuUsageTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApCpuUsageTrapTimer.setStatus("current")
_RuijieApStatTrapTimer_Type = Integer32
_RuijieApStatTrapTimer_Object = MibTableColumn
ruijieApStatTrapTimer = _RuijieApStatTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 44),
    _RuijieApStatTrapTimer_Type()
)
ruijieApStatTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApStatTrapTimer.setStatus("current")
_RuijieApLinkOnTimeInterval_Type = Integer32
_RuijieApLinkOnTimeInterval_Object = MibTableColumn
ruijieApLinkOnTimeInterval = _RuijieApLinkOnTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 45),
    _RuijieApLinkOnTimeInterval_Type()
)
ruijieApLinkOnTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApLinkOnTimeInterval.setStatus("current")
_RuijieApNetId_Type = DisplayString
_RuijieApNetId_Object = MibTableColumn
ruijieApNetId = _RuijieApNetId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 46),
    _RuijieApNetId_Type()
)
ruijieApNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApNetId.setStatus("current")
_RuijieApUptime_Type = DisplayString
_RuijieApUptime_Object = MibTableColumn
ruijieApUptime = _RuijieApUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 47),
    _RuijieApUptime_Type()
)
ruijieApUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApUptime.setStatus("current")
_RuijieApState_Type = Integer32
_RuijieApState_Object = MibTableColumn
ruijieApState = _RuijieApState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 48),
    _RuijieApState_Type()
)
ruijieApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApState.setStatus("current")
_RuijieApNasId_Type = DisplayString
_RuijieApNasId_Object = MibTableColumn
ruijieApNasId = _RuijieApNasId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 49),
    _RuijieApNasId_Type()
)
ruijieApNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApNasId.setStatus("current")
_RuijieApCoverArea_Type = Integer32
_RuijieApCoverArea_Object = MibTableColumn
ruijieApCoverArea = _RuijieApCoverArea_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 50),
    _RuijieApCoverArea_Type()
)
ruijieApCoverArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApCoverArea.setStatus("current")
_RuijieApLinkOnTimeIntervalMs_Type = TimeTicks
_RuijieApLinkOnTimeIntervalMs_Object = MibTableColumn
ruijieApLinkOnTimeIntervalMs = _RuijieApLinkOnTimeIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 51),
    _RuijieApLinkOnTimeIntervalMs_Type()
)
ruijieApLinkOnTimeIntervalMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApLinkOnTimeIntervalMs.setStatus("current")
_RuijieApUptimeMs_Type = TimeTicks
_RuijieApUptimeMs_Object = MibTableColumn
ruijieApUptimeMs = _RuijieApUptimeMs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 52),
    _RuijieApUptimeMs_Type()
)
ruijieApUptimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApUptimeMs.setStatus("current")
_RuijieApHbUptimeMs_Type = TimeTicks
_RuijieApHbUptimeMs_Object = MibTableColumn
ruijieApHbUptimeMs = _RuijieApHbUptimeMs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 53),
    _RuijieApHbUptimeMs_Type()
)
ruijieApHbUptimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApHbUptimeMs.setStatus("current")
_RuijieApIpv6_Type = InetAddress
_RuijieApIpv6_Object = MibTableColumn
ruijieApIpv6 = _RuijieApIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 54),
    _RuijieApIpv6_Type()
)
ruijieApIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6.setStatus("current")
_RuijieApIpv6Prefix_Type = DisplayString
_RuijieApIpv6Prefix_Object = MibTableColumn
ruijieApIpv6Prefix = _RuijieApIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 55),
    _RuijieApIpv6Prefix_Type()
)
ruijieApIpv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6Prefix.setStatus("current")
_RuijieApIpv6PrefixLen_Type = Integer32
_RuijieApIpv6PrefixLen_Object = MibTableColumn
ruijieApIpv6PrefixLen = _RuijieApIpv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 56),
    _RuijieApIpv6PrefixLen_Type()
)
ruijieApIpv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6PrefixLen.setStatus("current")


class _RuijieApIpv6Type_Type(Integer32):
    """Custom type ruijieApIpv6Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicase", 1),
          ("anycase", 2),
          ("multicase", 3))
    )


_RuijieApIpv6Type_Type.__name__ = "Integer32"
_RuijieApIpv6Type_Object = MibTableColumn
ruijieApIpv6Type = _RuijieApIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 57),
    _RuijieApIpv6Type_Type()
)
ruijieApIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6Type.setStatus("current")
_RuijieApIpv6Gateway_Type = DisplayString
_RuijieApIpv6Gateway_Object = MibTableColumn
ruijieApIpv6Gateway = _RuijieApIpv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 58),
    _RuijieApIpv6Gateway_Type()
)
ruijieApIpv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6Gateway.setStatus("current")
_RuijieApIpv6StaNum_Type = Integer32
_RuijieApIpv6StaNum_Object = MibTableColumn
ruijieApIpv6StaNum = _RuijieApIpv6StaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 59),
    _RuijieApIpv6StaNum_Type()
)
ruijieApIpv6StaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIpv6StaNum.setStatus("current")


class _RuijieApMacAddrColon_Type(DisplayString):
    """Custom type ruijieApMacAddrColon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApMacAddrColon_Type.__name__ = "DisplayString"
_RuijieApMacAddrColon_Object = MibTableColumn
ruijieApMacAddrColon = _RuijieApMacAddrColon_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 60),
    _RuijieApMacAddrColon_Type()
)
ruijieApMacAddrColon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMacAddrColon.setStatus("current")


class _RuijieApMacAddrLine_Type(DisplayString):
    """Custom type ruijieApMacAddrLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApMacAddrLine_Type.__name__ = "DisplayString"
_RuijieApMacAddrLine_Object = MibTableColumn
ruijieApMacAddrLine = _RuijieApMacAddrLine_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 61),
    _RuijieApMacAddrLine_Type()
)
ruijieApMacAddrLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMacAddrLine.setStatus("current")


class _RuijieApMacAddrDot_Type(DisplayString):
    """Custom type ruijieApMacAddrDot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_RuijieApMacAddrDot_Type.__name__ = "DisplayString"
_RuijieApMacAddrDot_Object = MibTableColumn
ruijieApMacAddrDot = _RuijieApMacAddrDot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 62),
    _RuijieApMacAddrDot_Type()
)
ruijieApMacAddrDot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMacAddrDot.setStatus("current")
_RuijieApEchoRequestCnt_Type = Counter32
_RuijieApEchoRequestCnt_Object = MibTableColumn
ruijieApEchoRequestCnt = _RuijieApEchoRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 63),
    _RuijieApEchoRequestCnt_Type()
)
ruijieApEchoRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEchoRequestCnt.setStatus("current")
_RuijieApEchoResponseDropCnt_Type = Counter32
_RuijieApEchoResponseDropCnt_Object = MibTableColumn
ruijieApEchoResponseDropCnt = _RuijieApEchoResponseDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 64),
    _RuijieApEchoResponseDropCnt_Type()
)
ruijieApEchoResponseDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEchoResponseDropCnt.setStatus("current")
_RuijieApEchoDelayTimeMS_Type = Integer32
_RuijieApEchoDelayTimeMS_Object = MibTableColumn
ruijieApEchoDelayTimeMS = _RuijieApEchoDelayTimeMS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 65),
    _RuijieApEchoDelayTimeMS_Type()
)
ruijieApEchoDelayTimeMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApEchoDelayTimeMS.setStatus("current")
_RuijieApIsIsharePlus_Type = Integer32
_RuijieApIsIsharePlus_Object = MibTableColumn
ruijieApIsIsharePlus = _RuijieApIsIsharePlus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 66),
    _RuijieApIsIsharePlus_Type()
)
ruijieApIsIsharePlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApIsIsharePlus.setStatus("current")
_RuijieApTotalMicrolApNum_Type = Integer32
_RuijieApTotalMicrolApNum_Object = MibTableColumn
ruijieApTotalMicrolApNum = _RuijieApTotalMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 67),
    _RuijieApTotalMicrolApNum_Type()
)
ruijieApTotalMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApTotalMicrolApNum.setStatus("current")
_RuijieApOnlineMicrolApNum_Type = Integer32
_RuijieApOnlineMicrolApNum_Object = MibTableColumn
ruijieApOnlineMicrolApNum = _RuijieApOnlineMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 68),
    _RuijieApOnlineMicrolApNum_Type()
)
ruijieApOnlineMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOnlineMicrolApNum.setStatus("current")
_RuijieApOfflineMicrolApNum_Type = Integer32
_RuijieApOfflineMicrolApNum_Object = MibTableColumn
ruijieApOfflineMicrolApNum = _RuijieApOfflineMicrolApNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 69),
    _RuijieApOfflineMicrolApNum_Type()
)
ruijieApOfflineMicrolApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOfflineMicrolApNum.setStatus("current")
_RuijieApStateTime_Type = DisplayString
_RuijieApStateTime_Object = MibTableColumn
ruijieApStateTime = _RuijieApStateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 1, 1, 70),
    _RuijieApStateTime_Type()
)
ruijieApStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApStateTime.setStatus("current")
_RuijieApCfgRadioTable_Object = MibTable
ruijieApCfgRadioTable = _RuijieApCfgRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieApCfgRadioTable.setStatus("current")
_RuijieApCfgRadioEntry_Object = MibTableRow
ruijieApCfgRadioEntry = _RuijieApCfgRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1)
)
ruijieApCfgRadioEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
)
if mibBuilder.loadTexts:
    ruijieApCfgRadioEntry.setStatus("current")


class _RuijieApCfgRadioId_Type(Integer32):
    """Custom type ruijieApCfgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_RuijieApCfgRadioId_Type.__name__ = "Integer32"
_RuijieApCfgRadioId_Object = MibTableColumn
ruijieApCfgRadioId = _RuijieApCfgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 1),
    _RuijieApCfgRadioId_Type()
)
ruijieApCfgRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApCfgRadioId.setStatus("current")


class _RuijieApRadioEn_Type(Integer32):
    """Custom type ruijieApRadioEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApRadioEn_Type.__name__ = "Integer32"
_RuijieApRadioEn_Object = MibTableColumn
ruijieApRadioEn = _RuijieApRadioEn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 2),
    _RuijieApRadioEn_Type()
)
ruijieApRadioEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApRadioEn.setStatus("current")


class _RuijieApTxPower_Type(Integer32):
    """Custom type ruijieApTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuijieApTxPower_Type.__name__ = "Integer32"
_RuijieApTxPower_Object = MibTableColumn
ruijieApTxPower = _RuijieApTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 3),
    _RuijieApTxPower_Type()
)
ruijieApTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApTxPower.setStatus("current")


class _RuijieApDtimPeriod_Type(Integer32):
    """Custom type ruijieApDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijieApDtimPeriod_Type.__name__ = "Integer32"
_RuijieApDtimPeriod_Object = MibTableColumn
ruijieApDtimPeriod = _RuijieApDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 4),
    _RuijieApDtimPeriod_Type()
)
ruijieApDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApDtimPeriod.setStatus("current")


class _RuijieApBeaconPeriod_Type(Integer32):
    """Custom type ruijieApBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_RuijieApBeaconPeriod_Type.__name__ = "Integer32"
_RuijieApBeaconPeriod_Object = MibTableColumn
ruijieApBeaconPeriod = _RuijieApBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 5),
    _RuijieApBeaconPeriod_Type()
)
ruijieApBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApBeaconPeriod.setStatus("current")


class _RuijieApCountry_Type(DisplayString):
    """Custom type ruijieApCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RuijieApCountry_Type.__name__ = "DisplayString"
_RuijieApCountry_Object = MibTableColumn
ruijieApCountry = _RuijieApCountry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 6),
    _RuijieApCountry_Type()
)
ruijieApCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApCountry.setStatus("current")


class _RuijieApPreaShort_Type(Integer32):
    """Custom type ruijieApPreaShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApPreaShort_Type.__name__ = "Integer32"
_RuijieApPreaShort_Object = MibTableColumn
ruijieApPreaShort = _RuijieApPreaShort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 7),
    _RuijieApPreaShort_Type()
)
ruijieApPreaShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApPreaShort.setStatus("current")
_RuijieApRadioBssid_Type = MacAddress
_RuijieApRadioBssid_Object = MibTableColumn
ruijieApRadioBssid = _RuijieApRadioBssid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 8),
    _RuijieApRadioBssid_Type()
)
ruijieApRadioBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadioBssid.setStatus("current")


class _RuijieApTxPowerLevel_Type(Integer32):
    """Custom type ruijieApTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RuijieApTxPowerLevel_Type.__name__ = "Integer32"
_RuijieApTxPowerLevel_Object = MibTableColumn
ruijieApTxPowerLevel = _RuijieApTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 9),
    _RuijieApTxPowerLevel_Type()
)
ruijieApTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApTxPowerLevel.setStatus("current")


class _RuijieApTxPowerGlobal_Type(Integer32):
    """Custom type ruijieApTxPowerGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApTxPowerGlobal_Type.__name__ = "Integer32"
_RuijieApTxPowerGlobal_Object = MibTableColumn
ruijieApTxPowerGlobal = _RuijieApTxPowerGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 10),
    _RuijieApTxPowerGlobal_Type()
)
ruijieApTxPowerGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApTxPowerGlobal.setStatus("current")


class _RuijieApCurChan_Type(Integer32):
    """Custom type ruijieApCurChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 165),
    )


_RuijieApCurChan_Type.__name__ = "Integer32"
_RuijieApCurChan_Object = MibTableColumn
ruijieApCurChan = _RuijieApCurChan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 11),
    _RuijieApCurChan_Type()
)
ruijieApCurChan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApCurChan.setStatus("current")


class _RuijieApRfGlobal_Type(Integer32):
    """Custom type ruijieApRfGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApRfGlobal_Type.__name__ = "Integer32"
_RuijieApRfGlobal_Object = MibTableColumn
ruijieApRfGlobal = _RuijieApRfGlobal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 12),
    _RuijieApRfGlobal_Type()
)
ruijieApRfGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApRfGlobal.setStatus("current")


class _RuijieApRadioType_Type(Integer32):
    """Custom type ruijieApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieApRadioType_Type.__name__ = "Integer32"
_RuijieApRadioType_Object = MibTableColumn
ruijieApRadioType = _RuijieApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 13),
    _RuijieApRadioType_Type()
)
ruijieApRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApRadioType.setStatus("current")


class _RuijieApRadio11bSup_Type(Integer32):
    """Custom type ruijieApRadio11bSup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieApRadio11bSup_Type.__name__ = "Integer32"
_RuijieApRadio11bSup_Object = MibTableColumn
ruijieApRadio11bSup = _RuijieApRadio11bSup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 14),
    _RuijieApRadio11bSup_Type()
)
ruijieApRadio11bSup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadio11bSup.setStatus("current")
_RuijieApMaxTxPower_Type = Integer32
_RuijieApMaxTxPower_Object = MibTableColumn
ruijieApMaxTxPower = _RuijieApMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 15),
    _RuijieApMaxTxPower_Type()
)
ruijieApMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMaxTxPower.setStatus("current")
_RuijieApMinTxPower_Type = Integer32
_RuijieApMinTxPower_Object = MibTableColumn
ruijieApMinTxPower = _RuijieApMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 16),
    _RuijieApMinTxPower_Type()
)
ruijieApMinTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMinTxPower.setStatus("current")
_RuijieApCurTxPower_Type = Integer32
_RuijieApCurTxPower_Object = MibTableColumn
ruijieApCurTxPower = _RuijieApCurTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 17),
    _RuijieApCurTxPower_Type()
)
ruijieApCurTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApCurTxPower.setStatus("current")
_RuijieApMaxTxPowerPer_Type = Integer32
_RuijieApMaxTxPowerPer_Object = MibTableColumn
ruijieApMaxTxPowerPer = _RuijieApMaxTxPowerPer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 18),
    _RuijieApMaxTxPowerPer_Type()
)
ruijieApMaxTxPowerPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMaxTxPowerPer.setStatus("current")
_RuijieApMinTxPowerPer_Type = Integer32
_RuijieApMinTxPowerPer_Object = MibTableColumn
ruijieApMinTxPowerPer = _RuijieApMinTxPowerPer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 2, 1, 19),
    _RuijieApMinTxPowerPer_Type()
)
ruijieApMinTxPowerPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMinTxPowerPer.setStatus("current")
_RuijieApRadioRateCfgTable_Object = MibTable
ruijieApRadioRateCfgTable = _RuijieApRadioRateCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieApRadioRateCfgTable.setStatus("current")
_RuijieApRadioRateCfgEntry_Object = MibTableRow
ruijieApRadioRateCfgEntry = _RuijieApRadioRateCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 3, 1)
)
ruijieApRadioRateCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApCfgRadioId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApRadioRate"),
)
if mibBuilder.loadTexts:
    ruijieApRadioRateCfgEntry.setStatus("current")


class _RuijieApRadioRate_Type(Integer32):
    """Custom type ruijieApRadioRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuijieApRadioRate_Type.__name__ = "Integer32"
_RuijieApRadioRate_Object = MibTableColumn
ruijieApRadioRate = _RuijieApRadioRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 3, 1, 1),
    _RuijieApRadioRate_Type()
)
ruijieApRadioRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApRadioRate.setStatus("current")


class _RuijieApRadioRateType_Type(Integer32):
    """Custom type ruijieApRadioRateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieApRadioRateType_Type.__name__ = "Integer32"
_RuijieApRadioRateType_Object = MibTableColumn
ruijieApRadioRateType = _RuijieApRadioRateType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 3, 1, 2),
    _RuijieApRadioRateType_Type()
)
ruijieApRadioRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApRadioRateType.setStatus("current")
_RuijieApStaticIpCfgTable_Object = MibTable
ruijieApStaticIpCfgTable = _RuijieApStaticIpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieApStaticIpCfgTable.setStatus("current")
_RuijieApStaticIpCfgEntry_Object = MibTableRow
ruijieApStaticIpCfgEntry = _RuijieApStaticIpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4, 1)
)
ruijieApStaticIpCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApStaticIpCfgEntry.setStatus("current")
_RuijieApIpAddr_Type = IpAddress
_RuijieApIpAddr_Object = MibTableColumn
ruijieApIpAddr = _RuijieApIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4, 1, 1),
    _RuijieApIpAddr_Type()
)
ruijieApIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApIpAddr.setStatus("current")
_RuijieApIpMask_Type = IpAddress
_RuijieApIpMask_Object = MibTableColumn
ruijieApIpMask = _RuijieApIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4, 1, 2),
    _RuijieApIpMask_Type()
)
ruijieApIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApIpMask.setStatus("current")
_RuijieApIpGetway_Type = IpAddress
_RuijieApIpGetway_Object = MibTableColumn
ruijieApIpGetway = _RuijieApIpGetway_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4, 1, 3),
    _RuijieApIpGetway_Type()
)
ruijieApIpGetway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApIpGetway.setStatus("current")
_RuijieApStaticIpRS_Type = RowStatus
_RuijieApStaticIpRS_Object = MibTableColumn
ruijieApStaticIpRS = _RuijieApStaticIpRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 4, 1, 4),
    _RuijieApStaticIpRS_Type()
)
ruijieApStaticIpRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApStaticIpRS.setStatus("current")
_RuijieApOfflineTable_Object = MibTable
ruijieApOfflineTable = _RuijieApOfflineTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieApOfflineTable.setStatus("current")
_RuijieApOfflineEntry_Object = MibTableRow
ruijieApOfflineEntry = _RuijieApOfflineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1)
)
ruijieApOfflineEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApOffMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApOfflineEntry.setStatus("current")
_RuijieApOfftime_Type = Integer32
_RuijieApOfftime_Object = MibTableColumn
ruijieApOfftime = _RuijieApOfftime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 1),
    _RuijieApOfftime_Type()
)
ruijieApOfftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOfftime.setStatus("current")


class _RuijieApOffApName_Type(DisplayString):
    """Custom type ruijieApOffApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieApOffApName_Type.__name__ = "DisplayString"
_RuijieApOffApName_Object = MibTableColumn
ruijieApOffApName = _RuijieApOffApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 2),
    _RuijieApOffApName_Type()
)
ruijieApOffApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffApName.setStatus("current")
_RuijieApOffMacAddr_Type = MacAddress
_RuijieApOffMacAddr_Object = MibTableColumn
ruijieApOffMacAddr = _RuijieApOffMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 3),
    _RuijieApOffMacAddr_Type()
)
ruijieApOffMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffMacAddr.setStatus("current")
_RuijieApOffIp_Type = IpAddress
_RuijieApOffIp_Object = MibTableColumn
ruijieApOffIp = _RuijieApOffIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 4),
    _RuijieApOffIp_Type()
)
ruijieApOffIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffIp.setStatus("current")


class _RuijieApOffMacAddrColon_Type(DisplayString):
    """Custom type ruijieApOffMacAddrColon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApOffMacAddrColon_Type.__name__ = "DisplayString"
_RuijieApOffMacAddrColon_Object = MibTableColumn
ruijieApOffMacAddrColon = _RuijieApOffMacAddrColon_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 5),
    _RuijieApOffMacAddrColon_Type()
)
ruijieApOffMacAddrColon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffMacAddrColon.setStatus("current")


class _RuijieApOffMacAddrLine_Type(DisplayString):
    """Custom type ruijieApOffMacAddrLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApOffMacAddrLine_Type.__name__ = "DisplayString"
_RuijieApOffMacAddrLine_Object = MibTableColumn
ruijieApOffMacAddrLine = _RuijieApOffMacAddrLine_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 6),
    _RuijieApOffMacAddrLine_Type()
)
ruijieApOffMacAddrLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffMacAddrLine.setStatus("current")


class _RuijieApOffMacAddrDot_Type(DisplayString):
    """Custom type ruijieApOffMacAddrDot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_RuijieApOffMacAddrDot_Type.__name__ = "DisplayString"
_RuijieApOffMacAddrDot_Object = MibTableColumn
ruijieApOffMacAddrDot = _RuijieApOffMacAddrDot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 7),
    _RuijieApOffMacAddrDot_Type()
)
ruijieApOffMacAddrDot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffMacAddrDot.setStatus("current")
_RuijieApOffStateTime_Type = DisplayString
_RuijieApOffStateTime_Object = MibTableColumn
ruijieApOffStateTime = _RuijieApOffStateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 5, 1, 8),
    _RuijieApOffStateTime_Type()
)
ruijieApOffStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOffStateTime.setStatus("current")
_RuijieApBackupStateTable_Object = MibTable
ruijieApBackupStateTable = _RuijieApBackupStateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ruijieApBackupStateTable.setStatus("current")
_RuijieApBackupStateEntry_Object = MibTableRow
ruijieApBackupStateEntry = _RuijieApBackupStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 6, 1)
)
ruijieApBackupStateEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApBackupStateEntry.setStatus("current")


class _RuijieApBackupState_Type(Integer32):
    """Custom type ruijieApBackupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("master", 1),
          ("slave", 2))
    )


_RuijieApBackupState_Type.__name__ = "Integer32"
_RuijieApBackupState_Object = MibTableColumn
ruijieApBackupState = _RuijieApBackupState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 6, 1, 1),
    _RuijieApBackupState_Type()
)
ruijieApBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApBackupState.setStatus("current")
_RuijieApMicroApTable_Object = MibTable
ruijieApMicroApTable = _RuijieApMicroApTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieApMicroApTable.setStatus("current")
_RuijieApMicroApEntry_Object = MibTableRow
ruijieApMicroApEntry = _RuijieApMicroApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1)
)
ruijieApMicroApEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMicroApSlot"),
)
if mibBuilder.loadTexts:
    ruijieApMicroApEntry.setStatus("current")


class _RuijieApMicroApSlot_Type(Integer32):
    """Custom type ruijieApMicroApSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_RuijieApMicroApSlot_Type.__name__ = "Integer32"
_RuijieApMicroApSlot_Object = MibTableColumn
ruijieApMicroApSlot = _RuijieApMicroApSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 1),
    _RuijieApMicroApSlot_Type()
)
ruijieApMicroApSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApSlot.setStatus("current")


class _RuijieApMicroApName_Type(DisplayString):
    """Custom type ruijieApMicroApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieApMicroApName_Type.__name__ = "DisplayString"
_RuijieApMicroApName_Object = MibTableColumn
ruijieApMicroApName = _RuijieApMicroApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 2),
    _RuijieApMicroApName_Type()
)
ruijieApMicroApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApMicroApName.setStatus("current")


class _RuijieApMicroApReset_Type(Integer32):
    """Custom type ruijieApMicroApReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApMicroApReset_Type.__name__ = "Integer32"
_RuijieApMicroApReset_Object = MibTableColumn
ruijieApMicroApReset = _RuijieApMicroApReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 3),
    _RuijieApMicroApReset_Type()
)
ruijieApMicroApReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApMicroApReset.setStatus("current")


class _RuijieApMicroApUninstall_Type(Integer32):
    """Custom type ruijieApMicroApUninstall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApMicroApUninstall_Type.__name__ = "Integer32"
_RuijieApMicroApUninstall_Object = MibTableColumn
ruijieApMicroApUninstall = _RuijieApMicroApUninstall_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 4),
    _RuijieApMicroApUninstall_Type()
)
ruijieApMicroApUninstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApMicroApUninstall.setStatus("current")
_RuijieApMicroApMac_Type = MacAddress
_RuijieApMicroApMac_Object = MibTableColumn
ruijieApMicroApMac = _RuijieApMicroApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 5),
    _RuijieApMicroApMac_Type()
)
ruijieApMicroApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApMac.setStatus("current")


class _RuijieApMicroApBoard_Type(DisplayString):
    """Custom type ruijieApMicroApBoard based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieApMicroApBoard_Type.__name__ = "DisplayString"
_RuijieApMicroApBoard_Object = MibTableColumn
ruijieApMicroApBoard = _RuijieApMicroApBoard_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 6),
    _RuijieApMicroApBoard_Type()
)
ruijieApMicroApBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApBoard.setStatus("current")


class _RuijieApMicroApState_Type(Integer32):
    """Custom type ruijieApMicroApState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RuijieApMicroApState_Type.__name__ = "Integer32"
_RuijieApMicroApState_Object = MibTableColumn
ruijieApMicroApState = _RuijieApMicroApState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 7),
    _RuijieApMicroApState_Type()
)
ruijieApMicroApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApState.setStatus("current")


class _RuijieApMicroApRole_Type(DisplayString):
    """Custom type ruijieApMicroApRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApMicroApRole_Type.__name__ = "DisplayString"
_RuijieApMicroApRole_Object = MibTableColumn
ruijieApMicroApRole = _RuijieApMicroApRole_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 8),
    _RuijieApMicroApRole_Type()
)
ruijieApMicroApRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApRole.setStatus("current")


class _RuijieApMicroApMasterSlot_Type(Integer32):
    """Custom type ruijieApMicroApMasterSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RuijieApMicroApMasterSlot_Type.__name__ = "Integer32"
_RuijieApMicroApMasterSlot_Object = MibTableColumn
ruijieApMicroApMasterSlot = _RuijieApMicroApMasterSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 7, 1, 9),
    _RuijieApMicroApMasterSlot_Type()
)
ruijieApMicroApMasterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApMasterSlot.setStatus("current")
_RuijieApGeneralCfgTable_Object = MibTable
ruijieApGeneralCfgTable = _RuijieApGeneralCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieApGeneralCfgTable.setStatus("current")
_RuijieApGeneralCfgEntry_Object = MibTableRow
ruijieApGeneralCfgEntry = _RuijieApGeneralCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1)
)
ruijieApGeneralCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApGeneralMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApGeneralCfgEntry.setStatus("current")
_RuijieApGeneralMacAddr_Type = MacAddress
_RuijieApGeneralMacAddr_Object = MibTableColumn
ruijieApGeneralMacAddr = _RuijieApGeneralMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 1),
    _RuijieApGeneralMacAddr_Type()
)
ruijieApGeneralMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMacAddr.setStatus("current")


class _RuijieApGeneralApName_Type(DisplayString):
    """Custom type ruijieApGeneralApName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApGeneralApName_Type.__name__ = "DisplayString"
_RuijieApGeneralApName_Object = MibTableColumn
ruijieApGeneralApName = _RuijieApGeneralApName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 2),
    _RuijieApGeneralApName_Type()
)
ruijieApGeneralApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApGeneralApName.setStatus("current")


class _RuijieApGeneralState_Type(Integer32):
    """Custom type ruijieApGeneralState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_RuijieApGeneralState_Type.__name__ = "Integer32"
_RuijieApGeneralState_Object = MibTableColumn
ruijieApGeneralState = _RuijieApGeneralState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 3),
    _RuijieApGeneralState_Type()
)
ruijieApGeneralState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralState.setStatus("current")
_RuijieApGeneralTime_Type = DisplayString
_RuijieApGeneralTime_Object = MibTableColumn
ruijieApGeneralTime = _RuijieApGeneralTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 4),
    _RuijieApGeneralTime_Type()
)
ruijieApGeneralTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralTime.setStatus("current")
_RuijieApGeneralTimeMs_Type = TimeTicks
_RuijieApGeneralTimeMs_Object = MibTableColumn
ruijieApGeneralTimeMs = _RuijieApGeneralTimeMs_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 5),
    _RuijieApGeneralTimeMs_Type()
)
ruijieApGeneralTimeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralTimeMs.setStatus("current")
_RuijieApGeneralIp_Type = IpAddress
_RuijieApGeneralIp_Object = MibTableColumn
ruijieApGeneralIp = _RuijieApGeneralIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 6),
    _RuijieApGeneralIp_Type()
)
ruijieApGeneralIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralIp.setStatus("current")


class _RuijieApGeneralMacAddrColon_Type(DisplayString):
    """Custom type ruijieApGeneralMacAddrColon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApGeneralMacAddrColon_Type.__name__ = "DisplayString"
_RuijieApGeneralMacAddrColon_Object = MibTableColumn
ruijieApGeneralMacAddrColon = _RuijieApGeneralMacAddrColon_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 7),
    _RuijieApGeneralMacAddrColon_Type()
)
ruijieApGeneralMacAddrColon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMacAddrColon.setStatus("current")


class _RuijieApGeneralMacAddrLine_Type(DisplayString):
    """Custom type ruijieApGeneralMacAddrLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_RuijieApGeneralMacAddrLine_Type.__name__ = "DisplayString"
_RuijieApGeneralMacAddrLine_Object = MibTableColumn
ruijieApGeneralMacAddrLine = _RuijieApGeneralMacAddrLine_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 8),
    _RuijieApGeneralMacAddrLine_Type()
)
ruijieApGeneralMacAddrLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMacAddrLine.setStatus("current")


class _RuijieApGeneralMacAddrDot_Type(DisplayString):
    """Custom type ruijieApGeneralMacAddrDot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )
    fixed_length = 14


_RuijieApGeneralMacAddrDot_Type.__name__ = "DisplayString"
_RuijieApGeneralMacAddrDot_Object = MibTableColumn
ruijieApGeneralMacAddrDot = _RuijieApGeneralMacAddrDot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 9),
    _RuijieApGeneralMacAddrDot_Type()
)
ruijieApGeneralMacAddrDot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMacAddrDot.setStatus("current")


class _RuijieApGeneralLocation_Type(DisplayString):
    """Custom type ruijieApGeneralLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_RuijieApGeneralLocation_Type.__name__ = "DisplayString"
_RuijieApGeneralLocation_Object = MibTableColumn
ruijieApGeneralLocation = _RuijieApGeneralLocation_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 10),
    _RuijieApGeneralLocation_Type()
)
ruijieApGeneralLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApGeneralLocation.setStatus("current")
_RuijieApGeneralCPUCurrentUsage_Type = Integer32
_RuijieApGeneralCPUCurrentUsage_Object = MibTableColumn
ruijieApGeneralCPUCurrentUsage = _RuijieApGeneralCPUCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 11),
    _RuijieApGeneralCPUCurrentUsage_Type()
)
ruijieApGeneralCPUCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralCPUCurrentUsage.setStatus("current")
_RuijieApGeneralCPUAverageUsage_Type = Integer32
_RuijieApGeneralCPUAverageUsage_Object = MibTableColumn
ruijieApGeneralCPUAverageUsage = _RuijieApGeneralCPUAverageUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 12),
    _RuijieApGeneralCPUAverageUsage_Type()
)
ruijieApGeneralCPUAverageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralCPUAverageUsage.setStatus("current")
_RuijieApGeneralMemoryCurrentUsage_Type = Integer32
_RuijieApGeneralMemoryCurrentUsage_Object = MibTableColumn
ruijieApGeneralMemoryCurrentUsage = _RuijieApGeneralMemoryCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 13),
    _RuijieApGeneralMemoryCurrentUsage_Type()
)
ruijieApGeneralMemoryCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMemoryCurrentUsage.setStatus("current")
_RuijieApGeneralMemoryAverageUsage_Type = Integer32
_RuijieApGeneralMemoryAverageUsage_Object = MibTableColumn
ruijieApGeneralMemoryAverageUsage = _RuijieApGeneralMemoryAverageUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 14),
    _RuijieApGeneralMemoryAverageUsage_Type()
)
ruijieApGeneralMemoryAverageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralMemoryAverageUsage.setStatus("current")
_RuijieApGeneralApStaNum_Type = Counter32
_RuijieApGeneralApStaNum_Object = MibTableColumn
ruijieApGeneralApStaNum = _RuijieApGeneralApStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 15),
    _RuijieApGeneralApStaNum_Type()
)
ruijieApGeneralApStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralApStaNum.setStatus("current")
_RuijieApGeneralApUpRate_Type = Counter64
_RuijieApGeneralApUpRate_Object = MibTableColumn
ruijieApGeneralApUpRate = _RuijieApGeneralApUpRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 16),
    _RuijieApGeneralApUpRate_Type()
)
ruijieApGeneralApUpRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralApUpRate.setStatus("current")
_RuijieApGeneralApDownRate_Type = Counter64
_RuijieApGeneralApDownRate_Object = MibTableColumn
ruijieApGeneralApDownRate = _RuijieApGeneralApDownRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 17),
    _RuijieApGeneralApDownRate_Type()
)
ruijieApGeneralApDownRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralApDownRate.setStatus("current")
_RuijieApGeneralAp24GChannel_Type = Counter32
_RuijieApGeneralAp24GChannel_Object = MibTableColumn
ruijieApGeneralAp24GChannel = _RuijieApGeneralAp24GChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 18),
    _RuijieApGeneralAp24GChannel_Type()
)
ruijieApGeneralAp24GChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralAp24GChannel.setStatus("current")
_RuijieApGeneralAp5GChannel_Type = Counter32
_RuijieApGeneralAp5GChannel_Object = MibTableColumn
ruijieApGeneralAp5GChannel = _RuijieApGeneralAp5GChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 19),
    _RuijieApGeneralAp5GChannel_Type()
)
ruijieApGeneralAp5GChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGeneralAp5GChannel.setStatus("current")
_RuijieApGeneralStatus_Type = RowStatus
_RuijieApGeneralStatus_Object = MibTableColumn
ruijieApGeneralStatus = _RuijieApGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 8, 1, 20),
    _RuijieApGeneralStatus_Type()
)
ruijieApGeneralStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApGeneralStatus.setStatus("current")
_RuijieApOnlineJsonTable_Object = MibTable
ruijieApOnlineJsonTable = _RuijieApOnlineJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieApOnlineJsonTable.setStatus("current")
_RuijieApOnlineJsonEntry_Object = MibTableRow
ruijieApOnlineJsonEntry = _RuijieApOnlineJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 9, 1)
)
ruijieApOnlineJsonEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApOnlineJsonMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApOnlineJsonEntry.setStatus("current")
_RuijieApOnlineJsonMacAddr_Type = MacAddress
_RuijieApOnlineJsonMacAddr_Object = MibTableColumn
ruijieApOnlineJsonMacAddr = _RuijieApOnlineJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 9, 1, 1),
    _RuijieApOnlineJsonMacAddr_Type()
)
ruijieApOnlineJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOnlineJsonMacAddr.setStatus("current")


class _RuijieApOnlineJsonContent_Type(OctetString):
    """Custom type ruijieApOnlineJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieApOnlineJsonContent_Type.__name__ = "OctetString"
_RuijieApOnlineJsonContent_Object = MibTableColumn
ruijieApOnlineJsonContent = _RuijieApOnlineJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 9, 1, 2),
    _RuijieApOnlineJsonContent_Type()
)
ruijieApOnlineJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApOnlineJsonContent.setStatus("current")
_RuijieApMicroApJsonTable_Object = MibTable
ruijieApMicroApJsonTable = _RuijieApMicroApJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieApMicroApJsonTable.setStatus("current")
_RuijieApMicroApJsonEntry_Object = MibTableRow
ruijieApMicroApJsonEntry = _RuijieApMicroApJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 10, 1)
)
ruijieApMicroApJsonEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMicroApJsonMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApMicroApJsonSlot"),
)
if mibBuilder.loadTexts:
    ruijieApMicroApJsonEntry.setStatus("current")
_RuijieApMicroApJsonMacAddr_Type = MacAddress
_RuijieApMicroApJsonMacAddr_Object = MibTableColumn
ruijieApMicroApJsonMacAddr = _RuijieApMicroApJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 10, 1, 1),
    _RuijieApMicroApJsonMacAddr_Type()
)
ruijieApMicroApJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApJsonMacAddr.setStatus("current")


class _RuijieApMicroApJsonSlot_Type(Integer32):
    """Custom type ruijieApMicroApJsonSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_RuijieApMicroApJsonSlot_Type.__name__ = "Integer32"
_RuijieApMicroApJsonSlot_Object = MibTableColumn
ruijieApMicroApJsonSlot = _RuijieApMicroApJsonSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 10, 1, 2),
    _RuijieApMicroApJsonSlot_Type()
)
ruijieApMicroApJsonSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApJsonSlot.setStatus("current")


class _RuijieApMicroApJsonContent_Type(OctetString):
    """Custom type ruijieApMicroApJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieApMicroApJsonContent_Type.__name__ = "OctetString"
_RuijieApMicroApJsonContent_Object = MibTableColumn
ruijieApMicroApJsonContent = _RuijieApMicroApJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 10, 1, 3),
    _RuijieApMicroApJsonContent_Type()
)
ruijieApMicroApJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApMicroApJsonContent.setStatus("current")
_RuijieApRadioWlanJsonTable_Object = MibTable
ruijieApRadioWlanJsonTable = _RuijieApRadioWlanJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonTable.setStatus("current")
_RuijieApRadioWlanJsonEntry_Object = MibTableRow
ruijieApRadioWlanJsonEntry = _RuijieApRadioWlanJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11, 1)
)
ruijieApRadioWlanJsonEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApRadioWlanJsonMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApRadioWlanJsonRadioId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApRadioWlanJsonWlanId"),
)
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonEntry.setStatus("current")
_RuijieApRadioWlanJsonMacAddr_Type = MacAddress
_RuijieApRadioWlanJsonMacAddr_Object = MibTableColumn
ruijieApRadioWlanJsonMacAddr = _RuijieApRadioWlanJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11, 1, 1),
    _RuijieApRadioWlanJsonMacAddr_Type()
)
ruijieApRadioWlanJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonMacAddr.setStatus("current")


class _RuijieApRadioWlanJsonRadioId_Type(Integer32):
    """Custom type ruijieApRadioWlanJsonRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_RuijieApRadioWlanJsonRadioId_Type.__name__ = "Integer32"
_RuijieApRadioWlanJsonRadioId_Object = MibTableColumn
ruijieApRadioWlanJsonRadioId = _RuijieApRadioWlanJsonRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11, 1, 2),
    _RuijieApRadioWlanJsonRadioId_Type()
)
ruijieApRadioWlanJsonRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonRadioId.setStatus("current")


class _RuijieApRadioWlanJsonWlanId_Type(Integer32):
    """Custom type ruijieApRadioWlanJsonWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieApRadioWlanJsonWlanId_Type.__name__ = "Integer32"
_RuijieApRadioWlanJsonWlanId_Object = MibTableColumn
ruijieApRadioWlanJsonWlanId = _RuijieApRadioWlanJsonWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11, 1, 3),
    _RuijieApRadioWlanJsonWlanId_Type()
)
ruijieApRadioWlanJsonWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonWlanId.setStatus("current")


class _RuijieApRadioWlanJsonContent_Type(OctetString):
    """Custom type ruijieApRadioWlanJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieApRadioWlanJsonContent_Type.__name__ = "OctetString"
_RuijieApRadioWlanJsonContent_Object = MibTableColumn
ruijieApRadioWlanJsonContent = _RuijieApRadioWlanJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 11, 1, 4),
    _RuijieApRadioWlanJsonContent_Type()
)
ruijieApRadioWlanJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApRadioWlanJsonContent.setStatus("current")
_RuijieApDMJsonTable_Object = MibTable
ruijieApDMJsonTable = _RuijieApDMJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ruijieApDMJsonTable.setStatus("current")
_RuijieApDMJsonEntry_Object = MibTableRow
ruijieApDMJsonEntry = _RuijieApDMJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 12, 1)
)
ruijieApDMJsonEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApDMJsonMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApDMJsonEntry.setStatus("current")
_RuijieApDMJsonMacAddr_Type = MacAddress
_RuijieApDMJsonMacAddr_Object = MibTableColumn
ruijieApDMJsonMacAddr = _RuijieApDMJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 12, 1, 1),
    _RuijieApDMJsonMacAddr_Type()
)
ruijieApDMJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApDMJsonMacAddr.setStatus("current")


class _RuijieApDMJsonContent_Type(OctetString):
    """Custom type ruijieApDMJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieApDMJsonContent_Type.__name__ = "OctetString"
_RuijieApDMJsonContent_Object = MibTableColumn
ruijieApDMJsonContent = _RuijieApDMJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 12, 1, 2),
    _RuijieApDMJsonContent_Type()
)
ruijieApDMJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApDMJsonContent.setStatus("current")
_RuijieApDeviceGpsTable_Object = MibTable
ruijieApDeviceGpsTable = _RuijieApDeviceGpsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ruijieApDeviceGpsTable.setStatus("current")
_RuijieApDeviceGpsEntry_Object = MibTableRow
ruijieApDeviceGpsEntry = _RuijieApDeviceGpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 13, 1)
)
ruijieApDeviceGpsEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApGpsMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieApDeviceGpsEntry.setStatus("current")
_RuijieApGpsMacAddr_Type = MacAddress
_RuijieApGpsMacAddr_Object = MibTableColumn
ruijieApGpsMacAddr = _RuijieApGpsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 13, 1, 1),
    _RuijieApGpsMacAddr_Type()
)
ruijieApGpsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGpsMacAddr.setStatus("current")


class _RuijieApGpsLongitude_Type(DisplayString):
    """Custom type ruijieApGpsLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApGpsLongitude_Type.__name__ = "DisplayString"
_RuijieApGpsLongitude_Object = MibTableColumn
ruijieApGpsLongitude = _RuijieApGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 13, 1, 2),
    _RuijieApGpsLongitude_Type()
)
ruijieApGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGpsLongitude.setStatus("current")


class _RuijieApGpsLatitude_Type(DisplayString):
    """Custom type ruijieApGpsLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApGpsLatitude_Type.__name__ = "DisplayString"
_RuijieApGpsLatitude_Object = MibTableColumn
ruijieApGpsLatitude = _RuijieApGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 13, 1, 3),
    _RuijieApGpsLatitude_Type()
)
ruijieApGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApGpsLatitude.setStatus("current")
_RuijieApWiredTable_Object = MibTable
ruijieApWiredTable = _RuijieApWiredTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 14)
)
if mibBuilder.loadTexts:
    ruijieApWiredTable.setStatus("current")
_RuijieApWiredEntry_Object = MibTableRow
ruijieApWiredEntry = _RuijieApWiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 14, 1)
)
ruijieApWiredEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApWiredMacAddr"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApWiredPort"),
)
if mibBuilder.loadTexts:
    ruijieApWiredEntry.setStatus("current")
_RuijieApWiredMacAddr_Type = MacAddress
_RuijieApWiredMacAddr_Object = MibTableColumn
ruijieApWiredMacAddr = _RuijieApWiredMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 14, 1, 1),
    _RuijieApWiredMacAddr_Type()
)
ruijieApWiredMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApWiredMacAddr.setStatus("current")
_RuijieApWiredPort_Type = Integer32
_RuijieApWiredPort_Object = MibTableColumn
ruijieApWiredPort = _RuijieApWiredPort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 14, 1, 2),
    _RuijieApWiredPort_Type()
)
ruijieApWiredPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApWiredPort.setStatus("current")


class _RuijieApWiredVlanId_Type(Integer32):
    """Custom type ruijieApWiredVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RuijieApWiredVlanId_Type.__name__ = "Integer32"
_RuijieApWiredVlanId_Object = MibTableColumn
ruijieApWiredVlanId = _RuijieApWiredVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 1, 14, 1, 3),
    _RuijieApWiredVlanId_Type()
)
ruijieApWiredVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApWiredVlanId.setStatus("current")
_RuijieAcMgmtApIf_ObjectIdentity = ObjectIdentity
ruijieAcMgmtApIf = _RuijieAcMgmtApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 2, 2)
)
_RuijieAcMgmtApgMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtApgMIBObjects = _RuijieAcMgmtApgMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3)
)
_RuijieAcMgmtApg_ObjectIdentity = ObjectIdentity
ruijieAcMgmtApg = _RuijieAcMgmtApg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1)
)
_RuijieApgCfgTable_Object = MibTable
ruijieApgCfgTable = _RuijieApgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieApgCfgTable.setStatus("current")
_RuijieApgCfgEntry_Object = MibTableRow
ruijieApgCfgEntry = _RuijieApgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1)
)
ruijieApgCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgApgName"),
)
if mibBuilder.loadTexts:
    ruijieApgCfgEntry.setStatus("current")


class _RuijieApgApgName_Type(DisplayString):
    """Custom type ruijieApgApgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieApgApgName_Type.__name__ = "DisplayString"
_RuijieApgApgName_Object = MibTableColumn
ruijieApgApgName = _RuijieApgApgName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 1),
    _RuijieApgApgName_Type()
)
ruijieApgApgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApgApgName.setStatus("current")


class _RuijieApgDiscTimer_Type(Integer32):
    """Custom type ruijieApgDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 180),
    )


_RuijieApgDiscTimer_Type.__name__ = "Integer32"
_RuijieApgDiscTimer_Object = MibTableColumn
ruijieApgDiscTimer = _RuijieApgDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 2),
    _RuijieApgDiscTimer_Type()
)
ruijieApgDiscTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgDiscTimer.setStatus("current")


class _RuijieApgEchoReqTimer_Type(Integer32):
    """Custom type ruijieApgEchoReqTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_RuijieApgEchoReqTimer_Type.__name__ = "Integer32"
_RuijieApgEchoReqTimer_Object = MibTableColumn
ruijieApgEchoReqTimer = _RuijieApgEchoReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 3),
    _RuijieApgEchoReqTimer_Type()
)
ruijieApgEchoReqTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgEchoReqTimer.setStatus("current")


class _RuijieApgEroReportTimer_Type(Integer32):
    """Custom type ruijieApgEroReportTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1080),
    )


_RuijieApgEroReportTimer_Type.__name__ = "Integer32"
_RuijieApgEroReportTimer_Object = MibTableColumn
ruijieApgEroReportTimer = _RuijieApgEroReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 4),
    _RuijieApgEroReportTimer_Type()
)
ruijieApgEroReportTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgEroReportTimer.setStatus("current")


class _RuijieApgStaTimeoutTimer_Type(Integer32):
    """Custom type ruijieApgStaTimeoutTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_RuijieApgStaTimeoutTimer_Type.__name__ = "Integer32"
_RuijieApgStaTimeoutTimer_Object = MibTableColumn
ruijieApgStaTimeoutTimer = _RuijieApgStaTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 5),
    _RuijieApgStaTimeoutTimer_Type()
)
ruijieApgStaTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgStaTimeoutTimer.setStatus("current")


class _RuijieApgStatisticsTimer_Type(Integer32):
    """Custom type ruijieApgStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieApgStatisticsTimer_Type.__name__ = "Integer32"
_RuijieApgStatisticsTimer_Object = MibTableColumn
ruijieApgStatisticsTimer = _RuijieApgStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 6),
    _RuijieApgStatisticsTimer_Type()
)
ruijieApgStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgStatisticsTimer.setStatus("current")


class _RuijieApgFallback_Type(Integer32):
    """Custom type ruijieApgFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieApgFallback_Type.__name__ = "Integer32"
_RuijieApgFallback_Object = MibTableColumn
ruijieApgFallback = _RuijieApgFallback_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 7),
    _RuijieApgFallback_Type()
)
ruijieApgFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgFallback.setStatus("current")


class _RuijieApgImageId_Type(DisplayString):
    """Custom type ruijieApgImageId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuijieApgImageId_Type.__name__ = "DisplayString"
_RuijieApgImageId_Object = MibTableColumn
ruijieApgImageId = _RuijieApgImageId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 8),
    _RuijieApgImageId_Type()
)
ruijieApgImageId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgImageId.setStatus("current")


class _RuijieApgCreatEn_Type(Integer32):
    """Custom type ruijieApgCreatEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApgCreatEn_Type.__name__ = "Integer32"
_RuijieApgCreatEn_Object = MibTableColumn
ruijieApgCreatEn = _RuijieApgCreatEn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 1, 1, 9),
    _RuijieApgCreatEn_Type()
)
ruijieApgCreatEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgCreatEn.setStatus("current")
_RuijieApgCfgRadioTable_Object = MibTable
ruijieApgCfgRadioTable = _RuijieApgCfgRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieApgCfgRadioTable.setStatus("current")
_RuijieApgCfgRadioEntry_Object = MibTableRow
ruijieApgCfgRadioEntry = _RuijieApgCfgRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 2, 1)
)
ruijieApgCfgRadioEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgApgName"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgEnableRadioId"),
)
if mibBuilder.loadTexts:
    ruijieApgCfgRadioEntry.setStatus("current")


class _RuijieApgEnableRadioId_Type(Integer32):
    """Custom type ruijieApgEnableRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_RuijieApgEnableRadioId_Type.__name__ = "Integer32"
_RuijieApgEnableRadioId_Object = MibTableColumn
ruijieApgEnableRadioId = _RuijieApgEnableRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 2, 1, 1),
    _RuijieApgEnableRadioId_Type()
)
ruijieApgEnableRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieApgEnableRadioId.setStatus("current")


class _RuijieApgEnableRadioEn_Type(Integer32):
    """Custom type ruijieApgEnableRadioEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieApgEnableRadioEn_Type.__name__ = "Integer32"
_RuijieApgEnableRadioEn_Object = MibTableColumn
ruijieApgEnableRadioEn = _RuijieApgEnableRadioEn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 2, 1, 2),
    _RuijieApgEnableRadioEn_Type()
)
ruijieApgEnableRadioEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgEnableRadioEn.setStatus("current")
_RuijieApgIntfMapTable_Object = MibTable
ruijieApgIntfMapTable = _RuijieApgIntfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieApgIntfMapTable.setStatus("current")
_RuijieApgIntfMapEntry_Object = MibTableRow
ruijieApgIntfMapEntry = _RuijieApgIntfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1)
)
ruijieApgIntfMapEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgApgName"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieApgWlanIndex"),
)
if mibBuilder.loadTexts:
    ruijieApgIntfMapEntry.setStatus("current")


class _RuijieApgWlanIndex_Type(Integer32):
    """Custom type ruijieApgWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RuijieApgWlanIndex_Type.__name__ = "Integer32"
_RuijieApgWlanIndex_Object = MibTableColumn
ruijieApgWlanIndex = _RuijieApgWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1, 1),
    _RuijieApgWlanIndex_Type()
)
ruijieApgWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieApgWlanIndex.setStatus("current")


class _RuijieApgWlanId_Type(Integer32):
    """Custom type ruijieApgWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieApgWlanId_Type.__name__ = "Integer32"
_RuijieApgWlanId_Object = MibTableColumn
ruijieApgWlanId = _RuijieApgWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1, 2),
    _RuijieApgWlanId_Type()
)
ruijieApgWlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgWlanId.setStatus("current")


class _RuijieApgVlanId_Type(Integer32):
    """Custom type ruijieApgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieApgVlanId_Type.__name__ = "Integer32"
_RuijieApgVlanId_Object = MibTableColumn
ruijieApgVlanId = _RuijieApgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1, 3),
    _RuijieApgVlanId_Type()
)
ruijieApgVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgVlanId.setStatus("current")


class _RuijieApgRadioId_Type(Integer32):
    """Custom type ruijieApgRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RuijieApgRadioId_Type.__name__ = "Integer32"
_RuijieApgRadioId_Object = MibTableColumn
ruijieApgRadioId = _RuijieApgRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1, 4),
    _RuijieApgRadioId_Type()
)
ruijieApgRadioId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgRadioId.setStatus("current")
_RuijieApgWlanIntfMapRS_Type = RowStatus
_RuijieApgWlanIntfMapRS_Object = MibTableColumn
ruijieApgWlanIntfMapRS = _RuijieApgWlanIntfMapRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 1, 3, 1, 5),
    _RuijieApgWlanIntfMapRS_Type()
)
ruijieApgWlanIntfMapRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieApgWlanIntfMapRS.setStatus("current")
_RuijieAcMgmtApgIf_ObjectIdentity = ObjectIdentity
ruijieAcMgmtApgIf = _RuijieAcMgmtApgIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 3, 2)
)
_RuijieAcMgmtWlanMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtWlanMIBObjects = _RuijieAcMgmtWlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4)
)
_RuijieAcMgmtWlan_ObjectIdentity = ObjectIdentity
ruijieAcMgmtWlan = _RuijieAcMgmtWlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1)
)
_RuijieWlanCfgTable_Object = MibTable
ruijieWlanCfgTable = _RuijieWlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWlanCfgTable.setStatus("current")
_RuijieWlanCfgEntry_Object = MibTableRow
ruijieWlanCfgEntry = _RuijieWlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1)
)
ruijieWlanCfgEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWlanCfgEntry.setStatus("current")


class _RuijieWlanId_Type(Integer32):
    """Custom type ruijieWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RuijieWlanId_Type.__name__ = "Integer32"
_RuijieWlanId_Object = MibTableColumn
ruijieWlanId = _RuijieWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 1),
    _RuijieWlanId_Type()
)
ruijieWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanId.setStatus("current")


class _RuijieWlanShort_Type(Integer32):
    """Custom type ruijieWlanShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RuijieWlanShort_Type.__name__ = "Integer32"
_RuijieWlanShort_Object = MibTableColumn
ruijieWlanShort = _RuijieWlanShort_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 2),
    _RuijieWlanShort_Type()
)
ruijieWlanShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanShort.setStatus("current")


class _RuijieWlanSpctMgmt_Type(Integer32):
    """Custom type ruijieWlanSpctMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanSpctMgmt_Type.__name__ = "Integer32"
_RuijieWlanSpctMgmt_Object = MibTableColumn
ruijieWlanSpctMgmt = _RuijieWlanSpctMgmt_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 3),
    _RuijieWlanSpctMgmt_Type()
)
ruijieWlanSpctMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanSpctMgmt.setStatus("current")


class _RuijieWlanEnQos_Type(Integer32):
    """Custom type ruijieWlanEnQos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanEnQos_Type.__name__ = "Integer32"
_RuijieWlanEnQos_Object = MibTableColumn
ruijieWlanEnQos = _RuijieWlanEnQos_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 4),
    _RuijieWlanEnQos_Type()
)
ruijieWlanEnQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanEnQos.setStatus("current")


class _RuijieWlanShortSlotTime_Type(Integer32):
    """Custom type ruijieWlanShortSlotTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanShortSlotTime_Type.__name__ = "Integer32"
_RuijieWlanShortSlotTime_Object = MibTableColumn
ruijieWlanShortSlotTime = _RuijieWlanShortSlotTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 5),
    _RuijieWlanShortSlotTime_Type()
)
ruijieWlanShortSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanShortSlotTime.setStatus("current")


class _RuijieWlanEnableApsd_Type(Integer32):
    """Custom type ruijieWlanEnableApsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanEnableApsd_Type.__name__ = "Integer32"
_RuijieWlanEnableApsd_Object = MibTableColumn
ruijieWlanEnableApsd = _RuijieWlanEnableApsd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 6),
    _RuijieWlanEnableApsd_Type()
)
ruijieWlanEnableApsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanEnableApsd.setStatus("current")


class _RuijieWlanAckType_Type(Integer32):
    """Custom type ruijieWlanAckType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanAckType_Type.__name__ = "Integer32"
_RuijieWlanAckType_Object = MibTableColumn
ruijieWlanAckType = _RuijieWlanAckType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 7),
    _RuijieWlanAckType_Type()
)
ruijieWlanAckType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanAckType.setStatus("current")


class _RuijieWlanTunnelType_Type(Integer32):
    """Custom type ruijieWlanTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_RuijieWlanTunnelType_Type.__name__ = "Integer32"
_RuijieWlanTunnelType_Object = MibTableColumn
ruijieWlanTunnelType = _RuijieWlanTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 8),
    _RuijieWlanTunnelType_Type()
)
ruijieWlanTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanTunnelType.setStatus("current")


class _RuijieWlanBroadSsid_Type(Integer32):
    """Custom type ruijieWlanBroadSsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanBroadSsid_Type.__name__ = "Integer32"
_RuijieWlanBroadSsid_Object = MibTableColumn
ruijieWlanBroadSsid = _RuijieWlanBroadSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 9),
    _RuijieWlanBroadSsid_Type()
)
ruijieWlanBroadSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanBroadSsid.setStatus("current")


class _RuijieWlanRts_Type(Integer32):
    """Custom type ruijieWlanRts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWlanRts_Type.__name__ = "Integer32"
_RuijieWlanRts_Object = MibTableColumn
ruijieWlanRts = _RuijieWlanRts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 10),
    _RuijieWlanRts_Type()
)
ruijieWlanRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanRts.setStatus("current")


class _RuijieWlanShortTry_Type(Integer32):
    """Custom type ruijieWlanShortTry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWlanShortTry_Type.__name__ = "Integer32"
_RuijieWlanShortTry_Object = MibTableColumn
ruijieWlanShortTry = _RuijieWlanShortTry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 11),
    _RuijieWlanShortTry_Type()
)
ruijieWlanShortTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanShortTry.setStatus("current")


class _RuijieWlanLongTry_Type(Integer32):
    """Custom type ruijieWlanLongTry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWlanLongTry_Type.__name__ = "Integer32"
_RuijieWlanLongTry_Object = MibTableColumn
ruijieWlanLongTry = _RuijieWlanLongTry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 12),
    _RuijieWlanLongTry_Type()
)
ruijieWlanLongTry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanLongTry.setStatus("current")
_RuijieWlanStaNum_Type = Integer32
_RuijieWlanStaNum_Object = MibTableColumn
ruijieWlanStaNum = _RuijieWlanStaNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 13),
    _RuijieWlanStaNum_Type()
)
ruijieWlanStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWlanStaNum.setStatus("current")
_RuijieWlanNasId_Type = DisplayString
_RuijieWlanNasId_Object = MibTableColumn
ruijieWlanNasId = _RuijieWlanNasId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 1, 1, 14),
    _RuijieWlanNasId_Type()
)
ruijieWlanNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanNasId.setStatus("current")
_RuijieWlanWlanCreatTable_Object = MibTable
ruijieWlanWlanCreatTable = _RuijieWlanWlanCreatTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieWlanWlanCreatTable.setStatus("current")
_RuijieWlanWlanCreatEntry_Object = MibTableRow
ruijieWlanWlanCreatEntry = _RuijieWlanWlanCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 2, 1)
)
ruijieWlanWlanCreatEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWlanWlanCreatEntry.setStatus("current")


class _RuijieWlanWlanSsid_Type(DisplayString):
    """Custom type ruijieWlanWlanSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieWlanWlanSsid_Type.__name__ = "DisplayString"
_RuijieWlanWlanSsid_Object = MibTableColumn
ruijieWlanWlanSsid = _RuijieWlanWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 2, 1, 1),
    _RuijieWlanWlanSsid_Type()
)
ruijieWlanWlanSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanWlanSsid.setStatus("current")


class _RuijieWlanWlanProfile_Type(DisplayString):
    """Custom type ruijieWlanWlanProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieWlanWlanProfile_Type.__name__ = "DisplayString"
_RuijieWlanWlanProfile_Object = MibTableColumn
ruijieWlanWlanProfile = _RuijieWlanWlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 2, 1, 2),
    _RuijieWlanWlanProfile_Type()
)
ruijieWlanWlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanWlanProfile.setStatus("current")
_RuijieWlanCreateMapRS_Type = RowStatus
_RuijieWlanCreateMapRS_Object = MibTableColumn
ruijieWlanCreateMapRS = _RuijieWlanCreateMapRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 2, 1, 3),
    _RuijieWlanCreateMapRS_Type()
)
ruijieWlanCreateMapRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanCreateMapRS.setStatus("current")
_RuijieWlanChanBandTable_Object = MibTable
ruijieWlanChanBandTable = _RuijieWlanChanBandTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieWlanChanBandTable.setStatus("current")
_RuijieWlanChanBandEntry_Object = MibTableRow
ruijieWlanChanBandEntry = _RuijieWlanChanBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3, 1)
)
ruijieWlanChanBandEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieWlanId"),
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieWlanBandV"),
)
if mibBuilder.loadTexts:
    ruijieWlanChanBandEntry.setStatus("current")


class _RuijieWlanBandV_Type(Integer32):
    """Custom type ruijieWlanBandV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RuijieWlanBandV_Type.__name__ = "Integer32"
_RuijieWlanBandV_Object = MibTableColumn
ruijieWlanBandV = _RuijieWlanBandV_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3, 1, 1),
    _RuijieWlanBandV_Type()
)
ruijieWlanBandV.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijieWlanBandV.setStatus("current")


class _RuijieWlanChanV_Type(Integer32):
    """Custom type ruijieWlanChanV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWlanChanV_Type.__name__ = "Integer32"
_RuijieWlanChanV_Object = MibTableColumn
ruijieWlanChanV = _RuijieWlanChanV_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3, 1, 2),
    _RuijieWlanChanV_Type()
)
ruijieWlanChanV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanChanV.setStatus("current")


class _RuijieWlanChanBandEn_Type(Integer32):
    """Custom type ruijieWlanChanBandEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RuijieWlanChanBandEn_Type.__name__ = "Integer32"
_RuijieWlanChanBandEn_Object = MibTableColumn
ruijieWlanChanBandEn = _RuijieWlanChanBandEn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3, 1, 3),
    _RuijieWlanChanBandEn_Type()
)
ruijieWlanChanBandEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanChanBandEn.setStatus("current")
_RuijieWlanChanBandRS_Type = RowStatus
_RuijieWlanChanBandRS_Object = MibTableColumn
ruijieWlanChanBandRS = _RuijieWlanChanBandRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 3, 1, 4),
    _RuijieWlanChanBandRS_Type()
)
ruijieWlanChanBandRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanChanBandRS.setStatus("current")
_RuijieWlanLimitChanTable_Object = MibTable
ruijieWlanLimitChanTable = _RuijieWlanLimitChanTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieWlanLimitChanTable.setStatus("current")
_RuijieWlanLimitChanEntry_Object = MibTableRow
ruijieWlanLimitChanEntry = _RuijieWlanLimitChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4, 1)
)
ruijieWlanLimitChanEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieWlanId"),
)
if mibBuilder.loadTexts:
    ruijieWlanLimitChanEntry.setStatus("current")


class _RuijieWlanLimitChanFirstV_Type(Integer32):
    """Custom type ruijieWlanLimitChanFirstV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijieWlanLimitChanFirstV_Type.__name__ = "Integer32"
_RuijieWlanLimitChanFirstV_Object = MibTableColumn
ruijieWlanLimitChanFirstV = _RuijieWlanLimitChanFirstV_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4, 1, 1),
    _RuijieWlanLimitChanFirstV_Type()
)
ruijieWlanLimitChanFirstV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanLimitChanFirstV.setStatus("current")


class _RuijieWlanLimitChanNumV_Type(Integer32):
    """Custom type ruijieWlanLimitChanNumV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_RuijieWlanLimitChanNumV_Type.__name__ = "Integer32"
_RuijieWlanLimitChanNumV_Object = MibTableColumn
ruijieWlanLimitChanNumV = _RuijieWlanLimitChanNumV_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4, 1, 2),
    _RuijieWlanLimitChanNumV_Type()
)
ruijieWlanLimitChanNumV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanLimitChanNumV.setStatus("current")


class _RuijieWlanLimitChanMaxTxPowerLv_Type(Integer32):
    """Custom type ruijieWlanLimitChanMaxTxPowerLv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_RuijieWlanLimitChanMaxTxPowerLv_Type.__name__ = "Integer32"
_RuijieWlanLimitChanMaxTxPowerLv_Object = MibTableColumn
ruijieWlanLimitChanMaxTxPowerLv = _RuijieWlanLimitChanMaxTxPowerLv_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4, 1, 3),
    _RuijieWlanLimitChanMaxTxPowerLv_Type()
)
ruijieWlanLimitChanMaxTxPowerLv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanLimitChanMaxTxPowerLv.setStatus("current")
_RuijieWlanLimitChanRS_Type = RowStatus
_RuijieWlanLimitChanRS_Object = MibTableColumn
ruijieWlanLimitChanRS = _RuijieWlanLimitChanRS_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 1, 4, 1, 4),
    _RuijieWlanLimitChanRS_Type()
)
ruijieWlanLimitChanRS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieWlanLimitChanRS.setStatus("current")
_RuijieAcMgmtWlanIf_ObjectIdentity = ObjectIdentity
ruijieAcMgmtWlanIf = _RuijieAcMgmtWlanIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 4, 2)
)
_RuijieAcMgmtStaMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtStaMIBObjects = _RuijieAcMgmtStaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5)
)
_RuijieAcMgmtSta_ObjectIdentity = ObjectIdentity
ruijieAcMgmtSta = _RuijieAcMgmtSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1)
)
_RuijieStaTable_Object = MibTable
ruijieStaTable = _RuijieStaTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieStaTable.setStatus("current")
_RuijieStaEntry_Object = MibTableRow
ruijieStaEntry = _RuijieStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1)
)
ruijieStaEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieStaEntry.setStatus("current")
_RuijieStaMacAddr_Type = MacAddress
_RuijieStaMacAddr_Object = MibTableColumn
ruijieStaMacAddr = _RuijieStaMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 1),
    _RuijieStaMacAddr_Type()
)
ruijieStaMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaMacAddr.setStatus("current")
_RuijieStaApMacAddr_Type = MacAddress
_RuijieStaApMacAddr_Object = MibTableColumn
ruijieStaApMacAddr = _RuijieStaApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 2),
    _RuijieStaApMacAddr_Type()
)
ruijieStaApMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaApMacAddr.setStatus("current")
_RuijieStaVlan_Type = Integer32
_RuijieStaVlan_Object = MibTableColumn
ruijieStaVlan = _RuijieStaVlan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 3),
    _RuijieStaVlan_Type()
)
ruijieStaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaVlan.setStatus("current")
_RuijieStaWlanId_Type = Integer32
_RuijieStaWlanId_Object = MibTableColumn
ruijieStaWlanId = _RuijieStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 4),
    _RuijieStaWlanId_Type()
)
ruijieStaWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaWlanId.setStatus("current")
_RuijieStaIp_Type = IpAddress
_RuijieStaIp_Object = MibTableColumn
ruijieStaIp = _RuijieStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 5),
    _RuijieStaIp_Type()
)
ruijieStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaIp.setStatus("current")
_RuijieStaApIp_Type = IpAddress
_RuijieStaApIp_Object = MibTableColumn
ruijieStaApIp = _RuijieStaApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 6),
    _RuijieStaApIp_Type()
)
ruijieStaApIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaApIp.setStatus("current")
_RuijieStaApRadioId_Type = Integer32
_RuijieStaApRadioId_Object = MibTableColumn
ruijieStaApRadioId = _RuijieStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 7),
    _RuijieStaApRadioId_Type()
)
ruijieStaApRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaApRadioId.setStatus("current")
_RuijieStaApRadioType_Type = Integer32
_RuijieStaApRadioType_Object = MibTableColumn
ruijieStaApRadioType = _RuijieStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 8),
    _RuijieStaApRadioType_Type()
)
ruijieStaApRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaApRadioType.setStatus("current")
_RuijieStaAssoType_Type = Integer32
_RuijieStaAssoType_Object = MibTableColumn
ruijieStaAssoType = _RuijieStaAssoType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 9),
    _RuijieStaAssoType_Type()
)
ruijieStaAssoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssoType.setStatus("current")
_RuijieStaAuthType_Type = Integer32
_RuijieStaAuthType_Object = MibTableColumn
ruijieStaAuthType = _RuijieStaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 10),
    _RuijieStaAuthType_Type()
)
ruijieStaAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAuthType.setStatus("current")
_RuijieStaRoamTimesPerMin_Type = Integer32
_RuijieStaRoamTimesPerMin_Object = MibTableColumn
ruijieStaRoamTimesPerMin = _RuijieStaRoamTimesPerMin_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 11),
    _RuijieStaRoamTimesPerMin_Type()
)
ruijieStaRoamTimesPerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaRoamTimesPerMin.setStatus("current")
_RuijieStaOnTimesPerHour_Type = Integer32
_RuijieStaOnTimesPerHour_Object = MibTableColumn
ruijieStaOnTimesPerHour = _RuijieStaOnTimesPerHour_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 12),
    _RuijieStaOnTimesPerHour_Type()
)
ruijieStaOnTimesPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaOnTimesPerHour.setStatus("current")
_RuijieStaOffTimesPerHour_Type = Integer32
_RuijieStaOffTimesPerHour_Object = MibTableColumn
ruijieStaOffTimesPerHour = _RuijieStaOffTimesPerHour_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 13),
    _RuijieStaOffTimesPerHour_Type()
)
ruijieStaOffTimesPerHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaOffTimesPerHour.setStatus("current")
_RuijieStaIpv6_Type = InetAddress
_RuijieStaIpv6_Object = MibTableColumn
ruijieStaIpv6 = _RuijieStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 14),
    _RuijieStaIpv6_Type()
)
ruijieStaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaIpv6.setStatus("current")


class _RuijieStaAssoAuthMode_Type(Integer32):
    """Custom type ruijieStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_RuijieStaAssoAuthMode_Type.__name__ = "Integer32"
_RuijieStaAssoAuthMode_Object = MibTableColumn
ruijieStaAssoAuthMode = _RuijieStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 15),
    _RuijieStaAssoAuthMode_Type()
)
ruijieStaAssoAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaAssoAuthMode.setStatus("current")


class _RuijieStaNetAuthMode_Type(Integer32):
    """Custom type ruijieStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_RuijieStaNetAuthMode_Type.__name__ = "Integer32"
_RuijieStaNetAuthMode_Object = MibTableColumn
ruijieStaNetAuthMode = _RuijieStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 16),
    _RuijieStaNetAuthMode_Type()
)
ruijieStaNetAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaNetAuthMode.setStatus("current")
_RuijieStaSsid_Type = DisplayString
_RuijieStaSsid_Object = MibTableColumn
ruijieStaSsid = _RuijieStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 17),
    _RuijieStaSsid_Type()
)
ruijieStaSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaSsid.setStatus("current")
_RuijieStaLinkRate_Type = Integer32
_RuijieStaLinkRate_Object = MibTableColumn
ruijieStaLinkRate = _RuijieStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 18),
    _RuijieStaLinkRate_Type()
)
ruijieStaLinkRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaLinkRate.setStatus("current")
_RuijieStaCurChan_Type = Integer32
_RuijieStaCurChan_Object = MibTableColumn
ruijieStaCurChan = _RuijieStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 19),
    _RuijieStaCurChan_Type()
)
ruijieStaCurChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaCurChan.setStatus("current")


class _RuijieStaClientType_Type(DisplayString):
    """Custom type ruijieStaClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RuijieStaClientType_Type.__name__ = "DisplayString"
_RuijieStaClientType_Object = MibTableColumn
ruijieStaClientType = _RuijieStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 20),
    _RuijieStaClientType_Type()
)
ruijieStaClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaClientType.setStatus("current")
_RuijieStaRssi_Type = Integer32
_RuijieStaRssi_Object = MibTableColumn
ruijieStaRssi = _RuijieStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 21),
    _RuijieStaRssi_Type()
)
ruijieStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaRssi.setStatus("current")
_RuijieStaUserName_Type = DisplayString
_RuijieStaUserName_Object = MibTableColumn
ruijieStaUserName = _RuijieStaUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 22),
    _RuijieStaUserName_Type()
)
ruijieStaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaUserName.setStatus("current")
_RuijieStaTerminalType_Type = DisplayString
_RuijieStaTerminalType_Object = MibTableColumn
ruijieStaTerminalType = _RuijieStaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 23),
    _RuijieStaTerminalType_Type()
)
ruijieStaTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaTerminalType.setStatus("current")
_RuijieStaOnlineTime_Type = DisplayString
_RuijieStaOnlineTime_Object = MibTableColumn
ruijieStaOnlineTime = _RuijieStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 24),
    _RuijieStaOnlineTime_Type()
)
ruijieStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaOnlineTime.setStatus("current")
_RuijieStaUpTimeInterval_Type = Integer32
_RuijieStaUpTimeInterval_Object = MibTableColumn
ruijieStaUpTimeInterval = _RuijieStaUpTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 25),
    _RuijieStaUpTimeInterval_Type()
)
ruijieStaUpTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaUpTimeInterval.setStatus("current")
_RuijieStaUserAuthTime_Type = DisplayString
_RuijieStaUserAuthTime_Object = MibTableColumn
ruijieStaUserAuthTime = _RuijieStaUserAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 1, 1, 26),
    _RuijieStaUserAuthTime_Type()
)
ruijieStaUserAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaUserAuthTime.setStatus("current")
_RuijieStaJsonTable_Object = MibTable
ruijieStaJsonTable = _RuijieStaJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieStaJsonTable.setStatus("current")
_RuijieStaJsonEntry_Object = MibTableRow
ruijieStaJsonEntry = _RuijieStaJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 2, 1)
)
ruijieStaJsonEntry.setIndexNames(
    (0, "RUIJIE-AC-MGMT-MIB", "ruijieStaJsonMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieStaJsonEntry.setStatus("current")
_RuijieStaJsonMacAddr_Type = MacAddress
_RuijieStaJsonMacAddr_Object = MibTableColumn
ruijieStaJsonMacAddr = _RuijieStaJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 2, 1, 1),
    _RuijieStaJsonMacAddr_Type()
)
ruijieStaJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaJsonMacAddr.setStatus("current")


class _RuijieStaJsonContent_Type(OctetString):
    """Custom type ruijieStaJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_RuijieStaJsonContent_Type.__name__ = "OctetString"
_RuijieStaJsonContent_Object = MibTableColumn
ruijieStaJsonContent = _RuijieStaJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 1, 2, 1, 2),
    _RuijieStaJsonContent_Type()
)
ruijieStaJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieStaJsonContent.setStatus("current")
_RuijieAcMgmtStaIf_ObjectIdentity = ObjectIdentity
ruijieAcMgmtStaIf = _RuijieAcMgmtStaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 5, 2)
)
_RuijieAcMgmtNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtNotificationsMIBObjects = _RuijieAcMgmtNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6)
)
_RuijieAcMgmtNtfObjects_ObjectIdentity = ObjectIdentity
ruijieAcMgmtNtfObjects = _RuijieAcMgmtNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1)
)
_RuijieNotifyApMac_Type = MacAddress
_RuijieNotifyApMac_Object = MibScalar
ruijieNotifyApMac = _RuijieNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 1),
    _RuijieNotifyApMac_Type()
)
ruijieNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyApMac.setStatus("current")
_RuijieNotifyStaMac_Type = MacAddress
_RuijieNotifyStaMac_Object = MibScalar
ruijieNotifyStaMac = _RuijieNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 2),
    _RuijieNotifyStaMac_Type()
)
ruijieNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaMac.setStatus("current")
_RuijieNotifyApIp_Type = IpAddress
_RuijieNotifyApIp_Object = MibScalar
ruijieNotifyApIp = _RuijieNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 3),
    _RuijieNotifyApIp_Type()
)
ruijieNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyApIp.setStatus("current")
_RuijieNotifyStaIp_Type = IpAddress
_RuijieNotifyStaIp_Object = MibScalar
ruijieNotifyStaIp = _RuijieNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 4),
    _RuijieNotifyStaIp_Type()
)
ruijieNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaIp.setStatus("current")
_RuijieNotifyStaOperType_Type = Integer32
_RuijieNotifyStaOperType_Object = MibScalar
ruijieNotifyStaOperType = _RuijieNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 5),
    _RuijieNotifyStaOperType_Type()
)
ruijieNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaOperType.setStatus("current")


class _RuijieNotifyStaApRadioId_Type(Integer32):
    """Custom type ruijieNotifyStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieNotifyStaApRadioId_Type.__name__ = "Integer32"
_RuijieNotifyStaApRadioId_Object = MibScalar
ruijieNotifyStaApRadioId = _RuijieNotifyStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 6),
    _RuijieNotifyStaApRadioId_Type()
)
ruijieNotifyStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaApRadioId.setStatus("current")


class _RuijieNotifyStaApRadioType_Type(Integer32):
    """Custom type ruijieNotifyStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieNotifyStaApRadioType_Type.__name__ = "Integer32"
_RuijieNotifyStaApRadioType_Object = MibScalar
ruijieNotifyStaApRadioType = _RuijieNotifyStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 7),
    _RuijieNotifyStaApRadioType_Type()
)
ruijieNotifyStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaApRadioType.setStatus("current")


class _RuijieNotifyStaVlanId_Type(Integer32):
    """Custom type ruijieNotifyStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieNotifyStaVlanId_Type.__name__ = "Integer32"
_RuijieNotifyStaVlanId_Object = MibScalar
ruijieNotifyStaVlanId = _RuijieNotifyStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 8),
    _RuijieNotifyStaVlanId_Type()
)
ruijieNotifyStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaVlanId.setStatus("current")


class _RuijieNotifyStaWlanId_Type(Integer32):
    """Custom type ruijieNotifyStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieNotifyStaWlanId_Type.__name__ = "Integer32"
_RuijieNotifyStaWlanId_Object = MibScalar
ruijieNotifyStaWlanId = _RuijieNotifyStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 9),
    _RuijieNotifyStaWlanId_Type()
)
ruijieNotifyStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaWlanId.setStatus("current")


class _RuijieNotifyAcMBChangeV_Type(Integer32):
    """Custom type ruijieNotifyAcMBChangeV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieNotifyAcMBChangeV_Type.__name__ = "Integer32"
_RuijieNotifyAcMBChangeV_Object = MibScalar
ruijieNotifyAcMBChangeV = _RuijieNotifyAcMBChangeV_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 10),
    _RuijieNotifyAcMBChangeV_Type()
)
ruijieNotifyAcMBChangeV.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyAcMBChangeV.setStatus("current")


class _RuijieNotifyStaOperTimes_Type(Integer32):
    """Custom type ruijieNotifyStaOperTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RuijieNotifyStaOperTimes_Type.__name__ = "Integer32"
_RuijieNotifyStaOperTimes_Object = MibScalar
ruijieNotifyStaOperTimes = _RuijieNotifyStaOperTimes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 11),
    _RuijieNotifyStaOperTimes_Type()
)
ruijieNotifyStaOperTimes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaOperTimes.setStatus("current")
_RuijieNotifyAcPowerIndex_Type = Integer32
_RuijieNotifyAcPowerIndex_Object = MibScalar
ruijieNotifyAcPowerIndex = _RuijieNotifyAcPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 12),
    _RuijieNotifyAcPowerIndex_Type()
)
ruijieNotifyAcPowerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyAcPowerIndex.setStatus("current")
_RuijieNotifyAcPowerStatu_Type = Integer32
_RuijieNotifyAcPowerStatu_Object = MibScalar
ruijieNotifyAcPowerStatu = _RuijieNotifyAcPowerStatu_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 13),
    _RuijieNotifyAcPowerStatu_Type()
)
ruijieNotifyAcPowerStatu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyAcPowerStatu.setStatus("current")
_RuijieNotifyTime_Type = DisplayString
_RuijieNotifyTime_Object = MibScalar
ruijieNotifyTime = _RuijieNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 14),
    _RuijieNotifyTime_Type()
)
ruijieNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyTime.setStatus("current")
_RuijieNotifyOldVer_Type = DisplayString
_RuijieNotifyOldVer_Object = MibScalar
ruijieNotifyOldVer = _RuijieNotifyOldVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 15),
    _RuijieNotifyOldVer_Type()
)
ruijieNotifyOldVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyOldVer.setStatus("current")
_RuijieNotifyNewVer_Type = DisplayString
_RuijieNotifyNewVer_Object = MibScalar
ruijieNotifyNewVer = _RuijieNotifyNewVer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 16),
    _RuijieNotifyNewVer_Type()
)
ruijieNotifyNewVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyNewVer.setStatus("current")


class _RuijieNotifyVerUpdtReason_Type(Integer32):
    """Custom type ruijieNotifyVerUpdtReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RuijieNotifyVerUpdtReason_Type.__name__ = "Integer32"
_RuijieNotifyVerUpdtReason_Object = MibScalar
ruijieNotifyVerUpdtReason = _RuijieNotifyVerUpdtReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 17),
    _RuijieNotifyVerUpdtReason_Type()
)
ruijieNotifyVerUpdtReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyVerUpdtReason.setStatus("current")
_RuijieNotifyStaIpv6_Type = InetAddress
_RuijieNotifyStaIpv6_Object = MibScalar
ruijieNotifyStaIpv6 = _RuijieNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 18),
    _RuijieNotifyStaIpv6_Type()
)
ruijieNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaIpv6.setStatus("current")


class _RuijieNotifyStaAssoAuthMode_Type(Integer32):
    """Custom type ruijieNotifyStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_RuijieNotifyStaAssoAuthMode_Type.__name__ = "Integer32"
_RuijieNotifyStaAssoAuthMode_Object = MibScalar
ruijieNotifyStaAssoAuthMode = _RuijieNotifyStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 19),
    _RuijieNotifyStaAssoAuthMode_Type()
)
ruijieNotifyStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaAssoAuthMode.setStatus("current")


class _RuijieNotifyStaNetAuthMode_Type(Integer32):
    """Custom type ruijieNotifyStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_RuijieNotifyStaNetAuthMode_Type.__name__ = "Integer32"
_RuijieNotifyStaNetAuthMode_Object = MibScalar
ruijieNotifyStaNetAuthMode = _RuijieNotifyStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 20),
    _RuijieNotifyStaNetAuthMode_Type()
)
ruijieNotifyStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaNetAuthMode.setStatus("current")
_RuijieNotifyStaSsid_Type = DisplayString
_RuijieNotifyStaSsid_Object = MibScalar
ruijieNotifyStaSsid = _RuijieNotifyStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 21),
    _RuijieNotifyStaSsid_Type()
)
ruijieNotifyStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaSsid.setStatus("current")
_RuijieNotifyStaLinkRate_Type = Integer32
_RuijieNotifyStaLinkRate_Object = MibScalar
ruijieNotifyStaLinkRate = _RuijieNotifyStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 22),
    _RuijieNotifyStaLinkRate_Type()
)
ruijieNotifyStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaLinkRate.setStatus("current")
_RuijieNotifyStaCurChan_Type = Integer32
_RuijieNotifyStaCurChan_Object = MibScalar
ruijieNotifyStaCurChan = _RuijieNotifyStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 23),
    _RuijieNotifyStaCurChan_Type()
)
ruijieNotifyStaCurChan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaCurChan.setStatus("current")
_RuijieNotifyStaClientType_Type = DisplayString
_RuijieNotifyStaClientType_Object = MibScalar
ruijieNotifyStaClientType = _RuijieNotifyStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 24),
    _RuijieNotifyStaClientType_Type()
)
ruijieNotifyStaClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaClientType.setStatus("current")
_RuijieNotifyStaRssi_Type = Integer32
_RuijieNotifyStaRssi_Object = MibScalar
ruijieNotifyStaRssi = _RuijieNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 25),
    _RuijieNotifyStaRssi_Type()
)
ruijieNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaRssi.setStatus("current")
_RuijieNotifyStaReason_Type = DisplayString
_RuijieNotifyStaReason_Object = MibScalar
ruijieNotifyStaReason = _RuijieNotifyStaReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 26),
    _RuijieNotifyStaReason_Type()
)
ruijieNotifyStaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaReason.setStatus("current")
_RuijieNotifyStaTimestamp_Type = Integer32
_RuijieNotifyStaTimestamp_Object = MibScalar
ruijieNotifyStaTimestamp = _RuijieNotifyStaTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 27),
    _RuijieNotifyStaTimestamp_Type()
)
ruijieNotifyStaTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaTimestamp.setStatus("current")
_RuijieNotifyStaOnlineTimeval_Type = Integer32
_RuijieNotifyStaOnlineTimeval_Object = MibScalar
ruijieNotifyStaOnlineTimeval = _RuijieNotifyStaOnlineTimeval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 28),
    _RuijieNotifyStaOnlineTimeval_Type()
)
ruijieNotifyStaOnlineTimeval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaOnlineTimeval.setStatus("current")
_RuijieNotifyStaIpv4Upflow_Type = Integer32
_RuijieNotifyStaIpv4Upflow_Object = MibScalar
ruijieNotifyStaIpv4Upflow = _RuijieNotifyStaIpv4Upflow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 29),
    _RuijieNotifyStaIpv4Upflow_Type()
)
ruijieNotifyStaIpv4Upflow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaIpv4Upflow.setStatus("current")
_RuijieNotifyStaIpv4Downflow_Type = Integer32
_RuijieNotifyStaIpv4Downflow_Object = MibScalar
ruijieNotifyStaIpv4Downflow = _RuijieNotifyStaIpv4Downflow_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 30),
    _RuijieNotifyStaIpv4Downflow_Type()
)
ruijieNotifyStaIpv4Downflow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyStaIpv4Downflow.setStatus("current")
_RuijieNotifyMicroApSlot_Type = Integer32
_RuijieNotifyMicroApSlot_Object = MibScalar
ruijieNotifyMicroApSlot = _RuijieNotifyMicroApSlot_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 31),
    _RuijieNotifyMicroApSlot_Type()
)
ruijieNotifyMicroApSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyMicroApSlot.setStatus("current")
_RuijieNotifyMicroApEvent_Type = Integer32
_RuijieNotifyMicroApEvent_Object = MibScalar
ruijieNotifyMicroApEvent = _RuijieNotifyMicroApEvent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 32),
    _RuijieNotifyMicroApEvent_Type()
)
ruijieNotifyMicroApEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyMicroApEvent.setStatus("current")


class _RuijieNotifyApLastFailureType_Type(Integer32):
    """Custom type ruijieNotifyApLastFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuijieNotifyApLastFailureType_Type.__name__ = "Integer32"
_RuijieNotifyApLastFailureType_Object = MibScalar
ruijieNotifyApLastFailureType = _RuijieNotifyApLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 1, 33),
    _RuijieNotifyApLastFailureType_Type()
)
ruijieNotifyApLastFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieNotifyApLastFailureType.setStatus("current")
_RuijieAcMgmtNotifications_ObjectIdentity = ObjectIdentity
ruijieAcMgmtNotifications = _RuijieAcMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2)
)
_RuijieAcMgmtAcMIBConformance_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAcMIBConformance = _RuijieAcMgmtAcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7)
)
_RuijieAcMgmtAcMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAcMIBCompliances = _RuijieAcMgmtAcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7, 1)
)
_RuijieAcMgmtAcMIBGroups_ObjectIdentity = ObjectIdentity
ruijieAcMgmtAcMIBGroups = _RuijieAcMgmtAcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7, 2)
)

# Managed Objects groups

ruijieAcMgmtAcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7, 2, 1)
)
ruijieAcMgmtAcMIBGroup.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieAcStaLimit"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcWtpLimit"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcRMacField"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcDataDtls"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcEcnSupport"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcBackAcIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcMtu"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcAcName"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcLocation"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcResetAp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAc80211aRateType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAc80211bRateType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFallback"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcMacAddr"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcDescriptor"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcPID"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcHwId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcSN"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcTemp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcAPUpDownCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcAPJoinFailCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcAPDecryEroReportCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApImageUpdtCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApConfigMsgEroCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApRadioOperStatuCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApAuthenFailCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcApTimestampCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOperCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNeid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcManufacturer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcSwVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcSwManufacturer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaResourceNotEnough"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcPppoeClientAct"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcPppoeClientMax"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaActThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaDisactThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaTotalRoamThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaPerRoamThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOffLineRemainTime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOffLineNumber"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOffLineDelSingle"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOffLineDelAll"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcRmOffLineApConfig"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName1"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName2"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName3"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName4"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName5"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName6"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName7"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName8"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName9"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlApName10"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcFlowBlRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName1"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName2"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName3"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName4"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName5"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName6"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName7"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName8"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName9"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlApName10"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNumBlRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcInAcRoamNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcBetweenAcRoamInNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOnOverThrodOperCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaOffOverThrodOperCtrl"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcBetweenAcRoamOutNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcCpusageSwitch"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcCpuUsageTrapTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStatTrapTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcHeartBeat"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcTotalApSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcTotalStaSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcTotalPppoeSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcCurTotalApSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcCurTotalStaSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcCurTotalPppoeSupNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcNasId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaLimitLicense"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcWtpLimitLicense"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcStaIpv6Num"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcIpv6"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcIpv6Prefix"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcIpv6Type"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcIpv6AddrType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApApName"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApApgName"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApDiscTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEchoReqTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEroReportTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStaTimeoutTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStatisticsTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApFallback"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApImageId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpDhcp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApLocation"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApWpsMfp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApLastRebootReason"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfName"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfMacAddress"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfAdminStatus"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfOperStatus"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfRxUcastPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfRxNUcastPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfTxUcastPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfTxNUcastPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfDuplex"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfLinkSpeed"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfPOEPower"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApAdminStatus"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfRxBoardPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfRxMultiPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfTxBoardPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfTxMultiPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEthernetIfDropPkts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApSn"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApToFat"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApSwVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApBootVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApPID"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApHwVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStaLimit"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApFactoryDefault"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApCpuUsageTrapTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStatTrapTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApLinkOnTimeInterval"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApNetId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApUptime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApOfftime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApState"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApNasId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApCoverArea"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApLinkOnTimeIntervalMs"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApUptimeMs"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApHbUptimeMs"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6Prefix"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6PrefixLen"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6Type"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6Gateway"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpv6StaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddrColon"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddrLine"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddrDot"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEchoRequestCnt"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEchoResponseDropCnt"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIsIsharePlus"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApTotalMicrolApNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApOnlineMicrolApNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApOfflineMicrolApNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStateTime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApEchoDelayTimeMS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRadioEn"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApTxPower"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApDtimPeriod"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApBeaconPeriod"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApCountry"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApPreaShort"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRadioBssid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApTxPowerLevel"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApTxPowerGlobal"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApCurChan"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRfGlobal"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRadioRateType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApRadio11bSup"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMaxTxPower"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMinTxPower"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApCurTxPower"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMaxTxPowerPer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApMinTxPowerPer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpAddr"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpMask"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApIpGetway"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApStaticIpRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgDiscTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgEchoReqTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgEroReportTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgStaTimeoutTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgStatisticsTimer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgFallback"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgImageId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgCreatEn"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgEnableRadioEn"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgWlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgVlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieApgWlanIntfMapRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanShort"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanSpctMgmt"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanEnQos"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanShortSlotTime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanEnableApsd"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanAckType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanTunnelType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanBroadSsid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanWlanSsid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanWlanProfile"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanCreateMapRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanRts"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanShortTry"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanLongTry"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanStaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanNasId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanChanV"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanChanBandEn"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanLimitChanRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieWlanChanBandRS"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaApMacAddr"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaVlan"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaWlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaApIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaAssoType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaAuthType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaRoamTimesPerMin"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaOnTimesPerHour"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieStaOffTimesPerHour"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaVlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaWlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyTime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyOldVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyNewVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyVerUpdtReason"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcMBChangeV"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperTimes"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerIndex"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerStatu"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcKickClient"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcOpenStaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcOpenStaAbnormalDownTimes"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcWepPskStaNum"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcWepPskStaAbnormalDownTimes"))
)
if mibBuilder.loadTexts:
    ruijieAcMgmtAcMIBGroup.setStatus("current")


# Notification objects

ruijieNotifyApTimeStampFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 1)
)
ruijieNotifyApTimeStampFail.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac")
)
if mibBuilder.loadTexts:
    ruijieNotifyApTimeStampFail.setStatus(
        "current"
    )

ruijieNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 2)
)
ruijieNotifyStaOper.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaVlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaWlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyTime"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIpv6"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaAssoAuthMode"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaNetAuthMode"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaSsid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaLinkRate"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaCurChan"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaClientType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaRssi"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaOper.setStatus(
        "current"
    )

ruijieNotifyAcMBChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 3)
)
ruijieNotifyAcMBChange.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcMBChangeV")
)
if mibBuilder.loadTexts:
    ruijieNotifyAcMBChange.setStatus(
        "current"
    )

ruijieNotifyApSwUpdtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 4)
)
ruijieNotifyApSwUpdtFail.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyOldVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyNewVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyVerUpdtReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApSwUpdtFail.setStatus(
        "current"
    )

ruijieNotifyStaActOverThredhold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 5)
)
ruijieNotifyStaActOverThredhold.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaActOverThredhold.setStatus(
        "current"
    )

ruijieNotifyStaDisactOverThredhold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 6)
)
ruijieNotifyStaDisactOverThredhold.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaDisactOverThredhold.setStatus(
        "current"
    )

ruijieNotifyStaRoamTotal = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 7)
)
ruijieNotifyStaRoamTotal.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaRoamTotal.setStatus(
        "current"
    )

ruijieNotifyStaRoamPerMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 8)
)
ruijieNotifyStaRoamPerMin.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperTimes"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaRoamPerMin.setStatus(
        "current"
    )

ruijieNotifyAcPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 9)
)
ruijieNotifyAcPowerStatus.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerIndex"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerStatu"))
)
if mibBuilder.loadTexts:
    ruijieNotifyAcPowerStatus.setStatus(
        "current"
    )

ruijieNotify86PowerOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 10)
)
ruijieNotify86PowerOffAlarm.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerIndex")
)
if mibBuilder.loadTexts:
    ruijieNotify86PowerOffAlarm.setStatus(
        "current"
    )

ruijieNotify86PowerOffAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 11)
)
ruijieNotify86PowerOffAlarmClear.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerIndex")
)
if mibBuilder.loadTexts:
    ruijieNotify86PowerOffAlarmClear.setStatus(
        "current"
    )

ruijieNotifyApSwUpdtSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 12)
)
ruijieNotifyApSwUpdtSuccess.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyOldVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyNewVer"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApSwUpdtSuccess.setStatus(
        "current"
    )

ruijieNotifyApUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 13)
)
ruijieNotifyApUp.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfAuthenMethod"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApLastFailureType"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApUp.setStatus(
        "current"
    )

ruijieNotifyApDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 14)
)
ruijieNotifyApDown.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelType"),
        ("CAPWAP-BASE-MIB", "capwapBaseNtfChannelDownReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApDown.setStatus(
        "current"
    )

ruijieNotifyApSwUpdtFailApMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 15)
)
ruijieNotifyApSwUpdtFailApMac.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyOldVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyNewVer"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyVerUpdtReason"))
)
if mibBuilder.loadTexts:
    ruijieNotifyApSwUpdtFailApMac.setStatus(
        "current"
    )

ruijieNotifyApTimeStampFailApMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 16)
)
ruijieNotifyApTimeStampFailApMac.setObjects(
    ("RUIJIE-AC-MGMT-MIB", "ruijieApMacAddr")
)
if mibBuilder.loadTexts:
    ruijieNotifyApTimeStampFailApMac.setStatus(
        "current"
    )

ruijieNotifyStaOperAlternate = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 17)
)
ruijieNotifyStaOperAlternate.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApIp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaWlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaSsid"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaVlanId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaLinkRate"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaCurChan"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaRssi"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaTimestamp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOnlineTimeval"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIpv4Upflow"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaIpv4Downflow"))
)
if mibBuilder.loadTexts:
    ruijieNotifyStaOperAlternate.setStatus(
        "current"
    )

ruijieNotifyNonrootOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 18)
)
ruijieNotifyNonrootOper.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOperType"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaApRadioId"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaTimestamp"))
)
if mibBuilder.loadTexts:
    ruijieNotifyNonrootOper.setStatus(
        "current"
    )

ruijieNotifyMicroApAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 6, 2, 19)
)
ruijieNotifyMicroApAction.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyMicroApSlot"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyMicroApEvent"))
)
if mibBuilder.loadTexts:
    ruijieNotifyMicroApAction.setStatus(
        "current"
    )


# Notifications groups

ruijieAcMgmtAcTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7, 2, 2)
)
ruijieAcMgmtAcTrapGroup.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApTimeStampFail"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaOper"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcMBChange"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApSwUpdtFail"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaActOverThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaDisactOverThredhold"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaRoamTotal"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyStaRoamPerMin"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyAcPowerStatus"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotify86PowerOffAlarm"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotify86PowerOffAlarmClear"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApSwUpdtSuccess"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApUp"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApDown"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApSwUpdtFailApMac"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieNotifyApTimeStampFailApMac"))
)
if mibBuilder.loadTexts:
    ruijieAcMgmtAcTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieAcMgmtAcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 56, 7, 1, 1)
)
ruijieAcMgmtAcMIBCompliance.setObjects(
      *(("RUIJIE-AC-MGMT-MIB", "ruijieAcMgmtAcMIBGroup"),
        ("RUIJIE-AC-MGMT-MIB", "ruijieAcMgmtAcTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieAcMgmtAcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AC-MGMT-MIB",
    **{"ruijieAcMgmtMIB": ruijieAcMgmtMIB,
       "ruijieAcMgmtAcMIBObjects": ruijieAcMgmtAcMIBObjects,
       "ruijieAcMgmtAc": ruijieAcMgmtAc,
       "ruijieAcStaLimit": ruijieAcStaLimit,
       "ruijieAcWtpLimit": ruijieAcWtpLimit,
       "ruijieAcRMacField": ruijieAcRMacField,
       "ruijieAcDataDtls": ruijieAcDataDtls,
       "ruijieAcEcnSupport": ruijieAcEcnSupport,
       "ruijieAcAcIpTable": ruijieAcAcIpTable,
       "ruijieAcAcIpTableEntry": ruijieAcAcIpTableEntry,
       "ruijieAcAcIpIndex": ruijieAcAcIpIndex,
       "ruijieAcBackAcIp": ruijieAcBackAcIp,
       "ruijieAcAcIpRS": ruijieAcAcIpRS,
       "ruijieAcMtu": ruijieAcMtu,
       "ruijieAcAcName": ruijieAcAcName,
       "ruijieAcLocation": ruijieAcLocation,
       "ruijieAcResetAp": ruijieAcResetAp,
       "ruijieAcApNum": ruijieAcApNum,
       "ruijieAc80211aRateTable": ruijieAc80211aRateTable,
       "ruijieAc80211aRateEntry": ruijieAc80211aRateEntry,
       "ruijieAc80211aRate": ruijieAc80211aRate,
       "ruijieAc80211aRateType": ruijieAc80211aRateType,
       "ruijieAc80211bRateTable": ruijieAc80211bRateTable,
       "ruijieAc80211bRateEntry": ruijieAc80211bRateEntry,
       "ruijieAc80211bRate": ruijieAc80211bRate,
       "ruijieAc80211bRateType": ruijieAc80211bRateType,
       "ruijieAcFallback": ruijieAcFallback,
       "ruijieAcStaNum": ruijieAcStaNum,
       "ruijieAcMacAddr": ruijieAcMacAddr,
       "ruijieAcDescriptor": ruijieAcDescriptor,
       "ruijieAcPID": ruijieAcPID,
       "ruijieAcHwId": ruijieAcHwId,
       "ruijieAcSN": ruijieAcSN,
       "ruijieAcTemp": ruijieAcTemp,
       "ruijieAcAPUpDownCtrl": ruijieAcAPUpDownCtrl,
       "ruijieAcAPJoinFailCtrl": ruijieAcAPJoinFailCtrl,
       "ruijieAcAPDecryEroReportCtrl": ruijieAcAPDecryEroReportCtrl,
       "ruijieAcApImageUpdtCtrl": ruijieAcApImageUpdtCtrl,
       "ruijieAcApConfigMsgEroCtrl": ruijieAcApConfigMsgEroCtrl,
       "ruijieAcApRadioOperStatuCtrl": ruijieAcApRadioOperStatuCtrl,
       "ruijieAcApAuthenFailCtrl": ruijieAcApAuthenFailCtrl,
       "ruijieAcApTimestampCtrl": ruijieAcApTimestampCtrl,
       "ruijieAcStaOperCtrl": ruijieAcStaOperCtrl,
       "ruijieAcType": ruijieAcType,
       "ruijieAcNeid": ruijieAcNeid,
       "ruijieAcManufacturer": ruijieAcManufacturer,
       "ruijieAcSwVer": ruijieAcSwVer,
       "ruijieAcSwManufacturer": ruijieAcSwManufacturer,
       "ruijieAcStaResourceNotEnough": ruijieAcStaResourceNotEnough,
       "ruijieAcPppoeClientAct": ruijieAcPppoeClientAct,
       "ruijieAcPppoeClientMax": ruijieAcPppoeClientMax,
       "ruijieAcStaActThredhold": ruijieAcStaActThredhold,
       "ruijieAcStaDisactThredhold": ruijieAcStaDisactThredhold,
       "ruijieAcStaTotalRoamThredhold": ruijieAcStaTotalRoamThredhold,
       "ruijieAcStaPerRoamThredhold": ruijieAcStaPerRoamThredhold,
       "ruijieAcStaOffLineRemainTime": ruijieAcStaOffLineRemainTime,
       "ruijieAcStaOffLineNumber": ruijieAcStaOffLineNumber,
       "ruijieAcStaOffLineDelSingle": ruijieAcStaOffLineDelSingle,
       "ruijieAcStaOffLineDelAll": ruijieAcStaOffLineDelAll,
       "ruijieAcRmOffLineApConfig": ruijieAcRmOffLineApConfig,
       "ruijieAcFlowBlGroupTable": ruijieAcFlowBlGroupTable,
       "ruijieAcFlowBlGroupEntry": ruijieAcFlowBlGroupEntry,
       "ruijieAcFlowBlGroupName": ruijieAcFlowBlGroupName,
       "ruijieAcFlowBlApName1": ruijieAcFlowBlApName1,
       "ruijieAcFlowBlApName2": ruijieAcFlowBlApName2,
       "ruijieAcFlowBlApName3": ruijieAcFlowBlApName3,
       "ruijieAcFlowBlApName4": ruijieAcFlowBlApName4,
       "ruijieAcFlowBlApName5": ruijieAcFlowBlApName5,
       "ruijieAcFlowBlApName6": ruijieAcFlowBlApName6,
       "ruijieAcFlowBlApName7": ruijieAcFlowBlApName7,
       "ruijieAcFlowBlApName8": ruijieAcFlowBlApName8,
       "ruijieAcFlowBlApName9": ruijieAcFlowBlApName9,
       "ruijieAcFlowBlApName10": ruijieAcFlowBlApName10,
       "ruijieAcFlowBlNum": ruijieAcFlowBlNum,
       "ruijieAcFlowBlRS": ruijieAcFlowBlRS,
       "ruijieAcFlowBlEnable": ruijieAcFlowBlEnable,
       "ruijieAcFlowBlBase": ruijieAcFlowBlBase,
       "ruijieAcFlowBlIsEnable": ruijieAcFlowBlIsEnable,
       "ruijieAcNumBlGroupTable": ruijieAcNumBlGroupTable,
       "ruijieAcNumBlGroupEntry": ruijieAcNumBlGroupEntry,
       "ruijieAcNumBlGroupName": ruijieAcNumBlGroupName,
       "ruijieAcNumBlApName1": ruijieAcNumBlApName1,
       "ruijieAcNumBlApName2": ruijieAcNumBlApName2,
       "ruijieAcNumBlApName3": ruijieAcNumBlApName3,
       "ruijieAcNumBlApName4": ruijieAcNumBlApName4,
       "ruijieAcNumBlApName5": ruijieAcNumBlApName5,
       "ruijieAcNumBlApName6": ruijieAcNumBlApName6,
       "ruijieAcNumBlApName7": ruijieAcNumBlApName7,
       "ruijieAcNumBlApName8": ruijieAcNumBlApName8,
       "ruijieAcNumBlApName9": ruijieAcNumBlApName9,
       "ruijieAcNumBlApName10": ruijieAcNumBlApName10,
       "ruijieAcNumBlNum": ruijieAcNumBlNum,
       "ruijieAcNumBlRS": ruijieAcNumBlRS,
       "ruijieAcNumBlEnable": ruijieAcNumBlEnable,
       "ruijieAcNumBlIsEnable": ruijieAcNumBlIsEnable,
       "ruijieAcInAcRoamNum": ruijieAcInAcRoamNum,
       "ruijieAcBetweenAcRoamInNum": ruijieAcBetweenAcRoamInNum,
       "ruijieAcStaOnOverThrodOperCtrl": ruijieAcStaOnOverThrodOperCtrl,
       "ruijieAcStaOffOverThrodOperCtrl": ruijieAcStaOffOverThrodOperCtrl,
       "ruijieAcBetweenAcRoamOutNum": ruijieAcBetweenAcRoamOutNum,
       "ruijieAcCpusageSwitch": ruijieAcCpusageSwitch,
       "ruijieAcCpuUsageTrapTimer": ruijieAcCpuUsageTrapTimer,
       "ruijieAcStatTrapTimer": ruijieAcStatTrapTimer,
       "ruijieAcHeartBeat": ruijieAcHeartBeat,
       "ruijieAcTotalApSupNum": ruijieAcTotalApSupNum,
       "ruijieAcTotalStaSupNum": ruijieAcTotalStaSupNum,
       "ruijieAcTotalPppoeSupNum": ruijieAcTotalPppoeSupNum,
       "ruijieAcCurTotalApSupNum": ruijieAcCurTotalApSupNum,
       "ruijieAcCurTotalStaSupNum": ruijieAcCurTotalStaSupNum,
       "ruijieAcCurTotalPppoeSupNum": ruijieAcCurTotalPppoeSupNum,
       "ruijieAcNasId": ruijieAcNasId,
       "ruijieAcStaLimitLicense": ruijieAcStaLimitLicense,
       "ruijieAcWtpLimitLicense": ruijieAcWtpLimitLicense,
       "ruijieAcStaIpv6Num": ruijieAcStaIpv6Num,
       "ruijieAcIpv6": ruijieAcIpv6,
       "ruijieAcIpv6Prefix": ruijieAcIpv6Prefix,
       "ruijieAcIpv6Type": ruijieAcIpv6Type,
       "ruijieAcIpv6AddrType": ruijieAcIpv6AddrType,
       "ruijieAcKickClient": ruijieAcKickClient,
       "ruijieAcOpenStaNum": ruijieAcOpenStaNum,
       "ruijieAcOpenStaAbnormalDownTimes": ruijieAcOpenStaAbnormalDownTimes,
       "ruijieAcWepPskStaNum": ruijieAcWepPskStaNum,
       "ruijieAcWepPskStaAbnormalDownTimes": ruijieAcWepPskStaAbnormalDownTimes,
       "ruijieAcPriorStaTable": ruijieAcPriorStaTable,
       "ruijieAcPriorStaEntry": ruijieAcPriorStaEntry,
       "ruijieAcPriorStaMac": ruijieAcPriorStaMac,
       "ruijieAcPriorStaRowStatus": ruijieAcPriorStaRowStatus,
       "ruijieAcMicroAPUpDownCtrl": ruijieAcMicroAPUpDownCtrl,
       "ruijieAcOfflineApNum": ruijieAcOfflineApNum,
       "ruijieAcTotalApNum": ruijieAcTotalApNum,
       "ruijieAcTotalMicrolApNum": ruijieAcTotalMicrolApNum,
       "ruijieAcOnlineMicrolApNum": ruijieAcOnlineMicrolApNum,
       "ruijieAcOfflineMicrolApNum": ruijieAcOfflineMicrolApNum,
       "ruijieAcStaLinkTimes": ruijieAcStaLinkTimes,
       "ruijieAcStaLinkSuccessTimes": ruijieAcStaLinkSuccessTimes,
       "ruijieAcStaLinkFailTimes": ruijieAcStaLinkFailTimes,
       "ruijieAcStaAuthTimes": ruijieAcStaAuthTimes,
       "ruijieAcStaAuthSuccessTimes": ruijieAcStaAuthSuccessTimes,
       "ruijieAcStaAuthFailTimes": ruijieAcStaAuthFailTimes,
       "ruijieAcMgmtAcIf": ruijieAcMgmtAcIf,
       "ruijieAcMgmtApMIBObjects": ruijieAcMgmtApMIBObjects,
       "ruijieAcMgmtAp": ruijieAcMgmtAp,
       "ruijieApCfgTable": ruijieApCfgTable,
       "ruijieApCfgEntry": ruijieApCfgEntry,
       "ruijieApMacAddr": ruijieApMacAddr,
       "ruijieApApName": ruijieApApName,
       "ruijieApApgName": ruijieApApgName,
       "ruijieApDiscTimer": ruijieApDiscTimer,
       "ruijieApEchoReqTimer": ruijieApEchoReqTimer,
       "ruijieApEroReportTimer": ruijieApEroReportTimer,
       "ruijieApStaTimeoutTimer": ruijieApStaTimeoutTimer,
       "ruijieApStatisticsTimer": ruijieApStatisticsTimer,
       "ruijieApFallback": ruijieApFallback,
       "ruijieApImageId": ruijieApImageId,
       "ruijieApIpDhcp": ruijieApIpDhcp,
       "ruijieApLocation": ruijieApLocation,
       "ruijieApWpsMfp": ruijieApWpsMfp,
       "ruijieApLastRebootReason": ruijieApLastRebootReason,
       "ruijieApEthernetIfName": ruijieApEthernetIfName,
       "ruijieApEthernetIfMacAddress": ruijieApEthernetIfMacAddress,
       "ruijieApEthernetIfAdminStatus": ruijieApEthernetIfAdminStatus,
       "ruijieApEthernetIfOperStatus": ruijieApEthernetIfOperStatus,
       "ruijieApEthernetIfRxUcastPkts": ruijieApEthernetIfRxUcastPkts,
       "ruijieApEthernetIfRxNUcastPkts": ruijieApEthernetIfRxNUcastPkts,
       "ruijieApEthernetIfTxUcastPkts": ruijieApEthernetIfTxUcastPkts,
       "ruijieApEthernetIfTxNUcastPkts": ruijieApEthernetIfTxNUcastPkts,
       "ruijieApEthernetIfDuplex": ruijieApEthernetIfDuplex,
       "ruijieApEthernetIfLinkSpeed": ruijieApEthernetIfLinkSpeed,
       "ruijieApEthernetIfPOEPower": ruijieApEthernetIfPOEPower,
       "ruijieApAdminStatus": ruijieApAdminStatus,
       "ruijieApEthernetIfRxBoardPkts": ruijieApEthernetIfRxBoardPkts,
       "ruijieApEthernetIfRxMultiPkts": ruijieApEthernetIfRxMultiPkts,
       "ruijieApEthernetIfTxBoardPkts": ruijieApEthernetIfTxBoardPkts,
       "ruijieApEthernetIfTxMultiPkts": ruijieApEthernetIfTxMultiPkts,
       "ruijieApEthernetIfDropPkts": ruijieApEthernetIfDropPkts,
       "ruijieApSn": ruijieApSn,
       "ruijieApIp": ruijieApIp,
       "ruijieApStaNum": ruijieApStaNum,
       "ruijieApToFat": ruijieApToFat,
       "ruijieApId": ruijieApId,
       "ruijieApSwVer": ruijieApSwVer,
       "ruijieApBootVer": ruijieApBootVer,
       "ruijieApPID": ruijieApPID,
       "ruijieApHwVer": ruijieApHwVer,
       "ruijieApStaLimit": ruijieApStaLimit,
       "ruijieApFactoryDefault": ruijieApFactoryDefault,
       "ruijieApCpuUsageTrapTimer": ruijieApCpuUsageTrapTimer,
       "ruijieApStatTrapTimer": ruijieApStatTrapTimer,
       "ruijieApLinkOnTimeInterval": ruijieApLinkOnTimeInterval,
       "ruijieApNetId": ruijieApNetId,
       "ruijieApUptime": ruijieApUptime,
       "ruijieApState": ruijieApState,
       "ruijieApNasId": ruijieApNasId,
       "ruijieApCoverArea": ruijieApCoverArea,
       "ruijieApLinkOnTimeIntervalMs": ruijieApLinkOnTimeIntervalMs,
       "ruijieApUptimeMs": ruijieApUptimeMs,
       "ruijieApHbUptimeMs": ruijieApHbUptimeMs,
       "ruijieApIpv6": ruijieApIpv6,
       "ruijieApIpv6Prefix": ruijieApIpv6Prefix,
       "ruijieApIpv6PrefixLen": ruijieApIpv6PrefixLen,
       "ruijieApIpv6Type": ruijieApIpv6Type,
       "ruijieApIpv6Gateway": ruijieApIpv6Gateway,
       "ruijieApIpv6StaNum": ruijieApIpv6StaNum,
       "ruijieApMacAddrColon": ruijieApMacAddrColon,
       "ruijieApMacAddrLine": ruijieApMacAddrLine,
       "ruijieApMacAddrDot": ruijieApMacAddrDot,
       "ruijieApEchoRequestCnt": ruijieApEchoRequestCnt,
       "ruijieApEchoResponseDropCnt": ruijieApEchoResponseDropCnt,
       "ruijieApEchoDelayTimeMS": ruijieApEchoDelayTimeMS,
       "ruijieApIsIsharePlus": ruijieApIsIsharePlus,
       "ruijieApTotalMicrolApNum": ruijieApTotalMicrolApNum,
       "ruijieApOnlineMicrolApNum": ruijieApOnlineMicrolApNum,
       "ruijieApOfflineMicrolApNum": ruijieApOfflineMicrolApNum,
       "ruijieApStateTime": ruijieApStateTime,
       "ruijieApCfgRadioTable": ruijieApCfgRadioTable,
       "ruijieApCfgRadioEntry": ruijieApCfgRadioEntry,
       "ruijieApCfgRadioId": ruijieApCfgRadioId,
       "ruijieApRadioEn": ruijieApRadioEn,
       "ruijieApTxPower": ruijieApTxPower,
       "ruijieApDtimPeriod": ruijieApDtimPeriod,
       "ruijieApBeaconPeriod": ruijieApBeaconPeriod,
       "ruijieApCountry": ruijieApCountry,
       "ruijieApPreaShort": ruijieApPreaShort,
       "ruijieApRadioBssid": ruijieApRadioBssid,
       "ruijieApTxPowerLevel": ruijieApTxPowerLevel,
       "ruijieApTxPowerGlobal": ruijieApTxPowerGlobal,
       "ruijieApCurChan": ruijieApCurChan,
       "ruijieApRfGlobal": ruijieApRfGlobal,
       "ruijieApRadioType": ruijieApRadioType,
       "ruijieApRadio11bSup": ruijieApRadio11bSup,
       "ruijieApMaxTxPower": ruijieApMaxTxPower,
       "ruijieApMinTxPower": ruijieApMinTxPower,
       "ruijieApCurTxPower": ruijieApCurTxPower,
       "ruijieApMaxTxPowerPer": ruijieApMaxTxPowerPer,
       "ruijieApMinTxPowerPer": ruijieApMinTxPowerPer,
       "ruijieApRadioRateCfgTable": ruijieApRadioRateCfgTable,
       "ruijieApRadioRateCfgEntry": ruijieApRadioRateCfgEntry,
       "ruijieApRadioRate": ruijieApRadioRate,
       "ruijieApRadioRateType": ruijieApRadioRateType,
       "ruijieApStaticIpCfgTable": ruijieApStaticIpCfgTable,
       "ruijieApStaticIpCfgEntry": ruijieApStaticIpCfgEntry,
       "ruijieApIpAddr": ruijieApIpAddr,
       "ruijieApIpMask": ruijieApIpMask,
       "ruijieApIpGetway": ruijieApIpGetway,
       "ruijieApStaticIpRS": ruijieApStaticIpRS,
       "ruijieApOfflineTable": ruijieApOfflineTable,
       "ruijieApOfflineEntry": ruijieApOfflineEntry,
       "ruijieApOfftime": ruijieApOfftime,
       "ruijieApOffApName": ruijieApOffApName,
       "ruijieApOffMacAddr": ruijieApOffMacAddr,
       "ruijieApOffIp": ruijieApOffIp,
       "ruijieApOffMacAddrColon": ruijieApOffMacAddrColon,
       "ruijieApOffMacAddrLine": ruijieApOffMacAddrLine,
       "ruijieApOffMacAddrDot": ruijieApOffMacAddrDot,
       "ruijieApOffStateTime": ruijieApOffStateTime,
       "ruijieApBackupStateTable": ruijieApBackupStateTable,
       "ruijieApBackupStateEntry": ruijieApBackupStateEntry,
       "ruijieApBackupState": ruijieApBackupState,
       "ruijieApMicroApTable": ruijieApMicroApTable,
       "ruijieApMicroApEntry": ruijieApMicroApEntry,
       "ruijieApMicroApSlot": ruijieApMicroApSlot,
       "ruijieApMicroApName": ruijieApMicroApName,
       "ruijieApMicroApReset": ruijieApMicroApReset,
       "ruijieApMicroApUninstall": ruijieApMicroApUninstall,
       "ruijieApMicroApMac": ruijieApMicroApMac,
       "ruijieApMicroApBoard": ruijieApMicroApBoard,
       "ruijieApMicroApState": ruijieApMicroApState,
       "ruijieApMicroApRole": ruijieApMicroApRole,
       "ruijieApMicroApMasterSlot": ruijieApMicroApMasterSlot,
       "ruijieApGeneralCfgTable": ruijieApGeneralCfgTable,
       "ruijieApGeneralCfgEntry": ruijieApGeneralCfgEntry,
       "ruijieApGeneralMacAddr": ruijieApGeneralMacAddr,
       "ruijieApGeneralApName": ruijieApGeneralApName,
       "ruijieApGeneralState": ruijieApGeneralState,
       "ruijieApGeneralTime": ruijieApGeneralTime,
       "ruijieApGeneralTimeMs": ruijieApGeneralTimeMs,
       "ruijieApGeneralIp": ruijieApGeneralIp,
       "ruijieApGeneralMacAddrColon": ruijieApGeneralMacAddrColon,
       "ruijieApGeneralMacAddrLine": ruijieApGeneralMacAddrLine,
       "ruijieApGeneralMacAddrDot": ruijieApGeneralMacAddrDot,
       "ruijieApGeneralLocation": ruijieApGeneralLocation,
       "ruijieApGeneralCPUCurrentUsage": ruijieApGeneralCPUCurrentUsage,
       "ruijieApGeneralCPUAverageUsage": ruijieApGeneralCPUAverageUsage,
       "ruijieApGeneralMemoryCurrentUsage": ruijieApGeneralMemoryCurrentUsage,
       "ruijieApGeneralMemoryAverageUsage": ruijieApGeneralMemoryAverageUsage,
       "ruijieApGeneralApStaNum": ruijieApGeneralApStaNum,
       "ruijieApGeneralApUpRate": ruijieApGeneralApUpRate,
       "ruijieApGeneralApDownRate": ruijieApGeneralApDownRate,
       "ruijieApGeneralAp24GChannel": ruijieApGeneralAp24GChannel,
       "ruijieApGeneralAp5GChannel": ruijieApGeneralAp5GChannel,
       "ruijieApGeneralStatus": ruijieApGeneralStatus,
       "ruijieApOnlineJsonTable": ruijieApOnlineJsonTable,
       "ruijieApOnlineJsonEntry": ruijieApOnlineJsonEntry,
       "ruijieApOnlineJsonMacAddr": ruijieApOnlineJsonMacAddr,
       "ruijieApOnlineJsonContent": ruijieApOnlineJsonContent,
       "ruijieApMicroApJsonTable": ruijieApMicroApJsonTable,
       "ruijieApMicroApJsonEntry": ruijieApMicroApJsonEntry,
       "ruijieApMicroApJsonMacAddr": ruijieApMicroApJsonMacAddr,
       "ruijieApMicroApJsonSlot": ruijieApMicroApJsonSlot,
       "ruijieApMicroApJsonContent": ruijieApMicroApJsonContent,
       "ruijieApRadioWlanJsonTable": ruijieApRadioWlanJsonTable,
       "ruijieApRadioWlanJsonEntry": ruijieApRadioWlanJsonEntry,
       "ruijieApRadioWlanJsonMacAddr": ruijieApRadioWlanJsonMacAddr,
       "ruijieApRadioWlanJsonRadioId": ruijieApRadioWlanJsonRadioId,
       "ruijieApRadioWlanJsonWlanId": ruijieApRadioWlanJsonWlanId,
       "ruijieApRadioWlanJsonContent": ruijieApRadioWlanJsonContent,
       "ruijieApDMJsonTable": ruijieApDMJsonTable,
       "ruijieApDMJsonEntry": ruijieApDMJsonEntry,
       "ruijieApDMJsonMacAddr": ruijieApDMJsonMacAddr,
       "ruijieApDMJsonContent": ruijieApDMJsonContent,
       "ruijieApDeviceGpsTable": ruijieApDeviceGpsTable,
       "ruijieApDeviceGpsEntry": ruijieApDeviceGpsEntry,
       "ruijieApGpsMacAddr": ruijieApGpsMacAddr,
       "ruijieApGpsLongitude": ruijieApGpsLongitude,
       "ruijieApGpsLatitude": ruijieApGpsLatitude,
       "ruijieApWiredTable": ruijieApWiredTable,
       "ruijieApWiredEntry": ruijieApWiredEntry,
       "ruijieApWiredMacAddr": ruijieApWiredMacAddr,
       "ruijieApWiredPort": ruijieApWiredPort,
       "ruijieApWiredVlanId": ruijieApWiredVlanId,
       "ruijieAcMgmtApIf": ruijieAcMgmtApIf,
       "ruijieAcMgmtApgMIBObjects": ruijieAcMgmtApgMIBObjects,
       "ruijieAcMgmtApg": ruijieAcMgmtApg,
       "ruijieApgCfgTable": ruijieApgCfgTable,
       "ruijieApgCfgEntry": ruijieApgCfgEntry,
       "ruijieApgApgName": ruijieApgApgName,
       "ruijieApgDiscTimer": ruijieApgDiscTimer,
       "ruijieApgEchoReqTimer": ruijieApgEchoReqTimer,
       "ruijieApgEroReportTimer": ruijieApgEroReportTimer,
       "ruijieApgStaTimeoutTimer": ruijieApgStaTimeoutTimer,
       "ruijieApgStatisticsTimer": ruijieApgStatisticsTimer,
       "ruijieApgFallback": ruijieApgFallback,
       "ruijieApgImageId": ruijieApgImageId,
       "ruijieApgCreatEn": ruijieApgCreatEn,
       "ruijieApgCfgRadioTable": ruijieApgCfgRadioTable,
       "ruijieApgCfgRadioEntry": ruijieApgCfgRadioEntry,
       "ruijieApgEnableRadioId": ruijieApgEnableRadioId,
       "ruijieApgEnableRadioEn": ruijieApgEnableRadioEn,
       "ruijieApgIntfMapTable": ruijieApgIntfMapTable,
       "ruijieApgIntfMapEntry": ruijieApgIntfMapEntry,
       "ruijieApgWlanIndex": ruijieApgWlanIndex,
       "ruijieApgWlanId": ruijieApgWlanId,
       "ruijieApgVlanId": ruijieApgVlanId,
       "ruijieApgRadioId": ruijieApgRadioId,
       "ruijieApgWlanIntfMapRS": ruijieApgWlanIntfMapRS,
       "ruijieAcMgmtApgIf": ruijieAcMgmtApgIf,
       "ruijieAcMgmtWlanMIBObjects": ruijieAcMgmtWlanMIBObjects,
       "ruijieAcMgmtWlan": ruijieAcMgmtWlan,
       "ruijieWlanCfgTable": ruijieWlanCfgTable,
       "ruijieWlanCfgEntry": ruijieWlanCfgEntry,
       "ruijieWlanId": ruijieWlanId,
       "ruijieWlanShort": ruijieWlanShort,
       "ruijieWlanSpctMgmt": ruijieWlanSpctMgmt,
       "ruijieWlanEnQos": ruijieWlanEnQos,
       "ruijieWlanShortSlotTime": ruijieWlanShortSlotTime,
       "ruijieWlanEnableApsd": ruijieWlanEnableApsd,
       "ruijieWlanAckType": ruijieWlanAckType,
       "ruijieWlanTunnelType": ruijieWlanTunnelType,
       "ruijieWlanBroadSsid": ruijieWlanBroadSsid,
       "ruijieWlanRts": ruijieWlanRts,
       "ruijieWlanShortTry": ruijieWlanShortTry,
       "ruijieWlanLongTry": ruijieWlanLongTry,
       "ruijieWlanStaNum": ruijieWlanStaNum,
       "ruijieWlanNasId": ruijieWlanNasId,
       "ruijieWlanWlanCreatTable": ruijieWlanWlanCreatTable,
       "ruijieWlanWlanCreatEntry": ruijieWlanWlanCreatEntry,
       "ruijieWlanWlanSsid": ruijieWlanWlanSsid,
       "ruijieWlanWlanProfile": ruijieWlanWlanProfile,
       "ruijieWlanCreateMapRS": ruijieWlanCreateMapRS,
       "ruijieWlanChanBandTable": ruijieWlanChanBandTable,
       "ruijieWlanChanBandEntry": ruijieWlanChanBandEntry,
       "ruijieWlanBandV": ruijieWlanBandV,
       "ruijieWlanChanV": ruijieWlanChanV,
       "ruijieWlanChanBandEn": ruijieWlanChanBandEn,
       "ruijieWlanChanBandRS": ruijieWlanChanBandRS,
       "ruijieWlanLimitChanTable": ruijieWlanLimitChanTable,
       "ruijieWlanLimitChanEntry": ruijieWlanLimitChanEntry,
       "ruijieWlanLimitChanFirstV": ruijieWlanLimitChanFirstV,
       "ruijieWlanLimitChanNumV": ruijieWlanLimitChanNumV,
       "ruijieWlanLimitChanMaxTxPowerLv": ruijieWlanLimitChanMaxTxPowerLv,
       "ruijieWlanLimitChanRS": ruijieWlanLimitChanRS,
       "ruijieAcMgmtWlanIf": ruijieAcMgmtWlanIf,
       "ruijieAcMgmtStaMIBObjects": ruijieAcMgmtStaMIBObjects,
       "ruijieAcMgmtSta": ruijieAcMgmtSta,
       "ruijieStaTable": ruijieStaTable,
       "ruijieStaEntry": ruijieStaEntry,
       "ruijieStaMacAddr": ruijieStaMacAddr,
       "ruijieStaApMacAddr": ruijieStaApMacAddr,
       "ruijieStaVlan": ruijieStaVlan,
       "ruijieStaWlanId": ruijieStaWlanId,
       "ruijieStaIp": ruijieStaIp,
       "ruijieStaApIp": ruijieStaApIp,
       "ruijieStaApRadioId": ruijieStaApRadioId,
       "ruijieStaApRadioType": ruijieStaApRadioType,
       "ruijieStaAssoType": ruijieStaAssoType,
       "ruijieStaAuthType": ruijieStaAuthType,
       "ruijieStaRoamTimesPerMin": ruijieStaRoamTimesPerMin,
       "ruijieStaOnTimesPerHour": ruijieStaOnTimesPerHour,
       "ruijieStaOffTimesPerHour": ruijieStaOffTimesPerHour,
       "ruijieStaIpv6": ruijieStaIpv6,
       "ruijieStaAssoAuthMode": ruijieStaAssoAuthMode,
       "ruijieStaNetAuthMode": ruijieStaNetAuthMode,
       "ruijieStaSsid": ruijieStaSsid,
       "ruijieStaLinkRate": ruijieStaLinkRate,
       "ruijieStaCurChan": ruijieStaCurChan,
       "ruijieStaClientType": ruijieStaClientType,
       "ruijieStaRssi": ruijieStaRssi,
       "ruijieStaUserName": ruijieStaUserName,
       "ruijieStaTerminalType": ruijieStaTerminalType,
       "ruijieStaOnlineTime": ruijieStaOnlineTime,
       "ruijieStaUpTimeInterval": ruijieStaUpTimeInterval,
       "ruijieStaUserAuthTime": ruijieStaUserAuthTime,
       "ruijieStaJsonTable": ruijieStaJsonTable,
       "ruijieStaJsonEntry": ruijieStaJsonEntry,
       "ruijieStaJsonMacAddr": ruijieStaJsonMacAddr,
       "ruijieStaJsonContent": ruijieStaJsonContent,
       "ruijieAcMgmtStaIf": ruijieAcMgmtStaIf,
       "ruijieAcMgmtNotificationsMIBObjects": ruijieAcMgmtNotificationsMIBObjects,
       "ruijieAcMgmtNtfObjects": ruijieAcMgmtNtfObjects,
       "ruijieNotifyApMac": ruijieNotifyApMac,
       "ruijieNotifyStaMac": ruijieNotifyStaMac,
       "ruijieNotifyApIp": ruijieNotifyApIp,
       "ruijieNotifyStaIp": ruijieNotifyStaIp,
       "ruijieNotifyStaOperType": ruijieNotifyStaOperType,
       "ruijieNotifyStaApRadioId": ruijieNotifyStaApRadioId,
       "ruijieNotifyStaApRadioType": ruijieNotifyStaApRadioType,
       "ruijieNotifyStaVlanId": ruijieNotifyStaVlanId,
       "ruijieNotifyStaWlanId": ruijieNotifyStaWlanId,
       "ruijieNotifyAcMBChangeV": ruijieNotifyAcMBChangeV,
       "ruijieNotifyStaOperTimes": ruijieNotifyStaOperTimes,
       "ruijieNotifyAcPowerIndex": ruijieNotifyAcPowerIndex,
       "ruijieNotifyAcPowerStatu": ruijieNotifyAcPowerStatu,
       "ruijieNotifyTime": ruijieNotifyTime,
       "ruijieNotifyOldVer": ruijieNotifyOldVer,
       "ruijieNotifyNewVer": ruijieNotifyNewVer,
       "ruijieNotifyVerUpdtReason": ruijieNotifyVerUpdtReason,
       "ruijieNotifyStaIpv6": ruijieNotifyStaIpv6,
       "ruijieNotifyStaAssoAuthMode": ruijieNotifyStaAssoAuthMode,
       "ruijieNotifyStaNetAuthMode": ruijieNotifyStaNetAuthMode,
       "ruijieNotifyStaSsid": ruijieNotifyStaSsid,
       "ruijieNotifyStaLinkRate": ruijieNotifyStaLinkRate,
       "ruijieNotifyStaCurChan": ruijieNotifyStaCurChan,
       "ruijieNotifyStaClientType": ruijieNotifyStaClientType,
       "ruijieNotifyStaRssi": ruijieNotifyStaRssi,
       "ruijieNotifyStaReason": ruijieNotifyStaReason,
       "ruijieNotifyStaTimestamp": ruijieNotifyStaTimestamp,
       "ruijieNotifyStaOnlineTimeval": ruijieNotifyStaOnlineTimeval,
       "ruijieNotifyStaIpv4Upflow": ruijieNotifyStaIpv4Upflow,
       "ruijieNotifyStaIpv4Downflow": ruijieNotifyStaIpv4Downflow,
       "ruijieNotifyMicroApSlot": ruijieNotifyMicroApSlot,
       "ruijieNotifyMicroApEvent": ruijieNotifyMicroApEvent,
       "ruijieNotifyApLastFailureType": ruijieNotifyApLastFailureType,
       "ruijieAcMgmtNotifications": ruijieAcMgmtNotifications,
       "ruijieNotifyApTimeStampFail": ruijieNotifyApTimeStampFail,
       "ruijieNotifyStaOper": ruijieNotifyStaOper,
       "ruijieNotifyAcMBChange": ruijieNotifyAcMBChange,
       "ruijieNotifyApSwUpdtFail": ruijieNotifyApSwUpdtFail,
       "ruijieNotifyStaActOverThredhold": ruijieNotifyStaActOverThredhold,
       "ruijieNotifyStaDisactOverThredhold": ruijieNotifyStaDisactOverThredhold,
       "ruijieNotifyStaRoamTotal": ruijieNotifyStaRoamTotal,
       "ruijieNotifyStaRoamPerMin": ruijieNotifyStaRoamPerMin,
       "ruijieNotifyAcPowerStatus": ruijieNotifyAcPowerStatus,
       "ruijieNotify86PowerOffAlarm": ruijieNotify86PowerOffAlarm,
       "ruijieNotify86PowerOffAlarmClear": ruijieNotify86PowerOffAlarmClear,
       "ruijieNotifyApSwUpdtSuccess": ruijieNotifyApSwUpdtSuccess,
       "ruijieNotifyApUp": ruijieNotifyApUp,
       "ruijieNotifyApDown": ruijieNotifyApDown,
       "ruijieNotifyApSwUpdtFailApMac": ruijieNotifyApSwUpdtFailApMac,
       "ruijieNotifyApTimeStampFailApMac": ruijieNotifyApTimeStampFailApMac,
       "ruijieNotifyStaOperAlternate": ruijieNotifyStaOperAlternate,
       "ruijieNotifyNonrootOper": ruijieNotifyNonrootOper,
       "ruijieNotifyMicroApAction": ruijieNotifyMicroApAction,
       "ruijieAcMgmtAcMIBConformance": ruijieAcMgmtAcMIBConformance,
       "ruijieAcMgmtAcMIBCompliances": ruijieAcMgmtAcMIBCompliances,
       "ruijieAcMgmtAcMIBCompliance": ruijieAcMgmtAcMIBCompliance,
       "ruijieAcMgmtAcMIBGroups": ruijieAcMgmtAcMIBGroups,
       "ruijieAcMgmtAcMIBGroup": ruijieAcMgmtAcMIBGroup,
       "ruijieAcMgmtAcTrapGroup": ruijieAcMgmtAcTrapGroup}
)
