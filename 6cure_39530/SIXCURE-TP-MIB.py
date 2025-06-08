# SNMP MIB module (SIXCURE-TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/6cure_39530/SIXCURE-TP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 22:13:16 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cleaning_center = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39530)
)
if mibBuilder.loadTexts:
    cleaning_center.setRevisions(
        ("2016-08-30 14:05",
         "2016-03-31 02:20",
         "2015-07-12 00:18",
         "2014-01-31 11:22",
         "2013-03-08 00:41",
         "2012-11-21 09:53")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcTraps_ObjectIdentity = ObjectIdentity
ccTraps = _CcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 0)
)
_CcSystemAlert_ObjectIdentity = ObjectIdentity
ccSystemAlert = _CcSystemAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1)
)
_CcTrafficAlert_ObjectIdentity = ObjectIdentity
ccTrafficAlert = _CcTrafficAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2)
)
_CcModuleAlert_ObjectIdentity = ObjectIdentity
ccModuleAlert = _CcModuleAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 0, 3)
)
_CcIdmef_ObjectIdentity = ObjectIdentity
ccIdmef = _CcIdmef_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 1)
)
_CcAnalyzer_ObjectIdentity = ObjectIdentity
ccAnalyzer = _CcAnalyzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1)
)


class _CcAnalyzerId_Type(OctetString):
    """Custom type ccAnalyzerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAnalyzerId_Type.__name__ = "OctetString"
_CcAnalyzerId_Object = MibScalar
ccAnalyzerId = _CcAnalyzerId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1, 1),
    _CcAnalyzerId_Type()
)
ccAnalyzerId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAnalyzerId.setStatus("current")


class _CcAnalyzerName_Type(OctetString):
    """Custom type ccAnalyzerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAnalyzerName_Type.__name__ = "OctetString"
_CcAnalyzerName_Object = MibScalar
ccAnalyzerName = _CcAnalyzerName_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1, 2),
    _CcAnalyzerName_Type()
)
ccAnalyzerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAnalyzerName.setStatus("current")


class _CcAnalyzerManufacturer_Type(OctetString):
    """Custom type ccAnalyzerManufacturer based on OctetString"""
    defaultValue = OctetString("6cure")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAnalyzerManufacturer_Type.__name__ = "OctetString"
_CcAnalyzerManufacturer_Object = MibScalar
ccAnalyzerManufacturer = _CcAnalyzerManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1, 3),
    _CcAnalyzerManufacturer_Type()
)
ccAnalyzerManufacturer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAnalyzerManufacturer.setStatus("current")


class _CcAnalyzerModel_Type(OctetString):
    """Custom type ccAnalyzerModel based on OctetString"""
    defaultValue = OctetString("Threat Protector")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAnalyzerModel_Type.__name__ = "OctetString"
_CcAnalyzerModel_Object = MibScalar
ccAnalyzerModel = _CcAnalyzerModel_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1, 4),
    _CcAnalyzerModel_Type()
)
ccAnalyzerModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAnalyzerModel.setStatus("current")


class _CcAnalyzerVersion_Type(OctetString):
    """Custom type ccAnalyzerVersion based on OctetString"""
    defaultValue = OctetString("2.0.0")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAnalyzerVersion_Type.__name__ = "OctetString"
_CcAnalyzerVersion_Object = MibScalar
ccAnalyzerVersion = _CcAnalyzerVersion_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 1, 5),
    _CcAnalyzerVersion_Type()
)
ccAnalyzerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAnalyzerVersion.setStatus("current")
_CcAlert_ObjectIdentity = ObjectIdentity
ccAlert = _CcAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2)
)


class _CcAlertId_Type(OctetString):
    """Custom type ccAlertId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CcAlertId_Type.__name__ = "OctetString"
_CcAlertId_Object = MibScalar
ccAlertId = _CcAlertId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 1),
    _CcAlertId_Type()
)
ccAlertId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertId.setStatus("current")
_CcAlertClassification_Type = DisplayString
_CcAlertClassification_Object = MibScalar
ccAlertClassification = _CcAlertClassification_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 2),
    _CcAlertClassification_Type()
)
ccAlertClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertClassification.setStatus("current")


class _CcAlertSeverity_Type(Integer32):
    """Custom type ccAlertSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CcAlertSeverity_Type.__name__ = "Integer32"
