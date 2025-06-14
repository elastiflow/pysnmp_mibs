# SNMP MIB module (CISCO-DIST-DIRECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DIST-DIRECTOR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:02:45 2025
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

(CiscoPort,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoPort")

(DnsName,
 DnsNameAsIndex,
 DnsType) = mibBuilder.importSymbols(
    "DNS-SERVER-MIB",
    "DnsName",
    "DnsNameAsIndex",
    "DnsType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDistDirMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197)
)
if mibBuilder.loadTexts:
    ciscoDistDirMIB.setRevisions(
        ("2005-11-14 00:00",
         "2001-03-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CddMetricType(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("drpExternal", 1),
          ("drpInternal", 2),
          ("drpServer", 3),
          ("drpRtt", 4),
          ("admin", 5),
          ("random", 6),
          ("portion", 7),
          ("dfpAvailability", 8),
          ("routeMap", 9))
    )



class CddMetricPriority(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )



class CddMetricWeight(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class CddMetricProfileId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CddMetricProfileIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoDistDirMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBObjects = _CiscoDistDirMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1)
)
_CddGeneral_ObjectIdentity = ObjectIdentity
cddGeneral = _CddGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1)
)
_CddGeneralMetricProfTable_Object = MibTable
cddGeneralMetricProfTable = _CddGeneralMetricProfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cddGeneralMetricProfTable.setStatus("current")
_CddGeneralMetricProfEntry_Object = MibTableRow
cddGeneralMetricProfEntry = _CddGeneralMetricProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1)
)
cddGeneralMetricProfEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricProfId"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricProfMetric"),
)
if mibBuilder.loadTexts:
    cddGeneralMetricProfEntry.setStatus("current")
_CddGeneralMetricProfId_Type = CddMetricProfileId
_CddGeneralMetricProfId_Object = MibTableColumn
cddGeneralMetricProfId = _CddGeneralMetricProfId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1, 1),
    _CddGeneralMetricProfId_Type()
)
cddGeneralMetricProfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddGeneralMetricProfId.setStatus("current")
_CddGeneralMetricProfMetric_Type = CddMetricType
_CddGeneralMetricProfMetric_Object = MibTableColumn
cddGeneralMetricProfMetric = _CddGeneralMetricProfMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1, 2),
    _CddGeneralMetricProfMetric_Type()
)
cddGeneralMetricProfMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddGeneralMetricProfMetric.setStatus("current")


class _CddGeneralMetricProfPriority_Type(CddMetricPriority):
    """Custom type cddGeneralMetricProfPriority based on CddMetricPriority"""
    defaultValue = 101


_CddGeneralMetricProfPriority_Type.__name__ = "CddMetricPriority"
_CddGeneralMetricProfPriority_Object = MibTableColumn
cddGeneralMetricProfPriority = _CddGeneralMetricProfPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1, 3),
    _CddGeneralMetricProfPriority_Type()
)
cddGeneralMetricProfPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddGeneralMetricProfPriority.setStatus("current")


class _CddGeneralMetricProfWeight_Type(CddMetricWeight):
    """Custom type cddGeneralMetricProfWeight based on CddMetricWeight"""
    defaultValue = 1


_CddGeneralMetricProfWeight_Type.__name__ = "CddMetricWeight"
_CddGeneralMetricProfWeight_Object = MibTableColumn
cddGeneralMetricProfWeight = _CddGeneralMetricProfWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1, 4),
    _CddGeneralMetricProfWeight_Type()
)
cddGeneralMetricProfWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddGeneralMetricProfWeight.setStatus("current")
_CddGeneralMetricProfRowStatus_Type = RowStatus
_CddGeneralMetricProfRowStatus_Object = MibTableColumn
cddGeneralMetricProfRowStatus = _CddGeneralMetricProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 1, 1, 5),
    _CddGeneralMetricProfRowStatus_Type()
)
cddGeneralMetricProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddGeneralMetricProfRowStatus.setStatus("current")
_CddGeneralQueries_Type = Counter32
_CddGeneralQueries_Object = MibScalar
cddGeneralQueries = _CddGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 2),
    _CddGeneralQueries_Type()
)
cddGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralQueries.setStatus("current")
_CddGeneralReplies_Type = Counter32
_CddGeneralReplies_Object = MibScalar
cddGeneralReplies = _CddGeneralReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 3),
    _CddGeneralReplies_Type()
)
cddGeneralReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralReplies.setStatus("current")
_CddGeneralQueueProcess_Type = Gauge32
_CddGeneralQueueProcess_Object = MibScalar
cddGeneralQueueProcess = _CddGeneralQueueProcess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 4),
    _CddGeneralQueueProcess_Type()
)
cddGeneralQueueProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralQueueProcess.setStatus("current")
_CddGeneralQueueMetric_Type = Gauge32
_CddGeneralQueueMetric_Object = MibScalar
cddGeneralQueueMetric = _CddGeneralQueueMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 5),
    _CddGeneralQueueMetric_Type()
)
cddGeneralQueueMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralQueueMetric.setStatus("current")
_CddGeneralMetricWaitMin_Type = TimeTicks
_CddGeneralMetricWaitMin_Object = MibScalar
cddGeneralMetricWaitMin = _CddGeneralMetricWaitMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 6),
    _CddGeneralMetricWaitMin_Type()
)
cddGeneralMetricWaitMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralMetricWaitMin.setStatus("current")
_CddGeneralMetricWaitAvg_Type = TimeTicks
_CddGeneralMetricWaitAvg_Object = MibScalar
cddGeneralMetricWaitAvg = _CddGeneralMetricWaitAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 7),
    _CddGeneralMetricWaitAvg_Type()
)
cddGeneralMetricWaitAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralMetricWaitAvg.setStatus("current")
_CddGeneralMetricWaitMax_Type = TimeTicks
_CddGeneralMetricWaitMax_Object = MibScalar
cddGeneralMetricWaitMax = _CddGeneralMetricWaitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 8),
    _CddGeneralMetricWaitMax_Type()
)
cddGeneralMetricWaitMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralMetricWaitMax.setStatus("current")
_CddGeneralCacheHits_Type = Counter32
_CddGeneralCacheHits_Object = MibScalar
cddGeneralCacheHits = _CddGeneralCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 9),
    _CddGeneralCacheHits_Type()
)
cddGeneralCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralCacheHits.setStatus("current")