_CcAlertSeverity_Object = MibScalar
ccAlertSeverity = _CcAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 3),
    _CcAlertSeverity_Type()
)
ccAlertSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertSeverity.setStatus("current")
_CcAlertCreateTime_Type = DateAndTime
_CcAlertCreateTime_Object = MibScalar
ccAlertCreateTime = _CcAlertCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 4),
    _CcAlertCreateTime_Type()
)
ccAlertCreateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertCreateTime.setStatus("current")
_CcAlertDetectTime_Type = DateAndTime
_CcAlertDetectTime_Object = MibScalar
ccAlertDetectTime = _CcAlertDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 5),
    _CcAlertDetectTime_Type()
)
ccAlertDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertDetectTime.setStatus("current")
_CcAlertAnalyzerTime_Type = DateAndTime
_CcAlertAnalyzerTime_Object = MibScalar
ccAlertAnalyzerTime = _CcAlertAnalyzerTime_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 6),
    _CcAlertAnalyzerTime_Type()
)
ccAlertAnalyzerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertAnalyzerTime.setStatus("current")
_CcAlertSourceTable_Object = MibTable
ccAlertSourceTable = _CcAlertSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ccAlertSourceTable.setStatus("current")
_CcAlertSourceEntry_Object = MibTableRow
ccAlertSourceEntry = _CcAlertSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7, 1)
)
ccAlertSourceEntry.setIndexNames(
    (0, "SIXCURE-TP-MIB", "ccAlertSourceId"),
)
if mibBuilder.loadTexts:
    ccAlertSourceEntry.setStatus("current")


class _CcAlertSourceId_Type(Integer32):
    """Custom type ccAlertSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAlertSourceId_Type.__name__ = "Integer32"
_CcAlertSourceId_Object = MibTableColumn
ccAlertSourceId = _CcAlertSourceId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7, 1, 1),
    _CcAlertSourceId_Type()
)
ccAlertSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAlertSourceId.setStatus("current")
_CcAlertSourceAddressType_Type = InetAddressType
_CcAlertSourceAddressType_Object = MibTableColumn
ccAlertSourceAddressType = _CcAlertSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7, 1, 2),
    _CcAlertSourceAddressType_Type()
)
ccAlertSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertSourceAddressType.setStatus("current")
_CcAlertSourceAddress_Type = InetAddress
_CcAlertSourceAddress_Object = MibTableColumn
ccAlertSourceAddress = _CcAlertSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7, 1, 3),
    _CcAlertSourceAddress_Type()
)
ccAlertSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertSourceAddress.setStatus("current")
_CcAlertSourceName_Type = DisplayString
_CcAlertSourceName_Object = MibTableColumn
ccAlertSourceName = _CcAlertSourceName_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 7, 1, 4),
    _CcAlertSourceName_Type()
)
ccAlertSourceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertSourceName.setStatus("current")
_CcAlertTargetTable_Object = MibTable
ccAlertTargetTable = _CcAlertTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ccAlertTargetTable.setStatus("current")
_CcAlertTargetEntry_Object = MibTableRow
ccAlertTargetEntry = _CcAlertTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8, 1)
)
ccAlertTargetEntry.setIndexNames(
    (0, "SIXCURE-TP-MIB", "ccAlertTargetId"),
)
if mibBuilder.loadTexts:
    ccAlertTargetEntry.setStatus("current")


class _CcAlertTargetId_Type(Integer32):
    """Custom type ccAlertTargetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CcAlertTargetId_Type.__name__ = "Integer32"