class _CddGeneralCacheEnable_Type(TruthValue):
    """Custom type cddGeneralCacheEnable based on TruthValue"""
    defaultValue = 1


_CddGeneralCacheEnable_Type.__name__ = "TruthValue"
_CddGeneralCacheEnable_Object = MibScalar
cddGeneralCacheEnable = _CddGeneralCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 10),
    _CddGeneralCacheEnable_Type()
)
cddGeneralCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cddGeneralCacheEnable.setStatus("current")


class _CddGeneralCacheTime_Type(Unsigned32):
    """Custom type cddGeneralCacheTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483),
    )


_CddGeneralCacheTime_Type.__name__ = "Unsigned32"
_CddGeneralCacheTime_Object = MibScalar
cddGeneralCacheTime = _CddGeneralCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 11),
    _CddGeneralCacheTime_Type()
)
cddGeneralCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cddGeneralCacheTime.setStatus("current")
if mibBuilder.loadTexts:
    cddGeneralCacheTime.setUnits("seconds")


class _CddGeneralTTL_Type(Unsigned32):
    """Custom type cddGeneralTTL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CddGeneralTTL_Type.__name__ = "Unsigned32"
_CddGeneralTTL_Object = MibScalar
cddGeneralTTL = _CddGeneralTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 12),
    _CddGeneralTTL_Type()
)
cddGeneralTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cddGeneralTTL.setStatus("current")


class _CddGeneralDefPriorityWeight_Type(CddMetricProfileIdOrZero):
    """Custom type cddGeneralDefPriorityWeight based on CddMetricProfileIdOrZero"""
    defaultValue = 0


_CddGeneralDefPriorityWeight_Type.__name__ = "CddMetricProfileIdOrZero"
_CddGeneralDefPriorityWeight_Object = MibScalar
cddGeneralDefPriorityWeight = _CddGeneralDefPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 13),
    _CddGeneralDefPriorityWeight_Type()
)
cddGeneralDefPriorityWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cddGeneralDefPriorityWeight.setStatus("current")
_CddGeneralQueryRate_Type = Gauge32
_CddGeneralQueryRate_Object = MibScalar
cddGeneralQueryRate = _CddGeneralQueryRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 14),
    _CddGeneralQueryRate_Type()
)
cddGeneralQueryRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralQueryRate.setStatus("current")
if mibBuilder.loadTexts:
    cddGeneralQueryRate.setUnits("queries per second")


class _CddGeneralAccessList_Type(Unsigned32):
    """Custom type cddGeneralAccessList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_CddGeneralAccessList_Type.__name__ = "Unsigned32"
_CddGeneralAccessList_Object = MibScalar
cddGeneralAccessList = _CddGeneralAccessList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 1, 15),
    _CddGeneralAccessList_Type()
)
cddGeneralAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddGeneralAccessList.setStatus("current")
_CddHost_ObjectIdentity = ObjectIdentity
cddHost = _CddHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2)
)
_CddHostTable_Object = MibTable
cddHostTable = _CddHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cddHostTable.setStatus("current")
_CddHostEntry_Object = MibTableRow
cddHostEntry = _CddHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1)
)
cddHostEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostName"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostQueryType"),
)
if mibBuilder.loadTexts:
    cddHostEntry.setStatus("current")
_CddHostName_Type = DnsNameAsIndex
_CddHostName_Object = MibTableColumn
cddHostName = _CddHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 1),
    _CddHostName_Type()
)
cddHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostName.setStatus("current")
_CddHostQueryType_Type = DnsType
_CddHostQueryType_Object = MibTableColumn
cddHostQueryType = _CddHostQueryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 2),
    _CddHostQueryType_Type()
)
cddHostQueryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostQueryType.setStatus("current")


class _CddHostServicePort_Type(CiscoPort):
    """Custom type cddHostServicePort based on CiscoPort"""
    defaultValue = 0


_CddHostServicePort_Type.__name__ = "CiscoPort"
_CddHostServicePort_Object = MibTableColumn
cddHostServicePort = _CddHostServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 3),
    _CddHostServicePort_Type()
)
cddHostServicePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostServicePort.setStatus("current")


class _CddHostPriorityWeight_Type(CddMetricProfileIdOrZero):
    """Custom type cddHostPriorityWeight based on CddMetricProfileIdOrZero"""
    defaultValue = 0


_CddHostPriorityWeight_Type.__name__ = "CddMetricProfileIdOrZero"
_CddHostPriorityWeight_Object = MibTableColumn
cddHostPriorityWeight = _CddHostPriorityWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 4),
    _CddHostPriorityWeight_Type()
)
cddHostPriorityWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostPriorityWeight.setStatus("current")


class _CddHostDrpMed_Type(TruthValue):
    """Custom type cddHostDrpMed based on TruthValue"""
    defaultValue = 2


_CddHostDrpMed_Type.__name__ = "TruthValue"
_CddHostDrpMed_Object = MibTableColumn
cddHostDrpMed = _CddHostDrpMed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 5),
    _CddHostDrpMed_Type()
)
cddHostDrpMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostDrpMed.setStatus("current")


class _CddHostDrpRttProbes_Type(Unsigned32):
    """Custom type cddHostDrpRttProbes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CddHostDrpRttProbes_Type.__name__ = "Unsigned32"