_CcAlertTargetId_Object = MibTableColumn
ccAlertTargetId = _CcAlertTargetId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8, 1, 1),
    _CcAlertTargetId_Type()
)
ccAlertTargetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAlertTargetId.setStatus("current")
_CcAlertTargetAddressType_Type = InetAddressType
_CcAlertTargetAddressType_Object = MibTableColumn
ccAlertTargetAddressType = _CcAlertTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8, 1, 2),
    _CcAlertTargetAddressType_Type()
)
ccAlertTargetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertTargetAddressType.setStatus("current")
_CcAlertTargetAddress_Type = InetAddress
_CcAlertTargetAddress_Object = MibTableColumn
ccAlertTargetAddress = _CcAlertTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8, 1, 3),
    _CcAlertTargetAddress_Type()
)
ccAlertTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertTargetAddress.setStatus("current")
_CcAlertTargetName_Type = DisplayString
_CcAlertTargetName_Object = MibTableColumn
ccAlertTargetName = _CcAlertTargetName_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 8, 1, 4),
    _CcAlertTargetName_Type()
)
ccAlertTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertTargetName.setStatus("current")
_CcAlertAdditionalTable_Object = MibTable
ccAlertAdditionalTable = _CcAlertAdditionalTable_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ccAlertAdditionalTable.setStatus("current")
_CcAlertAdditionalEntry_Object = MibTableRow
ccAlertAdditionalEntry = _CcAlertAdditionalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 9, 1)
)
ccAlertAdditionalEntry.setIndexNames(
    (0, "SIXCURE-TP-MIB", "ccAlertAdditionalId"),
)
if mibBuilder.loadTexts:
    ccAlertAdditionalEntry.setStatus("current")


class _CcAlertAdditionalId_Type(Integer32):
    """Custom type ccAlertAdditionalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CcAlertAdditionalId_Type.__name__ = "Integer32"
_CcAlertAdditionalId_Object = MibTableColumn
ccAlertAdditionalId = _CcAlertAdditionalId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 9, 1, 1),
    _CcAlertAdditionalId_Type()
)
ccAlertAdditionalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccAlertAdditionalId.setStatus("current")
_CcAlertAdditionalMeaning_Type = DisplayString
_CcAlertAdditionalMeaning_Object = MibTableColumn
ccAlertAdditionalMeaning = _CcAlertAdditionalMeaning_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 9, 1, 2),
    _CcAlertAdditionalMeaning_Type()
)
ccAlertAdditionalMeaning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertAdditionalMeaning.setStatus("current")
_CcAlertAdditionalValue_Type = DisplayString
_CcAlertAdditionalValue_Object = MibTableColumn
ccAlertAdditionalValue = _CcAlertAdditionalValue_Object(
    (1, 3, 6, 1, 4, 1, 39530, 1, 2, 9, 1, 3),
    _CcAlertAdditionalValue_Type()
)
ccAlertAdditionalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAlertAdditionalValue.setStatus("current")
_CcSystem_ObjectIdentity = ObjectIdentity
ccSystem = _CcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 2)
)
_CcUpTime_Type = TimeTicks
_CcUpTime_Object = MibScalar
ccUpTime = _CcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 1),
    _CcUpTime_Type()
)
ccUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccUpTime.setStatus("current")
_CcLastHeartbeat_Type = DateAndTime
_CcLastHeartbeat_Object = MibScalar
ccLastHeartbeat = _CcLastHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 2),
    _CcLastHeartbeat_Type()
)
ccLastHeartbeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLastHeartbeat.setStatus("current")
_CcLastConfiguration_Type = DateAndTime
_CcLastConfiguration_Object = MibScalar
ccLastConfiguration = _CcLastConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 3),
    _CcLastConfiguration_Type()
)
ccLastConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccLastConfiguration.setStatus("current")
_CcAverageCpuLoad_Type = Gauge32
_CcAverageCpuLoad_Object = MibScalar
ccAverageCpuLoad = _CcAverageCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 4),
    _CcAverageCpuLoad_Type()
)
ccAverageCpuLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccAverageCpuLoad.setStatus("current")
_CcFifoSize_Type = CounterBasedGauge64
_CcFifoSize_Object = MibScalar
ccFifoSize = _CcFifoSize_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 5),
    _CcFifoSize_Type()
)
ccFifoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccFifoSize.setStatus("current")
_CcNumberOfServices_Type = Integer32
_CcNumberOfServices_Object = MibScalar
ccNumberOfServices = _CcNumberOfServices_Object(
    (1, 3, 6, 1, 4, 1, 39530, 2, 6),
    _CcNumberOfServices_Type()
)
ccNumberOfServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccNumberOfServices.setStatus("current")
_CcTraffic_ObjectIdentity = ObjectIdentity
ccTraffic = _CcTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 3)
)
_CcTrafficTable_Object = MibTable
ccTrafficTable = _CcTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1)
)
if mibBuilder.loadTexts:
    ccTrafficTable.setStatus("current")
_CcTrafficEntry_Object = MibTableRow
ccTrafficEntry = _CcTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1)
)
ccTrafficEntry.setIndexNames(
    (0, "SIXCURE-TP-MIB", "ccTrafficId"),
)
if mibBuilder.loadTexts:
    ccTrafficEntry.setStatus("current")


class _CcTrafficId_Type(Integer32):
    """Custom type ccTrafficId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CcTrafficId_Type.__name__ = "Integer32"