_CddHostDrpRttProbes_Object = MibTableColumn
cddHostDrpRttProbes = _CddHostDrpRttProbes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 6),
    _CddHostDrpRttProbes_Type()
)
cddHostDrpRttProbes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostDrpRttProbes.setStatus("current")


class _CddHostDrpRttTol_Type(Unsigned32):
    """Custom type cddHostDrpRttTol based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CddHostDrpRttTol_Type.__name__ = "Unsigned32"
_CddHostDrpRttTol_Object = MibTableColumn
cddHostDrpRttTol = _CddHostDrpRttTol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 7),
    _CddHostDrpRttTol_Type()
)
cddHostDrpRttTol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostDrpRttTol.setStatus("current")


class _CddHostAccessControl_Type(TruthValue):
    """Custom type cddHostAccessControl based on TruthValue"""
    defaultValue = 2


_CddHostAccessControl_Type.__name__ = "TruthValue"
_CddHostAccessControl_Object = MibTableColumn
cddHostAccessControl = _CddHostAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 8),
    _CddHostAccessControl_Type()
)
cddHostAccessControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostAccessControl.setStatus("current")


class _CddHostMultipleRecord_Type(Unsigned32):
    """Custom type cddHostMultipleRecord based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CddHostMultipleRecord_Type.__name__ = "Unsigned32"
_CddHostMultipleRecord_Object = MibTableColumn
cddHostMultipleRecord = _CddHostMultipleRecord_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 9),
    _CddHostMultipleRecord_Type()
)
cddHostMultipleRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostMultipleRecord.setStatus("current")


class _CddHostLogging_Type(TruthValue):
    """Custom type cddHostLogging based on TruthValue"""
    defaultValue = 2


_CddHostLogging_Type.__name__ = "TruthValue"
_CddHostLogging_Object = MibTableColumn
cddHostLogging = _CddHostLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 10),
    _CddHostLogging_Type()
)
cddHostLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostLogging.setStatus("current")


class _CddHostUrlString_Type(SnmpAdminString):
    """Custom type cddHostUrlString based on SnmpAdminString"""
    defaultValue = OctetString("")


_CddHostUrlString_Type.__name__ = "SnmpAdminString"
_CddHostUrlString_Object = MibTableColumn
cddHostUrlString = _CddHostUrlString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 11),
    _CddHostUrlString_Type()
)
cddHostUrlString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostUrlString.setStatus("current")


class _CddHostUrlIntv_Type(TimeInterval):
    """Custom type cddHostUrlIntv based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_CddHostUrlIntv_Type.__name__ = "TimeInterval"
_CddHostUrlIntv_Object = MibTableColumn
cddHostUrlIntv = _CddHostUrlIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 12),
    _CddHostUrlIntv_Type()
)
cddHostUrlIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostUrlIntv.setStatus("current")
_CddHostRequests_Type = Counter32
_CddHostRequests_Object = MibTableColumn
cddHostRequests = _CddHostRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 13),
    _CddHostRequests_Type()
)
cddHostRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddHostRequests.setStatus("current")
_CddHostReplies_Type = Counter32
_CddHostReplies_Object = MibTableColumn
cddHostReplies = _CddHostReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 14),
    _CddHostReplies_Type()
)
cddHostReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddHostReplies.setStatus("current")
_CddHostRowStatus_Type = RowStatus
_CddHostRowStatus_Object = MibTableColumn
cddHostRowStatus = _CddHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 1, 1, 15),
    _CddHostRowStatus_Type()
)
cddHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostRowStatus.setStatus("current")
_CddHostConnectCfgTable_Object = MibTable
cddHostConnectCfgTable = _CddHostConnectCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cddHostConnectCfgTable.setStatus("current")
_CddHostConnectCfgEntry_Object = MibTableRow
cddHostConnectCfgEntry = _CddHostConnectCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 2, 1)
)
cddHostConnectCfgEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostName"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostQueryType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostConnectCfgPort"),
)
if mibBuilder.loadTexts:
    cddHostConnectCfgEntry.setStatus("current")


class _CddHostConnectCfgPort_Type(CiscoPort):
    """Custom type cddHostConnectCfgPort based on CiscoPort"""
    subtypeSpec = CiscoPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CddHostConnectCfgPort_Type.__name__ = "CiscoPort"
_CddHostConnectCfgPort_Object = MibTableColumn
cddHostConnectCfgPort = _CddHostConnectCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 2, 1, 1),
    _CddHostConnectCfgPort_Type()
)
cddHostConnectCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostConnectCfgPort.setStatus("current")


class _CddHostConnectCfgIntv_Type(TimeInterval):
    """Custom type cddHostConnectCfgIntv based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_CddHostConnectCfgIntv_Type.__name__ = "TimeInterval"