_CcTrafficId_Object = MibTableColumn
ccTrafficId = _CcTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 1),
    _CcTrafficId_Type()
)
ccTrafficId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficId.setStatus("current")
_CcTrafficRowStatus_Type = RowStatus
_CcTrafficRowStatus_Object = MibTableColumn
ccTrafficRowStatus = _CcTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 2),
    _CcTrafficRowStatus_Type()
)
ccTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccTrafficRowStatus.setStatus("current")
_CcTrafficServiceName_Type = DisplayString
_CcTrafficServiceName_Object = MibTableColumn
ccTrafficServiceName = _CcTrafficServiceName_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 3),
    _CcTrafficServiceName_Type()
)
ccTrafficServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrafficServiceName.setStatus("current")
_CcTrafficModuleName_Type = DisplayString
_CcTrafficModuleName_Object = MibTableColumn
ccTrafficModuleName = _CcTrafficModuleName_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 4),
    _CcTrafficModuleName_Type()
)
ccTrafficModuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccTrafficModuleName.setStatus("current")
_CcTrafficIncomingPacketsCount_Type = CounterBasedGauge64
_CcTrafficIncomingPacketsCount_Object = MibTableColumn
ccTrafficIncomingPacketsCount = _CcTrafficIncomingPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 5),
    _CcTrafficIncomingPacketsCount_Type()
)
ccTrafficIncomingPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficIncomingPacketsCount.setStatus("current")
_CcTrafficIncomingVolume_Type = CounterBasedGauge64
_CcTrafficIncomingVolume_Object = MibTableColumn
ccTrafficIncomingVolume = _CcTrafficIncomingVolume_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 6),
    _CcTrafficIncomingVolume_Type()
)
ccTrafficIncomingVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficIncomingVolume.setStatus("current")
_CcTrafficOutgoingPacketsCount_Type = CounterBasedGauge64
_CcTrafficOutgoingPacketsCount_Object = MibTableColumn
ccTrafficOutgoingPacketsCount = _CcTrafficOutgoingPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 7),
    _CcTrafficOutgoingPacketsCount_Type()
)
ccTrafficOutgoingPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficOutgoingPacketsCount.setStatus("current")
_CcTrafficOutgoingVolume_Type = CounterBasedGauge64
_CcTrafficOutgoingVolume_Object = MibTableColumn
ccTrafficOutgoingVolume = _CcTrafficOutgoingVolume_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 8),
    _CcTrafficOutgoingVolume_Type()
)
ccTrafficOutgoingVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficOutgoingVolume.setStatus("current")
_CcTrafficGeneratedPacketsCount_Type = CounterBasedGauge64
_CcTrafficGeneratedPacketsCount_Object = MibTableColumn
ccTrafficGeneratedPacketsCount = _CcTrafficGeneratedPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 9),
    _CcTrafficGeneratedPacketsCount_Type()
)
ccTrafficGeneratedPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficGeneratedPacketsCount.setStatus("current")
_CcTrafficGeneratedVolume_Type = CounterBasedGauge64
_CcTrafficGeneratedVolume_Object = MibTableColumn
ccTrafficGeneratedVolume = _CcTrafficGeneratedVolume_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 10),
    _CcTrafficGeneratedVolume_Type()
)
ccTrafficGeneratedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficGeneratedVolume.setStatus("current")
_CcTrafficRejectedPacketsCount_Type = CounterBasedGauge64
_CcTrafficRejectedPacketsCount_Object = MibTableColumn
ccTrafficRejectedPacketsCount = _CcTrafficRejectedPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 11),
    _CcTrafficRejectedPacketsCount_Type()
)
ccTrafficRejectedPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficRejectedPacketsCount.setStatus("current")
_CcTrafficRejectedVolume_Type = CounterBasedGauge64
_CcTrafficRejectedVolume_Object = MibTableColumn
ccTrafficRejectedVolume = _CcTrafficRejectedVolume_Object(
    (1, 3, 6, 1, 4, 1, 39530, 3, 1, 1, 12),
    _CcTrafficRejectedVolume_Type()
)
ccTrafficRejectedVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccTrafficRejectedVolume.setStatus("current")
_CcMibConformance_ObjectIdentity = ObjectIdentity
ccMibConformance = _CcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39530, 4)
)