_CddHostConnectCfgIntv_Object = MibTableColumn
cddHostConnectCfgIntv = _CddHostConnectCfgIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 2, 1, 2),
    _CddHostConnectCfgIntv_Type()
)
cddHostConnectCfgIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostConnectCfgIntv.setStatus("current")
_CddHostConnectCfgRowStatus_Type = RowStatus
_CddHostConnectCfgRowStatus_Object = MibTableColumn
cddHostConnectCfgRowStatus = _CddHostConnectCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 2, 1, 3),
    _CddHostConnectCfgRowStatus_Type()
)
cddHostConnectCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostConnectCfgRowStatus.setStatus("current")
_CddHostTolCfgTable_Object = MibTable
cddHostTolCfgTable = _CddHostTolCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cddHostTolCfgTable.setStatus("current")
_CddHostTolCfgEntry_Object = MibTableRow
cddHostTolCfgEntry = _CddHostTolCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 3, 1)
)
cddHostTolCfgEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostName"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostQueryType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostTolCfgPrio"),
)
if mibBuilder.loadTexts:
    cddHostTolCfgEntry.setStatus("current")


class _CddHostTolCfgPrio_Type(CddMetricPriority):
    """Custom type cddHostTolCfgPrio based on CddMetricPriority"""
    subtypeSpec = CddMetricPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 101),
    )


_CddHostTolCfgPrio_Type.__name__ = "CddMetricPriority"
_CddHostTolCfgPrio_Object = MibTableColumn
cddHostTolCfgPrio = _CddHostTolCfgPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 3, 1, 1),
    _CddHostTolCfgPrio_Type()
)
cddHostTolCfgPrio.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostTolCfgPrio.setStatus("current")


class _CddHostTolCfgPerc_Type(Unsigned32):
    """Custom type cddHostTolCfgPerc based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CddHostTolCfgPerc_Type.__name__ = "Unsigned32"
_CddHostTolCfgPerc_Object = MibTableColumn
cddHostTolCfgPerc = _CddHostTolCfgPerc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 3, 1, 2),
    _CddHostTolCfgPerc_Type()
)
cddHostTolCfgPerc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostTolCfgPerc.setStatus("current")
if mibBuilder.loadTexts:
    cddHostTolCfgPerc.setUnits("percentage")
_CddHostTolCfgRowStatus_Type = RowStatus
_CddHostTolCfgRowStatus_Object = MibTableColumn
cddHostTolCfgRowStatus = _CddHostTolCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 2, 3, 1, 3),
    _CddHostTolCfgRowStatus_Type()
)
cddHostTolCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostTolCfgRowStatus.setStatus("current")
_CddServer_ObjectIdentity = ObjectIdentity
cddServer = _CddServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3)
)
_CddServerTable_Object = MibTable
cddServerTable = _CddServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cddServerTable.setStatus("current")
_CddServerEntry_Object = MibTableRow
cddServerEntry = _CddServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1)
)
cddServerEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddrType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddr"),
)
if mibBuilder.loadTexts:
    cddServerEntry.setStatus("current")
_CddServerAddrType_Type = InetAddressType
_CddServerAddrType_Object = MibTableColumn
cddServerAddrType = _CddServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 1),
    _CddServerAddrType_Type()
)
cddServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddServerAddrType.setStatus("current")
_CddServerAddr_Type = InetAddress
_CddServerAddr_Object = MibTableColumn
cddServerAddr = _CddServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 2),
    _CddServerAddr_Type()
)
cddServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddServerAddr.setStatus("current")
_CddServerDrpAddrType_Type = InetAddressType
_CddServerDrpAddrType_Object = MibTableColumn
cddServerDrpAddrType = _CddServerDrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 3),
    _CddServerDrpAddrType_Type()
)
cddServerDrpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerDrpAddrType.setStatus("current")
_CddServerDrpAddr_Type = InetAddress
_CddServerDrpAddr_Object = MibTableColumn
cddServerDrpAddr = _CddServerDrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 4),
    _CddServerDrpAddr_Type()
)
cddServerDrpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerDrpAddr.setStatus("current")


class _CddServerAdmin_Type(Integer32):
    """Custom type cddServerAdmin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_CddServerAdmin_Type.__name__ = "Integer32"
_CddServerAdmin_Object = MibTableColumn
cddServerAdmin = _CddServerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 5),
    _CddServerAdmin_Type()
)
cddServerAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerAdmin.setStatus("current")


class _CddServerPortion_Type(Unsigned32):
    """Custom type cddServerPortion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CddServerPortion_Type.__name__ = "Unsigned32"
_CddServerPortion_Object = MibTableColumn
cddServerPortion = _CddServerPortion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 6),
    _CddServerPortion_Type()
)
cddServerPortion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortion.setStatus("current")


class _CddServerName_Type(DnsName):
    """Custom type cddServerName based on DnsName"""
    defaultValue = OctetString("")


_CddServerName_Type.__name__ = "DnsName"
_CddServerName_Object = MibTableColumn
cddServerName = _CddServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 7),
    _CddServerName_Type()
)
cddServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerName.setStatus("current")


class _CddServerAvail_Type(Unsigned32):
    """Custom type cddServerAvail based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CddServerAvail_Type.__name__ = "Unsigned32"
_CddServerAvail_Object = MibTableColumn
cddServerAvail = _CddServerAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 8),
    _CddServerAvail_Type()
)
cddServerAvail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerAvail.setStatus("current")
_CddServerHits_Type = Counter32
_CddServerHits_Object = MibTableColumn
cddServerHits = _CddServerHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 9),
    _CddServerHits_Type()
)
cddServerHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerHits.setStatus("current")
_CddServerLastHitTime_Type = TimeStamp
_CddServerLastHitTime_Object = MibTableColumn
cddServerLastHitTime = _CddServerLastHitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 10),
    _CddServerLastHitTime_Type()
)
cddServerLastHitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerLastHitTime.setStatus("current")
_CddServerDrpSerMetric_Type = Unsigned32
_CddServerDrpSerMetric_Object = MibTableColumn
cddServerDrpSerMetric = _CddServerDrpSerMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 11),
    _CddServerDrpSerMetric_Type()
)
cddServerDrpSerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerDrpSerMetric.setStatus("current")
_CddServerPortionHits_Type = Counter32
_CddServerPortionHits_Object = MibTableColumn
cddServerPortionHits = _CddServerPortionHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 12),
    _CddServerPortionHits_Type()
)
cddServerPortionHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortionHits.setStatus("current")


class _CddServerAccessList_Type(Unsigned32):
    """Custom type cddServerAccessList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CddServerAccessList_Type.__name__ = "Unsigned32"
_CddServerAccessList_Object = MibTableColumn
cddServerAccessList = _CddServerAccessList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 13),
    _CddServerAccessList_Type()
)
cddServerAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerAccessList.setStatus("current")
_CddServerRowStatus_Type = RowStatus
_CddServerRowStatus_Object = MibTableColumn
cddServerRowStatus = _CddServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 1, 1, 14),
    _CddServerRowStatus_Type()
)
cddServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerRowStatus.setStatus("current")
_CddServerPortTable_Object = MibTable
cddServerPortTable = _CddServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cddServerPortTable.setStatus("current")
_CddServerPortEntry_Object = MibTableRow
cddServerPortEntry = _CddServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1)
)
cddServerPortEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddrType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddr"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerPortNum"),
)
if mibBuilder.loadTexts:
    cddServerPortEntry.setStatus("current")


class _CddServerPortNum_Type(CiscoPort):
    """Custom type cddServerPortNum based on CiscoPort"""
    subtypeSpec = CiscoPort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CddServerPortNum_Type.__name__ = "CiscoPort"
_CddServerPortNum_Object = MibTableColumn
cddServerPortNum = _CddServerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 1),
    _CddServerPortNum_Type()
)
cddServerPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddServerPortNum.setStatus("current")


class _CddServerPortAdmin_Type(Integer32):
    """Custom type cddServerPortAdmin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_CddServerPortAdmin_Type.__name__ = "Integer32"
_CddServerPortAdmin_Object = MibTableColumn
cddServerPortAdmin = _CddServerPortAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 2),
    _CddServerPortAdmin_Type()
)
cddServerPortAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortAdmin.setStatus("current")


class _CddServerPortConnIntv_Type(TimeInterval):
    """Custom type cddServerPortConnIntv based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_CddServerPortConnIntv_Type.__name__ = "TimeInterval"
_CddServerPortConnIntv_Object = MibTableColumn
cddServerPortConnIntv = _CddServerPortConnIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 3),
    _CddServerPortConnIntv_Type()
)
cddServerPortConnIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortConnIntv.setStatus("current")


class _CddServerPortPortion_Type(Unsigned32):
    """Custom type cddServerPortPortion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CddServerPortPortion_Type.__name__ = "Unsigned32"
_CddServerPortPortion_Object = MibTableColumn
cddServerPortPortion = _CddServerPortPortion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 4),
    _CddServerPortPortion_Type()
)
cddServerPortPortion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortPortion.setStatus("current")


class _CddServerPortAvail_Type(Unsigned32):
    """Custom type cddServerPortAvail based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CddServerPortAvail_Type.__name__ = "Unsigned32"
_CddServerPortAvail_Object = MibTableColumn
cddServerPortAvail = _CddServerPortAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 5),
    _CddServerPortAvail_Type()
)
cddServerPortAvail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortAvail.setStatus("current")


class _CddServerPortUrlString_Type(SnmpAdminString):
    """Custom type cddServerPortUrlString based on SnmpAdminString"""
    defaultValue = OctetString("")


_CddServerPortUrlString_Type.__name__ = "SnmpAdminString"
_CddServerPortUrlString_Object = MibTableColumn
cddServerPortUrlString = _CddServerPortUrlString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 6),
    _CddServerPortUrlString_Type()
)
cddServerPortUrlString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortUrlString.setStatus("current")


class _CddServerPortUrlIntv_Type(TimeInterval):
    """Custom type cddServerPortUrlIntv based on TimeInterval"""
    defaultValue = 0

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3276700),
    )


_CddServerPortUrlIntv_Type.__name__ = "TimeInterval"
_CddServerPortUrlIntv_Object = MibTableColumn
cddServerPortUrlIntv = _CddServerPortUrlIntv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 7),
    _CddServerPortUrlIntv_Type()
)
cddServerPortUrlIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortUrlIntv.setStatus("current")
_CddServerPortHits_Type = Counter32
_CddServerPortHits_Object = MibTableColumn
cddServerPortHits = _CddServerPortHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 8),
    _CddServerPortHits_Type()
)
cddServerPortHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortHits.setStatus("current")


class _CddServerPortStatus_Type(Integer32):
    """Custom type cddServerPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("undetermined", 3))
    )


_CddServerPortStatus_Type.__name__ = "Integer32"
_CddServerPortStatus_Object = MibTableColumn
cddServerPortStatus = _CddServerPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 9),
    _CddServerPortStatus_Type()
)
cddServerPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortStatus.setStatus("current")