# Managed Objects groups

ccIdmefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39530, 4, 2)
)
ccIdmefGroup.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerId"),
        ("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAnalyzerManufacturer"),
        ("SIXCURE-TP-MIB", "ccAnalyzerModel"),
        ("SIXCURE-TP-MIB", "ccAnalyzerVersion"),
        ("SIXCURE-TP-MIB", "ccAlertId"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertCreateTime"),
        ("SIXCURE-TP-MIB", "ccAlertDetectTime"),
        ("SIXCURE-TP-MIB", "ccAlertAnalyzerTime"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddressType"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccAlertSourceName"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddressType"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddress"),
        ("SIXCURE-TP-MIB", "ccAlertTargetName"),
        ("SIXCURE-TP-MIB", "ccAlertAdditionalMeaning"),
        ("SIXCURE-TP-MIB", "ccAlertAdditionalValue"))
)
if mibBuilder.loadTexts:
    ccIdmefGroup.setStatus("current")

ccSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39530, 4, 3)
)
ccSystemGroup.setObjects(
      *(("SIXCURE-TP-MIB", "ccUpTime"),
        ("SIXCURE-TP-MIB", "ccLastHeartbeat"),
        ("SIXCURE-TP-MIB", "ccLastConfiguration"),
        ("SIXCURE-TP-MIB", "ccAverageCpuLoad"),
        ("SIXCURE-TP-MIB", "ccFifoSize"),
        ("SIXCURE-TP-MIB", "ccNumberOfServices"))
)
if mibBuilder.loadTexts:
    ccSystemGroup.setStatus("current")

ccTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39530, 4, 4)
)
ccTrafficGroup.setObjects(
      *(("SIXCURE-TP-MIB", "ccTrafficRowStatus"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficModuleName"),
        ("SIXCURE-TP-MIB", "ccTrafficIncomingPacketsCount"),
        ("SIXCURE-TP-MIB", "ccTrafficIncomingVolume"),
        ("SIXCURE-TP-MIB", "ccTrafficOutgoingPacketsCount"),
        ("SIXCURE-TP-MIB", "ccTrafficOutgoingVolume"),
        ("SIXCURE-TP-MIB", "ccTrafficGeneratedPacketsCount"),
        ("SIXCURE-TP-MIB", "ccTrafficGeneratedVolume"),
        ("SIXCURE-TP-MIB", "ccTrafficRejectedPacketsCount"),
        ("SIXCURE-TP-MIB", "ccTrafficRejectedVolume"))
)
if mibBuilder.loadTexts:
    ccTrafficGroup.setStatus("current")


# Notification objects

ccSystemStorageSuspendedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 1)
)
ccSystemStorageSuspendedAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemStorageSuspendedAlert.setStatus(
        "current"
    )

ccSystemStorageResumedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 2)
)
ccSystemStorageResumedAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemStorageResumedAlert.setStatus(
        "current"
    )

ccSystemOverloadAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 3)
)
ccSystemOverloadAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemOverloadAlert.setStatus(
        "current"
    )

ccSystemFarmCcDownAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 4)
)
ccSystemFarmCcDownAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemFarmCcDownAlert.setStatus(
        "current"
    )

ccSystemFarmCcUpAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 5)
)
ccSystemFarmCcUpAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemFarmCcUpAlert.setStatus(
        "current"
    )

ccSystemFarmGroupEmptyAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 6)
)
ccSystemFarmGroupEmptyAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemFarmGroupEmptyAlert.setStatus(
        "current"
    )

ccSystemFarmCcAloneAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 7)
)
ccSystemFarmCcAloneAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemFarmCcAloneAlert.setStatus(
        "current"
    )

ccSystemStatisticsSuspendedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 8)
)
ccSystemStatisticsSuspendedAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemStatisticsSuspendedAlert.setStatus(
        "current"
    )

ccSystemStatisticsResumedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 9)
)
ccSystemStatisticsResumedAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemStatisticsResumedAlert.setStatus(
        "current"
    )

ccSystemLogFailureAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 10)
)
ccSystemLogFailureAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemLogFailureAlert.setStatus(
        "current"
    )

ccSystemRingBufferAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 11)
)
ccSystemRingBufferAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemRingBufferAlert.setStatus(
        "current"
    )

ccSystemIllegalFrameAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 12)
)
ccSystemIllegalFrameAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemIllegalFrameAlert.setStatus(
        "current"
    )

ccSystemLogExportAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 1, 13)
)
ccSystemLogExportAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccSystemLogExportAlert.setStatus(
        "current"
    )

ccTrafficDosAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 1)
)
ccTrafficDosAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"))
)
if mibBuilder.loadTexts:
    ccTrafficDosAlert.setStatus(
        "current"
    )

ccTrafficRateAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 2)
)
ccTrafficRateAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"))
)
if mibBuilder.loadTexts:
    ccTrafficRateAlert.setStatus(
        "current"
    )

ccTrafficScanAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 3)
)
ccTrafficScanAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"))
)
if mibBuilder.loadTexts:
    ccTrafficScanAlert.setStatus(
        "current"
    )

ccTrafficFloodAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 4)
)
ccTrafficFloodAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddress"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"))
)
if mibBuilder.loadTexts:
    ccTrafficFloodAlert.setStatus(
        "current"
    )

ccModuleAttackAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 4)
)
ccModuleAttackAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"),
        ("SIXCURE-TP-MIB", "ccTrafficModuleName"))
)
if mibBuilder.loadTexts:
    ccModuleAttackAlert.setStatus(
        "current"
    )

ccTrafficDnsFloodAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 5)
)
ccTrafficDnsFloodAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddress"),
        ("SIXCURE-TP-MIB", "ccTrafficServiceName"),
        ("SIXCURE-TP-MIB", "ccTrafficId"))
)
if mibBuilder.loadTexts:
    ccTrafficDnsFloodAlert.setStatus(
        "current"
    )

ccTrafficPacketAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 6)
)
ccTrafficPacketAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddress"))
)
if mibBuilder.loadTexts:
    ccTrafficPacketAlert.setStatus(
        "current"
    )

ccTrafficCachePoisonAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 7)
)
ccTrafficCachePoisonAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"),
        ("SIXCURE-TP-MIB", "ccAlertSourceAddress"),
        ("SIXCURE-TP-MIB", "ccAlertTargetAddress"))
)
if mibBuilder.loadTexts:
    ccTrafficCachePoisonAlert.setStatus(
        "current"
    )

ccTrafficWaterTortureAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 39530, 0, 2, 8)
)
ccTrafficWaterTortureAlert.setObjects(
      *(("SIXCURE-TP-MIB", "ccAnalyzerName"),
        ("SIXCURE-TP-MIB", "ccAlertClassification"),
        ("SIXCURE-TP-MIB", "ccAlertSeverity"))
)
if mibBuilder.loadTexts:
    ccTrafficWaterTortureAlert.setStatus(
        "current"
    )