class _CddServerPortDownCertainty_Type(Gauge32):
    """Custom type cddServerPortDownCertainty based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_CddServerPortDownCertainty_Type.__name__ = "Gauge32"
_CddServerPortDownCertainty_Object = MibTableColumn
cddServerPortDownCertainty = _CddServerPortDownCertainty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 10),
    _CddServerPortDownCertainty_Type()
)
cddServerPortDownCertainty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortDownCertainty.setStatus("current")
if mibBuilder.loadTexts:
    cddServerPortDownCertainty.setUnits("percentage")
_CddServerPortNextRetry_Type = TimeTicks
_CddServerPortNextRetry_Object = MibTableColumn
cddServerPortNextRetry = _CddServerPortNextRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 11),
    _CddServerPortNextRetry_Type()
)
cddServerPortNextRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortNextRetry.setStatus("current")
_CddServerPortPortionHits_Type = Counter32
_CddServerPortPortionHits_Object = MibTableColumn
cddServerPortPortionHits = _CddServerPortPortionHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 12),
    _CddServerPortPortionHits_Type()
)
cddServerPortPortionHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortPortionHits.setStatus("current")


class _CddServerPortAccessList_Type(Unsigned32):
    """Custom type cddServerPortAccessList based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CddServerPortAccessList_Type.__name__ = "Unsigned32"
_CddServerPortAccessList_Object = MibTableColumn
cddServerPortAccessList = _CddServerPortAccessList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 13),
    _CddServerPortAccessList_Type()
)
cddServerPortAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cddServerPortAccessList.setStatus("current")
_CddServerPortRowStatus_Type = RowStatus
_CddServerPortRowStatus_Object = MibTableColumn
cddServerPortRowStatus = _CddServerPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 2, 1, 14),
    _CddServerPortRowStatus_Type()
)
cddServerPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortRowStatus.setStatus("current")
_CddServerPortMetricTable_Object = MibTable
cddServerPortMetricTable = _CddServerPortMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cddServerPortMetricTable.setStatus("current")
_CddServerPortMetricEntry_Object = MibTableRow
cddServerPortMetricEntry = _CddServerPortMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 3, 1)
)
cddServerPortMetricEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddrType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerAddr"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerPortNum"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddServerPortMetricType"),
)
if mibBuilder.loadTexts:
    cddServerPortMetricEntry.setStatus("current")
_CddServerPortMetricType_Type = CddMetricType
_CddServerPortMetricType_Object = MibTableColumn
cddServerPortMetricType = _CddServerPortMetricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 3, 1, 1),
    _CddServerPortMetricType_Type()
)
cddServerPortMetricType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddServerPortMetricType.setStatus("current")


class _CddServerPortMetricWeight_Type(CddMetricWeight):
    """Custom type cddServerPortMetricWeight based on CddMetricWeight"""
    defaultValue = 0


_CddServerPortMetricWeight_Type.__name__ = "CddMetricWeight"
_CddServerPortMetricWeight_Object = MibTableColumn
cddServerPortMetricWeight = _CddServerPortMetricWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 3, 1, 2),
    _CddServerPortMetricWeight_Type()
)
cddServerPortMetricWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortMetricWeight.setStatus("current")
_CddServerPortMetricRowStatus_Type = RowStatus
_CddServerPortMetricRowStatus_Object = MibTableColumn
cddServerPortMetricRowStatus = _CddServerPortMetricRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 3, 3, 1, 3),
    _CddServerPortMetricRowStatus_Type()
)
cddServerPortMetricRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddServerPortMetricRowStatus.setStatus("current")
_CddMapping_ObjectIdentity = ObjectIdentity
cddMapping = _CddMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4)
)
_CddHostServerMappingTable_Object = MibTable
cddHostServerMappingTable = _CddHostServerMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cddHostServerMappingTable.setStatus("current")
_CddHostServerMappingEntry_Object = MibTableRow
cddHostServerMappingEntry = _CddHostServerMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4, 1, 1)
)
cddHostServerMappingEntry.setIndexNames(
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostName"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostQueryType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostServerMappingServerAddrType"),
    (0, "CISCO-DIST-DIRECTOR-MIB", "cddHostServerMappingServerAddr"),
)
if mibBuilder.loadTexts:
    cddHostServerMappingEntry.setStatus("current")
_CddHostServerMappingServerAddrType_Type = InetAddressType
_CddHostServerMappingServerAddrType_Object = MibTableColumn
cddHostServerMappingServerAddrType = _CddHostServerMappingServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4, 1, 1, 1),
    _CddHostServerMappingServerAddrType_Type()
)
cddHostServerMappingServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostServerMappingServerAddrType.setStatus("current")
_CddHostServerMappingServerAddr_Type = InetAddress
_CddHostServerMappingServerAddr_Object = MibTableColumn
cddHostServerMappingServerAddr = _CddHostServerMappingServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4, 1, 1, 2),
    _CddHostServerMappingServerAddr_Type()
)
cddHostServerMappingServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cddHostServerMappingServerAddr.setStatus("current")
_CddHostServerMappingRowStatus_Type = RowStatus
_CddHostServerMappingRowStatus_Object = MibTableColumn
cddHostServerMappingRowStatus = _CddHostServerMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 1, 4, 1, 1, 3),
    _CddHostServerMappingRowStatus_Type()
)
cddHostServerMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cddHostServerMappingRowStatus.setStatus("current")
_CiscoDistDirMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBNotificationPrefix = _CiscoDistDirMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 2)
)
_CiscoDistDirMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBNotifications = _CiscoDistDirMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 2, 0)
)
_CiscoDistDirMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBConformance = _CiscoDistDirMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3)
)
_CiscoDistDirMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBCompliances = _CiscoDistDirMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 1)
)
_CiscoDistDirMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDistDirMIBGroups = _CiscoDistDirMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2)
)

# Managed Objects groups

ciscoDistDirGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2, 1)
)
ciscoDistDirGeneralGroup.setObjects(
      *(("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricProfPriority"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricProfWeight"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricProfRowStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralQueries"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralReplies"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralQueueProcess"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralQueueMetric"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricWaitMin"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricWaitAvg"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralMetricWaitMax"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralCacheHits"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralCacheEnable"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralCacheTime"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralTTL"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralDefPriorityWeight"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralQueryRate"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralAccessList"))
)
if mibBuilder.loadTexts:
    ciscoDistDirGeneralGroup.setStatus("current")

ciscoDistDirHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2, 2)
)
ciscoDistDirHostGroup.setObjects(
      *(("CISCO-DIST-DIRECTOR-MIB", "cddHostServicePort"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostPriorityWeight"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostDrpMed"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostDrpRttProbes"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostDrpRttTol"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostAccessControl"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostMultipleRecord"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostLogging"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostUrlString"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostUrlIntv"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostRequests"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostReplies"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostRowStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostConnectCfgIntv"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostConnectCfgRowStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostTolCfgPerc"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddHostTolCfgRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDistDirHostGroup.setStatus("current")

ciscoDistDirServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2, 3)
)
ciscoDistDirServerGroup.setObjects(
      *(("CISCO-DIST-DIRECTOR-MIB", "cddServerDrpAddrType"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerDrpAddr"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerAdmin"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortion"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerName"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerAvail"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerHits"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerLastHitTime"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerDrpSerMetric"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortionHits"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerAccessList"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerRowStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortAdmin"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortConnIntv"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortAvail"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortUrlString"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortUrlIntv"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortPortion"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortHits"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortDownCertainty"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortNextRetry"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortPortionHits"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortAccessList"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortRowStatus"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortMetricWeight"),
        ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortMetricRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoDistDirServerGroup.setStatus("current")

ciscoDistDirMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2, 4)
)
ciscoDistDirMappingGroup.setObjects(
    ("CISCO-DIST-DIRECTOR-MIB", "cddHostServerMappingRowStatus")
)
if mibBuilder.loadTexts:
    ciscoDistDirMappingGroup.setStatus("current")


# Notification objects

ciscoDistDirEventServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 2, 0, 1)
)
ciscoDistDirEventServerUp.setObjects(
    ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortStatus")
)
if mibBuilder.loadTexts:
    ciscoDistDirEventServerUp.setStatus(
        "current"
    )

ciscoDistDirEventServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 2, 0, 2)
)
ciscoDistDirEventServerDown.setObjects(
    ("CISCO-DIST-DIRECTOR-MIB", "cddServerPortStatus")
)
if mibBuilder.loadTexts:
    ciscoDistDirEventServerDown.setStatus(
        "current"
    )

ciscoDistDirEventHitRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 2, 0, 3)
)
ciscoDistDirEventHitRateHigh.setObjects(
    ("CISCO-DIST-DIRECTOR-MIB", "cddGeneralQueryRate")
)
if mibBuilder.loadTexts:
    ciscoDistDirEventHitRateHigh.setStatus(
        "current"
    )


# Notifications groups

ciscoDistDirNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 2, 5)
)
ciscoDistDirNotificationGroup.setObjects(
      *(("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirEventServerUp"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirEventServerDown"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirEventHitRateHigh"))
)
if mibBuilder.loadTexts:
    ciscoDistDirNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDistDirMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 197, 3, 1, 1)
)
ciscoDistDirMIBCompliance.setObjects(
      *(("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirGeneralGroup"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirHostGroup"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirServerGroup"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirMappingGroup"),
        ("CISCO-DIST-DIRECTOR-MIB", "ciscoDistDirNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoDistDirMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DIST-DIRECTOR-MIB",
    **{"CddMetricType": CddMetricType,
       "CddMetricPriority": CddMetricPriority,
       "CddMetricWeight": CddMetricWeight,
       "CddMetricProfileId": CddMetricProfileId,
       "CddMetricProfileIdOrZero": CddMetricProfileIdOrZero,
       "ciscoDistDirMIB": ciscoDistDirMIB,
       "ciscoDistDirMIBObjects": ciscoDistDirMIBObjects,
       "cddGeneral": cddGeneral,
       "cddGeneralMetricProfTable": cddGeneralMetricProfTable,
       "cddGeneralMetricProfEntry": cddGeneralMetricProfEntry,
       "cddGeneralMetricProfId": cddGeneralMetricProfId,
       "cddGeneralMetricProfMetric": cddGeneralMetricProfMetric,
       "cddGeneralMetricProfPriority": cddGeneralMetricProfPriority,
       "cddGeneralMetricProfWeight": cddGeneralMetricProfWeight,
       "cddGeneralMetricProfRowStatus": cddGeneralMetricProfRowStatus,
       "cddGeneralQueries": cddGeneralQueries,
       "cddGeneralReplies": cddGeneralReplies,
       "cddGeneralQueueProcess": cddGeneralQueueProcess,
       "cddGeneralQueueMetric": cddGeneralQueueMetric,
       "cddGeneralMetricWaitMin": cddGeneralMetricWaitMin,
       "cddGeneralMetricWaitAvg": cddGeneralMetricWaitAvg,
       "cddGeneralMetricWaitMax": cddGeneralMetricWaitMax,
       "cddGeneralCacheHits": cddGeneralCacheHits,
       "cddGeneralCacheEnable": cddGeneralCacheEnable,
       "cddGeneralCacheTime": cddGeneralCacheTime,
       "cddGeneralTTL": cddGeneralTTL,
       "cddGeneralDefPriorityWeight": cddGeneralDefPriorityWeight,
       "cddGeneralQueryRate": cddGeneralQueryRate,
       "cddGeneralAccessList": cddGeneralAccessList,
       "cddHost": cddHost,
       "cddHostTable": cddHostTable,
       "cddHostEntry": cddHostEntry,
       "cddHostName": cddHostName,
       "cddHostQueryType": cddHostQueryType,
       "cddHostServicePort": cddHostServicePort,
       "cddHostPriorityWeight": cddHostPriorityWeight,
       "cddHostDrpMed": cddHostDrpMed,
       "cddHostDrpRttProbes": cddHostDrpRttProbes,
       "cddHostDrpRttTol": cddHostDrpRttTol,
       "cddHostAccessControl": cddHostAccessControl,
       "cddHostMultipleRecord": cddHostMultipleRecord,
       "cddHostLogging": cddHostLogging,
       "cddHostUrlString": cddHostUrlString,
       "cddHostUrlIntv": cddHostUrlIntv,
       "cddHostRequests": cddHostRequests,
       "cddHostReplies": cddHostReplies,
       "cddHostRowStatus": cddHostRowStatus,
       "cddHostConnectCfgTable": cddHostConnectCfgTable,
       "cddHostConnectCfgEntry": cddHostConnectCfgEntry,
       "cddHostConnectCfgPort": cddHostConnectCfgPort,
       "cddHostConnectCfgIntv": cddHostConnectCfgIntv,
       "cddHostConnectCfgRowStatus": cddHostConnectCfgRowStatus,
       "cddHostTolCfgTable": cddHostTolCfgTable,
       "cddHostTolCfgEntry": cddHostTolCfgEntry,
       "cddHostTolCfgPrio": cddHostTolCfgPrio,
       "cddHostTolCfgPerc": cddHostTolCfgPerc,
       "cddHostTolCfgRowStatus": cddHostTolCfgRowStatus,
       "cddServer": cddServer,
       "cddServerTable": cddServerTable,
       "cddServerEntry": cddServerEntry,
       "cddServerAddrType": cddServerAddrType,
       "cddServerAddr": cddServerAddr,
       "cddServerDrpAddrType": cddServerDrpAddrType,
       "cddServerDrpAddr": cddServerDrpAddr,
       "cddServerAdmin": cddServerAdmin,
       "cddServerPortion": cddServerPortion,
       "cddServerName": cddServerName,
       "cddServerAvail": cddServerAvail,
       "cddServerHits": cddServerHits,
       "cddServerLastHitTime": cddServerLastHitTime,
       "cddServerDrpSerMetric": cddServerDrpSerMetric,
       "cddServerPortionHits": cddServerPortionHits,
       "cddServerAccessList": cddServerAccessList,
       "cddServerRowStatus": cddServerRowStatus,
       "cddServerPortTable": cddServerPortTable,
       "cddServerPortEntry": cddServerPortEntry,
       "cddServerPortNum": cddServerPortNum,
       "cddServerPortAdmin": cddServerPortAdmin,
       "cddServerPortConnIntv": cddServerPortConnIntv,
       "cddServerPortPortion": cddServerPortPortion,
       "cddServerPortAvail": cddServerPortAvail,
       "cddServerPortUrlString": cddServerPortUrlString,
       "cddServerPortUrlIntv": cddServerPortUrlIntv,
       "cddServerPortHits": cddServerPortHits,
       "cddServerPortStatus": cddServerPortStatus,
       "cddServerPortDownCertainty": cddServerPortDownCertainty,
       "cddServerPortNextRetry": cddServerPortNextRetry,
       "cddServerPortPortionHits": cddServerPortPortionHits,
       "cddServerPortAccessList": cddServerPortAccessList,
       "cddServerPortRowStatus": cddServerPortRowStatus,
       "cddServerPortMetricTable": cddServerPortMetricTable,
       "cddServerPortMetricEntry": cddServerPortMetricEntry,
       "cddServerPortMetricType": cddServerPortMetricType,
       "cddServerPortMetricWeight": cddServerPortMetricWeight,
       "cddServerPortMetricRowStatus": cddServerPortMetricRowStatus,
       "cddMapping": cddMapping,
       "cddHostServerMappingTable": cddHostServerMappingTable,
       "cddHostServerMappingEntry": cddHostServerMappingEntry,
       "cddHostServerMappingServerAddrType": cddHostServerMappingServerAddrType,
       "cddHostServerMappingServerAddr": cddHostServerMappingServerAddr,
       "cddHostServerMappingRowStatus": cddHostServerMappingRowStatus,
       "ciscoDistDirMIBNotificationPrefix": ciscoDistDirMIBNotificationPrefix,
       "ciscoDistDirMIBNotifications": ciscoDistDirMIBNotifications,
       "ciscoDistDirEventServerUp": ciscoDistDirEventServerUp,
       "ciscoDistDirEventServerDown": ciscoDistDirEventServerDown,
       "ciscoDistDirEventHitRateHigh": ciscoDistDirEventHitRateHigh,
       "ciscoDistDirMIBConformance": ciscoDistDirMIBConformance,
       "ciscoDistDirMIBCompliances": ciscoDistDirMIBCompliances,
       "ciscoDistDirMIBCompliance": ciscoDistDirMIBCompliance,
       "ciscoDistDirMIBGroups": ciscoDistDirMIBGroups,
       "ciscoDistDirGeneralGroup": ciscoDistDirGeneralGroup,
       "ciscoDistDirHostGroup": ciscoDistDirHostGroup,
       "ciscoDistDirServerGroup": ciscoDistDirServerGroup,
       "ciscoDistDirMappingGroup": ciscoDistDirMappingGroup,
       "ciscoDistDirNotificationGroup": ciscoDistDirNotificationGroup}
)