# Notifications groups

ccNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39530, 4, 5)
)
ccNotificationGroup.setObjects(
      *(("SIXCURE-TP-MIB", "ccSystemStorageSuspendedAlert"),
        ("SIXCURE-TP-MIB", "ccSystemStorageResumedAlert"),
        ("SIXCURE-TP-MIB", "ccSystemOverloadAlert"),
        ("SIXCURE-TP-MIB", "ccSystemFarmCcDownAlert"),
        ("SIXCURE-TP-MIB", "ccSystemFarmCcUpAlert"),
        ("SIXCURE-TP-MIB", "ccSystemFarmGroupEmptyAlert"),
        ("SIXCURE-TP-MIB", "ccSystemFarmCcAloneAlert"),
        ("SIXCURE-TP-MIB", "ccSystemStatisticsSuspendedAlert"),
        ("SIXCURE-TP-MIB", "ccSystemStatisticsResumedAlert"),
        ("SIXCURE-TP-MIB", "ccSystemLogFailureAlert"),
        ("SIXCURE-TP-MIB", "ccSystemRingBufferAlert"),
        ("SIXCURE-TP-MIB", "ccSystemIllegalFrameAlert"),
        ("SIXCURE-TP-MIB", "ccSystemLogExportAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficDosAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficRateAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficScanAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficFloodAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficDnsFloodAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficPacketAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficCachePoisonAlert"),
        ("SIXCURE-TP-MIB", "ccTrafficWaterTortureAlert"),
        ("SIXCURE-TP-MIB", "ccModuleAttackAlert"))
)
if mibBuilder.loadTexts:
    ccNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ccMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 39530, 4, 1)
)
ccMibCompliance.setObjects(
      *(("SIXCURE-TP-MIB", "ccIdmefGroup"),
        ("SIXCURE-TP-MIB", "ccSystemGroup"),
        ("SIXCURE-TP-MIB", "ccTrafficGroup"),
        ("SIXCURE-TP-MIB", "ccNotificationGroup"))
)
if mibBuilder.loadTexts:
    ccMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIXCURE-TP-MIB",
    **{"cleaning-center": cleaning_center,
       "ccTraps": ccTraps,
       "ccSystemAlert": ccSystemAlert,
       "ccSystemStorageSuspendedAlert": ccSystemStorageSuspendedAlert,
       "ccSystemStorageResumedAlert": ccSystemStorageResumedAlert,
       "ccSystemOverloadAlert": ccSystemOverloadAlert,
       "ccSystemFarmCcDownAlert": ccSystemFarmCcDownAlert,
       "ccSystemFarmCcUpAlert": ccSystemFarmCcUpAlert,
       "ccSystemFarmGroupEmptyAlert": ccSystemFarmGroupEmptyAlert,
       "ccSystemFarmCcAloneAlert": ccSystemFarmCcAloneAlert,
       "ccSystemStatisticsSuspendedAlert": ccSystemStatisticsSuspendedAlert,
       "ccSystemStatisticsResumedAlert": ccSystemStatisticsResumedAlert,
       "ccSystemLogFailureAlert": ccSystemLogFailureAlert,
       "ccSystemRingBufferAlert": ccSystemRingBufferAlert,
       "ccSystemIllegalFrameAlert": ccSystemIllegalFrameAlert,
       "ccSystemLogExportAlert": ccSystemLogExportAlert,
       "ccTrafficAlert": ccTrafficAlert,
       "ccTrafficDosAlert": ccTrafficDosAlert,
       "ccTrafficRateAlert": ccTrafficRateAlert,
       "ccTrafficScanAlert": ccTrafficScanAlert,
       "ccTrafficFloodAlert": ccTrafficFloodAlert,
       "ccModuleAttackAlert": ccModuleAttackAlert,
       "ccTrafficDnsFloodAlert": ccTrafficDnsFloodAlert,
       "ccTrafficPacketAlert": ccTrafficPacketAlert,
       "ccTrafficCachePoisonAlert": ccTrafficCachePoisonAlert,
       "ccTrafficWaterTortureAlert": ccTrafficWaterTortureAlert,
       "ccModuleAlert": ccModuleAlert,
       "ccIdmef": ccIdmef,
       "ccAnalyzer": ccAnalyzer,
       "ccAnalyzerId": ccAnalyzerId,
       "ccAnalyzerName": ccAnalyzerName,
       "ccAnalyzerManufacturer": ccAnalyzerManufacturer,
       "ccAnalyzerModel": ccAnalyzerModel,
       "ccAnalyzerVersion": ccAnalyzerVersion,
       "ccAlert": ccAlert,
       "ccAlertId": ccAlertId,
       "ccAlertClassification": ccAlertClassification,
       "ccAlertSeverity": ccAlertSeverity,
       "ccAlertCreateTime": ccAlertCreateTime,
       "ccAlertDetectTime": ccAlertDetectTime,
       "ccAlertAnalyzerTime": ccAlertAnalyzerTime,
       "ccAlertSourceTable": ccAlertSourceTable,
       "ccAlertSourceEntry": ccAlertSourceEntry,
       "ccAlertSourceId": ccAlertSourceId,
       "ccAlertSourceAddressType": ccAlertSourceAddressType,
       "ccAlertSourceAddress": ccAlertSourceAddress,
       "ccAlertSourceName": ccAlertSourceName,
       "ccAlertTargetTable": ccAlertTargetTable,
       "ccAlertTargetEntry": ccAlertTargetEntry,
       "ccAlertTargetId": ccAlertTargetId,
       "ccAlertTargetAddressType": ccAlertTargetAddressType,
       "ccAlertTargetAddress": ccAlertTargetAddress,
       "ccAlertTargetName": ccAlertTargetName,
       "ccAlertAdditionalTable": ccAlertAdditionalTable,
       "ccAlertAdditionalEntry": ccAlertAdditionalEntry,
       "ccAlertAdditionalId": ccAlertAdditionalId,
       "ccAlertAdditionalMeaning": ccAlertAdditionalMeaning,
       "ccAlertAdditionalValue": ccAlertAdditionalValue,
       "ccSystem": ccSystem,
       "ccUpTime": ccUpTime,
       "ccLastHeartbeat": ccLastHeartbeat,
       "ccLastConfiguration": ccLastConfiguration,
       "ccAverageCpuLoad": ccAverageCpuLoad,
       "ccFifoSize": ccFifoSize,
       "ccNumberOfServices": ccNumberOfServices,
       "ccTraffic": ccTraffic,
       "ccTrafficTable": ccTrafficTable,
       "ccTrafficEntry": ccTrafficEntry,
       "ccTrafficId": ccTrafficId,
       "ccTrafficRowStatus": ccTrafficRowStatus,
       "ccTrafficServiceName": ccTrafficServiceName,
       "ccTrafficModuleName": ccTrafficModuleName,
       "ccTrafficIncomingPacketsCount": ccTrafficIncomingPacketsCount,
       "ccTrafficIncomingVolume": ccTrafficIncomingVolume,
       "ccTrafficOutgoingPacketsCount": ccTrafficOutgoingPacketsCount,
       "ccTrafficOutgoingVolume": ccTrafficOutgoingVolume,
       "ccTrafficGeneratedPacketsCount": ccTrafficGeneratedPacketsCount,
       "ccTrafficGeneratedVolume": ccTrafficGeneratedVolume,
       "ccTrafficRejectedPacketsCount": ccTrafficRejectedPacketsCount,
       "ccTrafficRejectedVolume": ccTrafficRejectedVolume,
       "ccMibConformance": ccMibConformance,
       "ccMibCompliance": ccMibCompliance,
       "ccIdmefGroup": ccIdmefGroup,
       "ccSystemGroup": ccSystemGroup,
       "ccTrafficGroup": ccTrafficGroup,
       "ccNotificationGroup": ccNotificationGroup}
)
